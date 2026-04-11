# Contribution Factor Rubric

The Contribution Factor measures an engineer's material influence on an initiative or project. It is based on observable behaviors, not output volume.

**Scale:** 0.0 -- 1.0
**Assignment:** Self-assessment, then manager review, then calibration

---

## Rubric Levels

### 1.0 — Primary Driver

You probably deserve this if: **You wrote the design doc, made the final call, and would be blamed if it failed.**

| Observable Criteria |
|---|
| Owned technical design (wrote RFC, design doc, or architecture document) |
| Made final architectural decisions — the team followed your direction |
| Led implementation across multiple engineers |
| Accountable for delivery in planning meetings — your name was on the outcome |
| Drove the technical strategy, not just the execution |

**Evidence examples:**
- "I authored SAD-NOTIFY-001 and made the decision to use event-driven architecture over polling"
- "I led the 4-person implementation team and presented the delivery plan at the sprint review"
- "I was the escalation point when the migration hit dependency issues across 3 services"

**Frequency guidance:** Rare. Most initiatives have 0--1 Primary Drivers. If a team has 3 engineers all claiming 1.0 on the same project, at least 2 are inflating.

---

### 0.7 — Major Contributor

You probably deserve this if: **You owned a major piece, unblocked the team repeatedly, and shaped the direction.**

| Observable Criteria |
|---|
| Owned a significant subsystem or component end-to-end |
| Drove critical technical decisions in your area of ownership |
| Reviewed and approved others' designs (not just code reviews — design reviews) |
| Unblocked the team on technical challenges multiple times |
| Your removal would have significantly delayed or degraded the outcome |

**Evidence examples:**
- "I owned the caching layer, designed the invalidation strategy, and reviewed the data model for the persistence team"
- "I resolved the cross-service auth issue that had blocked two other engineers for a week"
- "I made the call to switch from REST to gRPC for the internal API, which the team adopted"

---

### 0.4 — Meaningful Contributor

You probably deserve this if: **You built something substantial, coordinated across teams, or led a critical fix.**

| Observable Criteria |
|---|
| Implemented substantial feature work (not just tickets — features with design decisions) |
| Provided technical guidance that shaped the direction (even if someone else made the final call) |
| Owned integration or cross-team coordination |
| Led incident response or critical bug fixes |
| Contributed domain expertise that was essential to the project |

**Evidence examples:**
- "I implemented the notification preference system, including the state machine for opt-in/opt-out"
- "I coordinated the API contract negotiation between our team and the mobile team"
- "I led the SEV2 incident response that identified the root cause in the connection pool configuration"

---

### 0.2 — Supporting Contributor

You probably deserve this if: **You implemented well-scoped work within someone else's design.**

| Observable Criteria |
|---|
| Implemented scoped tasks within a design someone else created |
| Participated in design reviews with meaningful input (not just approval) |
| Fixed bugs or wrote tests for others' features |
| Provided on-call support or operational maintenance |
| Contributed specific expertise when consulted |

**Evidence examples:**
- "I implemented the email template rendering per the design in the TDD"
- "I wrote the integration test suite for the notification delivery pipeline"
- "I was on-call during the rollout and handled 3 incidents during the exposure ramp"

---

### 0.1 — Peripheral Contributor

You probably deserve this if: **You contributed code or reviews but didn't shape decisions.**

| Observable Criteria |
|---|
| Made minor code contributions (small bug fixes, config changes) |
| Participated in discussions without decision authority |
| Performed code reviews without deep involvement in the design |
| Provided general support (answered questions, pair-programmed briefly) |

**Evidence examples:**
- "I fixed 2 bugs in the notification service and reviewed 5 PRs"
- "I attended the design review and asked clarifying questions"

---

## Assignment Process

1. **Self-assessment:** The engineer rates themselves using this rubric, citing specific evidence for the level they claim. When in doubt, choose the lower level.

2. **Manager assessment:** The manager independently rates the engineer, using their own observations and the evidence provided.

3. **Peer input (recommended for Tier 2):** 2--3 peers provide their rating with brief justification. This is advisory input to the manager.

4. **Tech lead validation:** For technical Contribution Factors (design ownership, architectural decisions), the tech lead confirms the rating matches their observations.

5. **Calibration:** The cross-team calibration panel reviews and may adjust ratings for consistency. See `templates/calibration-agenda.md`.

---

## Common Mistakes

| Mistake | Why It's Wrong | What to Do Instead |
|---------|---------------|-------------------|
| Rating based on hours worked | Activity is not contribution | Rate based on the rubric criteria above |
| Giving 1.0 to everyone "to be fair" | Inflation makes the framework useless | 1.0 is genuinely rare — most engineers on most projects are 0.2--0.4 |
| Rating 0.1 because you're "being humble" | Undervaluation is also a problem | Use the rubric honestly — if you led incident response, that's at least 0.4 |
| Ignoring enabling work | Unblocking others is high-value | Enablement counts — if you unblocked 3 engineers, rate that contribution |
| Summing to 1.0 across all contributors | Contribution factors are per-person, not a budget | Multiple people can be 0.4 on the same project. But only 1 can be 1.0. |
