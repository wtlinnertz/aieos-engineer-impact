# Engineer Impact Assessment — Process Guide

Step-by-step instructions for running quarterly engineer impact assessments.

---

## Overview

The assessment cycle runs quarterly. Each cycle has four phases:

```
Pre-Quarter Setup (Week 1)
    |
During Quarter: Contribution Logging (Ongoing)
    |
End of Quarter: Assessment (Weeks 11-12)
    |
Calibration and Archive (Week 13)
```

---

## Phase 1: Pre-Quarter Setup

**When:** First week of the quarter
**Who:** Engineering managers
**Time:** ~30 minutes

### Steps

1. **Confirm assessment roster.** List every engineer who will be assessed this quarter. Include engineers who joined mid-quarter (prorate their assessment window).

2. **Choose the tier.** Select Tier 1 (Starter) or Tier 2 (Advanced) for each team. A single team should use the same tier — don't mix tiers within a team.

3. **Confirm dimension weights.** By default, all four dimensions carry equal importance. If your organization values certain dimensions more (e.g., Enablement for a platform team), document the weighting and communicate it before the quarter starts.

4. **Distribute templates.** Give each engineer their assessment template:
   - Tier 1: `templates/tier1-assessment.md`
   - Tier 2: `templates/tier2-assessment.md`

5. **Set expectations.** Communicate:
   - This is about outcomes and contribution, not activity
   - Engineers should log contributions as they happen (not reconstruct from memory at quarter end)
   - Evidence matters — design doc ownership, decision leadership, incident response roles
   - The non-negotiable exclusions (no story points, LOC, commit counts, etc.)

---

## Phase 2: During Quarter — Contribution Logging

**When:** Throughout the quarter
**Who:** Each engineer
**Time:** ~5 minutes per significant contribution

### What to Log

As significant work completes, engineers note:

- What initiative or project it was for
- Their role (designed it, built it, reviewed it, coordinated it, led incident response)
- The outcome (shipped feature, reduced incidents, saved time, improved reliability)
- Evidence (design doc they authored, decision they drove, incident they led)

### Tips

- Log at natural milestones: feature shipped, incident resolved, design approved, quarter boundary
- Don't log every PR or ticket — log the things that mattered
- If you're unsure whether something counts, log it. You can remove it during self-assessment.
- Contribution logging is lightweight by design. If it takes more than 5 minutes per entry, you're over-documenting.

---

## Phase 3: End of Quarter — Assessment

**When:** Weeks 11--12 of the quarter
**Who:** Engineers (self-assessment), then managers (review)
**Time:** Tier 1: ~1 hour. Tier 2: ~4 hours.

### Step 3a: Engineer Self-Assessment

Each engineer completes their assessment template using their contribution log.

**For each dimension:**
1. List the initiatives/contributions with evidence
2. Self-rate a Contribution Factor (0--1) per initiative, referencing the rubric at `rubrics/contribution-factor.md`
3. (Tier 2 only) Score the Complexity Factor per initiative using `rubrics/complexity-factor.md`

**Self-assessment rules:**
- Use the rubric levels, not gut feel. "I think I deserve 0.7" is not sufficient — cite which observable criteria you meet.
- When in doubt, rate yourself lower and explain. Calibration can adjust upward; it's harder to adjust downward without friction.
- Be specific about evidence. "I contributed to the project" is not evidence. "I authored the SAD, made the caching vs. queue architectural decision, and led the cross-team integration" is evidence.

### Step 3b: Manager Review

Managers review each engineer's self-assessment within 1 week.

**For each engineer:**
1. Validate contribution claims against your own observations and available evidence
2. Assign your own Contribution Factor rating (independent of the self-assessment)
3. Note areas of agreement and disagreement
4. (Tier 2 only) Validate Complexity Factor scores — was the work actually that complex?

**Manager review rules:**
- Don't rubber-stamp self-assessments. Your independent rating is the input to calibration.
- If an engineer rated themselves significantly higher or lower than your assessment, note why. This becomes a calibration discussion point.
- Collect peer input from 2--3 peers per engineer. Peer input is advisory — it informs your rating but doesn't override it.

