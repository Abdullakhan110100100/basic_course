# Project Tracker

**Three** portfolio projects, in domains deliberately outside my day job (signals transfer of engineering principles — `instructions.md` §17). Every project must eventually meet the quality standard: README · problem definition · architecture diagram · setup · API docs · unit + integration tests · CI · Docker · structured logging · metrics · tracing · benchmark/load-test results · known limitations · failure scenarios · security considerations · trade-offs · ADRs.

**Craft gates (every project):** clean structure (SOLID/cohesion, no unjustified abstraction) · passes `ruff` + formatter + `mypy` via `pre-commit` · meaningful atomic commit history · ≥1 design choice justified as pattern/ADR + the simpler alternative it beat · security checklist (input validation, authz, secrets, dependency scan). Code that merely "works" but is poorly structured does not pass review.

Practical work also includes **Level-1 Labs** (30 min–3 h, no repos) and **Level-2 Phase Challenges** (3–8 h) — see `instructions.md` §13; these are logged in the weekly reviews, not here.

| # | Project | Phase(s) | Status | Milestone / next step |
|---|---------|----------|--------|----------------------|
| 1 | **LedgerFlow** — payments & double-entry ledger | 1–3 (Wk 1–12) | **Not started** | Kick off **M0** (repo scaffold + quality gates + `/accounts` API) in parallel with Week 1 |
| 2 | **SearchLab** — intelligent search & recommendation | 4 (Wk 13–17) | Not started | Begins Week 13; choose product dataset by Week 12 |
| 3 | **RepoPilot** — secure AI software-engineering agent (flagship) | 5 (Wk 18–21) | Not started | Begins Week 18 |

## LedgerFlow milestones (spec: `../course/projects/ledgerflow.md`)
- [ ] **M0** (Wk 1–4) — repo scaffold + tooling gates; FastAPI skeleton; `POST/GET /accounts` with validation + error model; account model; integration tests. *No DB internals / Redis / Kafka yet.*
- [ ] **M1** (Wk 5–6) — PG schema; double-entry ledger core; `POST /transfers` in one transaction; invariant tests (entries sum to 0).
- [ ] **M2** (Wk 7) — concurrency safety (Scenario B, locking ADR); idempotency keys (Scenario A); `/payments`, `/refunds`.
- [ ] **M3** (Wk 8) — Kafka events + idempotent consumer (Scenario D); Redis only if justified.
- [ ] **M4** (Wk 9) — transactional outbox (Scenario C); retries/backoff/DLQ; reconciliation task.
- [ ] **M5** (Wk 10–11) — Docker; observability (logs/metrics/traces); load test → measured p95/p99; deployable to practical k8s.
- [ ] **M6** (Wk 12) — audit history; ADRs; rate limiting (if justified); Phase-3 assessment + oral interview.

## SearchLab stages (spec: `../course/projects/searchlab.md`)
- [ ] Stage 1 lexical (inverted index + BM25 by hand) · Stage 2 dense · Stage 3 hybrid (weighted vs RRF) · Stage 4 reranking · Stage 5 evaluation (P@K/R@K/MRR/NDCG on ~100–500 labeled queries) + benchmark table · Stage 6 ranking features · Stage 7 recommendations (if time).

## RepoPilot stages (spec: `../course/projects/repopilot.md`)
- [ ] Stage 1 repo intelligence (read-only) · Stage 2 tool-using agent · Stage 3 controlled editing (sandbox) · Stage 4 validation loop · Stage 5 objective evaluation · Stage 6 AI security.
