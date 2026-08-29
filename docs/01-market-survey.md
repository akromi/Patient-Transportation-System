# Ontario Patient Transportation — Product Space & Market Survey

**Phase 0 discovery · August 2026**

> **Reading note.** Numbers in this document are rated `[H]` high, `[M]` medium,
> `[L]` low confidence. `[M]` and `[L]` figures were reconstructed from
> search-result summaries because direct document retrieval was blocked during
> research. See [`03-source-register.md`](03-source-register.md) before quoting
> any of them externally.

---

## 1. Executive summary

Ontario has a patient transportation *industry*. It does not have a patient
transportation *system*.

Six findings drive everything else in this document:

**1. The core waste is documented and enormous.** The only population-level
study of inter-facility transfers in Ontario found ~400,000 transfers a year —
about 1,000 a day — costing ~$283M, with **80% classified routine and
non-urgent**, yet largely carried by fully-equipped 911 ambulances with
paramedic crews. The single most common trip profile was a 10.5 km ride to a
cardiologist appointment or a dialysis session. `[H, but 2009 vintage]`

**2. There is no payer.** OHIP does not cover non-emergency transport. Emergency
ambulance carries a regulated $45 co-payment; non-urgent stretcher transport is
**unregulated in price and uncovered**, so a discharged patient can be handed a
bill for hundreds of dollars with no exemption available even on social
assistance. Ontario's Patient Ombudsman has flagged this directly. `[H]`

**3. That absence is why the US playbook does not transfer.** American NEMT
software — RouteGenie, Tobi, Bambi, MediRoutes — is built on top of Medicaid
managed-care brokers (ModivCare, MTM, Veyo) that supply trip volume, prior
authorization and a claims rail. **Ontario has no broker layer and no claims
rail.** Importing that architecture builds a product with nothing to plug into.

**4. The buyer is fragmented but each fragment is real.** Hospitals (discharge
and ALC pressure), long-term care operators, Ontario Health atHome and community
support agencies, regional renal programs, municipal paramedic services, and two
substantial single-payer pools: **NIHB medical transportation in Ontario at
$166.0M in 2023–24, growing ~20% a year** `[H]`, and the Northern Health Travel
Grant processing close to 200,000 reimbursements in 2023–24 `[M]`.

**5. Supply is consolidating.** Transdev/Voyago — 600+ medical attendants,
positioned as Canada's largest NEPT brand — has been buying up regional
operators, including Priority Patient Transfer Service in Ottawa. A neutral
coordination layer gets harder to build every year that consolidation runs.

**6. The obvious product is the wrong product.** Per-vehicle dispatch SaaS at
US benchmark pricing ($50–$200/vehicle/month) against Ontario's addressable
fleet yields roughly **$4M–$7M ARR at full penetration** — a decade of work for
a rounding error. The value is not in selling consoles to operators. It is in
owning the allocation decision and the settlement rail that currently do not
exist. See [`02-opportunity-model.md`](02-opportunity-model.md).

---

## 2. How patient transportation actually works in Ontario

Five separate systems serve overlapping demand with essentially no shared
visibility into each other. This is the central structural fact of the market.

### 2.1 The five silos

| # | System | Who runs it | Who pays | Coordination |
| --- | --- | --- | --- | --- |
| 1 | **911 land ambulance** | ~50 municipal/upper-tier paramedic services | Province 50% + municipality 50% | Central Ambulance Communications Centres |
| 2 | **Critical care & air** | Ornge; CritiCall Ontario for placement | Province | Provincial, genuinely coordinated |
| 3 | **Non-urgent patient transfer (PTS)** | ~dozens of private operators | Hospital, LTC home, or the patient | **None** |
| 4 | **Specialized/para transit** | Municipal transit (Wheel-Trans, TransHelp, …) | Municipal + fare | Municipal, siloed by boundary |
| 5 | **Community assisted transportation** | Community support agencies, volunteer drivers | Ontario Health + client co-pay | Agency by agency |

Silos 2 is well run. Silo 1 is well regulated. **Silos 3, 4 and 5 do not know
the others exist**, despite serving the same patient on different days of the
week — and often the same patient on the same day.

### 2.2 The parts that work

- **CritiCall Ontario** operates a provincial Repatriation Tool, available to
  all acute hospitals since 2014, with dashboards and business intelligence. It
  is the closest thing Ontario has to a working transfer coordination system —
  and it is scoped to acute-to-acute repatriation, not the routine 80%.