### Step 3c: Peer Input (Optional for Tier 1, Recommended for Tier 2)

2--3 peers provide brief input per engineer:
- What did this person contribute that you directly observed?
- What Contribution Factor would you assign for the work you saw? (Use the rubric)
- Any contribution the engineer might have missed in their self-assessment?

Peer input should take no more than 15 minutes per peer per engineer reviewed.

---

## Phase 4: Calibration and Archive

**When:** Week 13 (first week of next quarter)
**Who:** Calibration panel (managers, tech leads, skip-level)
**Time:** ~2 hours per 10 engineers

### Step 4a: Calibration Meeting

Use the calibration meeting template at `templates/calibration-agenda.md`.

**Pre-meeting (48 hours before):**
- Managers submit preliminary ratings (their ratings, not self-assessments)
- Calibration coordinator compiles the Contribution Factor distribution per team

**During meeting:**
1. Review Contribution Factor distribution — flag teams with >50% at 0.7+
2. Walk through each engineer: manager presents, panel discusses
3. Flag outliers (unusually high or low in any dimension)
4. Reach consensus on adjustments (with stated rationale for each)
5. Run the gaming detection checklist (`rubrics/gaming-detection.md`)

**Calibration rules:**
- No stack ranking. Engineers are assessed against the rubric, not against each other.
- No forced distribution. If a team genuinely has three Primary Drivers, that's fine — but validate with evidence.
- Every adjustment requires a stated rationale. "We just feel it should be lower" is not a rationale.
- Compare across similar roles and similar work types (backend to backend, not backend to SRE).

### Step 4b: Communication

Within 1 week of calibration:
- Manager shares the final assessment with each engineer in a 1:1
- Highlight strengths (highest-dimension scores)
- Discuss growth areas (lowest-dimension scores, if relevant to their role)
- If calibration adjusted a score, explain why transparently

### Step 4c: Archive

- Save the completed assessment template to the team's records
- (If using AIEOS integration) Update ER §16 Impact Attribution — see `aieos-integration.md`
- Note any process improvements for next quarter

---

## Annual Synthesis

At year end, compile the four quarterly assessments into a yearly view:

- Trend across quarters (improving, stable, declining per dimension)
- Portfolio balance (is the engineer developing across dimensions, or staying single-dimensional?)
- Growth trajectory (are growth areas from Q1 showing improvement by Q4?)

The annual synthesis is an input to performance conversations but is **not** a performance review itself. It is data, not judgment.

---

## Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Engineer** | Log contributions during quarter; complete self-assessment; participate in peer reviews |
| **Manager** | Distribute templates; review self-assessments; collect peer input; present at calibration; communicate results |
| **Tech Lead** | Validate technical contribution claims; provide calibration input on complexity and architectural impact |
| **Calibration Panel** | Cross-team calibration; outlier review; gaming detection; rubric consistency |
| **Skip-Level Manager** | Attend calibration as tie-breaker; ensure fairness across teams |

---

## Common Questions

**Q: What if an engineer worked on something that doesn't have measurable outcomes yet?**
A: Use leading indicators (adoption, engagement) as proxies for the first 3 months. Apply a confidence discount to the Outcome Value. See the Attribution Lag table in `framework.md`.

**Q: What if two engineers both claim Primary Driver?**
A: This is a calibration issue. There can only be one Primary Driver per initiative. Use evidence (who authored the design doc, who made the final architectural calls) to determine the primary. The other is likely a Major Contributor (0.7).

**Q: Should we compare scores across teams?**
A: Compare within similar roles and work types. A platform engineer and a product engineer will have different dimension profiles by design — that's not a problem.

**Q: What if an engineer only works on one initiative per quarter?**
A: That's fine. Their Contribution Factor on that one initiative carries their score. Complexity Factor ensures they aren't penalized for taking on a single hard problem.

**Q: How do we handle engineers who joined mid-quarter?**
A: Prorate the assessment window. An engineer who joined 6 weeks into a 13-week quarter is assessed on 7 weeks of contribution, with cost prorated to match.
