# Engineer Impact Framework

*Canonical reference for measuring engineer impact through outcomes, not activity.*

---

## Adoption Tiers: Choose Your Starting Point

This framework has two versions. Start with Tier 1, then upgrade when ready.

### Tier 1: Starter Framework (Recommended for New Adopters)

Use this if: You've never quantified engineer impact before, or you want a lightweight process.

**Time investment:** ~2 hours per quarter
**Complexity:** Low (one formula, three contribution levels, quarterly updates)

See `templates/tier1-assessment.md` for the Tier 1 template.

---

### Tier 2: Advanced Framework (This Document)

Use this if: You've used Tier 1 for 2+ quarters, or you need to compare different types of work (product vs platform vs ops).

**Time investment:** ~8 hours per quarter
**Complexity:** High (four dimensions, complexity factors, calibration meetings)

**Upgrade when:**
- 3+ teams are using Tier 1 comfortably
- Leadership asks for portfolio-level insights
- Engineers complain about fairness (hard projects not getting credit)
- You see gaming behaviors (cherry-picking easy work)

See `templates/tier2-assessment.md` for the Tier 2 template.

---

## The Rule of Engagement

Before the formulas, align on this sentence:

> *"Individual engineer impact can be estimated, but only as a proxy using outcomes the engineer materially influenced, over a defined time period and comparable domains (e.g., compare backend engineers to backend engineers, not to SREs; compare work within the same business context). This estimate is one input, not the sole input, for evaluating engineer contributions."*

This lets us provide math without claiming false precision.

---

## The Core Pattern

- Measure outcomes at the team/system level
- Allocate impact to individuals based on contribution, not output
- Normalize by cost
- Pair quantitative scores with qualitative assessments

This preserves business and engineering reality.

---

## Engineer Value Portfolio

Individual engineer value comes from four complementary dimensions. **Don't rely on a single number.**

```
Total Engineer Value =
  Outcome-Driven Impact
+ Enablement Impact
+ Operational Excellence
+ Team Multiplier
```

---

## Interpreting ROI Scores: Expected Ranges

Different dimensions of engineering work have different natural ROI profiles. This is expected and does not indicate underperformance.

| Dimension | Typical Range | Top Performer | Why Ranges Differ |
|---|---|---|---|
| **Outcome Impact** | 2x -- 10x | 15x+ | Direct business value; high leverage when product-market fit is strong |
| **Enablement Impact** | 1.5x -- 5x | 8x+ | Scales with team size; platform/infrastructure work can be very high-leverage |
| **Operational Excellence** | 1x -- 3x | 5x+ | Often underestimated; value is in risk/cost avoided rather than revenue created |
| **Team Multiplier** | 0.1x -- 0.5x | 1.0x+ | Hardest to quantify; conservative measurement; long-term compounding value |

---

## Why Team Multiplier Scores Are Lower (And That's OK)

Mentorship, knowledge-sharing, and cultural work have:

1. **Conservative measurement:** Hard to attribute productivity gains precisely, so we underestimate
2. **Lagging returns:** Mentees take 6--12 months to show improvement; value accrues slowly
3. **Compounding effects:** A mentee's growth continues for years; we only measure near-term impact
4. **Indirect attribution:** Mentee's manager and project also contributed to their growth

A Team Multiplier score of 0.1x--0.3x is **GOOD** for a senior/staff engineer. It indicates healthy investment in team capacity.

If we measured long-term compounding value (5-year horizon), this number would be much higher.

### Red Flags: When Low Scores Are a Problem

Small numbers are a problem if:

| Scenario | Red Flag | Action |
|---|---|---|
| **All dimensions below their expected typical range** (e.g., Outcome Impact < 2x, Team Multiplier < 0.1x) | Engineer is underperforming across the board relative to peers | Performance improvement plan; role mismatch; consider transition |
| **Outcome Impact < 0.5x for product engineer** | Primary job dimension is underperforming | Investigate: Blocked? Wrong projects? Skill gap? |
| **Team Multiplier = 0 for Staff+ engineer** | Not investing in team leverage | Coaching: Mentor, share knowledge, lead initiatives |
| **Scores declining over time** | Disengagement or burnout | 1:1 conversation; adjust workload or role |

But if an engineer has:
- High Outcome Impact (6.7x)
- Low Team Multiplier (0.12x)

That's fine -- they're focused on delivery, not mentorship. As long as they're not expected to mentor (e.g., IC track, not people-focused), this is appropriate specialization.

