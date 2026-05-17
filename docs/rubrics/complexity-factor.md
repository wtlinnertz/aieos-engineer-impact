     1|# Complexity Factor Rubric
     2|
     3|The Complexity Factor prevents penalizing engineers who take on hard, risky, long-term work. It adjusts the impact score to credit difficulty.
     4|
     5|**Scale:** 1.0 - 1.7
     6|**Formula:** `Complexity Factor = 1.0 + (Risk x 0.3) + (Novelty x 0.2) + (Org Friction x 0.2)`
     7|
     8|The complexity factor is about the **work**, not the **person**. A senior engineer doing routine work gets 1.0. A junior engineer taking on a novel problem gets the appropriate complexity credit.
     9|
    10|---
    11|
    12|## Three Dimensions
    13|
    14|Each dimension is scored 0.0 - 1.0.
    15|
    16|### Dimension 1: Risk (Weight: 0.3)
    17|
    18|How likely is this work to fail, and how costly would failure be?
    19|
    20|| Score | Label | Criteria |
    21||-------|-------|----------|
    22|| **0.0** | Low risk | Well-understood problem with proven solutions. Failure unlikely. Clear rollback path. |
    23|| **0.25** | Minor risk | Mostly understood, with a few unknowns. Failure would be contained and recoverable. |
    24|| **0.5** | Moderate risk | Some unknowns. Failure would require significant rework. Partial rollback possible. |
    25|| **0.75** | High risk | Significant unknowns. Failure could affect other systems. Limited rollback options. |
    26|| **1.0** | Very high risk | Novel approach with no precedent. Failure could have broad blast radius. No proven rollback path. |
    27|
    28|**Examples:**
    29|- 0.0: Adding a new field to an existing API endpoint
    30|- 0.5: Migrating a database from one provider to another with zero downtime
    31|- 1.0: Replacing the core authentication system across all services simultaneously
    32|
    33|---
    34|
    35|### Dimension 2: Novelty (Weight: 0.2)
    36|
    37|How new is this work relative to what the organization has done before?
    38|
    39|| Score | Label | Criteria |
    40||-------|-------|----------|
    41|| **0.0** | Routine | Maintenance, minor iteration on existing patterns. The organization has done this many times. |
    42|| **0.25** | Incremental | New feature using established patterns and technologies. Familiar territory with minor extensions. |
    43|| **0.5** | Greenfield component | New component or service within a known system architecture. The building blocks are familiar; the assembly is new. |
    44|| **0.75** | New technology | Introducing a technology or pattern the organization hasn't used before. Requires learning and experimentation. |
    45|| **1.0** | Entirely novel | New architecture, unproven technology, or a problem space the organization has never addressed. No internal precedent. |
    46|
    47|**Examples:**
    48|- 0.0: Adding a new CRUD endpoint to an existing service
    49|- 0.5: Building a new microservice using the organization's standard service template
    50|- 1.0: Introducing event sourcing to an organization that has only used CRUD
    51|
    52|---
    53|
    54|### Dimension 3: Organizational Friction (Weight: 0.2)
    55|
    56|How many teams, stakeholders, and organizational boundaries does this work cross?
    57|
    58|| Score | Label | Criteria |
    59||-------|-------|----------|
    60|| **0.0** | Single team | Clear ownership within one team. No external dependencies or approvals needed. |
    61|| **0.25** | Minor coordination | One external dependency or approval needed. Mostly self-contained. |
    62|| **0.5** | Cross-team | Coordination across 2--3 teams. Shared interfaces or data contracts to negotiate. |
    63|| **0.75** | Cross-org | Dependencies span multiple org units. External stakeholders involved. May require compliance review. |
    64|| **1.0** | Maximum friction | Cross-org dependencies, external vendor coordination, regulatory or compliance requirements, executive approvals. |
    65|
    66|**Examples:**
    67|- 0.0: Fixing a bug in your own team's service
    68|- 0.5: Building an integration between your service and two other teams' APIs
    69|- 1.0: Implementing a compliance mandate that requires changes across 5 teams, legal review, and external auditor approval
    70|
    71|---
    72|
    73|## Quick Reference
    74|
    75|| Range | Label | Typical Scenarios |
    76||-------|-------|-------------------|
    77|| **1.0 - 1.2** | Standard | Routine work, single team, low risk. Most day-to-day engineering work. |
    78|| **1.2 - 1.4** | Moderate | Some unknowns, 2--3 teams involved, moderate risk. Typical feature development. |
    79|| **1.4 - 1.5** | High | New technology or significant cross-team coordination. Major feature or platform work. |
    80|| **1.5 - 1.7** | Exceptional | Novel approach, cross-org dependencies, high technical risk. Major migrations, new platforms, compliance overhauls. |
    81|
    82|---
    83|
    84|## Calculation Examples
    85|
    86|### Example 1: Routine Feature
    87|
    88|- Risk: 0.0 (well-understood)
    89|- Novelty: 0.25 (new feature, established patterns)
    90|- Org Friction: 0.0 (single team)
    91|- **Complexity Factor = 1.0 + (0.0 x 0.3) + (0.25 x 0.2) + (0.0 x 0.2) = 1.05**
    92|
    93|### Example 2: Cross-Team Migration
    94|
    95|- Risk: 0.75 (significant unknowns, limited rollback)
    96|- Novelty: 0.5 (greenfield migration tooling)
    97|- Org Friction: 0.5 (3 teams coordinating)
    98|- **Complexity Factor = 1.0 + (0.75 x 0.3) + (0.5 x 0.2) + (0.5 x 0.2) = 1.425**
    99|
   100|### Example 3: Maximum Complexity
   101|
   102|- Risk: 1.0 (novel approach, broad blast radius)
   103|- Novelty: 1.0 (entirely new architecture)
   104|- Org Friction: 1.0 (cross-org, external stakeholders, compliance)
   105|- **Complexity Factor = 1.0 + (1.0 x 0.3) + (1.0 x 0.2) + (1.0 x 0.2) = 1.7**
   106|
   107|---
   108|
   109|## Common Mistakes
   110|
   111|| Mistake | Why It's Wrong | What to Do Instead |
   112||---------|---------------|-------------------|
   113|| Rating all projects 1.5+ | Inflation removes the value of complexity credit | Most projects are 1.0--1.3. Reserve 1.5+ for genuinely exceptional difficulty. |
   114|| Rating based on the person's seniority | Complexity is about the work, not the person | A junior engineer on a hard project deserves the same complexity factor as a senior. |
   115|| Confusing "I worked hard" with complexity | Effort is not complexity | A task that takes 200 hours of routine work is still 1.0 complexity. |
   116|| Ignoring org friction | Coordination work is genuinely harder | If you spent 30% of your time on cross-team negotiation, that's real friction. Score it. |
   117|