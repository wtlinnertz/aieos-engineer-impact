# Gaming Detection Checklist

Use this checklist during quarterly calibration to detect and address gaming behaviors. Gaming is not malicious — it's a natural response to any measurement system. The goal is to catch it early and adjust, not to punish.

---

## Red Flags

| Indicator | What It Might Mean | How to Investigate |
|-----------|-------------------|-------------------|
| **Contribution factors for the same initiative sum to >1.5** | Double-counting or inflation | Review who actually owned the design and decisions. Only 1 Primary Driver per initiative. |
| **Single engineer claims Primary Driver (1.0) on 3+ concurrent initiatives** | Impossible to be primary on that many things simultaneously | Ask: which one would suffer most if you were removed? That's likely the real primary. |
| **All projects on a team rated 1.5+ complexity** | Complexity inflation — making routine work sound hard | Compare with similar projects on other teams. Are these really novel/risky/cross-org? |
| **Team has >50% of engineers at 0.7+ contribution** | Contribution inflation — everyone can't be a major contributor | 0.7+ should be genuinely rare within a project. Most contributors are 0.2--0.4. |
| **Evidence is entirely self-referential** | Claims without external corroboration | Check: does the manager, tech lead, or peer input confirm this contribution? |
| **Dimension scores are suspiciously uniform across a team** | Scores were "negotiated" rather than independently assessed | Compare self-assessment with manager assessment. If they're identical, one wasn't independent. |
| **Engineer always picks high-outcome-value projects** | Cherry-picking visible work, avoiding necessary low-visibility tasks | Review: is there important work (tech debt, on-call, testing) that nobody is picking up? |
| **Outcome values keep increasing but never get validated** | Sandbagging — inflating expected value, never checking actual | Retrospectively validate: did last quarter's predicted outcomes actually materialize? |
| **Zero Team Multiplier for Staff+ engineer over 2+ quarters** | Not investing in team capacity | If the role expects mentorship/knowledge-sharing, this is a gap. Discuss in 1:1. |
| **Declining scores quarter-over-quarter with no explanation** | Disengagement, burnout, or role mismatch | 1:1 conversation — focus on what's blocking them, not the scores. |

---

## Calibration Checks

Run these checks before or during the calibration meeting:

### Check 1: Distribution Sanity

For each team, plot the Contribution Factor distribution:

- **Healthy distribution:** Most engineers at 0.2--0.4, a few at 0.7, rarely one at 1.0
- **Unhealthy distribution:** Clustered at 0.7--1.0 (inflation) or clustered at 0.1 (undervaluation)

### Check 2: Cross-Team Consistency

Compare Contribution Factors for similar roles doing similar work across teams:

- A backend engineer implementing features on Team A and Team B should have similar ratings for similar work
- If Team A rates everyone 0.7 and Team B rates everyone 0.2, one team's rubric interpretation is off

### Check 3: Outcome Value Validation

For high-value initiatives from prior quarters:

- Did the predicted outcome actually materialize?
- If not, what was the actual value? Should prior scores be retroactively noted (not changed, but noted)?

### Check 4: Complexity Factor Consistency

Compare Complexity Factors for objectively similar projects:

- Two teams doing API integrations with the same 3 partner teams should have similar Org Friction scores
- If one team rates a CRUD feature at 1.5 complexity, something is wrong

---

## What This Framework Does NOT Do

- **Does not punish.** Low scores are data points, not indictments. They trigger conversations, not consequences.
- **Does not stack rank.** Engineers are rated against the rubric, not against each other. Two engineers can both score well.
- **Does not create competition.** The framework values all four dimensions equally. A platform engineer's Enablement Impact is as valid as a product engineer's Outcome Impact.
- **Does not replace judgment.** Numbers are one input. Manager judgment, context, growth trajectory, and team dynamics are all inputs too.
- **Does not measure potential.** It measures what happened this quarter, not what might happen next quarter.

---

## When Gaming Is Detected

1. **Name the pattern** in the calibration meeting (not the person — focus on the behavior).
2. **Adjust the score** with stated rationale documented in calibration notes.
3. **Communicate privately** — the manager discusses the adjustment with the engineer in their 1:1.
4. **Clarify the rubric** — if the gaming happened because the rubric was ambiguous, fix the rubric for next quarter.
5. **Don't over-react.** First-time gaming is usually a misunderstanding of the rubric, not intentional manipulation.
