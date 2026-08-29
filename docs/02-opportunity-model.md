# Opportunity Model — Bottom-Up Sizing

**Every assumption in this document is stated explicitly so it can be attacked.**
Where an input is weak, it is marked. Nothing here should enter a business case
until the verification list in [`03-source-register.md`](03-source-register.md)
is cleared.

---

## 0. Why bottom-up

Third-party NEMT market reports disagree with each other by nearly 50% on the
same year — 2026 global NEMT variously put at USD 12.36B, 12.77B and 18.19B,
with CAGRs from 5.52% to 8.23%. That spread means the category definition is
unstable, so those numbers are useful only as a sanity ceiling, never as a
foundation. North America is credited with ~40.8% of 2025 revenue.

Ontario is ~39% of Canada's population and Canada is ~10% of North American
health spend, so a naive top-down slice would put Ontario NEMT somewhere near
USD 250–450M. That happens to bracket the bottom-up answer below, which is mild
reassurance and nothing more.

---

## 1. Anchor inputs

| Input | Value | Confidence | Source |
| --- | --- | --- | --- |
| Ontario inter-facility transfers/yr | ~400,000 | `[H]` for 2009 | ICES / *Healthcare Policy* 2009 |
| Annual cost of those transfers | ~$283M | `[H]` for 2009 | same |
| Share routine / non-urgent | 80% | `[H]` for 2009 | same |
| Median trip distance | 10.5 km | `[H]` for 2009 | same |
| Dialysis / MD appointment / return-home share | 24.3% (85,000 patients) | `[H]` for 2009 | same |
| Ontario population 2009 → 2025 | ~13.1M → ~16.4M (×1.25) | `[H]` | StatCan / Ontario projections |
| Ontario 65+ 2009 → 2025 | ~1.8M → 3.1M (×1.72) | `[H]` | Ontario population projections |
| Ontarians on dialysis | >11,000 | `[H]` | Ontario Renal Network |
| In-centre HD share (national) | 77.7% | `[H]` | CIHI CORR |
| Provincial land ambulance grant 2025 | ~$1B (= 50% of cost) | `[H]` | MOH / LASG announcements |
| NIHB medical transport, Ontario 23–24 | $166.0M | `[H]` | ISC NIHB Annual Report |
| Wheel-Trans trips 2024 | 3.54M | `[H]` | TTC |
| US NEMT SaaS pricing | $50–$200+/vehicle/mo | `[H]` | vendor pricing surveys |

---

## 2. Scaling the 2009 baseline to 2026

The core anchor is 17 years old. It must be aged, and the aging method must be
defensible.

**Volume.** Inter-facility transfer demand tracks the 65+ cohort more closely
than total population. Bounds:

```
  Lower bound  = 400,000 × 1.25 (total population)   = 500,000 transfers/yr
  Upper bound  = 400,000 × 1.72 (65+ cohort)         = 688,000 transfers/yr
  Working mid  = 400,000 × 1.45 (blended)            = 580,000 transfers/yr
```

**Spend.** Volume growth × price inflation. Canadian CPI 2009→2025 ≈ ×1.42;
labour-intensive transport has run ahead of headline CPI, so treat 1.42 as
conservative.

```
  Lower  = $283M × 1.25 × 1.42  = $502M/yr
  Upper  = $283M × 1.72 × 1.42  = $691M/yr
  Working mid                    ≈ $580M/yr
```

> **⚠️ Confidence: MEDIUM.** Two independent risks. (a) Some non-urgent volume
> has already migrated from 911 ambulances to cheaper private PTS, which would
> *lower* total spend while *raising* transfer counts. (b) The 2009 study's cost
> basis may be ambulance-loaded and not representative of today's mix. **A
> refreshed ICES-equivalent analysis is the single highest-value piece of
> primary research this venture could commission.**

---

## 3. Segment sizing

### S-A · Non-urgent inter-facility & discharge transfers

```
  Transfers/yr (working)                    580,000
  × non-urgent share                            80%
  = non-urgent transfers                    464,000/yr

  Already off 911 onto private PTS (est. 50%)   ~232,000 trips/yr
  × blended price $150–$500/trip
  = private PTS revenue pool          $35M – $116M/yr
```

**Directly contestable operator revenue: ~$35M–$116M/yr.** `[L]` — the 50%
migration figure and the price band are both estimates, not measurements.

### S-B · Recurring dialysis transport (the recommended wedge)

