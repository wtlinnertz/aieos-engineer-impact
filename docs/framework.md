     1|# Engineer Impact Framework
     2|
     3|*Canonical reference for measuring engineer impact through outcomes, not activity.*
     4|
     5|---
     6|
     7|## Adoption Tiers: Choose Your Starting Point
     8|
     9|This framework has two versions. Start with Tier 1, then upgrade when ready.
    10|
    11|### Tier 1: Starter Framework (Recommended for New Adopters)
    12|
    13|Use this if: You've never quantified engineer impact before, or you want a lightweight process.
    14|
    15|**Time investment:** ~2 hours per quarter
    16|**Complexity:** Low (one formula, three contribution levels, quarterly updates)
    17|
    18|See `templates/tier1-assessment.md` for the Tier 1 template.
    19|
    20|---
    21|
    22|### Tier 2: Advanced Framework (This Document)
    23|
    24|Use this if: You've used Tier 1 for 2+ quarters, or you need to compare different types of work (product vs platform vs ops).
    25|
    26|**Time investment:** ~8 hours per quarter
    27|**Complexity:** High (four dimensions, complexity factors, calibration meetings)
    28|
    29|**Upgrade when:**
    30|- 3+ teams are using Tier 1 comfortably
    31|- Leadership asks for portfolio-level insights
    32|- Engineers complain about fairness (hard projects not getting credit)
    33|- You see gaming behaviors (cherry-picking easy work)
    34|
    35|See `templates/tier2-assessment.md` for the Tier 2 template.
    36|
    37|---
    38|
    39|## The Rule of Engagement
    40|
    41|Before the formulas, align on this sentence:
    42|
    43|> *"Individual engineer impact can be estimated, but only as a proxy using outcomes the engineer materially influenced, over a defined time period and comparable domains (e.g., compare backend engineers to backend engineers, not to SREs; compare work within the same business context). This estimate is one input, not the sole input, for evaluating engineer contributions."*
    44|
    45|This lets us provide math without claiming false precision.
    46|
    47|---
    48|
    49|## The Core Pattern
    50|
    51|- Measure outcomes at the team/system level
    52|- Allocate impact to individuals based on contribution, not output
    53|- Normalize by cost
    54|- Pair quantitative scores with qualitative assessments
    55|
    56|This preserves business and engineering reality.
    57|
    58|---
    59|
    60|## Engineer Value Portfolio
    61|
    62|Individual engineer value comes from four complementary dimensions. **Don't rely on a single number.**
    63|
    64|```
    65|Total Engineer Value =
    66|  Outcome-Driven Impact
    67|+ Enablement Impact
    68|+ Operational Excellence
    69|+ Team Multiplier
    70|```
    71|
    72|---
    73|
    74|## Interpreting ROI Scores: Expected Ranges
    75|
    76|Different dimensions of engineering work have different natural ROI profiles. This is expected and does not indicate underperformance.
    77|
    78|| Dimension | Typical Range | Top Performer | Why Ranges Differ |
    79||---|---|---|---|
    80|| **Outcome Impact** | 2x - 10x | 15x+ | Direct business value; high leverage when product-market fit is strong |
    81|| **Enablement Impact** | 1.5x - 5x | 8x+ | Scales with team size; platform/infrastructure work can be very high-leverage |
    82|| **Operational Excellence** | 1x - 3x | 5x+ | Often underestimated; value is in risk/cost avoided rather than revenue created |
    83|| **Team Multiplier** | 0.1x - 0.5x | 1.0x+ | Hardest to quantify; conservative measurement; long-term compounding value |
    84|
    85|---
    86|
    87|## Why Team Multiplier Scores Are Lower (And That's OK)
    88|
    89|Mentorship, knowledge-sharing, and cultural work have:
    90|
    91|1. **Conservative measurement:** Hard to attribute productivity gains precisely, so we underestimate
    92|2. **Lagging returns:** Mentees take 6--12 months to show improvement; value accrues slowly
    93|3. **Compounding effects:** A mentee's growth continues for years; we only measure near-term impact
    94|4. **Indirect attribution:** Mentee's manager and project also contributed to their growth
    95|
    96|A Team Multiplier score of 0.1x--0.3x is **GOOD** for a senior/staff engineer. It indicates healthy investment in team capacity.
    97|
    98|If we measured long-term compounding value (5-year horizon), this number would be much higher.
    99|
   100|### Red Flags: When Low Scores Are a Problem
   101|
   102|Small numbers are a problem if:
   103|
   104|| Scenario | Red Flag | Action |
   105||---|---|---|
   106|| **All dimensions below their expected typical range** (e.g., Outcome Impact < 2x, Team Multiplier < 0.1x) | Engineer is underperforming across the board relative to peers | Performance improvement plan; role mismatch; consider transition |
   107|| **Outcome Impact < 0.5x for product engineer** | Primary job dimension is underperforming | Investigate: Blocked? Wrong projects? Skill gap? |
   108|| **Team Multiplier = 0 for Staff+ engineer** | Not investing in team leverage | Coaching: Mentor, share knowledge, lead initiatives |
   109|| **Scores declining over time** | Disengagement or burnout | 1:1 conversation; adjust workload or role |
   110|
   111|But if an engineer has:
   112|- High Outcome Impact (6.7x)
   113|- Low Team Multiplier (0.12x)
   114|
   115|That's fine: they're focused on delivery, not mentorship. As long as they're not expected to mentor (e.g., IC track, not people-focused), this is appropriate specialization.
   116|
   117|**Critical:** An engineer may score high in one dimension and low in others. A balanced portfolio is healthier than a single-dimension specialist (except for specialists like platform engineers).
   118|
   119|---
   120|
   121|## Shared Component: Engineer Cost
   122|
   123|**Fully loaded cost:**
   124|
   125|```
   126|Salary + Benefits + Overhead (facilities, tools, recruiting, management)
   127|```
   128|
   129|- Business-standard denominator
   130|- Lets finance compare investments
   131|- With Complexity Factor, doesn't unfairly penalize senior engineers
   132|
   133|**Rule:** Normalize cost over the same window as the outcome measurement (e.g., trimester/year), especially for long-running initiatives.
   134|
   135|---
   136|
   137|## 1. Outcome-Driven Impact Score
   138|
   139|### Formula
   140|
   141|```
   142|Engineer Impact Score =
   143|  SUM ((Outcome Value x Confidence Level) x Contribution Factor x Complexity Factor) / Engineer Cost
   144|```
   145|
   146|> **Note:** `Confidence Level` defaults to 1.0 when outcome is certain. Apply a discount (e.g., 0.6) only when the outcome is uncertain or still materializing. See *Risk-Adjusted Value* below.
   147|
   148|### Component 1: Outcome Value
   149|
   150|Measured after delivery, not predicted. Each outcome must have a defined measurement and baseline (e.g., pre/post or A/B):
   151|
   152|- Revenue increase
   153|- Cost reduction
   154|- Risk reduction (incident cost avoided)
   155|- Productivity unlocked (hours saved x blended rate)
   156|- Customer retention improvement
   157|
   158|**Guardrail:** For any single initiative, Outcome Value must be "owned" once and then allocated across contributors, to prevent double-counting across sub-teams.
   159|
   160|### Handling Attribution Lag
   161|
   162|Many outcomes take 6--12 months to materialize. Use this approach:
   163|
   164|| Timeline | Measurement Approach |
   165||---|---|
   166|| **0--3 months** | Use leading indicators (adoption rate, engagement, usage) as proxies |
   167|| **3--6 months** | Blend leading indicators with early lagging indicators (revenue trend, support ticket reduction) |
   168|| **6+ months** | Use full lagging indicators (actual revenue, retention, cost savings) |
   169|
   170|### Risk-Adjusted Value
   171|
   172|If confidence in outcome is uncertain, discount the value:
   173|
   174|```
   175|Attributed Value = Expected Value x Confidence Level
   176|```
   177|
   178|**Example:**
   179|- Expected churn reduction: $1M
   180|- Confidence: 60%
   181|- Attributed Value: $600k
   182|
   183|### Handling Failed Experiments
   184|
   185|High-quality work that doesn't produce business results should not be penalized:
   186|
   187|- If failure was due to market/customer rejection: Attribute effort value (cost of equivalent work that succeeded)
   188|- If failure was due to poor execution: Use retrospective to improve process, don't attribute negative value
   189|- If failure taught critical lessons: Attribute learning value (cost of alternative path avoided)
   190|
   191|**Never attribute negative outcome value except in cases of gross negligence (rare).**
   192|
   193|---
   194|
   195|### Component 2: Contribution Factor (0--1 scale)
   196|
   197|Represents material influence, not lines of code. Assignment requires judgment based on demonstrated behaviors.
   198|
   199|See `rubrics/contribution-factor.md` for the full rubric with observable criteria.
   200|
   201|| Score | Label | Summary |
   202||---|---|---|
   203|| **1.0** | **Primary Driver** | Owned technical design, made final architectural decisions, led implementation, accountable for delivery |
   204|| **0.7** | **Major Contributor** | Owned significant subsystem, drove critical decisions, unblocked team |
   205|| **0.4** | **Meaningful Contributor** | Implemented substantial features, coordinated across teams, led critical fixes |
   206|| **0.2** | **Supporting Contributor** | Implemented scoped tasks within others' designs, meaningful review input |
   207|| **0.1** | **Peripheral Contributor** | Minor code contributions, participated without decision authority |
   208|
   209|### How to Assign Contribution Factors
   210|
   211|**Process:**
   212|
   213|1. Self-assessment (engineer rates themselves with evidence)
   214|2. Manager assessment (validates against observable criteria and applies judgment)
   215|3. Peer input (2--3 peers provide scores + justification)
   216|4. Tech lead calibration (ensures consistency across projects)
   217|5. Cross-team calibration (quarterly review to prevent inflation, see Calibration section)
   218|
   219|**Evidence Sources:**
   220|
   221|- Design doc authorship/ownership
   222|- RFC/ADR (Architecture Decision Record) leadership
   223|- Pull request review activity (who was the final approver on critical design decisions, not just routine code reviews)
   224|- Meeting notes (who drove technical decisions?)
   225|- Incident reports (who led response?)
   226|- Communication threads (who unblocked the team?)
   227|
   228|---
   229|
   230|### Component 3: Complexity Factor
   231|
   232|Prevents penalizing senior engineers who take on hard, risky, long-term work.
   233|
   234|See `rubrics/complexity-factor.md` for the full rubric with dimension scoring.
   235|
   236|```
   237|Complexity Factor = 1.0 + (Risk x 0.3) + (Novelty x 0.2) + (Org Friction x 0.2)
   238|```
   239|
   240|Each dimension scored 0.0--1.0:
   241|
   242|| Dimension | 0.0 | 0.5 | 1.0 |
   243||---|---|---|---|
   244|| **Risk** | Low-risk, well-understood problem | Moderate risk, some unknowns | High technical risk, novel approach, potential for failure |
   245|| **Novelty** | Maintenance, minor iteration | Greenfield component within known system | Entirely new architecture, unproven technology |
   246|| **Org Friction** | Single team, clear ownership | Cross-team coordination (2--3 teams) | Cross-org dependencies, external stakeholders, compliance |
   247|
   248|**Complexity Factor Range:** 1.0 (routine work) to 1.7 (maximum complexity)
   249|
   250|This means the highest-complexity work can earn up to **70% bonus credit** for difficulty.
   251|
   252|**Example:**
   253|- High-risk migration (Risk = 1.0)
   254|- Greenfield platform (Novelty = 1.0)
   255|- 5 teams involved (Org Friction = 1.0)
   256|- Complexity Factor = 1.0 + 0.3 + 0.2 + 0.2 = **1.7**
   257|
   258|---
   259|
   260|## 2. Enablement Impact Score
   261|
   262|Critical for platform engineers, SREs, and tooling teams.
   263|
   264|### Formula
   265|
   266|```
   267|Enablement Impact =
   268|  (SUM Team Productivity Gains Enabled x Contribution Factor) / Engineer Cost
   269|```
   270|
   271|### What Counts as Productivity Gains
   272|
   273|| Type | Measurement |
   274||---|---|
   275|| **Time savings** | Hours saved per engineer x # engineers x blended rate x 220 work days |
   276|| **Velocity increase** | % reduction in lead time x team throughput x value per delivery |
   277|| **Defect reduction** | Incidents avoided x average incident cost |
   278|| **Onboarding acceleration** | Days saved to productivity x new hire count x blended rate |
   279|| **Tech debt reduction** | Future maintenance hours avoided x blended rate |
   280|
   281|### Example
   282|
   283|**Scenario:**
   284|- CI/CD automation saves 20 engineers 1 hour/day
   285|- 20 x 1 hour x 220 days x $90/hr = $396k/year
   286|- Platform engineer cost: $170k
   287|- Contribution Factor: 1.0 (sole owner)
   288|
   289|```
   290|Enablement Impact = ($396k x 1.0) / $170k = 2.3x
   291|```
   292|
   293|---
   294|
   295|## 3. Operational Excellence Score
   296|
   297|For incident response, on-call, reliability, and technical debt work.
   298|
   299|### Formula
   300|
   301|```
   302|Operational Excellence Score =
   303|  (SUM (Cost Avoided + Reliability Value) x Contribution Factor) / Engineer Cost
   304|```
   305|
   306|> **Note:** Contribution Factor is applied here for the same reason as other dimensions: when multiple engineers collaborate on incident response or reliability work, the total value must be allocated by individual contribution rather than attributed in full to each person.
   307|
   308|### Component 1: Cost Avoided
   309|
   310|> Captures direct, incident-driven costs. **MTTR-related savings belong here only.** Do not also count them in Reliability Value.
   311|
   312|| Activity | Measurement |
   313||---|---|
   314|| **Incident response** | (MTTR reduction) x (incident frequency) x (average incident cost per hour) |
   315|| **Preventive fixes** | Estimated future incident cost avoided (use historical data) |
   316|| **Technical debt cleanup** | Future velocity improvement x team hourly cost |
   317|| **Security hardening** | Estimated breach cost x probability reduction |
   318|
   319|### Component 2: Reliability Value
   320|
   321|> Captures structural reliability improvements **not already counted in Cost Avoided**. Do not include MTTR here if it was already measured above.
   322|
   323|| Metric | Measurement |
   324||---|---|
   325|| **Uptime improvement** | SLA compliance improvement x revenue at risk |
   326|| **Change failure rate reduction** | Deployments per month x CFR improvement x avg rollback cost |
   327|
   328|### Example
   329|
   330|**Scenario:**
   331|- Engineer reduced MTTR from 45 min to 15 min (saves 0.5 hr per incident)
   332|- 12 incidents/year
   333|- Avg incident cost: $50k/hour
   334|- Cost avoided: 12 x 0.5 hr x $50k/hr = $300k
   335|- Reliability Value (uptime/CFR improvements): $0 (not applicable here)
   336|- Contribution Factor: 1.0 (sole responder on MTTR work)
   337|- Engineer cost: $160k
   338|
   339|```
   340|Operational Excellence = (($300k + $0) x 1.0) / $160k = 1.9x
   341|```
   342|
   343|---
   344|
   345|## 4. Team Multiplier Score
   346|
   347|For mentorship, hiring, knowledge sharing, and cultural contributions.
   348|
   349|### Formula
   350|
   351|```
   352|Team Multiplier Score =
   353|  (Team Productivity Increase Attributable to Mentorship/Enablement) / Engineer Cost
   354|```
   355|
   356|### What Counts
   357|
   358|| Activity | Measurement |
   359||---|---|
   360|| **Mentorship:** Demonstrated improvement in mentee's autonomy, code quality, and project ownership. | Mentee productivity increase x mentee cost x attribution factor |
   361|| **Hiring:** Active participation in interview loops, providing high-quality feedback, and contributing to debriefs. | New hire quality x cost of bad hire avoided x attribution factor |
   362|| **Knowledge sharing:** Creating durable documentation, leading tech talks, or establishing new team rituals that reduce knowledge silos. | Time saved across team (documentation, internal talks, pairing) x blended rate |
   363|| **Process improvement:** Identifying and driving changes to team workflows that demonstrably reduce friction or increase quality. | Team velocity increase x team cost x attribution factor |
   364|
   365|### Example
   366|
   367|**Scenario:**
   368|- Senior engineer mentors 2 junior engineers
   369|- Mentees each improve productivity by 20% (measured via delivery output)
   370|- Mentee avg cost: $120k
   371|- Productivity gain: 2 x $120k x 0.2 = $48k
   372|- Attribution factor: 0.5 (shared with other mentors/managers)
   373|- Senior engineer cost: $200k
   374|
   375|```
   376|Team Multiplier = ($48k x 0.5) / $200k = 0.12x
   377|```
   378|
   379|Note: This score will be lower than outcome-driven scores. That's expected. Senior engineers should have a portfolio across all four dimensions.
   380|
   381|---
   382|
   383|## Sub-Team Calibration Process
   384|
   385|Prevents score inflation and gaming. See `templates/calibration-agenda.md` for the meeting template.
   386|
   387|### Quarterly Calibration Meeting
   388|
   389|**Attendees:** Engineering managers, tech leads, skip-level manager
   390|
   391|**Agenda:**
   392|
   393|1. **Review Contribution Factor distribution across teams**
   394|   - Flag sub-teams with >50% of engineers at 0.7+ (likely inflation: 0.7 and above should not be the norm)
   395|   - Compare similar projects across sub-teams for consistency
   396|
   397|2. **Review Complexity Factor assignments**
   398|   - Ensure "high complexity" isn't overused
   399|   - Validate against objective criteria
   400|
   401|3. **Spot-check outcome value attribution**
   402|   - Ensure business value isn't double-counted across sub-teams
   403|   - Validate attribution lag assumptions
   404|
   405|4. **Normalize outliers**
   406|   - If one team's scores are significantly higher than all other teams (e.g., 30%+ above average), investigate
   407|   - Adjust rubric interpretation or provide feedback
   408|
   409|5. **Share learnings**
   410|   - What worked well in attribution?
   411|   - What was hard to measure?
   412|
   413|**Output:** Calibrated scores, updated rubric guidance, process improvements
   414|
   415|---
   416|
   417|## What NOT to Include (Non-Negotiable)
   418|
   419|**Never use these as impact measures:**
   420|
   421|- Story count
   422|- Story points
   423|- Individual velocity
   424|- Lines of code
   425|- Commit counts
   426|- "Delivery time per engineer"
   427|- Time tracking (incentivizes long hours, not outcomes)
   428|- PR count (incentivizes small, low-value changes)
   429|- Code churn (can be positive or negative, context-dependent)
   430|- Review comment count (incentivizes nitpicking)
   431|
   432|These invalidate the calculation and will be gamed.
   433|
   434|---
   435|
   436|## Elevator Pitch
   437|
   438|> "We can absolutely quantify engineer impact, but it has to be grounded in outcomes the business cares about.
   439|>
   440|> Instead of measuring activity, we measure business results and allocate impact based on contribution.
   441|>
   442|> Here's how it works:
   443|>
   444|> 1. Measure results (revenue, cost savings, risk reduction): the numbers finance already trusts
   445|> 2. Allocate credit based on who drove the work (not who wrote the most code), using an observable rubric
   446|> 3. Normalize by cost so we can compare investments
   447|> 4. Adjust for complexity so hard, risky work isn't penalized
   448|>
   449|> This gives us a number finance can trust, aligns engineers with company goals, and avoids the gaming problems you see with story points or velocity.
   450|>
   451|> But this is one input, not the whole picture. We pair it with:
   452|> - Qualitative assessments (peer feedback, growth, mentorship)
   453|> - Portfolio balance (outcome impact, enablement, operational excellence, team multiplier)
   454|> - Calibration across teams to prevent inflation
   455|>
   456|> This way, we get credible numbers without destroying engineering culture."
   457|
   458|---
   459|
   460|## Gaming Risks and Mitigation
   461|
   462|See `rubrics/gaming-detection.md` for the full detection checklist.
   463|
   464|| Gaming Behavior | Risk | Mitigation |
   465||---|---|---|
   466|| **Cherry-picking high-value work** | Avoid necessary low-visibility tasks | Manager oversight (balanced portfolio requirement); Operational excellence score (rewards grunt work) |
   467|| **Inflating contribution factors** | Self-promotion, politics | Multi-source input (self + manager + peers + tech lead); Cross-team calibration |
   468|| **Avoiding risky work** | Stick to safe bets, kill innovation | Complexity factor (rewards risk-taking); Qualitative assessment (growth, experimentation) |
   469|| **Sandbagging estimates** | Inflate expected value, look good when it hits | Risk-adjusted value (discount uncertain outcomes); Retrospective validation (did value materialize?) |
   470|| **Claiming credit for others' work** | Attribution theft | Peer review in contribution assignment; Version control evidence (design docs, PRs, decisions) |
   471|
   472|**Manager responsibility:** Managers must actively monitor for gaming and override scores when necessary. The framework is a tool, backed by evidence and judgment.
   473|
   474|---
   475|
   476|## Final Truth
   477|
   478|There is no perfect individual productivity formula. But this approach:
   479|
   480|- Preserves system thinking
   481|- Produces credible math
   482|- Survives executive scrutiny
   483|- Doesn't rot engineering culture
   484|- Balances quantitative rigor with qualitative judgment
   485|- Prevents gaming through calibration and portfolio thinking
   486|- Values all types of engineering work, not just feature delivery
   487|