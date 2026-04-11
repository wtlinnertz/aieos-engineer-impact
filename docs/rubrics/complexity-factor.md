# Complexity Factor Rubric

The Complexity Factor prevents penalizing engineers who take on hard, risky, long-term work. It adjusts the impact score to credit difficulty.

**Scale:** 1.0 -- 1.7
**Formula:** `Complexity Factor = 1.0 + (Risk x 0.3) + (Novelty x 0.2) + (Org Friction x 0.2)`

The complexity factor is about the **work**, not the **person**. A senior engineer doing routine work gets 1.0. A junior engineer taking on a novel problem gets the appropriate complexity credit.

---

## Three Dimensions

Each dimension is scored 0.0 -- 1.0.

### Dimension 1: Risk (Weight: 0.3)

How likely is this work to fail, and how costly would failure be?

| Score | Label | Criteria |
|-------|-------|----------|
| **0.0** | Low risk | Well-understood problem with proven solutions. Failure unlikely. Clear rollback path. |
| **0.25** | Minor risk | Mostly understood, with a few unknowns. Failure would be contained and recoverable. |
| **0.5** | Moderate risk | Some unknowns. Failure would require significant rework. Partial rollback possible. |
| **0.75** | High risk | Significant unknowns. Failure could affect other systems. Limited rollback options. |
| **1.0** | Very high risk | Novel approach with no precedent. Failure could have broad blast radius. No proven rollback path. |

**Examples:**
- 0.0: Adding a new field to an existing API endpoint
- 0.5: Migrating a database from one provider to another with zero downtime
- 1.0: Replacing the core authentication system across all services simultaneously

---

### Dimension 2: Novelty (Weight: 0.2)

How new is this work relative to what the organization has done before?

| Score | Label | Criteria |
|-------|-------|----------|
| **0.0** | Routine | Maintenance, minor iteration on existing patterns. The organization has done this many times. |
| **0.25** | Incremental | New feature using established patterns and technologies. Familiar territory with minor extensions. |
| **0.5** | Greenfield component | New component or service within a known system architecture. The building blocks are familiar; the assembly is new. |
| **0.75** | New technology | Introducing a technology or pattern the organization hasn't used before. Requires learning and experimentation. |
| **1.0** | Entirely novel | New architecture, unproven technology, or a problem space the organization has never addressed. No internal precedent. |

**Examples:**
- 0.0: Adding a new CRUD endpoint to an existing service
- 0.5: Building a new microservice using the organization's standard service template
- 1.0: Introducing event sourcing to an organization that has only used CRUD

---

### Dimension 3: Organizational Friction (Weight: 0.2)

How many teams, stakeholders, and organizational boundaries does this work cross?

| Score | Label | Criteria |
|-------|-------|----------|
| **0.0** | Single team | Clear ownership within one team. No external dependencies or approvals needed. |
| **0.25** | Minor coordination | One external dependency or approval needed. Mostly self-contained. |
| **0.5** | Cross-team | Coordination across 2--3 teams. Shared interfaces or data contracts to negotiate. |
| **0.75** | Cross-org | Dependencies span multiple org units. External stakeholders involved. May require compliance review. |
| **1.0** | Maximum friction | Cross-org dependencies, external vendor coordination, regulatory or compliance requirements, executive approvals. |

**Examples:**
- 0.0: Fixing a bug in your own team's service
- 0.5: Building an integration between your service and two other teams' APIs
- 1.0: Implementing a compliance mandate that requires changes across 5 teams, legal review, and external auditor approval

---

## Quick Reference

| Range | Label | Typical Scenarios |
|-------|-------|-------------------|
| **1.0 -- 1.2** | Standard | Routine work, single team, low risk. Most day-to-day engineering work. |
| **1.2 -- 1.4** | Moderate | Some unknowns, 2--3 teams involved, moderate risk. Typical feature development. |
| **1.4 -- 1.5** | High | New technology or significant cross-team coordination. Major feature or platform work. |
| **1.5 -- 1.7** | Exceptional | Novel approach, cross-org dependencies, high technical risk. Major migrations, new platforms, compliance overhauls. |

---

## Calculation Examples

### Example 1: Routine Feature

- Risk: 0.0 (well-understood)
- Novelty: 0.25 (new feature, established patterns)
- Org Friction: 0.0 (single team)
- **Complexity Factor = 1.0 + (0.0 x 0.3) + (0.25 x 0.2) + (0.0 x 0.2) = 1.05**

### Example 2: Cross-Team Migration

- Risk: 0.75 (significant unknowns, limited rollback)
- Novelty: 0.5 (greenfield migration tooling)
- Org Friction: 0.5 (3 teams coordinating)
- **Complexity Factor = 1.0 + (0.75 x 0.3) + (0.5 x 0.2) + (0.5 x 0.2) = 1.425**

### Example 3: Maximum Complexity

- Risk: 1.0 (novel approach, broad blast radius)
- Novelty: 1.0 (entirely new architecture)
- Org Friction: 1.0 (cross-org, external stakeholders, compliance)
- **Complexity Factor = 1.0 + (1.0 x 0.3) + (1.0 x 0.2) + (1.0 x 0.2) = 1.7**

---

## Common Mistakes

| Mistake | Why It's Wrong | What to Do Instead |
|---------|---------------|-------------------|
| Rating all projects 1.5+ | Inflation removes the value of complexity credit | Most projects are 1.0--1.3. Reserve 1.5+ for genuinely exceptional difficulty. |
| Rating based on the person's seniority | Complexity is about the work, not the person | A junior engineer on a hard project deserves the same complexity factor as a senior. |
| Confusing "I worked hard" with complexity | Effort is not complexity | A task that takes 200 hours of routine work is still 1.0 complexity. |
| Ignoring org friction | Coordination work is genuinely harder | If you spent 30% of your time on cross-team negotiation, that's real friction. Score it. |
