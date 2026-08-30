# EMSS (AidPost) Reuse Assessment

**Read-only review of `akromi/emergency-medical-support-system` at `a8eb1d9`
(2026-08-23), conducted August 2026.** Nothing in that repository was modified.

This document replaces the speculative §10 of the Phase 0 survey, which was
written before the codebase was available and assumed EMSS meant a dispatch/CAD
system. **That assumption was wrong.**

---

## 1. What AidPost actually is

An **offline-first Progressive Web App for casualty care and transport
documentation**. Field responders capture patient identity, injuries on an
anatomical 2-D body chart, vitals and treatments, then sign off and hand over to
a hospital as an HL7 FHIR R4 bundle. Fully usable with zero connectivity.
Multilingual EN/FR/AR/FA/ES including right-to-left.

| | |
| --- | --- |
| Scale | 195 TS/TSX files · ~45,500 LOC · 73 docs · 61 remote branches |
| Client | React + TypeScript + Vite PWA · IndexedDB via Dexie · Workbox service worker |
| Packages | `@triage-link/core` (3,163 LOC, framework-free) · `ehr-gateway` · `sync-service` |
| Backend | **Optional and default-off** — org-server (Postgres) or field-kit (Pi/SQLite) |
| Licence | Proprietary, all rights reserved (moved from MIT) |
| Status | Explicitly a prototype; not a medical device; not for clinical use |

**It is not a dispatch system.** There is no CAD, no AVL or vehicle telematics,
no crew scheduling, no response-time or coverage modelling, no resource
allocation engine. The Phase 0 survey listed all of those as assets that would
carry over. None of them exist.

---

## 2. What genuinely carries over

Ranked by how much work it saves a patient transportation product.

### 2.1 Ontario Health EHR integration — the highest-value asset

`packages/core/src/ehr/` is a provider-agnostic gateway port with a working
**Ontario Health adapter**:

- `ehr/port.ts` — the `EhrGateway` seam. Framework-free by design: no fetch, no
  Fastify, no secrets. Carries `PatientIdentity` (OHIP health card number and
  version code), `PatientMatch` with normalised confidence scoring, and a typed
  `EhrError` taxonomy (`unauthorized`, `forbidden`, `invalid-request`,
  `rate-limited`, `unavailable`, `transport`) so callers branch without
  string-matching.
- `ehr/ontario.ts` — **Provincial Client Registry `Patient/$match`** request
  construction, Ontario canonical identifier systems
  (`fhir.infoway-inforoute.ca/NamingSystem/ca-on-patient-hcn` and its version
  code), FHIR match-grade → 0..1 score mapping, and **ATNA AuditEvent for every
  access**. Written against the PCR FHIR Implementation Guide and the ONE Access
  Gateway Transport Specification.
- `packages/ehr-gateway/` — the transport half: `one-id.ts` (ONE ID auth),
  `ontario-health-gateway.ts`, `http.ts`, and a `mock-gateway.ts` for dev.

The Phase 0 survey's recommendation was "build FHIR-native from day one, against
the Provincial Client and Provider registries." **That work is already done and
is the single strongest reason to build on this codebase rather than beside it.**

### 2.2 Conflict-aware sync

`packages/core/src/sync/oplog.ts` — a deterministic, framework-free op-log
engine, explicitly **not** last-write-wins:

- Every change is an append-only `Op` carrying a Lamport clock.
- State is the fold of all ops in a total canonical order (lamport → clientId →
  op id), so any two replicas holding the same ops compute **byte-identical
  state regardless of arrival order**.
- Scalars resolve per-path, collections per-item-id — edits to different fields
  or different items never clobber each other. Genuine same-target conflicts
  pick a deterministic winner and emit a `ConflictReport` for the audit trail;
  the losing op is retained.

For a transport product this is directly reusable for driver/vehicle devices
that go offline in rural and Northern Ontario and reconcile later — a real
problem the US NEMT platforms handle poorly.

### 2.3 Multi-tenant backend

`packages/sync-service/` is a genuine multi-tenant service, not a stub:
`tenant-context.ts`, `tenant-store.ts`, `oidc.ts`, `auth-config.ts`,
`ops-store.ts`, `blob-store.ts`, `retention.ts`, `admin-audit-store.ts`,
`ehr-audit-store.ts`, `metrics.ts`, `export-openapi.ts`, with both Postgres and
SQLite backends. Deployable as org-server or air-gapped field kit.

### 2.4 PHIPA-relevant security primitives

At-rest encryption vault (AES-256-GCM), encrypted backups, operator roster with
RBAC-lite, step-up PIN, **tamper-evident audit log**, and a minimum-necessary
view that masks identities and photos behind a timed, audited break-glass.
Photo erasure propagates across devices and server.

The Phase 0 survey named PHIPA agent design as one of two decisions determining
whether the product can sit inside a hospital workflow. Much of the control
surface that argument needs already exists.

### 2.5 Domain and interop scaffolding