- **Ornge** performed 23,725 patient transport legs for 19,550 patients in
  2024/25, covering 13M people across a million square kilometres, ~98% of fixed
  wing originating in Northern Ontario. `[H]`

The lesson is not that Ontario cannot coordinate transport. It is that Ontario
already proved it can — for the acute, high-severity, provincially-funded 15%.
The routine 80% was never given the same treatment because no ministry owns it.

### 2.3 The part that does not

Non-urgent patient transfer sits outside the Ambulance Act. Consequences:

- **No licensing, no vehicle standard, no crew standard, no price regulation.**
- Vehicles are described in press coverage as looking like ambulances without
  being ambulances. `[M]`
- Regulation has been asked for repeatedly and never delivered: a coroner has
  called for it since 1995; a 2011 bill died when the legislature dissolved;
  Ontario's Ombudsman has called the paramedic oversight system "complicated,
  overburdened, and wholly inadequate." `[M]`
- The Ministry can only investigate contraventions of the Ambulance Act, so
  conduct governed by local service policy falls into an acknowledged
  enforcement gap. `[M]`

**Strategic read:** an unregulated market is cheap to enter and hard to defend —
but a credible quality, credentialing and audit spine becomes a moat the moment
regulation arrives, and pre-positions the vendor as the reference implementation.
Twenty-five years of failed attempts say do not *bet* on regulation. Build so
that it is upside, not a dependency.

---

## 3. Demand drivers

### 3.1 Demographics — the load is compounding

Ontario had **3.1 million people aged 65+ in 2025, 18.9% of the population**,
heading to 4.6 million (22.7%) by 2051; all baby boomers cross 65 by 2031. `[H]`
The 65+ cohort has grown roughly **1.7×** since the 400,000-transfer study was
published, against ~1.25× total population growth. Transfer demand tracks the
older cohort, not the headcount.

### 3.2 Hospital flow — transport is the last-mile blocker on a bed

- **ALC:** ~17.0% of hospital days in Canada were alternate-level-of-care in
  2022–23, range 6.8%–26.1% by jurisdiction. `[H]` A patient medically ready to
  leave still occupies a bed until a vehicle exists.
- **Offload delay:** Toronto ~300,000 hours a year, Ottawa 93,686 hours. Essex
  declared an emergency after code reds/blacks, with 26 crews delayed at
  hospitals at once and no ambulance available for nearly three hours. `[M]`
- **The loop closes:** non-urgent transfers consume ambulances → fewer
  ambulances for 911 → longer offload queues → less capacity still.

### 3.3 Recurring treatment travel — the highest-value demand in the system

More than **11,000 Ontarians are on dialysis**; nationally ~78% of prevalent
dialysis patients are in-centre haemodialysis. `[H]` In-centre means **three
trips a week, indefinitely** — a patient population unlike any other in health
care in its transport dependency.

The consequences are measured: **10% of dialysis patients miss at least one
session a month and 35% miss one every three months**, with transportation a
contributing cause and missed treatments associated with increased morbidity.
`[M]` Canadian-specific research names travel distance and time, cost, mode, and
service reliability as the recurring themes.

This is the best wedge in the market and §10 argues for it: highest frequency,
fully schedulable, geographically clustered, clinically owned by an identifiable
buyer, with a hard outcome metric already being tracked.

### 3.4 Missed appointments generally

Canadian no-show rates run **10%–25%** depending on setting, with transportation
named by 15.1% of patients in a Quebec study as their reason for missing. `[M]`
Living more than 5 km away measurably reduces attendance.

### 3.5 New demand the province is actively creating

- **57 new community surgical and diagnostic centres** funded at $155M over two
  years — 35 for MRI/CT serving a claimed 800,000+ patients, plus four cataract
  centres, under Bill 60's Integrated Community Health Services Centre
  framework. `[H]` **Every one of these decouples the procedure from the
  hospital and therefore manufactures a trip that did not previously exist.**
- **Community Paramedicine for LTC made permanent** at $89M, having served
  81,000+ people and delivered 310,000+ hours of care since 2020. `[H]` This
  program's explicit purpose is avoiding transport — a partial substitute and a
  possible channel.
- **627 long-term care homes, ~78,000 beds** `[M]`, plus a 23,977-bed
  construction pipeline `[M]`. LTC and retirement homes already account for
  **~10% of all ambulance-transported ED arrivals** nationally. `[H]`

### 3.6 Geography and equity

