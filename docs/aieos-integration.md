# AIEOS Integration Guide

This document describes how the Engineer Impact Framework optionally connects to the AIEOS governance framework. **This integration is entirely optional.** The Engineer Impact Framework works standalone — teams do not need AIEOS to use it.

---

## Overview

The integration has two touchpoints:

1. **Engagement Record §16 (Impact Attribution)** — a lightweight section in the AIEOS Engagement Record that tracks who contributed what at each artifact freeze point. This records contribution data as it happens (during the initiative) rather than reconstructing it quarterly.

2. **Insight & Evolution Kit (IEK)** — the Evolution Signal (ES) and Portfolio Evolution Signal (PES) can optionally consume impact attribution data to enrich their analysis of reliability patterns and cross-initiative trends.

---

## How ER §16 Connects to Impact Assessments

### ER §16 Records Contribution in Real Time

When an AIEOS initiative freezes an artifact, ER §16 captures:

| Layer | Artifact ID | Contributor | Role | Contribution Level | Notes |
|-------|-------------|-------------|------|-------------------|-------|
| 4 | SAD-NOTIFY-001 | J. Smith | System Architect | Primary | Authored design, made caching decision |
| 4 | TDD-NOTIFY-001 | A. Lee | Test Lead | Significant | Owned test strategy and state machine coverage |
| 5 | RR-NOTIFY-001 | J. Smith | Release Owner | Primary | Led release execution |

### Quarterly Assessment Uses ER §16 as Evidence

When engineers complete their quarterly impact assessment (Tier 1 or Tier 2), they can reference ER §16 entries as evidence for their Contribution Factor self-rating.

**Example mapping:**

| ER §16 Entry | Assessment Evidence |
|-------------|-------------------|
| "Primary" on SAD-NOTIFY-001, role: System Architect | Supports Contribution Factor 1.0 claim: "Owned technical design, made final architectural decisions" |
| "Significant" on TDD-NOTIFY-001, role: Test Lead | Supports Contribution Factor 0.7 claim: "Owned significant subsystem (test strategy)" |
| "Supporting" on RR-NOTIFY-001, role: On-call responder | Supports Contribution Factor 0.2 claim: "Provided on-call support during rollout" |

### Contribution Level Mapping

ER §16 uses three coarse levels for quick recording at freeze time. The quarterly assessment rubric uses a fine-grained 0--1 scale. The mapping:

| ER §16 Level | Typical Assessment Range | Meaning |
|-------------|------------------------|---------|
| **Primary** | 0.7 -- 1.0 | Drove the artifact — design ownership, final decisions, accountability |
| **Significant** | 0.4 -- 0.6 | Major contributor — owned a subsystem, shaped direction, unblocked team |
| **Supporting** | 0.1 -- 0.3 | Reviewed, consulted, assisted — meaningful input without decision authority |

The fine-grained score is determined by the rubric criteria in `rubrics/contribution-factor.md`, not by the ER §16 level alone. ER §16 is evidence; the rubric is the standard.

---

## Pseudonym Consistency

Both ER §16 and impact assessments support pseudonyms (consistent with the AIEOS release-entry-spec.md convention). When using pseudonyms:

- Use the **same pseudonym** in both ER §16 and the quarterly assessment
- Reference the **same identity mapping location** (e.g., "mapping maintained in {location}") in both places
- The mapping location must be accessible to the calibration panel but need not be in the artifacts themselves

---

## IEK Consumption

### Evolution Signal (ES)

When generating an ES for an initiative that has ER §16 data:

- The ES may reference execution patterns in §7 Recommended Actions (e.g., "artifacts with single-contributor Primary had higher re-entry rates for this initiative")
- This is advisory context — it does not affect the re-entry signal or hard gates
- If ER §16 is not populated, the ES proceeds normally with no impact

### Portfolio Evolution Signal (PES)

When generating a PES across multiple initiatives that have ER §16 data:

- The PES may note correlations between contributor patterns and outcomes in §4 Cross-Initiative Reliability Patterns (e.g., "initiatives with distributed contribution across 3+ engineers showed more stable reliability trends")
- This is optional analysis — it does not affect improvement proposals or hard gates
- If fewer than 2 initiatives have ER §16 data, this analysis is skipped

---

## What This Integration Does NOT Do

- **Does not make impact assessment a governed artifact.** Impact assessments are not validated by AIEOS validators. They are team-internal documents.
- **Does not add hard gates.** ER §16 is optional. IEK references to impact data are advisory. No artifact can fail validation due to missing impact data.
- **Does not evaluate performance through AIEOS.** The ES spec explicitly states it is "not a performance review." Impact data enriches pattern analysis — it does not judge individuals.
- **Does not require AIEOS adoption.** Teams can use the Engineer Impact Framework with no AIEOS integration at all.
