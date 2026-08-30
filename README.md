# Ontario Patient Transportation System

A discovery repository for a new patient transportation platform designed
specifically for Ontario's health system.

## Where this is

**Phase 0 — Product space and market survey.** No code yet. This repository
currently holds the research that decides what gets built.

| Document | What it covers |
| --- | --- |
| [`docs/01-market-survey.md`](docs/01-market-survey.md) | The full survey: system map, demand drivers, payer flows, regulation, competitors, whitespace |
| [`docs/02-opportunity-model.md`](docs/02-opportunity-model.md) | Bottom-up sizing with every assumption written down and auditable |
| [`docs/03-source-register.md`](docs/03-source-register.md) | Every source used, with a confidence rating and a verification to-do list |
| [`docs/04-emss-reuse-assessment.md`](docs/04-emss-reuse-assessment.md) | Read-only review of the EMSS codebase: what actually carries over, what does not, and why the architectural thesis doesn't |

## The one-paragraph version

Ontario runs somewhere around half a million to seven hundred thousand
inter-facility patient transfers every year — trips, not unique people — and
roughly eight in ten of those transfers are clinically routine. A large share
still ride in fully-equipped 911 ambulances staffed by paramedics, inside a
province that spends on the order of $2B a year on land ambulance. The non-emergency side of the market is not
regulated, not covered by OHIP, and has no single payer — cost lands on
hospitals, long-term care homes, families, Indigenous Services Canada, and
municipalities in unconnected pieces. Nobody holds a view of the whole thing.
That missing coordination layer, not another dispatch console, is the product.

## EMSS — resolved

EMSS is **AidPost** (`akromi/emergency-medical-support-system`), an offline-first
PWA for casualty care and transport documentation — reviewed **read-only** at
commit `a8eb1d9`; nothing in that repository was modified.

The survey's original §08 assumed EMSS meant a dispatch/CAD system. **It does
not** — there is no CAD, AVL, crew scheduling or allocation engine in it. What
does carry over is more useful than what was assumed: a working **Ontario Health
Provincial Client Registry FHIR adapter** with ONE ID auth and ATNA audit, a
Lamport-clocked conflict-aware sync engine, a multi-tenant backend, and PHIPA-grade
security primitives. What does *not* carry over is the product thesis — AidPost's
"no backend" differentiator is the opposite of what a transport coordination
layer needs. See `docs/04-emss-reuse-assessment.md`.

AidPost also carries its own four-pass Canadian market survey, better-evidenced
than this one. Its findings are merged into the survey and marked `[AidPost]`;
where the two disagree, theirs wins.

## Working assumptions flagged for the team

- **Figures came from search-result summaries, not fetched primary documents.**
  Network egress restrictions during this research blocked direct retrieval of
  ICES, PubMed, ontario.ca, CIHI and Ombudsman sources. Every number carries a
  confidence rating in the source register. Verify anything marked MEDIUM or LOW
  before it enters a business case or an investor deck.

## Next

Phase 1 depends on two decisions that are the team's to make, not the
research's: which beachhead segment to attack first, and whether the product is
a coordination layer, an operator, or a payer-side utility. See §10.

## Published version

The survey is also published as a readable page:
<https://claude.ai/code/artifact/748f9af1-5f57-4cf7-9de7-75e11062ca51>

Source for that page is checked in at
[`docs/ontario-transport-gap.html`](docs/ontario-transport-gap.html).
