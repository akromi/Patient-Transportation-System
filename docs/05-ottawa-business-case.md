# Business Case — Patient Transportation Service, Ottawa

**A case for *operating* a non-urgent patient transportation service in Ottawa.**
Prepared August 2026. Companion to the Phase 0 survey; read §7 of
[`01-market-survey.md`](01-market-survey.md) first.

> **⚠️ This contradicts the survey's own recommendation, deliberately.**
> [`01-market-survey.md`](01-market-survey.md) §12 concludes that the value in
> Ontario is in a coordination and settlement layer, and that running vehicles is
> a low-margin, labour-constrained business. This document was requested and is
> delivered in full — but §9 states plainly where the two conflict and what would
> have to be true for the operator path to win. The conflict is not resolved by
> hand-waving; it turns on one contract.

> **Figures are modelled, not quoted.** Cost inputs come from published market
> rates and wage surveys, not from vendor quotes or a broker. Every input is
> listed in §8 with its source and what would firm it up. **Do not take this to a
> lender or an investor without replacing §8's estimates with real quotes.**

---

## 1. The proposition in one paragraph

Ottawa has the most concentrated block of recurring, schedulable medical
transport demand in Ontario — **900+ dialysis patients across 10 sites under a
single hospital program** — inside a market where the ambulance-availability
crisis that dominates provincial discussion has already been largely solved, so
the competitive conversation is about service and cost rather than emergency. A
bilingual operator anchored on that recurring book, expanding into hospital
discharge, can reach roughly **$1.95M revenue and ~$242K EBITDA by year three on
13 vehicles**, requiring about **$850K of funding**. Whether that is a good
business depends almost entirely on one question, answered in §9.

---

## 2. Why Ottawa rather than Toronto

Set out in survey §7–§8. In short:

| | Ottawa | Toronto |
| --- | --- | --- |
| Dialysis anchor | **900+ patients, one program** | Larger but split across corporations |
| Competitive density | Moderate | Highest in Ontario, **plus Uber Health** |
| Offload crisis | Largely resolved | Severe — but that helps a *platform*, not an operator |
| Language | **Bilingual required** (FLSA, Montfort) | Multilingual, not statutorily bound |

The operator-relevant point is the **anchor tenant**. A transport business lives
or dies on vehicle utilisation, and utilisation comes from recurring contracted
volume, not ad-hoc calls. Ottawa has a single buyer holding ~109,000 round trips
a year. Toronto does not.

---

## 3. Service model

**Phase in, do not launch broad.**

| Tier | Vehicle | Crew | Target work |
| --- | --- | --- | --- |
| **1 — Wheelchair (core)** | WAV, rear-entry ramp, 2–3 securement positions | 1 trained operator | Dialysis runs, clinic appointments, LTC transfers |
| **2 — Stretcher** | Stretcher-equipped van, oxygen, stair chair | 2 attendants | Hospital discharge, inter-facility, bed-to-bed |
| **3 — Ambulatory** | Sedan/minivan | 1 driver | Overflow, escorted ambulatory — **contested by Uber Health; enter last or not at all** |

**Design decision: pool the dialysis runs.** In-centre haemodialysis patients
arrive and leave in shift blocks at fixed times to fixed addresses. Carrying 2–3
wheelchair patients per run is the single largest lever on unit economics in this
document — it is what moves a vehicle from ~5 billable legs a day to ~8.

> ⚠️ **The three-year projection in §6 models a wheelchair-only fleet.** Tier 2
> stretcher vehicles need **two** attendants, so their labour cost is roughly
> double a wheelchair van's — and an earlier draft priced all 13 vehicles at the
> single-operator rate, which would have overstated year-three EBITDA by more
> than its entire value. Stretcher economics are modelled separately in §4.3 and
> are **not** included in the projection. Adding stretcher capability is a
> deliberate later decision, not an assumed part of the plan.

**Bilingual capability from day one — but understand *why*.** Ottawa is a
designated area under the French Language Services Act, and Montfort is the
province's francophone teaching hospital. **The Act binds government and
designated public-service agencies, not a private transport operator directly.**
An operator's French obligation flows through its *contract* with a designated
entity.