**Critical:** An engineer may score high in one dimension and low in others. A balanced portfolio is healthier than a single-dimension specialist (except for specialists like platform engineers).

---

## Shared Component: Engineer Cost

**Fully loaded cost:**

```
Salary + Benefits + Overhead (facilities, tools, recruiting, management)
```

- Business-standard denominator
- Lets finance compare investments
- With Complexity Factor, doesn't unfairly penalize senior engineers

**Rule:** Normalize cost over the same window as the outcome measurement (e.g., trimester/year), especially for long-running initiatives.

---

## 1. Outcome-Driven Impact Score

### Formula

```
Engineer Impact Score =
  SUM ((Outcome Value x Confidence Level) x Contribution Factor x Complexity Factor) / Engineer Cost
```

> **Note:** `Confidence Level` defaults to 1.0 when outcome is certain. Apply a discount (e.g., 0.6) only when the outcome is uncertain or still materializing. See *Risk-Adjusted Value* below.

### Component 1: Outcome Value

Measured after delivery, not predicted. Each outcome must have a defined measurement and baseline (e.g., pre/post or A/B):

- Revenue increase
- Cost reduction
- Risk reduction (incident cost avoided)
- Productivity unlocked (hours saved x blended rate)
- Customer retention improvement

**Guardrail:** For any single initiative, Outcome Value must be "owned" once and then allocated across contributors, to prevent double-counting across sub-teams.

### Handling Attribution Lag

Many outcomes take 6--12 months to materialize. Use this approach:

| Timeline | Measurement Approach |
|---|---|
| **0--3 months** | Use leading indicators (adoption rate, engagement, usage) as proxies |
| **3--6 months** | Blend leading indicators with early lagging indicators (revenue trend, support ticket reduction) |
| **6+ months** | Use full lagging indicators (actual revenue, retention, cost savings) |

### Risk-Adjusted Value

If confidence in outcome is uncertain, discount the value:

```
Attributed Value = Expected Value x Confidence Level
```

**Example:**
- Expected churn reduction: $1M
- Confidence: 60%
- Attributed Value: $600k

### Handling Failed Experiments

High-quality work that doesn't produce business results should not be penalized:

- If failure was due to market/customer rejection: Attribute effort value (cost of equivalent work that succeeded)
- If failure was due to poor execution: Use retrospective to improve process, don't attribute negative value
- If failure taught critical lessons: Attribute learning value (cost of alternative path avoided)

**Never attribute negative outcome value except in cases of gross negligence (rare).**

---

### Component 2: Contribution Factor (0--1 scale)

Represents material influence, not lines of code. Assignment requires judgment based on demonstrated behaviors.

See `rubrics/contribution-factor.md` for the full rubric with observable criteria.

| Score | Label | Summary |
|---|---|---|
| **1.0** | **Primary Driver** | Owned technical design, made final architectural decisions, led implementation, accountable for delivery |
| **0.7** | **Major Contributor** | Owned significant subsystem, drove critical decisions, unblocked team |
| **0.4** | **Meaningful Contributor** | Implemented substantial features, coordinated across teams, led critical fixes |
| **0.2** | **Supporting Contributor** | Implemented scoped tasks within others' designs, meaningful review input |
| **0.1** | **Peripheral Contributor** | Minor code contributions, participated without decision authority |

### How to Assign Contribution Factors

**Process:**

1. Self-assessment (engineer rates themselves with evidence)
2. Manager assessment (validates against observable criteria and applies judgment)
3. Peer input (2--3 peers provide scores + justification)
4. Tech lead calibration (ensures consistency across projects)
5. Cross-team calibration (quarterly review to prevent inflation -- see Calibration section)

**Evidence Sources:**

- Design doc authorship/ownership
- RFC/ADR (Architecture Decision Record) leadership
- Pull request review activity (who was the final approver on critical design decisions, not just routine code reviews)
- Meeting notes (who drove technical decisions?)
- Incident reports (who led response?)
- Communication threads (who unblocked the team?)

---

### Component 3: Complexity Factor

Prevents penalizing senior engineers who take on hard, risky, long-term work.

See `rubrics/complexity-factor.md` for the full rubric with dimension scoring.

```
Complexity Factor = 1.0 + (Risk x 0.3) + (Novelty x 0.2) + (Org Friction x 0.2)
```

Each dimension scored 0.0--1.0:

| Dimension | 0.0 | 0.5 | 1.0 |
|---|---|---|---|
| **Risk** | Low-risk, well-understood problem | Moderate risk, some unknowns | High technical risk, novel approach, potential for failure |
| **Novelty** | Maintenance, minor iteration | Greenfield component within known system | Entirely new architecture, unproven technology |
| **Org Friction** | Single team, clear ownership | Cross-team coordination (2--3 teams) | Cross-org dependencies, external stakeholders, compliance |

**Complexity Factor Range:** 1.0 (routine work) to 1.7 (maximum complexity)

This means the highest-complexity work can earn up to **70% bonus credit** for difficulty.

**Example:**
- High-risk migration (Risk = 1.0)
- Greenfield platform (Novelty = 1.0)
- 5 teams involved (Org Friction = 1.0)
- Complexity Factor = 1.0 + 0.3 + 0.2 + 0.2 = **1.7**

---

## 2. Enablement Impact Score

Critical for platform engineers, SREs, and tooling teams.

### Formula

```
Enablement Impact =
  (SUM Team Productivity Gains Enabled x Contribution Factor) / Engineer Cost
```

### What Counts as Productivity Gains

| Type | Measurement |
|---|---|
| **Time savings** | Hours saved per engineer x # engineers x blended rate x 220 work days |
| **Velocity increase** | % reduction in lead time x team throughput x value per delivery |
| **Defect reduction** | Incidents avoided x average incident cost |
| **Onboarding acceleration** | Days saved to productivity x new hire count x blended rate |
| **Tech debt reduction** | Future maintenance hours avoided x blended rate |

### Example

**Scenario:**
- CI/CD automation saves 20 engineers 1 hour/day
- 20 x 1 hour x 220 days x $90/hr = $396k/year
- Platform engineer cost: $170k
- Contribution Factor: 1.0 (sole owner)

```
Enablement Impact = ($396k x 1.0) / $170k = 2.3x
```

---

## 3. Operational Excellence Score

For incident response, on-call, reliability, and technical debt work.

### Formula

```
Operational Excellence Score =
  (SUM (Cost Avoided + Reliability Value) x Contribution Factor) / Engineer Cost
```

> **Note:** Contribution Factor is applied here for the same reason as other dimensions -- when multiple engineers collaborate on incident response or reliability work, the total value must be allocated by individual contribution rather than attributed in full to each person.

### Component 1: Cost Avoided

> Captures direct, incident-driven costs. **MTTR-related savings belong here only** -- do not also count them in Reliability Value.

| Activity | Measurement |
|---|---|
| **Incident response** | (MTTR reduction) x (incident frequency) x (average incident cost per hour) |
| **Preventive fixes** | Estimated future incident cost avoided (use historical data) |
| **Technical debt cleanup** | Future velocity improvement x team hourly cost |
| **Security hardening** | Estimated breach cost x probability reduction |

### Component 2: Reliability Value

> Captures structural reliability improvements **not already counted in Cost Avoided**. Do not include MTTR here if it was already measured above.

| Metric | Measurement |
|---|---|
| **Uptime improvement** | SLA compliance improvement x revenue at risk |
| **Change failure rate reduction** | Deployments per month x CFR improvement x avg rollback cost |

### Example

**Scenario:**
- Engineer reduced MTTR from 45 min to 15 min (saves 0.5 hr per incident)
- 12 incidents/year
- Avg incident cost: $50k/hour
- Cost avoided: 12 x 0.5 hr x $50k/hr = $300k
- Reliability Value (uptime/CFR improvements): $0 (not applicable here)
- Contribution Factor: 1.0 (sole responder on MTTR work)
- Engineer cost: $160k

```
Operational Excellence = (($300k + $0) x 1.0) / $160k = 1.9x
```

---

## 4. Team Multiplier Score

For mentorship, hiring, knowledge sharing, and cultural contributions.

### Formula

```
Team Multiplier Score =
  (Team Productivity Increase Attributable to Mentorship/Enablement) / Engineer Cost
```

### What Counts

| Activity | Measurement |
|---|---|
| **Mentorship** -- Demonstrated improvement in mentee's autonomy, code quality, and project ownership. | Mentee productivity increase x mentee cost x attribution factor |
| **Hiring** -- Active participation in interview loops, providing high-quality feedback, and contributing to debriefs. | New hire quality x cost of bad hire avoided x attribution factor |
| **Knowledge sharing** -- Creating durable documentation, leading tech talks, or establishing new team rituals that reduce knowledge silos. | Time saved across team (documentation, internal talks, pairing) x blended rate |
| **Process improvement** -- Identifying and driving changes to team workflows that demonstrably reduce friction or increase quality. | Team velocity increase x team cost x attribution factor |

