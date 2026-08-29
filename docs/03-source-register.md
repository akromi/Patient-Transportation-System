# Source Register & Verification List

## Research method and its limits

Research was conducted August 2026 using web search. **Direct document retrieval
was blocked by network egress policy for every primary-source domain attempted**
— including `ices.on.ca`, `pmc.ncbi.nlm.nih.gov`, `ontario.ca`, `cihi.ca`,
`ombudsman.on.ca`, `longwoods.com` and `ontariohealth.ca`.

Consequently **facts below were reconstructed from search-result summaries of
those documents, not from the documents themselves.** That is adequate for
shaping product strategy. It is not adequate for a business case, a board deck,
a funding application, or anything a third party will rely on.

## Confidence ratings

- `[H]` **High** — specific figure, named authoritative source, internally consistent
- `[M]` **Medium** — figure appeared in summary but source, year or scope is imprecise
- `[L]` **Low** — this document's own estimate or inference; treat as a hypothesis

---

## Register

### Volumes and system structure

| Fact | Rating | Attributed to |
| --- | --- | --- |
| ~400,000 Ontario inter-facility transfers/yr; ~1,000/day | `[H]` 2009 | *Healthcare Policy* / ICES, U of T, Ornge, Sunnybrook |
| ~$283M annual cost of those transfers | `[H]` 2009 | same |
| 80% routine and non-urgent | `[H]` 2009 | same |
| 10.5 km typical trip; cardiology or dialysis | `[H]` 2009 | same |
| 85,000 patients (24.3%) — dialysis, MD appointments, return home | `[H]` 2009 | same |
| Ornge 23,725 legs / 19,550 patients 2024–25 | `[H]` | Ornge Annual Report 2024/25 |
| Ornge ~98% fixed wing originates Northern Ontario | `[H]` | Ornge |
| CritiCall Repatriation Tool, all acute hospitals since 2014 | `[H]` | CritiCall Ontario |
| Wheel-Trans 3.54M trips 2024, 42,000+ registrants | `[H]` | TTC |
| 16.1M ED visits Canada 2024–25; 17% by ambulance | `[H]` | CIHI NACRS |
| ~10% of ambulance ED arrivals from LTC/retirement homes | `[H]` | CIHI |
| 627 Ontario LTC homes; ~78,000 spaces | `[M]` | OLTCA / CIHI |
| 23,977 beds in construction pipeline (May 2025) | `[M]` | Ministry of Long-Term Care |

### Money

| Fact | Rating | Attributed to |
| --- | --- | --- |
| ~$1B provincial land ambulance funding 2025, +8.7% | `[H]` | MOH / LASG |
| 50/50 provincial–municipal cost share | `[H]` | LASG |
| NIHB Ontario medical transport $166.0M (23–24) | `[H]` | ISC NIHB Annual Report 2023–24 |
| NIHB Ontario $140.3M (22–23), $114.8M (21–22) | `[H]` | ISC NIHB Annual Reports |
| $45M/3yr NHTG expansion; $0.41/km; $175/night to $1,150 | `[M]` | MOH announcements |
| ~66,000 NHTG users 22–23; ~200,000 reimbursements 23–24 | `[M]` | news coverage of MOH data |
| $45 ambulance co-pay; $240 if not medically necessary | `[H]` | Patient Ombudsman |
| Stretcher transport unregulated and uncovered by OHIP | `[H]` | Patient Ombudsman |
| $155M / 57 community surgical & diagnostic centres | `[H]` | MOH 2025 |
| $89M Community Paramedicine for LTC made permanent | `[H]` | MOH 2025 |
| US NEMT SaaS $50–$200+/vehicle/month | `[H]` | vendor pricing surveys 2026 |

### Clinical and demographic