The practical conclusion is unchanged and the reasoning is now correct: if you
want Montfort or TOH business, **expect French capability to be a contract
requirement**, and price crew rotations accordingly. It is contractually
near-certain, not statutorily automatic — and the scope of health-transport
designation is still unconfirmed in the source register. Do not build a labour
plan around it as a legal absolute before that scope is established.

---

## 4. Unit economics — one wheelchair vehicle

### Revenue

Market rates observed in the GTA `[M]`: ~$150 for a ~20 km wheelchair trip;
long-distance modelled near $299 base + $2.95/km; wait time $60/hr for wheelchair,
$170/hr for stretcher; add-ons for same-day ($95), after-hours ($75), weekend
($65), oxygen ($30), stairs ($45–140).

Contract rates run below rack rate. **The base case is dialysis-anchored and
prices every leg at the contract rate** — ad-hoc work at rack rate is upside, not
assumed:

```
  Contracted dialysis leg (pooled)             $85
  Pooled legs per vehicle per day                8
  Operating days                          260/year
  Mature utilisation                           85%

  8 × 260 × 0.85 × $85       =  $150,280/year  ≈ $150,000
```

**Upside not in the base case:** ad-hoc discharge and clinic work bills ~$150 a
trip. A vehicle running 5 ad-hoc trips a day at that rate earns ~$165,750 —
about 10% more — but that work is unscheduled, unpoolable and unpredictable, so
it is left out of the plan rather than blended in.

> ⚠️ **An earlier draft quoted a "$120 blended rate" alongside this $150,000
> figure. The two were inconsistent** — a $120 blended rate across 8 legs a day
> gives $212,160, not $150,000 — and the mix was therefore unauditable. The
> blended rate has been removed; the base case now prices one way.

### Direct cost per vehicle per year

| Item | Modelled | Basis |
| --- | --- | --- |
| Operator wage + burden | **$61,200** | $21/hr `[M]` + ~22% burden, plus 15% relief coverage |
| Vehicle (lease) | **$19,200** | ~$1,600/mo; purchase alternative in §5 |
| Fuel | **$8,680** | 40,000 km @ 14 L/100km @ $1.55/L |
| Insurance | **$5,500** | Ontario commercial auto $1,500–3,000 `[M]`; medical passenger carries a premium — **broker quote required** |
| Maintenance and tires | **$6,000** | Modelled |
| Licensing, permits, misc. | **$1,500** | Modelled |
| **Total direct** | **$102,163** | |

```
  Contribution per vehicle at maturity   $150,000 − $102,163 = $47,837
  Gross margin                                                  ~32%
```

> **The critical structural fact:** the operator's wage is paid whether the van is
> full or empty. Direct cost is ~90% fixed per vehicle. **Utilisation is the
> entire business.** A van at 55% utilisation loses money; the same van at 85%
> makes $48K.

### 4.3 Stretcher tier — a different business, modelled separately

Not in the §6 projection. Shown so the difference is explicit rather than
implied.

| Item | Wheelchair van | Stretcher van |
| --- | ---: | ---: |
| Crew | 1 operator | **2 attendants** |
| Trips per day | 8 pooled legs | 4 (stretchers cannot be pooled) |
| Rate | $85/leg contract | ~$350/trip |
| **Revenue** | **$150,280** | **$309,400** |
| Crew cost | $61,200 | **$122,400** |
| Lease | $19,200 | $25,200 |
| Fuel · maintenance · insurance · licensing | $21,680 | $26,180 |
| **Total direct** | **$102,163** | **$173,946** |
| **Contribution** | **$48,117** | **$135,454** |

**A stretcher vehicle contributes ~2.8× a wheelchair van despite double the
labour**, because it bills roughly 2× the revenue and cannot be undercut by
rideshare. The catch is on the demand side: stretcher work is hospital-discharge
driven, which is **ad-hoc and unschedulable** — precisely the utilisation risk
§3 exists to avoid. It is a strong second phase and a poor first one.

