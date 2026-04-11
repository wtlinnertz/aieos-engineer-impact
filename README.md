# Engineer Impact Framework

A quarterly assessment system for measuring individual engineer impact through business outcomes, not activity metrics.

## The problem with activity metrics

Most engineering measurement systems fail because they measure activity (story points, lines of code, commit counts) instead of outcomes. This framework measures what the business actually cares about: revenue, cost savings, risk reduction, team productivity. It allocates credit based on who materially influenced those outcomes.

## Two tiers

| | Tier 1: Starter | Tier 2: Advanced |
|---|---|---|
| **Time** | ~2 hours per quarter | ~8 hours per quarter |
| **Complexity** | One formula, three contribution levels | Four dimensions, complexity factors, calibration |
| **Best for** | Teams new to impact measurement | Teams ready for portfolio-level insights |
| **Template** | `docs/templates/tier1-assessment.md` | `docs/templates/tier2-assessment.md` |

Start with Tier 1. Upgrade to Tier 2 when 3+ teams are comfortable with Tier 1, leadership asks for deeper insights, or engineers complain about fairness.

## The four dimensions

Individual engineer value comes from four complementary dimensions:

| Dimension | What it measures | Typical range |
|-----------|-----------------|---------------|
| Outcome-driven impact | Business results: revenue, cost savings, risk reduction | 2x to 10x |
| Enablement impact | Making other engineers productive: tools, platforms, automation | 1.5x to 5x |
| Operational excellence | Keeping systems running: incidents, reliability, tech debt | 1x to 3x |
| Team multiplier | Growing people: mentorship, hiring, knowledge sharing | 0.1x to 0.5x |

Don't rely on a single number. A balanced portfolio across dimensions is healthier than a single-dimension specialist.

## Getting started

1. Choose your tier (Tier 1 if you're new to this, Tier 2 if you've done it before)
2. Read `docs/process-guide.md` for the quarterly cycle
3. Distribute templates at the start of the quarter
4. Run the cycle: engineers log contributions, self-assess, managers review, panel calibrates
5. Reference `docs/rubrics/` for scoring criteria on contribution and complexity

## What we measure (and what we don't)

**We measure:** Business outcomes, contribution to those outcomes, complexity of the work, team productivity gains, operational excellence, mentorship impact.

**We never measure:** Story points, lines of code, commit counts, individual velocity, PR count, time tracking, code churn, review comment count. These are non-negotiable exclusions. They invalidate the framework and will be gamed.

## Key documents

| Document | What it covers |
|----------|---------------|
| `docs/framework.md` | Complete framework reference: all formulas, dimensions, philosophy |
| `docs/process-guide.md` | Step-by-step quarterly assessment process |
| `docs/templates/tier1-assessment.md` | Starter assessment template |
| `docs/templates/tier2-assessment.md` | Advanced assessment template |
| `docs/templates/calibration-agenda.md` | Quarterly calibration meeting template |
| `docs/rubrics/contribution-factor.md` | How to rate material influence (0 to 1 scale) |
| `docs/rubrics/complexity-factor.md` | How to credit difficulty (1.0 to 1.7 scale) |
| `docs/rubrics/gaming-detection.md` | How to catch and address gaming behaviors |

## AIEOS integration

This framework works entirely standalone but is part of the [AIEOS](https://github.com/aieos) ecosystem. If your organization uses AIEOS governance:

- ER §16 Impact Attribution captures contribution data at artifact freeze points
- IEK Evolution Signals can consume impact data for pattern analysis

See `docs/aieos-integration.md` for details.