| Fact | Rating | Attributed to |
| --- | --- | --- |
| Ontario 65+: 3.1M / 18.9% (2025) → 4.6M / 22.7% (2051) | `[H]` | Ontario population projections |
| >11,000 Ontarians on dialysis | `[H]` | Ontario Renal Network |
| 77.7% of prevalent dialysis patients in-centre HD (national) | `[H]` | CIHI CORR |
| 10% of dialysis patients miss ≥1 session/month; 35% quarterly | `[M]` | dialysis transportation literature |
| ALC = 17.0% of Canadian hospital days 2022–23 | `[H]` | CIHI |
| Canadian no-show rates 10–25%; 15.1% cite transportation | `[M]` | CMAJ / CADTH |
| Toronto ~300,000 offload hours/yr; Ottawa 93,686 | `[M]` | news reporting of service data |

### Regulatory

| Fact | Rating | Attributed to |
| --- | --- | --- |
| PTS sector outside the Ambulance Act / unregulated | `[H]` | multiple, incl. Ombudsman & CBC |
| Ministry cannot enforce local EMS policy — acknowledged gap | `[M]` | Ombudsman Ontario, *Oversight 911* |
| 2011 regulation bill died on dissolution; coroner asking since 1995 | `[M]` | CBC |
| ~400,000/yr carried in private ambulance-like vehicles | `[M]` | CBC — **may double-count the ICES figure; verify** |
| "Medically necessary" undefined in policy or legislation | `[H]` | Patient Ombudsman |
| Bill 60 *Your Health Act* Royal Assent May 2023; ICHSC framework | `[H]` | Stikeman / Miller Thomson |
| PHIPA agent vs. PIPEDA distinction for vendors | `[H]` | IPC Ontario / PHIPA s.2 |
| Ontario FHIR R4 IGs: Patient Summary, Client & Provider Registry, ODHDR, OLIS, eReferral, OCRE | `[H]` | eHealth Ontario standards |

### Competitors

| Fact | Rating |
| --- | --- |
| Voyago/Transdev 600+ medical attendants; NEPT ~35% of contracts; acquired Priority Patient Transfer | `[H]` |
| Ontario Patient Transfer incorporated 1994, Hamilton HQ, named base network | `[M]` |
| RNR Hamilton-based, 16+ years | `[M]` |
| Uber Health live in Ontario; Hope Air partnership Aug 2024 | `[H]` |
| Ryde Central: hospital↔provider automation, EHR pull, Uber/Lyft, CAD/EHR integration | `[M]` — no Ontario presence confirmed |
| RouteGenie 25+ broker connections (MTM, ModivCare, Veyo…) | `[H]` |
| Spare Labs / Pantonium / Blaise profiles | `[H]` |

---

## Verification list — do these before external use

**Blocking for any business case:**

1. **Refresh the 2009 transfer study.** Obtain the *Healthcare Policy* paper
   (PMC2653709) and find or commission a current equivalent. Everything in
   `02-opportunity-model.md` §3 S-A rests on it.
2. **Resolve the double-count risk.** The CBC "400,000 in private
   ambulance-like vehicles" figure and the ICES "400,000 inter-facility
   transfers" figure are suspiciously identical. If they are the same number
   reported twice, the private-PTS pool estimate is wrong.
3. **Get real PTS pricing.** Quotes from 10–15 Ontario operators across
   modalities. Tightens S-A more than any other single input.
4. **Ontario Renal Network transport data.** The 30–50% assisted-transport
   assumption underpins the recommended wedge and is currently a guess.

**Important:**

5. Ontario-specific ED ambulance arrivals (CIHI provincial breakdown).
6. Current provincial offload-delay data — the province has previously declined
   to release it; may require FOI.
7. NIHB Ontario contracting structure — is the $166M platform-contestable?
8. Confirm no active Ontario patient-transfer regulation in the current
   legislative session (none found; absence of evidence only).
9. Ontario paramedic service count and total land ambulance fleet size.
10. Municipal specialized transit trip totals province-wide.
11. Whether Ryde Central or any US orchestration vendor has entered Ontario.

**Nice to have:**

12. Ontario Health atHome / community support services transportation budget.
13. WSIB and private-insurer medical transportation spend in Ontario.
14. Hope Air Ontario volumes.