*(All stretcher figures are modelled at `[L]` confidence; the $350 trip rate is
inferred from the observed "$500+ with paramedic support" ceiling and the
wheelchair rack rate, not quoted.)*

---

## 5. Fixed overhead and break-even

| Item | Annual |
| --- | --- |
| Owner / general manager | $110,000 |
| Dispatch & operations (1.5 FTE) | $97,500 |
| Facility, parking, yard | $36,000 |
| Dispatch/scheduling software | $12,000 |
| Bookkeeping, legal, accounting | $25,000 |
| General liability & E&O insurance | $12,000 |
| Marketing & business development | $20,000 |
| Contingency | $25,000 |
| **Total** | **$337,500** |

```
  Break-even fleet = $337,500 ÷ $47,837 = 7.1 vehicles at mature utilisation
```

**And that figure is fragile.** At 72% utilisation, contribution falls to
~$26,200 per vehicle and break-even moves to **12.9 vehicles** — nearly double.
The sensitivity is not linear because direct cost barely moves with utilisation.

**This is the number that should govern the decision.** It is not a
two-van side business. Seven vehicles running near 85% utilisation is the floor,
which means the contracted volume has to exist *before* the fleet does.

**Lease rather than buy.** Purchase is ~$95,000 per converted WAV (vehicle plus
$20,000–30,000 conversion `[M]`), depreciating to ~$13,570/year against
$19,200 to lease. Buying is ~$5,600/vehicle/year cheaper and costs $1.2M of
capital across the plan. In a business whose binding risk is filling vehicles
rather than owning them, **leasing converts capital risk into a cancellable
operating cost.** Revisit once utilisation is proven.

---

## 6. Three-year projection

| | Year 1 | Year 2 | Year 3 |
| --- | ---: | ---: | ---: |
| Vehicles (avg) | 5 | 9 | 13 |
| Average utilisation | 55% | 72% | 85% |
| Revenue per vehicle | $97,059 | $127,059 | $150,000 |
| **Revenue** | **$485,000** | **$1,143,500** | **$1,950,000** |
| Direct costs | $495,000 | $908,000 | $1,328,000 |
| Contribution | −$10,000 | $235,500 | $622,000 |
| Fixed overhead | $290,000 | $337,500 | $380,000 |
| **EBITDA** | **−$300,000** | **−$102,000** | **+$242,000** |

*(Direct costs in years 1–2 are fuel-adjusted downward for lower kilometres; the
rest of the per-vehicle cost does not scale with utilisation.)*

**Year 1 contribution is negative.** Five vehicles at 55% utilisation do not
cover their own operators, before a dollar of overhead. That is the shape of this
business, not a modelling artefact — and it is why §9's gate matters.

Profitability arrives in **year 3**, not year 2: nine vehicles at 72%
utilisation is still short, because break-even at that utilisation is ~13
vehicles (§5).

### Funding requirement

| Item | Amount |
| --- | ---: |
| Cumulative operating losses (Y1–Y2) | $402,000 |
| Medical equipment — stretchers, stair chairs, oxygen, AEDs | $40,000 |
| Software setup and first year | $20,000 |
| Incorporation, legal, licensing, insurance deposits | $35,000 |
| Working capital — hospital AR at 60–90 days | $180,000 |
| Contingency (15%) | $101,500 |
| **Total** | **≈ $778,500** |

**Call it $850,000** to carry a variance without a second raise.

---

## 7. What has to be true

Ranked by how much each threatens the plan.

1. **Utilisation reaches 85%.** At 70% the mature fleet contributes ~$25K/vehicle
   and break-even moves from 7 to 13 vehicles. The plan does not survive
   sustained low utilisation.
2. **Crews can be recruited and kept.** Thirteen vehicles needs ~16 operators at
   ~$21/hr in a tight Ottawa labour market. **Labour, not capital or demand, is
   the binding operational constraint.** Turnover directly destroys utilisation.
3. **Contracted volume precedes fleet growth.** Every vehicle added ahead of
   committed volume costs ~$102K/year regardless of whether it moves.
