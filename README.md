# Ontario Patient Transportation System

A discovery repository for a new patient transportation platform designed
specifically for Ontario's health system.

## Where this is

**Phase 0 — Product space and market survey.** No code yet. This repository
currently holds the research that decides what gets built.

| Document | What it covers |
| --- | --- |
| [`docs/decision-memo.md`](docs/decision-memo.html) | **Start here.** The verdict: is there a market, what shape should it take, and the one conversation that settles it |
| [`docs/01-market-survey.md`](docs/01-market-survey.md) | The full survey: system map, demand drivers, payer flows, regulation, competitors, whitespace |
| [`docs/02-opportunity-model.md`](docs/02-opportunity-model.md) | Bottom-up sizing with every assumption written down and auditable |
| [`docs/03-source-register.md`](docs/03-source-register.md) | Every source used, with a confidence rating and a verification to-do list |
| [`docs/04-emss-reuse-assessment.md`](docs/04-emss-reuse-assessment.md) | Read-only review of the EMSS codebase: what actually carries over, what does not, and why the architectural thesis doesn't |
| [`docs/05-ottawa-business-case.md`](docs/05-ottawa-business-case.md) | Financial case for **operating** a service in Ottawa — unit economics, break-even, three-year projection, and the one contract it turns on |

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

The survey's original §10 assumed EMSS meant a dispatch/CAD system. **It does
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

## The verdict

Recorded in the [decision memo](https://claude.ai/code/artifact/b6fd4f4b-a85a-4d13-ae86-07da4b3b21cf):

**Software alone, sold as software, is a weak business here.** The pain is real
and large; the willingness to pay for software specifically is unproven, and the
per-vehicle SaaS ceiling ($3.4–5.8M ARR at total penetration) does not justify
the clinical and regulatory work. Prehos is the natural experiment — displaced
buyers chose another backend platform, not better architecture.

**The shape that works is services-led:** operate the Ottawa dialysis book,
instrument it, then sell the coordination layer outward from a working reference
site. Operating solves software's missing-payer problem; the software layer
solves operating's margin and defensibility problem.

**The case against is legitimate.** If the constraint is capital and speed, the
EMSS product's humanitarian path reaches revenue in months against a
three-to-five-year build here.

## Next

One conversation with The Ottawa Hospital's Regional Nephrology Program — what
missed treatments cost them, what transport costs them today, and whether a
contracted pooled service interests them. It costs nothing and collapses the
decision tree. Everything else in this repository is a plan waiting on it.

## Published versions

| Page | Source |
| --- | --- |
| [Ontario's Transport Gap](https://claude.ai/code/artifact/748f9af1-5f57-4cf7-9de7-75e11062ca51) — the survey | [`docs/ontario-transport-gap.html`](docs/ontario-transport-gap.html) |
| [Ottawa Service Business Case](https://claude.ai/code/artifact/47a03ec4-6909-4793-bdf8-0432118f1006) | [`docs/ottawa-business-case.html`](docs/ottawa-business-case.html) |
| [Build, Operate, or Neither](https://claude.ai/code/artifact/b6fd4f4b-a85a-4d13-ae86-07da4b3b21cf) — the decision memo | [`docs/decision-memo.html`](docs/decision-memo.html) |

## PDFs

Both studies render to print-ready PDFs in [`pdf/`](pdf/):

```bash
python3 scripts/build-pdfs.py
```

Headless Chromium prints the `docs/*.html` pages with a print stylesheet (Letter,
light theme forced, tables unclipped, logical units kept off page breaks). Note
that this sandbox blocks Google Fonts, so locally-built PDFs fall back to system
faces; the published web pages render the intended typography.

## City deep-dives

Survey §7 covers **Ottawa**, §8 covers **Toronto**. The short version: Ottawa's
ambulance-offload crisis is largely resolved (Montfort 224 → 53 minutes,
"level zero" down 92% year over year), so the ambulance-hours argument no longer
lands there — but its 900-patient single-program dialysis book is the strongest
anchor in the province. Toronto is the inverse: a severe, unresolved offload
problem, the densest competition in Ontario, Uber Health already live, and no
single buyer big enough to anchor a fleet. **Start in Ottawa, expand to Toronto.**