- **NIHB medical transportation in Ontario: $114.8M (21–22) → $140.3M (22–23) →
  $166.0M (23–24)**, second highest in Canada after Manitoba. `[H]` That is
  ~20% annual growth in a single federally-funded, contract-addressable pool.
- **Northern Health Travel Grant:** ~66,000 users in 2022–23, close to 200,000
  reimbursements processed in 2023–24, $45M over three years in expansion
  funding; as of the 2024 changes, $175/night accommodation to a $1,150 cap and
  **$0.41/km**. `[M]` Patient advocates say the per-kilometre rate does not
  reflect real cost. It is a *reimbursement* program — the patient must be able
  to front the money and file paperwork, which is itself an access barrier and
  an obvious product surface.

---

## 4. Payer map — the hardest problem in this market

```
                    WHO PAYS FOR AN ONTARIO PATIENT TRIP?

  EMERGENCY (911)          ┌─────────────────────────────────────────┐
  ────────────────         │ Province 50% / Municipality 50%         │
  Regulated. ~$2B/yr       │ Patient co-pay $45 (or $240 if deemed   │
  total land ambulance.    │ not medically necessary)                │
                           └─────────────────────────────────────────┘

  NON-URGENT               ┌─────────────────────────────────────────┐
  ────────────────         │ Hospital budget  ·  LTC home budget     │
  UNREGULATED.             │ Patient / family out of pocket          │
  No OHIP coverage.        │ NIHB ($166M ON)  ·  NHTG (reimburse)    │
  No exemptions.           │ WSIB  ·  private insurer  ·  charity    │
  No price ceiling.        │ Ontario Health atHome / CSS + co-pay    │
                           │ Municipal paratransit + fare            │
                           └─────────────────────────────────────────┘
```

Three properties make this the crux of the business model:

1. **"Medically necessary" is undefined** in policy, legislation or regulation —
   it is a physician judgement. Hospitals have told the Patient Ombudsman that
   *needing a stretcher does not by itself establish medical necessity*. `[H]`
   So the most consequential financial decision in the trip has no decision
   support behind it. That is a product.
2. **Nobody sees total cost.** A patient can consume a municipal paratransit
   trip Monday, a hospital-funded PTS transfer Wednesday, and an NIHB-funded
   trip Friday. No system reconciles this.
3. **Eligibility is unclaimed.** NHTG requires the patient to apply after the
   fact. Co-payment exemptions exist but "many people are not aware" of them
   `[H]`. Automated eligibility determination and split settlement is a
   genuinely unbuilt piece of infrastructure.

---

## 5. Regulatory and compliance envelope

| Instrument | Bearing on the product |
| --- | --- |
| **Ambulance Act** | Governs 911 land ambulance and certification. **Does not reach non-urgent PTS.** |
| **PHIPA** | The controlling constraint. A vendor handling PHI *for* a custodian is an **agent** and inherits obligations; operating on its own account puts it under PIPEDA instead. Agent status must be designed for deliberately, not stumbled into. |
| **Bill 60 / Your Health Act 2023** | Creates Integrated Community Health Services Centres — the licensing basis for the 57 new centres generating new trips. |
| **AODA** | Accessibility standards for transportation and for the digital product. Non-negotiable. |
| **Highway Traffic Act / MTO** | Vehicle and driver requirements. |
| **BPS Procurement Directive** | Hospitals and Ontario Health are broader-public-sector buyers: competitive RFP thresholds, long cycles, vendor-of-record regimes. Plan sales motion around this, not against it. |
| **eHealth Ontario / Ontario Health standards** | Ontario has real FHIR R4 implementation guides — Patient Summary, Provincial Client Registry, Provincial Provider Registry, ODHDR, OLIS, eReferral/eConsult, OCRE. **Build FHIR-native from day one.** The Provincial Client and Provider registries in particular are the identity spine. |

**Read:** PHIPA agent design and FHIR-native architecture are not compliance
overhead to be retrofitted — they are the two decisions that determine whether
this product can ever sit inside a hospital's workflow.

---

## 6. Competitive landscape

### 6.1 Operators (supply side)

