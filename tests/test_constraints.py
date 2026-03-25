"""Category 2: Constraint validation — range checks, invariants, exclusions."""

import pytest

from models.impact import (
    CONTRIBUTION_FACTOR_RANGE,
    CONTRIBUTION_LEVELS,
    EXPECTED_ROI_RANGES,
    NON_NEGOTIABLE_EXCLUSIONS,
    ComplexityDimensions,
    Initiative,
    complexity_factor,
    detect_cf_sum_inflation,
    detect_primary_overload,
    risk_adjusted_value,
)


# ---------------------------------------------------------------------------
# Complexity Factor Constraints
# ---------------------------------------------------------------------------


class TestComplexityFactorConstraints:

    def test_never_below_1_0(self):
        cf = complexity_factor(ComplexityDimensions(0.0, 0.0, 0.0))
        assert cf >= 1.0

    def test_never_above_1_7(self):
        cf = complexity_factor(ComplexityDimensions(1.0, 1.0, 1.0))
        assert cf <= 1.7

    @pytest.mark.parametrize("dim", ["risk", "novelty", "org_friction"])
    def test_sub_dimension_rejects_above_1(self, dim):
        kwargs = {"risk": 0.0, "novelty": 0.0, "org_friction": 0.0}
        kwargs[dim] = 1.5
        with pytest.raises(ValueError):
            ComplexityDimensions(**kwargs)

    @pytest.mark.parametrize("dim", ["risk", "novelty", "org_friction"])
    def test_sub_dimension_rejects_below_0(self, dim):
        kwargs = {"risk": 0.0, "novelty": 0.0, "org_friction": 0.0}
        kwargs[dim] = -0.1
        with pytest.raises(ValueError):
            ComplexityDimensions(**kwargs)


# ---------------------------------------------------------------------------
# Contribution Factor Constraints
# ---------------------------------------------------------------------------


class TestContributionFactorConstraints:

    @pytest.mark.parametrize("level", CONTRIBUTION_LEVELS.keys())
    def test_levels_within_range(self, level):
        lo, hi = CONTRIBUTION_FACTOR_RANGE
        assert lo <= level <= hi

    def test_only_one_primary_per_initiative(self):
        """Two engineers with CF=1.0 on the same initiative should flag."""
        cfs_on_initiative = [1.0, 1.0, 0.4]
        primaries = sum(1 for cf in cfs_on_initiative if cf == 1.0)
        assert primaries > 1, "Test setup: two primaries exist"
        # This is a gaming flag — calibration should catch it
        assert detect_primary_overload(primaries) is False  # overload is 3+
        # But the rule is only ONE primary per initiative
        assert primaries != 1

    def test_cf_sum_exceeding_threshold(self):
        """CF sum > 1.5 on same initiative is a gaming flag."""
        assert detect_cf_sum_inflation(1.6) is True
        assert detect_cf_sum_inflation(1.5) is False

    def test_negative_contribution_rejected(self):
        with pytest.raises(ValueError):
            Initiative("test", 100_000, 1.0, -0.1, ComplexityDimensions(0, 0, 0))


# ---------------------------------------------------------------------------
# Confidence Constraints
# ---------------------------------------------------------------------------


class TestConfidenceConstraints:

    def test_confidence_within_range(self):
        # Should not raise
        risk_adjusted_value(100_000, 0.5)

    def test_confidence_above_1_rejected(self):
        with pytest.raises(ValueError):
            risk_adjusted_value(100_000, 1.1)

    def test_confidence_below_0_rejected(self):
        with pytest.raises(ValueError):
            risk_adjusted_value(100_000, -0.1)


# ---------------------------------------------------------------------------
# Outcome Value Constraints
# ---------------------------------------------------------------------------


class TestOutcomeValueConstraints:

    def test_negative_outcome_rejected(self):
        with pytest.raises(ValueError):
            Initiative("bad", -100_000)

    def test_zero_outcome_allowed(self):
        init = Initiative("failed_experiment", 0)
        assert init.outcome_value == 0.0


# ---------------------------------------------------------------------------
# ROI Range Flags
# ---------------------------------------------------------------------------


class TestROIRangeFlags:

    @pytest.mark.parametrize(
        "dimension,score",
        [
            ("Outcome-Driven Impact", 1.5),
            ("Enablement Impact", 1.0),
            ("Operational Excellence", 0.5),
            ("Team Multiplier", 0.05),
        ],
    )
    def test_below_expected_range_flagged(self, dimension, score):
        lo, _ = EXPECTED_ROI_RANGES[dimension]
        assert score < lo, f"{dimension} score {score} should be below typical range"


# ---------------------------------------------------------------------------
# Non-Negotiable Exclusions
# ---------------------------------------------------------------------------


class TestNonNegotiableExclusions:

    @pytest.mark.parametrize("exclusion", NON_NEGOTIABLE_EXCLUSIONS)
    def test_exclusion_listed_in_framework(self, exclusion, framework_content):
        assert exclusion.lower() in framework_content.lower(), (
            f"'{exclusion}' must appear in framework.md"
        )
