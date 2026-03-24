# Calibration Meeting Agenda

## Meeting Details

| Field | Value |
|-------|-------|
| Quarter | {Q1/Q2/Q3/Q4 YYYY} |
| Date | {YYYY-MM-DD} |
| Duration | {2 hours per 10 engineers} |
| Facilitator | {name} |
| Attendees | {engineering managers, tech leads, skip-level manager} |
| Teams in Scope | {list of teams being calibrated} |

---

## Pre-Meeting Preparation (Due 48 Hours Before)

Each manager submits:

- [ ] Preliminary Contribution Factor ratings for each engineer (manager's rating, not self-assessment)
- [ ] Per-initiative Complexity Factor scores (Tier 2 only)
- [ ] Flagged outliers (engineers the manager expects the panel to discuss)
- [ ] Any disagreements with self-assessments that need panel input

Calibration coordinator compiles:

- [ ] Contribution Factor distribution per team (histogram: how many engineers at each level)
- [ ] Cross-team comparison of similar roles
- [ ] Gaming detection pre-screen (see `rubrics/gaming-detection.md`)

---

## Agenda

### 1. Distribution Review (15 minutes)

Review the Contribution Factor distribution across all teams in scope.

**Flags to check:**
- [ ] Any team with >50% of engineers rated 0.7+ (likely inflation)
- [ ] Any team with all engineers rated 0.2 or below (likely undervaluation or low-performing team)
- [ ] Contribution factors for the same initiative summing to >1.0 (double-counting)

**Discussion:** Are the distributions reasonable? Do they match what we know about team performance and project outcomes?

### 2. Complexity Factor Review — Tier 2 Only (15 minutes)

Review Complexity Factor assignments across teams.

**Flags to check:**
- [ ] Any team where all projects score 1.5+ complexity (inflation)
- [ ] Similar projects in different teams scored at very different complexity levels (inconsistency)
- [ ] Complexity scores that don't match observable criteria (Risk/Novelty/Org Friction)

### 3. Engineer Walk-Through (60--90 minutes)

For each engineer (focus on flagged outliers first, then sample across teams):

1. **Manager presents** (2--3 minutes per engineer):
   - Key contributions this quarter
   - Preliminary Contribution Factor and rationale
   - Self-assessment vs. manager-assessment delta (if significant)
   - Peer input highlights

2. **Panel discussion** (2--3 minutes per engineer):
   - Does the Contribution Factor match what the panel observed?
   - Is the Complexity Factor appropriate?
   - Any cross-team context (e.g., this engineer unblocked another team)?
   - Consensus on adjustment (if any)

3. **Record the outcome:**
   - Final Contribution Factor
   - Adjustment rationale (if changed from preliminary)

### 4. Outcome Value Spot-Check (10 minutes)

Select 2--3 high-value initiatives and verify:

- [ ] Business value isn't double-counted across teams
- [ ] Attribution lag assumptions are reasonable
- [ ] Risk-adjusted values reflect actual confidence levels

### 5. Gaming Detection Review (10 minutes)

Run through the gaming detection checklist (`rubrics/gaming-detection.md`):

- [ ] Any engineer claiming Primary Driver on 5+ concurrent initiatives?
- [ ] Any dimension scores that are suspiciously uniform across a team?
- [ ] Any evidence that is entirely self-referential (no external corroboration)?
- [ ] Any pattern of always choosing high-complexity work but delivering average outcomes?

### 6. Process Retrospective (10 minutes)

- What worked well in this quarter's assessment process?
- What was hard to measure or contentious?
- Any rubric clarifications needed for next quarter?
- Any process changes to recommend?

---

## Calibration Rules (Non-Negotiable)

1. **No stack ranking.** Engineers are assessed against the rubric, not ranked against each other.
2. **No forced distribution.** The rubric determines the score, not a predetermined curve.
3. **Every adjustment requires a stated rationale.** "We just feel it should be lower" is not acceptable.
4. **Compare within comparable domains.** Backend to backend, not backend to SRE. Same business context where possible.
5. **Evidence over opinion.** When there's disagreement, the person with evidence wins over the person with feelings.
6. **Confidentiality.** Individual scores discussed in calibration are not shared outside the panel and the engineer's manager.

---

## Post-Meeting Actions

| Action | Owner | Deadline |
|--------|-------|----------|
| Communicate final scores to each engineer in 1:1 | Each manager | Within 1 week |
| Update assessment templates with calibration notes | Each manager | Within 1 week |
| Archive completed assessments | Calibration coordinator | Within 2 weeks |
| Document process improvements for next quarter | Facilitator | Within 1 week |
| (Optional) Update ER §16 Impact Attribution | Each manager | At next artifact freeze |

---

## Meeting Notes

{Capture key discussion points, adjustment decisions, and process improvement ideas here during the meeting.}