| Player | Position | Note |
| --- | --- | --- |
| **Voyago / Voyago Health (Transdev)** | The consolidator | 600+ medical attendants incl. AEMCA paramedic graduates; NEPT ~35% of contracts; claims more patients and hospitals than any other Canadian NEPT brand; acquired Priority Patient Transfer (Ottawa); also operates ON/QC/MB |
| **Ontario Patient Transfer** | Incumbent scale | Incorporated 1994, Hamilton HQ; super-bases Hamilton/Toronto/Ottawa plus satellites Mississauga, Oshawa, Peterborough, Kingston, Winchester, Cornwall |
| **RNR Patient Transfer** | Established regional | Hamilton-based, 16+ years, full modality range |
| **Long tail** | Fragmented | Encore, Swift Med Care, Health Lync, Ontime, Med Runner, MD Transfer, York Simcoe, NUPT, Goldsmith and others — mostly single-region, sub-scale |
| **Municipal paramedic services** | Reluctant incumbent | Still carrying much of the non-urgent 80%; politically protected; the party that most wants this problem solved |
| **Community support agencies** | Undercounted capacity | CHATS, Community Care Durham et al. — mixed paid/volunteer drivers, Ontario Health funded. **Real fleet capacity invisible to every other silo.** |

### 6.2 Software (the actual competitive set)

| Category | Players | Threat |
| --- | --- | --- |
| **US NEMT SaaS** | RouteGenie, TobiCloud, Bambi, TripMaster, MediRoutes, NEMT Cloud Dispatch | **Low.** Architecturally coupled to Medicaid brokers — RouteGenie's headline feature is 25+ live broker connections (MTM, ModivCare, Veyo, Alivi, MAS…). None of those rails exist here. Pricing $50–$200+/vehicle/mo. |
| **Hospital transport orchestration** | Ryde Central (hospital↔provider automation, EHR pull, Uber/Lyft dispatch, CAD/EHR integration) | **High — closest analogue to the right product.** US-oriented; no evidence of Ontario presence or PHIPA posture. A fast follower could land here first. |
| **Operator-captive portals** | goPatient (Priority/Transdev), Voyago booking app | **Structural, not technical.** Every consolidator portal that locks a hospital in shrinks the neutral market. This is the clock on the opportunity. |
| **Rideshare healthcare** | Uber Health — live in Ontario (Toronto, Brampton and beyond), rider needs no app, multilingual, 3-year Hope Air partnership from Aug 2024 | **High for ambulatory only.** Cannot do stretcher, bariatric, oxygen, cognitive-impairment escort, or clinical handover. Will take the easy top of the market and leave the hard, high-acuity margin. |
| **Canadian transit tech** | Spare Labs (microtransit/paratransit/NEMT SaaS), Pantonium (Toronto; real-time self-adjusting routing; $2M SDTC), Blaise (Montreal) | **Medium and interesting.** Strong optimisation, municipal channel, Canadian data residency — but transit-agency shaped, not clinically shaped. Partner or compete-adjacent. |

### 6.3 The whitespace, stated plainly

Nobody occupies the intersection of:

> **clinical acuity triage** × **multi-provider neutrality** × **multi-payer
> settlement** × **Ontario regulatory fit**

US SaaS has neutrality and no clinical or payer fit. Uber Health has scale and
no acuity. Operator portals have clinical fit and no neutrality. Transit tech
has optimisation and no clinical model. CritiCall has coordination and no reach
into the routine 80%.

---

## 7. Product space — seven candidate surfaces

Ranked by defensibility × evidence of pain.

**S1 · Acuity triage and right-sizing engine.** Decide, per trip, whether the
patient needs a 911 ambulance, a stretcher van, a wheelchair van, a sedan, a
volunteer driver, or no trip at all. This is where the documented waste lives —
80% routine on ambulance resources — and where "medically necessary" is
currently decided with no decision support. Highest-value, hardest to copy,
carries clinical-safety risk that must be designed for explicitly.

**S2 · Recurring-trip subscription optimiser.** Standing orders for dialysis,
oncology, rehab, wound care; pooling across patients and providers; automatic
re-optimisation on schedule change. Highest-frequency demand, clearest ROI,
strongest lock-in.

**S3 · Neutral booking exchange.** One request, PHIPA-safe, fanned to a
multi-provider market with real acceptance and ETA. Directly contests
operator-captive portals — and is the surface with the shortest window before
consolidation closes it.

**S4 · Discharge-flow integration.** Predict discharge readiness from hospital
signals, pre-book transport, tie vehicle arrival to bed release. Sells against
ALC days, which hospitals already measure and are already judged on.

**S5 · Eligibility and split-settlement rail.** Determine who pays which
fraction — NIHB, NHTG, hospital, LTC, insurer, patient — and settle it.
Unbuilt. The deepest moat and the slowest build.

**S6 · Northern and Indigenous journey coordination.** Multi-leg land+air, NHTG
pre-authorisation instead of after-the-fact reimbursement, Ornge and Hope Air
handoffs. A federal payer growing 20% a year, and the strongest equity case.

