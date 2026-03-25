"""Category 1: Formula validation — pure unit tests for all calculations.

Every worked example from framework.md and rubric files is a test case.
"""

import pytest

from models.impact import (
    Assessment,
    ComplexityDimensions,
    EnablementContribution,
    Initiative,
    OpsContribution,
    TeamMultiplierContribution,
    complexity_factor,
    enablement_impact,
    operational_excellence,
    outcome_driven_impact,
    risk_adjusted_value,
    team_multiplier_score,
    total_engineer_value,
)


# ---------------------------------------------------------------------------
# Complexity Factor
# ---------------------------------------------------------------------------


class TestComplexityFactor:
    """CF = 1.0 + (Risk * 0.3) + (Novelty * 0.2) + (Org Friction * 0.2)"""

    def test_minimum_complexity(self):
        assert complexity_factor(ComplexityDimensions(0, 0, 0)) == pytest.approx(1.0)

    def test_maximum_complexity(self):
        assert complexity_factor(ComplexityDimensions(1, 1, 1)) == pytest.approx(1.7)

    def test_risk_only_max(self):
        assert complexity_factor(ComplexityDimensions(1, 0, 0)) == pytest.approx(1.3)

    def test_novelty_only_max(self):
        assert complexity_factor(ComplexityDimensions(0, 1, 0)) == pytest.approx(1.2)

    def test_org_friction_only_max(self):
        assert complexity_factor(ComplexityDimensions(0, 0, 1)) == pytest.approx(1.2)

    def test_midpoint(self):
        assert complexity_factor(ComplexityDimensions(0.5, 0.5, 0.5)) == pytest.approx(1.35)

    def test_example1_routine_feature(self):
        """complexity-factor.md Example 1: Risk=0, Novelty=0.25, Friction=0 -> 1.05"""
        dims = ComplexityDimensions(risk=0.0, novelty=0.25, org_friction=0.0)
        assert complexity_factor(dims) == pytest.approx(1.05)

    def test_example2_cross_team_migration(self):
        """complexity-factor.md Example 2: Risk=0.75, Novelty=0.5, Friction=0.5 -> 1.425"""
        dims = ComplexityDimensions(risk=0.75, novelty=0.5, org_friction=0.5)
        assert complexity_factor(dims) == pytest.approx(1.425)

    def test_example3_maximum(self):
        """complexity-factor.md Example 3 + framework.md example: all 1.0 -> 1.7"""
        dims = ComplexityDimensions(risk=1.0, novelty=1.0, org_friction=1.0)
        assert complexity_factor(dims) == pytest.approx(1.7)


# ---------------------------------------------------------------------------
# Risk-Adjusted Value
# ---------------------------------------------------------------------------


class TestRiskAdjustedValue:

    def test_full_confidence(self):
        assert risk_adjusted_value(1_000_000, 1.0) == pytest.approx(1_000_000)

    def test_framework_example(self):
        """framework.md: $1M * 0.6 = $600k"""
        assert risk_adjusted_value(1_000_000, 0.6) == pytest.approx(600_000)

    def test_zero_confidence(self):
        assert risk_adjusted_value(1_000_000, 0.0) == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# Outcome-Driven Impact
# ---------------------------------------------------------------------------


class TestOutcomeDrivenImpact:

    def test_single_initiative_baseline(self):
        """$100k outcome, CF=1.0, ComplexF=1.0, Cost=$100k -> 1.0x"""
        init = Initiative("test", 100_000, 1.0, 1.0, ComplexityDimensions(0, 0, 0))
        assert outcome_driven_impact([init], 100_000) == pytest.approx(1.0)

    def test_multiple_initiatives_sum(self):
        """Two initiatives: scores sum correctly."""
        i1 = Initiative("a", 100_000, 1.0, 1.0, ComplexityDimensions(0, 0, 0))
        i2 = Initiative("b", 200_000, 1.0, 0.5, ComplexityDimensions(0, 0, 0))
        # (100k*1*1*1 + 200k*1*0.5*1) / 100k = (100k + 100k) / 100k = 2.0
        assert outcome_driven_impact([i1, i2], 100_000) == pytest.approx(2.0)

    def test_with_complexity_factor_boost(self):
        """Complexity > 1.0 boosts the score."""
        dims = ComplexityDimensions(1.0, 1.0, 1.0)  # CF = 1.7
        init = Initiative("hard", 100_000, 1.0, 1.0, dims)
        # 100k * 1.0 * 1.0 * 1.7 / 100k = 1.7
        assert outcome_driven_impact([init], 100_000) == pytest.approx(1.7)


