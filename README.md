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

## The one-paragraph version

Ontario moves somewhere around half a million to seven hundred thousand
non-urgent patients between facilities every year, and roughly eight in ten of
those trips are routine. A large share still ride in fully-equipped 911
ambulances staffed by paramedics, inside a province that spends on the order of
$2B a year on land ambulance. The non-emergency side of the market is not
regulated, not covered by OHIP, and has no single payer — cost lands on
hospitals, long-term care homes, families, Indigenous Services Canada, and
municipalities in unconnected pieces. Nobody holds a view of the whole thing.
That missing coordination layer, not another dispatch console, is the product.

## Working assumptions flagged for the team

- **"EMSS experience" is unconfirmed in this repo.** The survey assumes it means
  prior work on an emergency medical services system (CAD / dispatch / AVL /
  ePCR / crew scheduling). Section 8 maps what carries over and what does not.
  Correct this before Phase 1.
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
