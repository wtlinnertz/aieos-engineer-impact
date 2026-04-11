# CLAUDE.md — Engineer Impact Framework

## What This Project Is

This is the **Engineer Impact Framework** — a quarterly assessment system for measuring individual engineer impact through business outcomes, not activity metrics. It is an AIEOS ecosystem project, not a governance kit. It has no specs, templates, prompts, or validators in the four-file sense. It is a standalone measurement framework.

**What it is NOT:**
- Not a governance kit (no four-file system, no hard gates, no validators)
- Not a performance review system (it produces data, not judgments)
- Not dependent on AIEOS (works standalone; optional AIEOS integration available)

## Repository Structure

```
aieos-engineer-impact/
  CLAUDE.md                        # This file
  README.md                        # Human-facing overview
  VERSION                          # Current version
  docs/
    framework.md                   # Full canonical framework reference
    process-guide.md               # Step-by-step quarterly assessment process
    aieos-integration.md           # Optional AIEOS integration guide
    templates/
      tier1-assessment.md          # Starter template (~2hrs/quarter)
      tier2-assessment.md          # Advanced template (~8hrs/quarter)
      calibration-agenda.md        # Quarterly calibration meeting template
    rubrics/
      contribution-factor.md       # 0-1 scale with observable criteria
      complexity-factor.md         # 1.0-1.7 scale with dimension scoring
      gaming-detection.md          # Anti-gaming red flags and mitigations
```

## How to Use

1. Read `README.md` for an overview
2. Choose Tier 1 (Starter) or Tier 2 (Advanced)
3. Follow `docs/process-guide.md` for the quarterly cycle
4. Use the templates in `docs/templates/` for assessments and calibration
5. Reference rubrics in `docs/rubrics/` when scoring

## Relationship to AIEOS

This project is part of the AIEOS ecosystem (ECO-008) but is fully standalone. Optional integration:

- **ER §16 Impact Attribution** — if your initiative uses AIEOS Engagement Records, §16 captures contribution data at artifact freeze points, which serves as evidence for quarterly assessments
- **IEK (Layer 7)** — Evolution Signals and Portfolio Evolution Signals can optionally consume ER §16 data to enrich pattern analysis

See `docs/aieos-integration.md` for details.

## Key Files

| File | Purpose |
|------|---------|
| `docs/framework.md` | Canonical reference — all formulas, dimensions, philosophy |
| `docs/process-guide.md` | How to run the quarterly cycle |
| `docs/templates/tier1-assessment.md` | Lightweight assessment for new adopters |
| `docs/templates/tier2-assessment.md` | Advanced assessment with per-initiative scoring |
| `docs/rubrics/contribution-factor.md` | How to rate material influence (0--1) |
| `docs/rubrics/complexity-factor.md` | How to credit difficulty (1.0--1.7) |
| `docs/rubrics/gaming-detection.md` | How to catch and address gaming |

## Four Dimensions

```
Total Engineer Value =
  Outcome-Driven Impact        (business results)
+ Enablement Impact            (making others productive)
+ Operational Excellence       (keeping things running)
+ Team Multiplier              (growing people and processes)
```

## Non-Negotiable Exclusions

Never use these as impact measures: story points, lines of code, commit counts, individual velocity, PR count, time tracking, code churn, review comment count.