```
  Ontarians on dialysis                      11,000
  × in-centre share                           77.7%
  = in-centre HD patients                    ~8,500

  × 3 sessions/week × 52 weeks
  = round trips                          1,326,000/yr   (2.65M one-way legs)

  × share needing assisted/paid transport (30–50%)
  = paid round trips                    398k – 663k/yr
  × $30–$120 per round trip
  = spend pool                          $12M – $80M/yr
```

**Why this is the wedge despite not being the biggest pool:** 1.33M round trips
is *more annual trip volume than the entire inter-facility transfer market*, and
every one of them is known in advance. Pooling and route optimisation have more
to bite on here than anywhere else in Ontario health transport.

### S-C · Specialized / paratransit

Wheel-Trans alone: 3.54M trips in 2024 (+541k over 2023), 42,000+ registrants,
~9,700 daily riders. Toronto is ~19% of Ontario's population; if specialized
transit scales even sub-linearly outside Toronto, province-wide paratransit is
plausibly **6–9M trips/yr** `[L]`. Medical trips are a large share.

Municipally funded and politically protected. **Treat as integration surface and
latent capacity, not as revenue.**

### S-D · Indigenous & Northern travel

```
  NIHB medical transportation, Ontario
    2021–22   $114.8M
    2022–23   $140.3M   (+22.2%)
    2023–24   $166.0M   (+18.3%)
  → ~20% CAGR, second-highest province in Canada

  NHTG: ~66,000 users (22–23); ~200,000 reimbursements processed (23–24);
        $45M/3yr expansion; $0.41/km; $175/night to $1,150 cap
```

**The most attractive payer structure in the entire Ontario market**: a single
federal payer, already contracting, growing ~20% a year, with an explicit
mandate. `[H]`

### S-E · The 911 value pool (indirect — the savings story, not revenue)

```
  Provincial land ambulance grant 2025      ~$1B  (= 50% cost share)
  → total Ontario land ambulance spend      ~$2B/yr

  Offload hours lost:  Toronto ~300,000/yr · Ottawa 93,686/yr
```

Not addressable revenue. **It is the number that justifies the price of
everything else.** A percentage point of $2B is $20M/yr — which is how a
$500k/yr contract gets signed by a paramedic service or a hospital.

---

## 4. The SaaS trap

The obvious business — sell dispatch software per vehicle — sized honestly:

```
  PTS vehicles      580,000 non-urgent trips ÷ (5 trips/veh/day × 250 days)
                    ≈ 460 vehicles
  Land ambulances   ~1,500 (est.)
  Paratransit + community fleets ~1,000–3,000 (est., incl. contracted taxi)
  ─────────────────────────────────────────────────────────────────────
  Total addressable fleet          ~3,000 – 5,000 vehicles

  × $100/vehicle/month × 12
  = $3.6M – $6.0M ARR at 100% penetration
```

**At 100% of every eligible vehicle in Ontario.** Realistic 20–30% penetration
against entrenched incumbents: **$0.7M–$1.8M ARR.** `[M]`

That is the whole prize for the obvious product. It does not support a venture,
and it does not justify the clinical and regulatory work this domain demands.

---

## 5. Where the money actually is

| Model | Basis | Ontario ceiling | Note |
| --- | --- | --- | --- |
| Per-vehicle SaaS | $100/veh/mo | **$4–6M** | The trap |
| Per-trip transaction | 3–8% of $500M+ services spend | **$15–45M** | Requires being in the flow of funds |
| Outcome / savings share | % of ALC days + ambulance hours + missed sessions avoided | **$20–60M** | Hardest to sell, highest ceiling, best moat |
| Payer utility contract | NIHB/NHTG administration + optimisation | **$5–20M** | Single buyer, slow, very sticky |

**Conclusion: price against avoided cost, never against seats.** Every viable
model in this market requires sitting in either the *allocation decision* or the
*flow of funds*. A product that sits in neither is a $4M business.

---

## 6. What would change these conclusions

Ranked by how much each would move the answer:

1. **A refreshed inter-facility transfer study.** The entire S-A estimate rests
   on a 2009 paper. Commission or find this first.
2. **Actual PTS price data.** The $150–$500/trip band is inferred. A dozen
   quotes from Ontario operators would tighten S-A by more than any other input.
3. **Ontario Renal Network transport data.** How many dialysis patients actually
   use assisted transport? The 30–50% band is the weakest assumption in the
   recommended wedge — and it is the wedge.
4. **How much non-urgent volume already left 911.** Determines whether S-A is a
   growth market or a displacement fight.
5. **NIHB Ontario contracting structure.** Whether $166M is contestable by a
   platform or locked in regional arrangements.