`domain/` (types, clinical, handover, elapsed, id, regions, sitrep),
`fhir/mapping.ts` and `fhir/types.ts` (Patient + Encounter + Provenance bundle),
`fixtures/personas.ts`. Plus in-house i18n with full RTL, loadable JSON language
packs requiring no code release, on-device barcode and AAMVA driver's-licence
scanning, and a self-identifying build chip.

### 2.6 The PWA-on-existing-hardware thesis

Worth carrying for a non-architectural reason. When Prehos collapsed, Sault Ste.
Marie's replacement stack would not run on the iPads it already owned, forcing a
laptop purchase (§3). A PWA installs on devices a service already has. That is a
procurement argument, not an engineering one, and it survives into transport.

---

## 3. What does not carry over — including the thesis

### 3.1 Absent capabilities

Dispatch/CAD, assignment and allocation logic, AVL and telematics, ETA
prediction, route optimisation, crew scheduling, fleet management, billing,
multi-payer settlement, eligibility determination, booking workflows, a provider
marketplace, and any patient- or family-facing surface. A patient transportation
system is mostly these things. **The majority of the product is new work.**

### 3.2 The architectural differentiator does not transfer

This is the finding that matters most, and it is uncomfortable.

AidPost's commercial thesis — sharpened deliberately across four survey passes —
is **"no backend, no sync server, no vendor relationship."** Its own fourth pass
concluded that "works offline" is near table stakes (Siren, ZOLL emsCharts NOW
and AmbuPad all do offline capture) and that the real differentiator is the
*absence* of a server, an account and a vendor.

**Transport coordination cannot be built that way.** Matching a trip request to a
provider, settling across payers, and holding a shared view of fleet state are
inherently multi-party and networked. A booking exchange requires a server by
definition. The product recommended in the Phase 0 survey is a coordination and
settlement layer — precisely the shape AidPost defines itself against.

What transfers is the **engine**: the domain core, the Ontario FHIR adapter, the
sync layer, the security primitives, the i18n. What does not transfer is the
**positioning**. Reusing the code is sound; reusing the pitch is not.

---

## 4. Strategic tension worth surfacing to the team

AidPost's `commercialization-index.md` scores four beachheads and rates
**Official EMS (provincial/municipal)** at ★ differentiation fit, ★
accessibility, heavy regulatory load, 12–24+ month revenue horizon — "the
biggest prize but a fortress." It recommends Path A: humanitarian / NGO /
disaster, documentation-tool intended use, revenue in months.

**Is an Ontario patient transportation product a return to the fortress?**

Mostly no, and for a specific reason: **non-urgent patient transfer sits outside
the Ambulance Act, and therefore outside OADS** (§5 of the survey). OADS v4.0 —
mandatory since 2 September 2025 under O. Reg. 257/00 — is identified in
AidPost's own survey as "the single biggest barrier to official Canadian
adoption." A transport product that never touches the 911 land-ambulance record
does not have to cross it.

So the transport lane is a **third path**, distinct from both:

| | Humanitarian (Path A) | Official EMS (Path C) | Patient transportation |
| --- | --- | --- | --- |
| OADS compliance | not applicable | **mandatory — the moat** | **not applicable** |
| Intended use | documentation tool | SaMD | logistics + documentation |
| Regulatory load | light | heavy | light–medium (PHIPA, AODA) |
| Buyer | NGOs, event medicine | paramedic services | renal programs, hospitals, NIHB |
| Revenue horizon | months | 12–24+ months | 6–18 months |

**Three honest caveats:**

1. **The exemption is conditional.** Product surface S1 (acuity triage and
   right-sizing) decides whether a patient needs a 911 ambulance. The closer that
   gets to diverting emergency resources, the closer it moves to the regulated
   boundary — and to a clinical-decision claim that the documentation-tool
   intended use depends on the product *not* making. AidPost's own §11.5 records
   getting exactly this wrong in a draft: it described its triage board as
   "deriving" a category when the board only displays clinician-selected ones.
   The same trap applies here, with more money attached.
2. **It is still Ontario health-system selling.** Lighter than paramedic-service
   RFPs, but not the months-to-revenue humanitarian path. Hospitals and Ontario
   Health are broader-public-sector buyers with procurement directives.
3. **It is a second front.** The same small team cannot run Path A and a
   transport product at full speed. That is a resourcing decision, not a research
   finding.

---

## 5. Recommendation on reuse

**Build on `@triage-link/core`, not on AidPost.**

Extract the framework-free core — domain types, FHIR mapping, the Ontario EHR
gateway port and adapter, the op-log sync engine — as the shared foundation, and
build the transport product as a separate application against it. The core is
already written to support exactly this: its own header says it exists "so they
can be reused by a future React Native client or the backend sync service
without change."

That gives the transport product a working Ontario PCR integration, ONE ID auth,
conflict-free sync and an audit posture on day one, without inheriting a
no-backend architecture that its business model contradicts.

**Licence note:** the repository is now proprietary, all rights reserved, and its
own commercialization doc flags open-core/dual-licensing as an unmade decision.
Sharing a core package across two products makes that decision more urgent, not
less. Settle it before the dependency exists.
