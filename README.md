# Engineer Impact Framework

A quarterly assessment system for measuring individual engineer impact through business outcomes, not activity metrics.

---

## Why This Exists

Most engineering measurement systems fail because they measure activity (story points, lines of code, commit counts) instead of outcomes. This framework measures what the business actually cares about — revenue, cost savings, risk reduction, team productivity — and allocates credit based on who materially influenced those outcomes.

## Two Tiers

| | Tier 1: Starter | Tier 2: Advanced |
|---|---|---|
| **Time** | ~2 hours per quarter | ~8 hours per quarter |
| **Complexity** | One formula, three contribution levels | Four dimensions, complexity factors, calibration |
| **Best for** | Teams new to impact measurement | Teams ready for portfolio-level insights |
| **Template** | `docs/templates/tier1-assessment.md` | `docs/templates/tier2-assessment.md` |

Start with Tier 1. Upgrade to Tier 2 when 3+ teams are comfortable with Tier 1, leadership asks for deeper insights, or engineers complain about fairness.

## Four Dimensions

Individual engineer value comes from four complementary dimensions:

| Dimension | What It Measures | Typical Range |
|-----------|-----------------|---------------|
| **Outcome-Driven Impact** | Business results: revenue, cost savings, risk reduction | 2x -- 10x |
| **Enablement Impact** | Making other engineers productive: tools, platforms, automation | 1.5x -- 5x |
| **Operational Excellence** | Keeping systems running: incidents, reliability, tech debt | 1x -- 3x |
| **Team Multiplier** | Growing people: mentorship, hiring, knowledge sharing | 0.1x -- 0.5x |

Don't rely on a single number. A balanced portfolio across dimensions is healthier than a single-dimension specialist.

## Quick Start

1. **Choose your tier** — Tier 1 if you're new to this, Tier 2 if you've done it before
2. **Read the process guide** — `docs/process-guide.md` walks through the quarterly cycle
3. **Distribute templates** — Give engineers their assessment template at the start of the quarter
4. **Run the cycle** — Engineers log contributions, self-assess, managers review, panel calibrates
5. **Reference the rubrics** — `docs/rubrics/` has the scoring criteria for contribution and complexity

## What We Measure (and What We Don't)

**We measure:** Business outcomes, contribution to those outcomes, complexity of the work, team productivity gains, operational excellence, mentorship impact.

**We never measure:** Story points, lines of code, commit counts, individual velocity, PR count, time tracking, code churn, review comment count. These are non-negotiable exclusions — they invalidate the framework and will be gamed.

## Key Documents

| Document | What It Covers |
|----------|---------------|
| `docs/framework.md` | Complete framework reference — all formulas, dimensions, philosophy |
| `docs/process-guide.md` | Step-by-step quarterly assessment process |
| `docs/templates/tier1-assessment.md` | Starter assessment template |
| `docs/templates/tier2-assessment.md` | Advanced assessment template |
| `docs/templates/calibration-agenda.md` | Quarterly calibration meeting template |
| `docs/rubrics/contribution-factor.md` | How to rate material influence (0--1 scale) |
| `docs/rubrics/complexity-factor.md` | How to credit difficulty (1.0--1.7 scale) |
| `docs/rubrics/gaming-detection.md` | How to catch and address gaming behaviors |

## AIEOS Integration (Optional)

This framework is part of the [AIEOS](https://github.com/aieos) ecosystem but works entirely standalone. If your organization uses AIEOS governance:

- **ER §16 Impact Attribution** captures contribution data at artifact freeze points
- **IEK Evolution Signals** can consume impact data for pattern analysis

See `docs/aieos-integration.md` for details.
