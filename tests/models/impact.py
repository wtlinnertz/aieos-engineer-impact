"""Engineer Impact Framework — canonical model.

Dataclasses, formulas, constants, and gaming detection functions.
Every formula matches the definitions in docs/framework.md and docs/rubrics/.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CONTRIBUTION_LEVELS: dict[float, str] = {
    1.0: "Primary Driver",
    0.7: "Major Contributor",
    0.4: "Meaningful Contributor",
    0.2: "Supporting Contributor",
    0.1: "Peripheral Contributor",
}

COMPLEXITY_FACTOR_RANGE: tuple[float, float] = (1.0, 1.7)
CONTRIBUTION_FACTOR_RANGE: tuple[float, float] = (0.0, 1.0)
CONFIDENCE_RANGE: tuple[float, float] = (0.0, 1.0)

EXPECTED_ROI_RANGES: dict[str, tuple[float, float]] = {
    "Outcome-Driven Impact": (2.0, 10.0),
    "Enablement Impact": (1.5, 5.0),
    "Operational Excellence": (1.0, 3.0),
    "Team Multiplier": (0.1, 0.5),
}

NON_NEGOTIABLE_EXCLUSIONS: list[str] = [
    "story points",
    "story count",
    "lines of code",
    "commit counts",
    "individual velocity",
    "PR count",
    "time tracking",
    "code churn",
    "review comment count",
    "delivery time per engineer",
]

ER_MAPPING: dict[str, tuple[float, float]] = {
    "Primary": (0.7, 1.0),
    "Significant": (0.4, 0.6),
    "Supporting": (0.1, 0.3),
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class ComplexityDimensions:
    """Three dimensions scored 0.0-1.0 each."""

    risk: float
    novelty: float
    org_friction: float

    def __post_init__(self) -> None:
        for name in ("risk", "novelty", "org_friction"):
            val = getattr(self, name)
            if not 0.0 <= val <= 1.0:
                raise ValueError(
                    f"{name} must be between 0.0 and 1.0, got {val}"
                )


@dataclass
class Initiative:
    """One initiative's outcome data for Dimension 1."""

    name: str
    outcome_value: float
    confidence: float = 1.0
    contribution_factor: float = 1.0
    complexity: ComplexityDimensions = field(
        default_factory=lambda: ComplexityDimensions(0.0, 0.0, 0.0)
    )

    def __post_init__(self) -> None:
        if self.outcome_value < 0:
            raise ValueError(
                f"outcome_value must be non-negative, got {self.outcome_value}"
            )
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                f"confidence must be between 0.0 and 1.0, got {self.confidence}"
            )
        if not 0.0 <= self.contribution_factor <= 1.0:
            raise ValueError(
                f"contribution_factor must be between 0.0 and 1.0, "
                f"got {self.contribution_factor}"
            )


@dataclass
class EnablementContribution:
    description: str
    productivity_gain: float
    contribution_factor: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.contribution_factor <= 1.0:
            raise ValueError(
                f"contribution_factor must be between 0.0 and 1.0, "
                f"got {self.contribution_factor}"
            )


@dataclass
class OpsContribution:
    description: str
    cost_avoided: float = 0.0
    reliability_value: float = 0.0
    contribution_factor: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.contribution_factor <= 1.0:
            raise ValueError(
                f"contribution_factor must be between 0.0 and 1.0, "
                f"got {self.contribution_factor}"
            )


@dataclass
class TeamMultiplierContribution:
    description: str
    productivity_increase: float


@dataclass
class Assessment:
    """Full quarterly assessment for one engineer."""

    engineer_cost: float
    initiatives: list[Initiative] = field(default_factory=list)
    enablement: list[EnablementContribution] = field(default_factory=list)
    ops: list[OpsContribution] = field(default_factory=list)
    team_multiplier: list[TeamMultiplierContribution] = field(
        default_factory=list
    )


# ---------------------------------------------------------------------------
# Formula functions
# ---------------------------------------------------------------------------

