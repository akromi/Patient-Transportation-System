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

## Second source: the EMSS repository (August 2026)

`akromi/emergency-medical-support-system` at `a8eb1d9` was reviewed **read-only**
after the first draft. Its `docs/canada-market-survey.md` is a four-pass survey
(2026-06-27, updated 06-27, 08-17, 08-18) using multi-source research with
**adversarial 3-vote claim verification** (2 of 3 refutes kills a claim), which
records its own refuted claims and one withdrawn attribution in the open.

**It hit the same constraint this survey did** — its second, third and fourth
passes each record that direct page fetches were blocked by network egress
policy, so its findings also rest on converging search-index summaries. It grades
accordingly. Facts taken from it are marked `[AidPost]` below and inherit its
grading, which is generally better-evidenced than this survey's because its
sources are named, dated and individually cited.

**Where the two documents disagree, AidPost's wins.**

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

### From the EMSS survey `[AidPost]`

| Fact | Rating | Note |
| --- | --- | --- |
| OADS v4.0 effective 2 Sept 2025, under O. Reg. 257/00 Part V Cl. 11.1 | `[H]` | Mandatory for ASOs, paramedics, EMAs, Base Hospitals |
| Prehos notice 8 June 2026; service end announced 7 July 2026 | `[H]` | Switch-off itself **announced and uncontradicted, not verified** — every source is June-dated |
| ~22 Ontario paramedic services displaced; ~$10M owed | `[H]` | Trade press; MOH sourced paper forms, adjusted reporting timelines |
| Prepaid fees became unsecured claims (~$29K at Sault Ste. Marie); recovery unknown | `[H]` | |
| Replacement forced iPad→laptop hardware refresh | `[H]` | |
| Sault Ste. Marie → Interdev/iMedic + HGlobal, ~$63K/yr + ~$33K one-time | `[H]` | Two vendors to replace one |
| No published roster of the ~22 exists | `[H]` | Searched repeatedly; a genuine absence. Renfrew, Parry Sound, Nipissing are documented customers but **only from 2018–2024** — not established as among the ~22 |
| ImageTrend delivered OADS v4.0 dataset March 2025; Middlesex-London Aug 2025; Cochrane District on Elite | `[H]` compliance / `[M]` deployment | "Growing number of services" is vendor language |
| ESO acquired Toronto-based Interdev March 2022; iMedic cloud SaaS with CADLink dispatch | `[H]` | |
| Siren is BC's official provincial ePCR, mandatory, store-and-sync ~5 min | `[H]` | **No Ontario Siren deployment evidenced** |
| ZOLL emsCharts NOW: offline create + chart lock, encrypted local store, MCI triage colour (v10.0), claimed FHIR | `[M-H]` | FHIR claim rests on a third-party profile, not ZOLL primary docs |
| Traumasoft: US private-EMS ops platform (CAD+ePCR+billing+fleet), founded 2006, ~200 customers, NEMSIS | `[H]` | **No Canadian footprint evidenced**; a Capterra `.ca` listing is not a deployment |
| Stryker is **not** an ePCR vendor — HealthEMS went to Sansio/Volaris | `[H]` | Best-sourced item in their survey: dated primary transactions |
| Records custody after cloud-ePCR shutdown is undocumented | `[H]` as an open question | Their sharpest unanswered question; inherited by any transport product |

### From the EMSS codebase (read-only inspection)

| Fact | Rating |
| --- | --- |
| ~45,500 LOC, 195 TS/TSX files, 73 docs, 61 remote branches, HEAD `a8eb1d9` | `[H]` — counted directly |
| `core/src/ehr/ontario.ts` implements PCR `Patient/$match`, OHIP identifier systems, ATNA AuditEvent | `[H]` — read directly |
| `packages/ehr-gateway` carries ONE ID auth, Ontario Health gateway, mock gateway | `[H]` — file listing |
| `core/src/sync/oplog.ts` is Lamport-clocked, total-order, per-path/per-item resolution, not LWW | `[H]` — read directly |
| `packages/sync-service` is multi-tenant with OIDC, tenant store, retention, audit stores, Postgres + SQLite | `[H]` — file listing |
| **No CAD, AVL, crew scheduling, or allocation engine exists** | `[H]` — absence confirmed across `src/` and `packages/` |
| Repository licence is proprietary, all rights reserved | `[H]` |

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

**Inherited from the EMSS survey's open questions, relevant here:**

15. **Confirm the OADS exemption in writing.** This survey's most valuable
    regulatory claim — that non-urgent patient transfer is outside the Ambulance
    Act and therefore outside OADS — is an inference from two separately sourced
    facts, not a statement anyone has confirmed. **Get a legal opinion before it
    becomes load-bearing in a pitch or a funding application.**
16. Whether the Prehos platform actually went dark on 7 July 2026, and where the
    other ~20 services went. Routes that would answer it: municipal/DSSAB council
    agendas June–September 2026, the Ontario Association of Paramedic Chiefs, or
    an FOI to the Ministry of Health. **None is a web search.**
17. Ontario's provincial eACR data flow under OADS v4.0, and Ornge's own
    documentation system — both still uncovered by either survey.
