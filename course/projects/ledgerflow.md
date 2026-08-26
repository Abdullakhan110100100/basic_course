# Project 1 — LedgerFlow (Payments & Double-Entry Ledger Platform)

**Purpose:** demonstrate strong **SDE-2 backend engineering** — transactions, concurrency, idempotency, messaging, distributed reliability — in a domain outside my day job.
**Domain:** fintech / payments. **This is an educational simulation, not a real financial service.**
**Runs across Phases 1–3 (Weeks 1–12), milestone-scoped M0–M6** (`instructions.md` §A-3) so it doesn't eat the course.

> **Design ownership:** this is a *specification of requirements, constraints, and milestones* — **not** a finished architecture. Key decisions are left to me and captured as ADRs: pessimistic vs optimistic locking; how idempotency keys are stored/expired; Kafka vs Redis Streams; outbox design; reconciliation strategy; where balances are derived vs cached.

---

## Core concept

A simplified payment + ledger platform. Money only moves through **balanced double-entry ledger entries** — never by mutating a `balance` column directly.

Candidate entities: **Account · Merchant · Payment · Transfer · Refund · LedgerEntry** (+ `IdempotencyKey`, `OutboxEvent` as they become justified).

Candidate APIs:
```
POST /accounts
GET  /accounts/{id}
GET  /accounts/{id}/balance
POST /transfers
POST /payments
POST /refunds
GET  /transactions/{id}
```

---

## The ledger requirement (the heart of the project)

Every movement produces **balanced entries**. Example — A pays Merchant ₹500:
```
A         -500
Merchant  +500
```
**Invariant:** the sum of ledger entries associated with a completed transfer balances to zero. Balances are **derived from entries** (optionally cached), never authoritative on their own.

I must be able to explain *why* a ledger differs from `account.balance += x`: auditability, reconstructable history, no lost updates, correctness under concurrency and partial failure.

---

## Functional requirements

- Create accounts and merchants; fetch account + derived balance.
- Execute transfers, payments, and refunds, each as **balanced ledger entries within a single DB transaction**.
- Every write endpoint that moves money accepts an **idempotency key**; a retried request with the same key must not double-apply.
- Emit domain events (`payment.completed`, `payment.failed`, `refund.completed`) reliably.
- Consumers react to events **idempotently** (e.g. notifications, projections) with no duplicate effects.
- A **reconciliation** task verifies invariants (entries balance; derived balances match ledger sums) and flags drift.
- Audit history: every money movement is reconstructable from ledger + event history.

## Non-functional / constraints

- **Correctness first:** no lost updates, no double spends, no unbalanced ledgers — provable by tests.
- Concurrency-safe under simultaneous operations on the same account.
- Reasonable throughput with measured **p95/p99**; document limits (no invented numbers, `instructions.md` §28).
- Observable: structured logs, metrics, tracing.
- Meets the craft/quality gates (`instructions.md` §27; `../../trackers/PROJECT_TRACKER.md`).

---

## Milestones (M0–M6)

| M | Weeks | Deliverable | Anti-cargo-cult gate |
|---|-------|-------------|----------------------|
| **M0** | 1–4 | Repo scaffold + quality gates; FastAPI skeleton; `POST/GET /accounts` with validation + error model; account domain model; integration tests | No DB internals/Redis/Kafka — not needed yet |
| **M1** | 5–6 | PostgreSQL schema; **double-entry ledger core**; `POST /transfers` inside one transaction; **invariant tests** (entries sum to 0) | Single-node PG only |
| **M2** | 7 | Concurrency safety: handle **Scenario B** (concurrent spend) via locking (justify pessimistic vs optimistic in an ADR); **idempotency keys** handling **Scenario A** (lost response); `POST /payments`, `POST /refunds` | Add locking only where a real race exists |
| **M3** | 8 | Kafka events (`payment.*`, `refund.completed`); **idempotent consumer** surviving **Scenario D** (crash before ack); Redis only if a concrete need is argued (e.g. rate limiting) | Must answer "why Redis / why Kafka here?" |
| **M4** | 9 | **Transactional outbox** resolving **Scenario C** (DB commit ok, publish fails); retries + backoff + DLQ; **reconciliation** task | Prove the dual-write problem exists before adding outbox |
| **M5** | 10–11 | Dockerize; structured logging + metrics + tracing (OTel); **load test → measured p95/p99**; deployable to practical k8s | Observability that answers real questions, not vanity metrics |
| **M6** | 12 | Audit history; ADRs for every significant choice; rate limiting if justified; **Phase-3 assessment + oral interview** | Complexity must be earned across the whole system |

---

## Required failure scenarios (make me reason *before* teaching the fix)

- **A — Lost response.** Payment commits; the network dies before the response reaches the client; client retries. *How do we prevent a duplicate payment?* → idempotency keys.
- **B — Concurrent spending.** Account A has ₹100; `A→B ₹100` and `A→C ₹100` fire simultaneously. *Can both succeed?* → isolation + locking (optimistic vs pessimistic).
- **C — DB / Kafka dual write.** Payment commits, but publishing `payment.completed` fails. *How do DB state and messaging state diverge?* → transactional outbox.
- **D — Consumer crash.** Consumer processes an event successfully, then crashes before acknowledging; the event is redelivered. *What prevents duplicate effects?* → idempotent consumers.

---

## Portfolio evidence (measurable)

Concurrency tests · invariant tests · throughput measurements · p95/p99 latency · EXPLAIN ANALYZE query plans · ADRs (locking choice, outbox, Kafka-vs-alternatives) · documented failure scenarios with how each is handled · reconciliation output.

## Concepts this project teaches (mapped to phases)

PostgreSQL modeling/constraints/indexes/transactions/MVCC/isolation/locking/deadlocks/EXPLAIN ANALYZE (Ph 2) · idempotency, retries, backoff, timeouts, outbox, eventual consistency, race conditions (Ph 2) · Redis (rate limiting/caching, justified) · Kafka delivery semantics/consumer groups/DLQ/idempotent processing (Ph 2) · Docker, observability, load testing, practical k8s (Ph 3) · API design, validation, error models, pagination, idempotency keys, auth concepts (Ph 1–2).
