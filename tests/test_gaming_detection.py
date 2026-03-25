"""Category 4: Gaming detection logic — parametrized scenarios."""

import pytest

from models.impact import (
    detect_cf_sum_inflation,
    detect_complexity_inflation,
    detect_declining_scores,
    detect_distribution_inflation,
    detect_missing_team_multiplier,
    detect_primary_overload,
)


# ---------------------------------------------------------------------------
# Distribution Sanity (>50% at 0.7+ is flagged)
# ---------------------------------------------------------------------------


class TestDistributionSanity:

    def test_healthy_distribution_passes(self):
        cfs = [0.2, 0.2, 0.4, 0.4, 0.7]  # 20% at 0.7+
        assert detect_distribution_inflation(cfs) is False

    def test_inflated_distribution_flagged(self):
        cfs = [0.7, 0.7, 1.0, 0.7, 0.4]  # 60% at 0.7+
        assert detect_distribution_inflation(cfs) is True

    def test_exactly_50_percent_not_flagged(self):
        """The rule is >50%, so exactly 50% should NOT be flagged."""
        cfs = [0.7, 0.7, 0.4, 0.4]  # exactly 50%
        assert detect_distribution_inflation(cfs) is False

    def test_empty_list_not_flagged(self):
        assert detect_distribution_inflation([]) is False


# ---------------------------------------------------------------------------
# Primary Overload (3+ concurrent primaries)
# ---------------------------------------------------------------------------


class TestPrimaryOverload:

    def test_two_primaries_ok(self):
        assert detect_primary_overload(2) is False

    def test_three_primaries_flagged(self):
        assert detect_primary_overload(3) is True

    def test_five_primaries_flagged(self):
        assert detect_primary_overload(5) is True


# ---------------------------------------------------------------------------
# CF Sum Inflation (>1.5 on same initiative)
# ---------------------------------------------------------------------------


class TestCFSumInflation:

    def test_sum_at_1_5_ok(self):
        assert detect_cf_sum_inflation(1.5) is False

    def test_sum_at_1_6_flagged(self):
        assert detect_cf_sum_inflation(1.6) is True

    def test_sum_at_2_0_flagged(self):
        assert detect_cf_sum_inflation(2.0) is True


# ---------------------------------------------------------------------------
# Complexity Inflation (ALL projects 1.5+)
# ---------------------------------------------------------------------------


class TestComplexityInflation:

    def test_mixed_complexity_ok(self):
        assert detect_complexity_inflation([1.2, 1.5, 1.0]) is False

    def test_all_high_complexity_flagged(self):
        assert detect_complexity_inflation([1.5, 1.6, 1.7]) is True

    def test_all_maximum_flagged(self):
        assert detect_complexity_inflation([1.7, 1.7, 1.7]) is True


# ---------------------------------------------------------------------------
# Missing Team Multiplier (Staff+ with 0 for 2+ quarters)
# ---------------------------------------------------------------------------


class TestMissingTeamMultiplier:

    def test_non_staff_zero_ok(self):
        assert detect_missing_team_multiplier(0.0, is_staff_plus=False, quarters_zero=3) is False

    def test_staff_one_quarter_zero_ok(self):
        assert detect_missing_team_multiplier(0.0, is_staff_plus=True, quarters_zero=1) is False

    def test_staff_two_quarters_zero_flagged(self):
        assert detect_missing_team_multiplier(0.0, is_staff_plus=True, quarters_zero=2) is True

    def test_staff_with_some_tm_ok(self):
        assert detect_missing_team_multiplier(0.1, is_staff_plus=True, quarters_zero=0) is False


# ---------------------------------------------------------------------------
# Declining Scores (monotonically declining over 2+ points)
# ---------------------------------------------------------------------------


class TestDecliningScores:

    def test_increasing_scores_ok(self):
        assert detect_declining_scores([3.0, 4.0, 5.0]) is False

    def test_stable_scores_ok(self):
        assert detect_declining_scores([3.0, 3.0, 3.0]) is False

    def test_declining_two_quarters_flagged(self):
        assert detect_declining_scores([5.0, 3.0]) is True

    def test_decline_then_recovery_ok(self):
        """Not monotonically declining if recovery happens."""
        assert detect_declining_scores([5.0, 3.0, 4.0]) is False


# ---------------------------------------------------------------------------
# Realistic Multi-Factor Scenarios
# ---------------------------------------------------------------------------


class TestRealisticScenarios:

    def test_healthy_team_no_flags(self):
        """A realistic healthy team triggers no gaming flags."""
        team_cfs = [0.2, 0.4, 0.4, 0.7, 0.2]
        team_complexities = [1.1, 1.2, 1.0, 1.4, 1.05]
        initiative_cf_sum = 0.2 + 0.4 + 0.7  # one initiative with 3 contributors

        assert detect_distribution_inflation(team_cfs) is False
        assert detect_complexity_inflation(team_complexities) is False
        assert detect_cf_sum_inflation(initiative_cf_sum) is False

    def test_inflated_team_multiple_flags(self):
        """A team with inflated scores triggers multiple flags."""
        team_cfs = [0.7, 0.7, 1.0, 0.7, 0.7]
        team_complexities = [1.5, 1.6, 1.7, 1.5, 1.5]

        assert detect_distribution_inflation(team_cfs) is True
        assert detect_complexity_inflation(team_complexities) is True

    def test_cherry_picker_scenario(self):
        """One engineer claiming 3 primaries on all high-complexity projects."""
        assert detect_primary_overload(3) is True
        assert detect_complexity_inflation([1.5, 1.6, 1.5]) is True