def complexity_factor(dims: ComplexityDimensions) -> float:
    """CF = 1.0 + (Risk * 0.3) + (Novelty * 0.2) + (Org Friction * 0.2)"""
    return 1.0 + (dims.risk * 0.3) + (dims.novelty * 0.2) + (dims.org_friction * 0.2)


def risk_adjusted_value(expected_value: float, confidence: float) -> float:
    """Attributed Value = Expected Value * Confidence Level"""
    if not 0.0 <= confidence <= 1.0:
        raise ValueError(f"confidence must be between 0.0 and 1.0, got {confidence}")
    return expected_value * confidence


def outcome_driven_impact(
    initiatives: list[Initiative], engineer_cost: float
) -> float:
    """SUM((OV * Confidence) * CF * ComplexF) / Engineer Cost"""
    total = 0.0
    for init in initiatives:
        cf = complexity_factor(init.complexity)
        total += (
            init.outcome_value * init.confidence * init.contribution_factor * cf
        )
    return total / engineer_cost


def enablement_impact(
    contributions: list[EnablementContribution], engineer_cost: float
) -> float:
    """(SUM Productivity Gains * Contribution Factor) / Engineer Cost"""
    total = sum(c.productivity_gain * c.contribution_factor for c in contributions)
    return total / engineer_cost


def operational_excellence(
    contributions: list[OpsContribution], engineer_cost: float
) -> float:
    """(SUM(Cost Avoided + Reliability Value) * Contribution Factor) / Cost"""
    total = sum(
        (c.cost_avoided + c.reliability_value) * c.contribution_factor
        for c in contributions
    )
    return total / engineer_cost


def team_multiplier_score(
    contributions: list[TeamMultiplierContribution], engineer_cost: float
) -> float:
    """Team Productivity Increase / Engineer Cost"""
    total = sum(c.productivity_increase for c in contributions)
    return total / engineer_cost


def total_engineer_value(assessment: Assessment) -> float:
    """Sum of all four dimensions."""
    return (
        outcome_driven_impact(assessment.initiatives, assessment.engineer_cost)
        + enablement_impact(assessment.enablement, assessment.engineer_cost)
        + operational_excellence(assessment.ops, assessment.engineer_cost)
        + team_multiplier_score(
            assessment.team_multiplier, assessment.engineer_cost
        )
    )


# ---------------------------------------------------------------------------
# Gaming detection functions
# ---------------------------------------------------------------------------

def detect_distribution_inflation(contribution_factors: list[float]) -> bool:
    """Returns True if >50% of CFs are at 0.7 or higher."""
    if not contribution_factors:
        return False
    high_count = sum(1 for cf in contribution_factors if cf >= 0.7)
    return high_count / len(contribution_factors) > 0.5


def detect_primary_overload(engineer_primaries: int) -> bool:
    """Returns True if engineer claims Primary Driver on 3+ concurrent initiatives."""
    return engineer_primaries >= 3


def detect_cf_sum_inflation(cf_sum: float) -> bool:
    """Returns True if CF sum on same initiative exceeds 1.5."""
    return cf_sum > 1.5


def detect_complexity_inflation(complexity_factors: list[float]) -> bool:
    """Returns True if ALL projects on team are rated 1.5+."""
    if not complexity_factors:
        return False
    return all(cf >= 1.5 for cf in complexity_factors)


def detect_missing_team_multiplier(
    score: float, is_staff_plus: bool, quarters_zero: int
) -> bool:
    """Returns True if Staff+ engineer has zero Team Multiplier for 2+ quarters."""
    if not is_staff_plus:
        return False
    return score == 0.0 and quarters_zero >= 2


def detect_declining_scores(scores: list[float]) -> bool:
    """Returns True if scores are monotonically declining over 2+ data points."""
    if len(scores) < 2:
        return False
    return all(scores[i] > scores[i + 1] for i in range(len(scores) - 1))
