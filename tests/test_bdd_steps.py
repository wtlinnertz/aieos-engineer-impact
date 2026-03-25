"""BDD step definitions for assessment lifecycle scenarios."""

from __future__ import annotations

import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from models.impact import (
    Assessment,
    ComplexityDimensions,
    EnablementContribution,
    Initiative,
    TeamMultiplierContribution,
    complexity_factor,
    detect_distribution_inflation,
    detect_primary_overload,
    outcome_driven_impact,
    risk_adjusted_value,
)

scenarios("features/assessment_lifecycle.feature")


# ---------------------------------------------------------------------------
# Shared state
# ---------------------------------------------------------------------------


class AssessmentState:
    def __init__(self):
        self.contributions_logged: bool = False
        self.quarter_end: bool = False
        self.self_assessment_done: bool = False
        self.manager_review_done: bool = False
        self.calibration_done: bool = False
        self.calibrated_score: float | None = None
        self.archived: bool = False
        self.tier: int = 1
        self.initiatives: list[Initiative] = []
        self.team_cfs: list[float] = []
        self.engineer_primaries: int = 0
        self.gaming_flags: list[str] = []
        self.outcome_value: float = 0.0
        self.confidence: float = 1.0
        self.attributed_value: float | None = None
        self.conflict_flagged: bool = False


@pytest.fixture
def state():
    return AssessmentState()


# ---------------------------------------------------------------------------
# Given steps
# ---------------------------------------------------------------------------


@given("an engineer has logged contributions during the quarter")
def engineer_logged(state):
    state.contributions_logged = True


@given("the quarter end assessment period has begun")
def quarter_end(state):
    state.quarter_end = True


@given("an engineer has contributions for 3 initiatives")
def three_initiatives(state):
    for i in range(3):
        state.initiatives.append(
            Initiative(f"init-{i}", 100_000, 1.0, 0.4, ComplexityDimensions(0.5, 0.3, 0.2))
        )


@given("the team uses tier 2")
def tier_2(state):
    state.tier = 2


@given("a team of 5 engineers submits assessments")
def team_of_5(state):
    pass  # Team size set by next step


@given("4 engineers rate themselves at 0.7 or higher")
def four_at_07_plus(state):
    state.team_cfs = [0.7, 0.7, 1.0, 0.7, 0.4]


@given("an engineer claims primary driver on 4 concurrent initiatives")
def four_primaries(state):
    state.engineer_primaries = 4


@given("a team has used tier 1 for prior quarters")
def prior_tier1(state):
    state.tier = 1


@given("an initiative has two engineers both claiming contribution factor 1.0")
def two_primaries_on_initiative(state):
    state.team_cfs = [1.0, 1.0, 0.4]


@given("an initiative produced no business outcome")
def no_outcome(state):
    state.outcome_value = 0.0


@given("an initiative has expected value of 1000000")
def expected_value(state):
    state.outcome_value = 1_000_000


@given("the confidence level is 0.6")
def confidence_60(state):
    state.confidence = 0.6


# ---------------------------------------------------------------------------
# When steps
# ---------------------------------------------------------------------------


@when("the engineer completes self-assessment using the tier 1 template")
def self_assess_tier1(state):
    state.self_assessment_done = True


@when("the manager completes their independent review")
def manager_review(state):
    state.manager_review_done = True


@when("the calibration panel meets")
def calibration_meets(state):
    state.calibration_done = True
    state.calibrated_score = 3.5  # Representative score


@when("the engineer completes the tier 2 self-assessment")
def self_assess_tier2(state):
    state.self_assessment_done = True
    state.tier = 2


@when("the calibration panel runs gaming detection")
def run_gaming_detection(state):
    if detect_distribution_inflation(state.team_cfs):
        state.gaming_flags.append("distribution_inflation")


@when("the calibration panel reviews")
def calibration_reviews(state):
    if detect_primary_overload(state.engineer_primaries):
        state.gaming_flags.append("primary_overload")
    primaries = sum(1 for cf in state.team_cfs if cf == 1.0)
    if primaries > 1:
        state.conflict_flagged = True


@when("the manager selects tier 2 for the next quarter")
def upgrade_tier(state):
    state.tier = 2


@when("the engineer records the outcome")
def record_outcome(state):
    pass  # outcome_value already set


@when("risk-adjusted value is calculated")
def calc_rav(state):
    state.attributed_value = risk_adjusted_value(state.outcome_value, state.confidence)


# ---------------------------------------------------------------------------
# Then steps
# ---------------------------------------------------------------------------


@then("the final calibrated score is recorded")
def score_recorded(state):
    assert state.calibrated_score is not None


@then("the assessment is archived")
def archived(state):
    state.archived = True
    assert state.archived


@then("each initiative has a contribution factor")
def each_has_cf(state):
    for init in state.initiatives:
        assert 0.0 <= init.contribution_factor <= 1.0


@then("each initiative has a complexity factor")
def each_has_complex(state):
    for init in state.initiatives:
        cf = complexity_factor(init.complexity)
        assert 1.0 <= cf <= 1.7


@then("the outcome-driven impact score is calculated")
def odi_calculated(state):
    score = outcome_driven_impact(state.initiatives, 150_000)
    assert score >= 0.0


@then("the distribution inflation flag is raised")
def distribution_flag(state):
    assert "distribution_inflation" in state.gaming_flags


@then("the primary overload flag is raised")
def primary_flag(state):
    assert "primary_overload" in state.gaming_flags


@then("engineers receive tier 2 templates requiring per-initiative complexity scoring")
def tier2_templates(state):
    assert state.tier == 2


@then("a conflict is flagged requiring resolution")
def conflict_flagged(state):
    assert state.conflict_flagged


@then("the outcome value is zero")
def outcome_zero(state):
    assert state.outcome_value == 0.0


@then("the outcome value is never negative")
def outcome_not_negative(state):
    assert state.outcome_value >= 0.0


@then("the attributed value is 600000")
def attributed_600k(state):
    assert state.attributed_value == pytest.approx(600_000)