# ---------------------------------------------------------------------------
# Enablement Impact
# ---------------------------------------------------------------------------


class TestEnablementImpact:

    def test_framework_example(self):
        """framework.md: CI/CD saves $396k, CF=1.0, cost=$170k -> 2.33x"""
        contrib = EnablementContribution("CI/CD", 396_000, 1.0)
        assert enablement_impact([contrib], 170_000) == pytest.approx(
            396_000 / 170_000, rel=1e-2
        )

    def test_multiple_contributions(self):
        c1 = EnablementContribution("tooling", 100_000, 1.0)
        c2 = EnablementContribution("docs", 50_000, 0.5)
        # (100k*1.0 + 50k*0.5) / 150k = 125k / 150k
        assert enablement_impact([c1, c2], 150_000) == pytest.approx(125_000 / 150_000)


# ---------------------------------------------------------------------------
# Operational Excellence
# ---------------------------------------------------------------------------


class TestOperationalExcellence:

    def test_framework_example(self):
        """framework.md: $300k cost avoided, $0 reliability, CF=1.0, cost=$160k -> 1.875"""
        contrib = OpsContribution("MTTR", cost_avoided=300_000, reliability_value=0, contribution_factor=1.0)
        assert operational_excellence([contrib], 160_000) == pytest.approx(300_000 / 160_000)

    def test_cost_plus_reliability(self):
        contrib = OpsContribution("combined", cost_avoided=200_000, reliability_value=100_000, contribution_factor=0.8)
        # (200k + 100k) * 0.8 / 160k = 240k / 160k = 1.5
        assert operational_excellence([contrib], 160_000) == pytest.approx(1.5)


# ---------------------------------------------------------------------------
# Team Multiplier
# ---------------------------------------------------------------------------


class TestTeamMultiplier:

    def test_framework_example(self):
        """framework.md: ($48k * 0.5) / $200k = 0.12x
        Note: the formula in the model sums productivity_increase directly.
        The framework example pre-applies the attribution factor in the numerator.
        """
        # Pre-computed: 2 mentees * $120k * 0.2 * 0.5 attribution = $24k
        contrib = TeamMultiplierContribution("mentorship", 24_000)
        assert team_multiplier_score([contrib], 200_000) == pytest.approx(0.12)

    def test_multiple_activities(self):
        c1 = TeamMultiplierContribution("mentoring", 20_000)
        c2 = TeamMultiplierContribution("tech talks", 10_000)
        # 30k / 200k = 0.15
        assert team_multiplier_score([c1, c2], 200_000) == pytest.approx(0.15)


# ---------------------------------------------------------------------------
# Total Engineer Value
# ---------------------------------------------------------------------------


class TestTotalEngineerValue:

    def test_sum_of_dimensions(self):
        assessment = Assessment(
            engineer_cost=100_000,
            initiatives=[Initiative("x", 200_000, 1.0, 1.0, ComplexityDimensions(0, 0, 0))],
            enablement=[EnablementContribution("tool", 150_000, 1.0)],
            ops=[OpsContribution("oncall", cost_avoided=100_000, contribution_factor=1.0)],
            team_multiplier=[TeamMultiplierContribution("mentor", 10_000)],
        )
        expected = (200_000 + 150_000 + 100_000 + 10_000) / 100_000
        assert total_engineer_value(assessment) == pytest.approx(expected)

    def test_empty_dimensions_zero(self):
        """No contributions in any dimension -> 0."""
        assessment = Assessment(engineer_cost=100_000)
        assert total_engineer_value(assessment) == pytest.approx(0.0)