**S7 · Quality, credentialing and audit spine.** Crew credentials, vehicle
standards, incident reporting, outcome tracking in a sector with none.
Low near-term revenue; the highest-leverage asset if regulation ever lands.

---

## 8. What carries over from EMSS — and what does not

> ⚠️ **Assumption.** This repository contains no EMSS code and the term is not
> defined anywhere in it. Taken to mean prior work on an emergency medical
> services system. **Confirm before Phase 1 planning.**

| Carries over | Needs rebuilding |
| --- | --- |
| Dispatch/CAD core, assignment logic | Scheduled/recurring demand — NEPT is largely *booked*, not stochastic |
| AVL, telematics, real-time ETA | Multi-tenant provider marketplace, not one agency's fleet |
| Crew scheduling, shift and certification tracking | Multi-payer billing, eligibility, split settlement |
| ePCR and clinical documentation | Patient- and family-facing experience — EMS has no consumer surface |
| Response-time modelling, coverage optimisation | Acuity *down*-triage — EMS triages severity up, NEPT must triage cost down safely |
| Integration discipline with CACC/hospital | FHIR R4 against Ontario provincial registries |
| Operational rigour, audit culture, safety posture | Consent and PHIPA agent model for a non-custodian vendor |

**The honest warning:** an EMS system is optimised for *stochastic, urgent,
single-payer, incident-centred* work. Non-emergency patient transport is
*scheduled, routine, multi-payer, patient-centred*. Reusing the EMS mental model
wholesale is the most likely way this product goes wrong. Reuse the engine;
rewrite the assumptions.

---

## 9. Risks

| Risk | Severity | Response |
| --- | --- | --- |
| No provincial payer → fragmented, slow sales | **High** | Beachhead with a segment that has a single identifiable budget holder |
| Transdev/Voyago consolidation forecloses neutrality | **High** | Move on S3 early, or reposition as payer-side where consolidation does not help them |
| Unregulated market → low willingness to pay for software | **High** | Price against *avoided cost* (ALC days, ambulance hours, missed sessions), never per seat |
| Clinical safety of automated down-triage | **High** | Clinician-in-the-loop by design; conservative defaults; full audit trail; never fully autonomous at launch |
| PHIPA breach | **High** | Agent model, Ontario data residency, IPC-defensible design reviewed before first line of code |
| BPS procurement cycles | Medium | Pilot via OHT/agency discretionary spend; build to vendor-of-record |
| Uber Health takes the ambulatory tier | Medium | Concede it; own stretcher/bariatric/escort/cognitive where they structurally cannot go |
| Municipal paratransit is politically protected | Medium | Integrate, never displace; position as capacity relief |
| Regulation never arrives | Medium | Never make S7 load-bearing |
| Key figures are 2009-vintage | Medium | Verification list in the source register — do this before fundraising |

---

## 10. Recommendation

**Do not build a dispatch platform.** Per-vehicle SaaS in Ontario tops out
around $4M–$7M ARR and puts you in a knife fight with US incumbents who have
better dispatch products and nothing to do with them here.

**Build the allocation and settlement layer that Ontario does not have** —
starting from a single wedge with a real budget holder and a measurable outcome.

**Recommended beachhead: recurring dialysis transport (S2 + S1), sold to
regional renal programs.**

Because it is the only segment where all five conditions hold at once:

1. **Frequency** — 3×/week per patient, forever. ~11,000 dialysis patients,
   ~78% in-centre.
2. **Schedulability** — treatment slots are fixed and known in advance; this is
   the most poolable demand in the entire health system.
3. **An identified buyer** — regional renal programs under Ontario Health, with
   an existing performance-reporting relationship.
4. **A metric already being tracked** — missed treatments (10%/month, 35%/quarter),
   with published morbidity consequences. You can prove value in one quarter.
5. **A natural expansion path** — oncology and rehab share the recurring
   structure; dialysis patients also generate discharge and inter-facility trips,
   which walks you into S4 and S3 through a door you already hold.

Then expand: **S4 discharge flow** (sell ALC days back to hospitals) → **S3
neutral exchange** (before consolidation closes it) → **S6 Northern/Indigenous**
(NIHB's $166M growing 20% a year) → **S5 settlement** as the long-term moat.

**The two open decisions in §10 are not research questions.** Whether to be a
coordination layer, an operator, or a payer-side utility — and which wedge to
fund — are the team's calls. Everything above is the input to them.