4. **Receivables get collected.** Hospital and LTC contracts pay slowly; patient
   pay is fast but small. The $180K working-capital line is not padding.
5. **Transdev/Voyago does not price to defend.** A global operator can run Ottawa
   below cost far longer than a startup can. This is a real and unhedgeable risk.

---

## 8. Input register — replace before external use

| Input | Value used | Confidence | To firm it up |
| --- | --- | --- | --- |
| Wheelchair trip rate ~20 km | $150 | `[M]` published GTA market rate | Quote 10–15 Ottawa operators |
| Contract dialysis leg | $85 | `[L]` **modelled** | Only a real contract settles this |
| Operator wage | $21/hr | `[M]` Ontario patient-transfer survey | Local postings; note Ontario minimum wage is the floor |
| WAV purchase + conversion | ~$95,000 | `[M]` conversion $20–30K over vehicle | Dealer quotes |
| Lease rate | $1,600/mo | `[L]` **modelled** | Lessor quotes |
| Commercial insurance | $5,500/veh/yr | `[L]` base commercial auto $1,500–3,000 `[M]` | **Broker quote — likeliest input to be badly wrong** |
| Trips per vehicle per day | 5 ad-hoc / 8 pooled | `[L]` **modelled** | Ride-along or pilot |
| Utilisation ramp | 55 / 72 / 85% | `[L]` **modelled** | Pilot |
| Dialysis population | 900+ across 10 sites | `[M]` TOH nephrology program | Confirm in-centre split with TOH |

**Six of nine load-bearing inputs are modelled, not sourced.** The projection is a
structure for thinking, not a forecast.

---

## 9. The honest assessment

### The arithmetic problem

Survey §9 sizes the *entire contestable private patient-transfer market in
Ontario* at **CAD $35–116M/year**. Ottawa is ~6.7% of Ontario's population,
implying an Ottawa private-PTS pool of roughly **$2.3M–$7.8M**.

A mature 13-vehicle operation at **$1.95M revenue would hold 25%–83% of that
pool** — against Transdev/Voyago, who own the incumbent (Priority Patient
Transfer, with the goPatient portal already installed at contract hospitals), and
Ontario Patient Transfer, who run an Ottawa super base.

**That share is not winnable by a new entrant competing for the same trips.**

### Which means the business is not what it looks like

The plan only works if it is **not** a fight for existing private-PTS volume. The
TOH dialysis book — ~109,000 round trips a year — is largely **not in that pool
today.** Those patients get there by family car, Para Transpo, taxi, or they
don't get there at all: recall that 10% of dialysis patients miss at least one
session a month, with transportation a contributing cause (survey §3).

So the real proposition is **converting unserved and self-served dialysis travel
into contracted service**, not taking share. Capture 25% of that book — 27,250
round trips, 54,500 legs at $85 — and that is **$4.6M of revenue from one
contract**, more than the entire three-year plan above.

### The go/no-go gate

> **Do not spend $850,000 until you have a signed contract, a funded pilot, or a
> written expression of interest from The Ottawa Hospital's Regional Nephrology
> Program.**

Everything else in this document is secondary to that one relationship. With it,
the fleet fills from day one, utilisation risk mostly disappears, and the
labour-recruitment problem becomes tractable because the schedule is predictable.
Without it, you are a seventh entrant in a $2–8M market against a global
operator, and the answer is no.

**Recommended first step is therefore not fundraising.** It is a single
conversation with the TOH renal program about missed treatments, what
transportation currently costs them in cancelled slots, and whether a contracted
pooled service interests them. That conversation costs nothing and determines
everything.

### Reconciling with the survey

The survey says build a coordination layer, not an operator. Both can be true in
sequence, and the operator path has one advantage the platform path lacks:
**operating the dialysis book generates the scheduling, utilisation and outcome
data that a coordination product needs to be credible**, and it puts you inside
the buyer relationship the platform would otherwise have to cold-sell.

The hybrid — **operate the anchor book, instrument it, then sell the coordination
layer outward from a working reference site** — is more defensible than either
alone. It is also more capital-intensive and slower. That trade is the decision,
and it belongs to whoever is signing.