### Example

**Scenario:**
- Senior engineer mentors 2 junior engineers
- Mentees each improve productivity by 20% (measured via delivery output)
- Mentee avg cost: $120k
- Productivity gain: 2 x $120k x 0.2 = $48k
- Attribution factor: 0.5 (shared with other mentors/managers)
- Senior engineer cost: $200k

```
Team Multiplier = ($48k x 0.5) / $200k = 0.12x
```

Note: This score will be lower than outcome-driven scores. That's expected. Senior engineers should have a portfolio across all four dimensions.

---

## Sub-Team Calibration Process

Prevents score inflation and gaming. See `templates/calibration-agenda.md` for the meeting template.

### Quarterly Calibration Meeting

**Attendees:** Engineering managers, tech leads, skip-level manager

**Agenda:**

1. **Review Contribution Factor distribution across teams**
   - Flag sub-teams with >50% of engineers at 0.7+ (likely inflation -- 0.7 and above should not be the norm)
   - Compare similar projects across sub-teams for consistency

2. **Review Complexity Factor assignments**
   - Ensure "high complexity" isn't overused
   - Validate against objective criteria

3. **Spot-check outcome value attribution**
   - Ensure business value isn't double-counted across sub-teams
   - Validate attribution lag assumptions

4. **Normalize outliers**
   - If one team's scores are significantly higher than all other teams (e.g., 30%+ above average), investigate
   - Adjust rubric interpretation or provide feedback

5. **Share learnings**
   - What worked well in attribution?
   - What was hard to measure?

**Output:** Calibrated scores, updated rubric guidance, process improvements

---

## What NOT to Include (Non-Negotiable)

**Never use these as impact measures:**

- Story count
- Story points
- Individual velocity
- Lines of code
- Commit counts
- "Delivery time per engineer"
- Time tracking (incentivizes long hours, not outcomes)
- PR count (incentivizes small, low-value changes)
- Code churn (can be positive or negative, context-dependent)
- Review comment count (incentivizes nitpicking)

These invalidate the calculation and will be gamed.

---

## Elevator Pitch

> "We can absolutely quantify engineer impact, but it has to be grounded in outcomes the business cares about.
>
> Instead of measuring activity, we measure business results and allocate impact based on contribution.
>
> Here's how it works:
>
> 1. Measure results (revenue, cost savings, risk reduction) -- the numbers finance already trusts
> 2. Allocate credit based on who drove the work (not who wrote the most code), using an observable rubric
> 3. Normalize by cost so we can compare investments
> 4. Adjust for complexity so hard, risky work isn't penalized
>
> This gives us a number finance can trust, aligns engineers with company goals, and avoids the gaming problems you see with story points or velocity.
>
> But -- this is one input, not the whole picture. We pair it with:
> - Qualitative assessments (peer feedback, growth, mentorship)
> - Portfolio balance (outcome impact, enablement, operational excellence, team multiplier)
> - Calibration across teams to prevent inflation
>
> This way, we get credible numbers without destroying engineering culture."

---

## Gaming Risks and Mitigation

See `rubrics/gaming-detection.md` for the full detection checklist.

| Gaming Behavior | Risk | Mitigation |
|---|---|---|
| **Cherry-picking high-value work** | Avoid necessary low-visibility tasks | Manager oversight (balanced portfolio requirement); Operational excellence score (rewards grunt work) |
| **Inflating contribution factors** | Self-promotion, politics | Multi-source input (self + manager + peers + tech lead); Cross-team calibration |
| **Avoiding risky work** | Stick to safe bets, kill innovation | Complexity factor (rewards risk-taking); Qualitative assessment (growth, experimentation) |
| **Sandbagging estimates** | Inflate expected value, look good when it hits | Risk-adjusted value (discount uncertain outcomes); Retrospective validation (did value materialize?) |
| **Claiming credit for others' work** | Attribution theft | Peer review in contribution assignment; Version control evidence (design docs, PRs, decisions) |

**Manager responsibility:** Managers must actively monitor for gaming and override scores when necessary. The framework is a tool, backed by evidence and judgment.

---

## Final Truth

There is no perfect individual productivity formula. But this approach:

- Preserves system thinking
- Produces credible math
- Survives executive scrutiny
- Doesn't rot engineering culture
- Balances quantitative rigor with qualitative judgment
- Prevents gaming through calibration and portfolio thinking
- Values all types of engineering work, not just feature delivery
