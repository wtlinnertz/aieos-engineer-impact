"""Category 3: Cross-file consistency — formulas, levels, references must match."""

import re

import pytest

from models.impact import CONTRIBUTION_LEVELS, ER_MAPPING
from parsers.doc_parser import extract_code_blocks, extract_file_references, extract_headings


# ---------------------------------------------------------------------------
# Complexity Formula Consistency
# ---------------------------------------------------------------------------


def _normalize_formula(text: str) -> str:
    """Normalize formula text for comparison: lowercase, collapse whitespace, unify operators."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    # Normalize multiplication: × or x or *
    text = text.replace("×", "*").replace(" x ", " * ")
    return text


class TestComplexityFormulaConsistency:

    def test_formula_present_in_both_files(self, framework_content, complexity_rubric_content):
        """Both files contain the complexity factor formula."""
        # framework.md uses a fenced code block; complexity-factor.md uses inline code
        for label, content in [
            ("framework.md", framework_content),
            ("complexity-factor.md", complexity_rubric_content),
        ]:
            assert "1.0" in content and "0.3" in content and "0.2" in content, (
                f"Complexity formula components missing in {label}"
            )
            # Check the structural formula reference exists
            assert "Risk" in content and "Novelty" in content, (
                f"Formula dimension names missing in {label}"
            )

    def test_weights_match(self, framework_content, complexity_rubric_content):
        """Risk weight 0.3, Novelty 0.2, Org Friction 0.2 in both files."""
        for label, content in [
            ("framework.md", framework_content),
            ("complexity-factor.md", complexity_rubric_content),
        ]:
            assert "0.3" in content, f"Risk weight 0.3 missing in {label}"
            # Check 0.2 appears at least twice (novelty + org friction)
            assert content.count("0.2") >= 2, f"Novelty/Friction weights 0.2 missing in {label}"


# ---------------------------------------------------------------------------
# Contribution Level Consistency
# ---------------------------------------------------------------------------


class TestContributionLevelConsistency:

    def test_levels_present_in_framework(self, framework_content):
        """All 5 contribution level scores appear in framework.md."""
        for score in CONTRIBUTION_LEVELS:
            assert f"**{score}**" in framework_content or str(score) in framework_content

    def test_labels_present_in_rubric(self, contribution_rubric_content):
        """All 5 contribution level labels appear in rubric."""
        for label in CONTRIBUTION_LEVELS.values():
            assert label in contribution_rubric_content, (
                f"Label '{label}' missing from contribution-factor.md"
            )

    def test_er_mapping_covers_all_levels(self):
        """Every contribution level falls within one of the ER mapping ranges."""
        for score, label in CONTRIBUTION_LEVELS.items():
            covered = False
            for er_level, (lo, hi) in ER_MAPPING.items():
                if lo <= score <= hi:
                    covered = True
                    break
            assert covered, (
                f"Contribution level {score} ({label}) not covered by any ER mapping range"
            )


# ---------------------------------------------------------------------------
# ER Mapping Ranges
# ---------------------------------------------------------------------------


class TestERMappingRanges:

    def test_no_overlaps(self):
        """The three ER mapping ranges do not overlap."""
        ranges = sorted(ER_MAPPING.values(), key=lambda r: r[0])
        for i in range(len(ranges) - 1):
            _, hi = ranges[i]
            lo_next, _ = ranges[i + 1]
            assert hi < lo_next, (
                f"ER mapping ranges overlap: {ranges[i]} and {ranges[i+1]}"
            )

    def test_no_gaps_for_discrete_levels(self):
        """All 5 discrete contribution levels are covered (no level falls in a gap)."""
        for score in CONTRIBUTION_LEVELS:
            in_range = any(lo <= score <= hi for lo, hi in ER_MAPPING.values())
            assert in_range, f"Score {score} falls in a gap between ER ranges"


# ---------------------------------------------------------------------------
# Template → Rubric References
# ---------------------------------------------------------------------------


class TestTemplateRubricReferences:

    def test_tier1_references_contribution_rubric(self, tier1_content):
        assert "rubrics/contribution-factor.md" in tier1_content

    def test_tier2_references_contribution_rubric(self, tier2_content):
        assert "rubrics/contribution-factor.md" in tier2_content

    def test_tier2_references_complexity_rubric(self, tier2_content):
        assert "rubrics/complexity-factor.md" in tier2_content

    def test_process_guide_references_all_templates(self, process_guide_content):
        for template in [
            "templates/tier1-assessment.md",
            "templates/tier2-assessment.md",
            "templates/calibration-agenda.md",
        ]:
            assert template in process_guide_content, (
                f"process-guide.md missing reference to {template}"
            )


# ---------------------------------------------------------------------------
# Process Guide → Rubric References
# ---------------------------------------------------------------------------


class TestProcessGuideRubricReferences:

    def test_references_contribution_rubric(self, process_guide_content):
        assert "rubrics/contribution-factor.md" in process_guide_content

    def test_references_complexity_rubric(self, process_guide_content):
        assert "rubrics/complexity-factor.md" in process_guide_content

    def test_references_gaming_detection(self, process_guide_content):
        assert "rubrics/gaming-detection.md" in process_guide_content


# ---------------------------------------------------------------------------
# Expected Ranges Consistency
# ---------------------------------------------------------------------------


class TestExpectedRangesConsistency:

    def test_ranges_in_tier2_match_framework(self, framework_content, tier2_content):
        """The expected ranges in framework.md appear in tier2's Quarter Summary."""
        # framework.md uses "2x -- 10x" with spaces; tier2 uses "2x--10x"
        # Normalize by removing all spaces around dashes
        def normalize(text: str) -> str:
            return text.replace(" -- ", "--").replace(" - ", "-")

        fw = normalize(framework_content)
        t2 = normalize(tier2_content)

        range_strings = ["2x--10x", "1.5x--5x", "1x--3x", "0.1x--0.5x"]
        for rs in range_strings:
            assert rs in fw, f"Range {rs} not found in framework.md"
            assert rs in t2, f"Range {rs} not found in tier2-assessment.md"


# ---------------------------------------------------------------------------
# Template Sections Match Process Guide
# ---------------------------------------------------------------------------


class TestTemplateSectionsMatchProcessGuide:

    def test_tier1_has_sections_for_all_phases(self, tier1_content):
        """Tier 1 has sections for: self-assessment (Phase 3), manager review, calibration."""
        headings = [h for _, h in extract_headings(tier1_content)]
        required = ["Self-Assessment Summary", "Manager Review", "Calibration Notes"]
        for section in required:
            assert any(section in h for h in headings), (
                f"Tier 1 missing phase section: {section}"
            )

    def test_tier2_has_all_phase_sections(self, tier2_content):
        """Tier 2 has all Phase 3/4 sections plus advanced sections."""
        headings = [h for _, h in extract_headings(tier2_content)]
        required = [
            "Self-Assessment Summary",
            "Manager Review",
            "Calibration Notes",
            "Cross-Quarter Trend",
            "Development Goals",
        ]
        for section in required:
            assert any(section in h for h in headings), (
                f"Tier 2 missing phase section: {section}"
            )
