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

1. **Confirm the roster.** List every engineer to assess this quarter. Include mid-quarter joiners — prorate their window.

2. **Pick a tier.** Select Tier 1 (Starter) or Tier 2 (Advanced) for the team. Use the same tier across the team, not mixed.

3. **Lock in dimension weights.** All four dimensions are equally weighted by default. If your org values some more (say, Enablement for platform teams), document that and announce it before the quarter starts.

4. **Hand out templates:**
   - Tier 1: `templates/tier1-assessment.md`
   - Tier 2: `templates/tier2-assessment.md`

5. **Set clear expectations:**
   - This measures outcomes and contribution, not activity.
   - Engineers log contributions as they happen, not from memory at quarter end.
   - Evidence matters — design doc ownership, decision calls, incident leadership.
   - No story points, lines of code, or commit counts.

---

## Phase 2: During Quarter — Contribution Logging

**When:** Throughout the quarter
**Who:** Each engineer
**Time:** ~5 minutes per contribution

Log significant work as it finishes:

- The initiative or project
- Your role: designed, built, reviewed, coordinated, or led incident response
- The outcome: shipped feature, fewer incidents, time saved, better reliability
- Evidence: design doc you authored, decision you made, incident you led

Log at natural stops — shipped feature, resolved incident, approved design, quarter end. Skip the routine PRs and tickets. Log what moved the needle.

If you're not sure, log it. Trim during self-assessment. Five minutes per entry is the right pace. If you're spending more, you're overthinking it.

---

## Phase 3: End of Quarter — Assessment

**When:** Weeks 11--12 of the quarter
**Who:** Engineers (self-assessment), then managers (review)
**Time:** Tier 1: ~1 hour. Tier 2: ~4 hours.

### Step 3a: Engineer Self-Assessment

Fill out your assessment template using your contribution log.

For each dimension:
1. List initiatives and contributions with evidence.
2. Self-rate a Contribution Factor (0–1) per initiative using `rubrics/contribution-factor.md`.
3. (Tier 2 only) Score Complexity Factor using `rubrics/complexity-factor.md`.

**Rules for self-assessment:**
- Use the rubric levels, not intuition. "I think I deserve 0.7" doesn't work — say which criteria you meet.
- When unsure, rate lower and explain. Calibration can move you up. Moving down hurts.
- Be specific. "I contributed" isn't evidence. "I authored the SAD, chose the caching vs. queue approach, and led cross-team integration" is evidence.

### Step 3b: Manager Review

Review each engineer's self-assessment within a week.

For each engineer:
1. Validate contribution claims against what you saw and what the record shows.
2. Assign your own Contribution Factor (independent of their self-rating).
3. Flag agreement and disagreement.
4. (Tier 2 only) Validate Complexity Factor — was that work really that hard?

**Rules for manager review:**
- Don't rubber-stamp. Your independent rating feeds calibration.
- If they rated themselves much higher or lower than you would, note why. That's a calibration conversation.
- Grab peer input from 2–3 people. It's advisory — it informs you but doesn't override you.

### Step 3c: Peer Input (Optional for Tier 1, Recommended for Tier 2)

Get input from 2–3 peers. Each peer answers:
- What did they contribute that you saw directly?
- What Contribution Factor for the work you observed? (Use the rubric)
- Did they leave anything out?

Peer input: 15 minutes per person, per engineer.

---

## Phase 4: Calibration and Archive

**When:** Week 13 (first week of next quarter)
**Who:** Calibration panel (managers, tech leads, skip-level)
**Time:** ~2 hours per 10 engineers

### Step 4a: Calibration Meeting

Use `templates/calibration-agenda.md`.

**48 hours before:**
- Managers submit their ratings (not self-assessments).
- Coordinator compiles Contribution Factor distribution per team.

**During the meeting:**
1. Review Contribution Factor distribution. Flag teams with >50% at 0.7+.
2. Walk through each engineer: manager presents, panel discusses.
3. Flag outliers (unusually high or low per dimension).
4. Reach consensus on changes (state why for each one).
5. Run `rubrics/gaming-detection.md`.

**Rules:**
- No stack ranking. Assess against the rubric, not each other.
- No forced distribution. Three Primary Drivers on one team is fine if the evidence backs it.
- Every change needs a reason. "We just feel it" doesn't count.
- Compare like to like: backend to backend, not backend to SRE.

### Step 4b: Communication

Within a week of calibration, managers meet each engineer 1:1:
- Show strengths (highest scores).
- Talk through growth areas (lowest scores, if they matter to the role).
- If calibration changed a score, say why.

### Step 4c: Archive

- Save the completed assessment template to the team's records
- (If using AIEOS integration) Update ER §16 Impact Attribution — see `aieos-integration.md`
- Note any process improvements for next quarter

---

## Annual Synthesis

At year end, pull the four quarterly assessments together:

- Trend per dimension (improving, flat, declining).
- Balance (developing across all dimensions, or staying narrow).
- Trajectory (did they work on growth areas from Q1 and improve by Q4).

The synthesis feeds performance conversations. It's not the review itself — it's the data the review uses.

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

**Q: What if an engineer worked on something without measurable outcomes yet?**
A: Use leading signals (adoption, engagement) for the first 3 months. Discount the Outcome Value for confidence. See the Attribution Lag table in `framework.md`.

**Q: Two engineers both claim Primary Driver. What happens?**
A: Calibration decides. One Primary Driver per initiative. Use evidence — design doc authorship, key architectural calls — to pick the primary. The other scores as Major Contributor (0.7).

**Q: Compare scores across teams?**
A: Compare within similar roles and work. Platform and product engineers have different dimension profiles by design. That's expected.

**Q: What if an engineer owns just one initiative per quarter?**
A: Their score comes from that one initiative. Complexity Factor makes sure a single hard problem doesn't hurt them.

**Q: Mid-quarter joiners?**
A: Prorate the window. Six weeks into a 13-week quarter means assess 7 weeks of work, with cost prorated.
