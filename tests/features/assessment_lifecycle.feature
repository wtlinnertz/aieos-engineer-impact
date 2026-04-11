Feature: Assessment Lifecycle
  The quarterly impact assessment follows a defined four-phase process
  with specific roles, inputs, and outputs at each phase.

  # Happy Path
  Scenario: Complete quarterly assessment cycle
    Given an engineer has logged contributions during the quarter
    And the quarter end assessment period has begun
    When the engineer completes self-assessment using the tier 1 template
    And the manager completes their independent review
    And the calibration panel meets
    Then the final calibrated score is recorded
    And the assessment is archived

  Scenario: Tier 2 assessment includes per-initiative scoring
    Given an engineer has contributions for 3 initiatives
    And the team uses tier 2
    When the engineer completes the tier 2 self-assessment
    Then each initiative has a contribution factor
    And each initiative has a complexity factor
    And the outcome-driven impact score is calculated

  # Gaming Detection Path
  Scenario: Calibration flags inflated team scores
    Given a team of 5 engineers submits assessments
    And 4 engineers rate themselves at 0.7 or higher
    When the calibration panel runs gaming detection
    Then the distribution inflation flag is raised

  Scenario: Engineer claims primary driver on too many initiatives
    Given an engineer claims primary driver on 4 concurrent initiatives
    When the calibration panel reviews
    Then the primary overload flag is raised

  # Tier Upgrade Path
  Scenario: Team upgrades from tier 1 to tier 2
    Given a team has used tier 1 for prior quarters
    When the manager selects tier 2 for the next quarter
    Then engineers receive tier 2 templates requiring per-initiative complexity scoring

  # Constraint Enforcement
  Scenario: Only one primary driver per initiative
    Given an initiative has two engineers both claiming contribution factor 1.0
    When the calibration panel reviews
    Then a conflict is flagged requiring resolution

  Scenario: Failed experiment does not produce negative scores
    Given an initiative produced no business outcome
    When the engineer records the outcome
    Then the outcome value is zero
    And the outcome value is never negative

  Scenario: Uncertain outcome is discounted by confidence
    Given an initiative has expected value of 1000000
    And the confidence level is 0.6
    When risk-adjusted value is calculated
    Then the attributed value is 600000
