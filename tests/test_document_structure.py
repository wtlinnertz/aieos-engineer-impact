"""Category 5: Document structure validation — file existence, sections, vendor-free."""

import re

import pytest

from parsers.doc_parser import extract_headings


# ---------------------------------------------------------------------------
# Required Files
# ---------------------------------------------------------------------------

REQUIRED_FILES = [
    "CLAUDE.md",
    "README.md",
    "VERSION",
    "docs/framework.md",
    "docs/process-guide.md",
    "docs/aieos-integration.md",
    "docs/templates/tier1-assessment.md",
    "docs/templates/tier2-assessment.md",
    "docs/templates/calibration-agenda.md",
    "docs/rubrics/contribution-factor.md",
    "docs/rubrics/complexity-factor.md",
    "docs/rubrics/gaming-detection.md",
]


class TestRequiredFilesExist:

    @pytest.mark.parametrize("rel_path", REQUIRED_FILES)
    def test_required_file_exists(self, rel_path, project_root):
        path = project_root / rel_path
        assert path.exists(), f"Missing required file: {rel_path}"


# ---------------------------------------------------------------------------
# Document Control Sections
# ---------------------------------------------------------------------------


class TestDocumentControlSections:

    def test_tier1_has_document_control(self, tier1_content):
        headings = [h for _, h in extract_headings(tier1_content)]
        assert "Document Control" in headings

    def test_tier2_has_document_control(self, tier2_content):
        headings = [h for _, h in extract_headings(tier2_content)]
        assert "Document Control" in headings

    def test_calibration_has_meeting_details(self, calibration_content):
        headings = [h for _, h in extract_headings(calibration_content)]
        assert "Meeting Details" in headings


# ---------------------------------------------------------------------------
# Tier 1 Structure
# ---------------------------------------------------------------------------

FOUR_DIMENSIONS = [
    "Outcome-Driven Impact",
    "Enablement Impact",
    "Operational Excellence",
    "Team Multiplier",
]


class TestTier1Structure:

    def test_tier1_has_four_dimensions(self, tier1_content):
        headings = [h for _, h in extract_headings(tier1_content)]
        for dim in FOUR_DIMENSIONS:
            matches = [h for h in headings if dim in h]
            assert matches, f"Tier 1 missing dimension heading: {dim}"

    def test_tier1_has_assessment_sections(self, tier1_content):
        headings = [h for _, h in extract_headings(tier1_content)]
        for section in ["Self-Assessment Summary", "Manager Review", "Calibration Notes"]:
            assert any(section in h for h in headings), (
                f"Tier 1 missing section: {section}"
            )


# ---------------------------------------------------------------------------
# Tier 2 Structure
# ---------------------------------------------------------------------------


class TestTier2Structure:

    def test_tier2_has_four_dimensions(self, tier2_content):
        headings = [h for _, h in extract_headings(tier2_content)]
        for dim in FOUR_DIMENSIONS:
            matches = [h for h in headings if dim in h]
            assert matches, f"Tier 2 missing dimension heading: {dim}"

    def test_tier2_has_per_initiative_detail(self, tier2_content):
        headings = [h for _, h in extract_headings(tier2_content)]
        assert any("Per-Initiative Detail" in h for h in headings)

    def test_tier2_has_advanced_sections(self, tier2_content):
        headings = [h for _, h in extract_headings(tier2_content)]
        for section in [
            "Cross-Quarter Trend",
            "Risk-Adjusted Value",
            "Development Goals",
            "Quarter Summary",
        ]:
            assert any(section in h for h in headings), (
                f"Tier 2 missing advanced section: {section}"
            )


# ---------------------------------------------------------------------------
# Calibration Agenda Structure
# ---------------------------------------------------------------------------


class TestCalibrationAgendaStructure:

    def test_calibration_has_six_agenda_items(self, calibration_content):
        headings = [h for _, h in extract_headings(calibration_content)]
        expected_items = [
            "Distribution Review",
            "Complexity Factor Review",
            "Engineer Walk-Through",
            "Outcome Value Spot-Check",
            "Gaming Detection Review",
            "Process Retrospective",
        ]
        for item in expected_items:
            assert any(item in h for h in headings), (
                f"Calibration agenda missing item: {item}"
            )


# ---------------------------------------------------------------------------
# No Tool-Specific References
# ---------------------------------------------------------------------------

VENDOR_TERMS = ["GitHub", "Jira", "Confluence", "Slack", "Linear", "Notion"]

# Files that should be vendor-free (rubrics and framework)
VENDOR_FREE_FILES = [
    "docs/framework.md",
    "docs/rubrics/contribution-factor.md",
    "docs/rubrics/complexity-factor.md",
    "docs/rubrics/gaming-detection.md",
]


class TestNoToolSpecificReferences:

    @pytest.mark.parametrize("rel_path", VENDOR_FREE_FILES)
    def test_no_vendor_references(self, rel_path, project_root):
        content = (project_root / rel_path).read_text()
        for term in VENDOR_TERMS:
            # Case-insensitive word boundary match to avoid false positives
            matches = re.findall(rf"\b{term}\b", content, re.IGNORECASE)
            assert not matches, (
                f"Found vendor reference '{term}' in {rel_path}"
            )


# ---------------------------------------------------------------------------
# Non-Negotiable Exclusions in Docs
# ---------------------------------------------------------------------------


class TestNonNegotiableExclusionsInDocs:

    def test_framework_lists_all_exclusions(self, framework_content):
        content_lower = framework_content.lower()
        exclusions = [
            "story points", "story count", "lines of code", "commit counts",
            "individual velocity", "time tracking", "code churn",
            "review comment count",
        ]
        for excl in exclusions:
            assert excl in content_lower, (
                f"framework.md missing exclusion: {excl}"
            )

    def test_claude_md_mentions_exclusions(self, claude_md_content):
        content_lower = claude_md_content.lower()
        # CLAUDE.md mentions the key exclusions
        for excl in ["story points", "lines of code", "commit counts"]:
            assert excl in content_lower, (
                f"CLAUDE.md missing key exclusion: {excl}"
            )
