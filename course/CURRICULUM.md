# 24-Week Curriculum — Focused SDE-2 Backend + AI Engineer

**Goal:** be genuinely interview-ready for **two** roles — SDE-2 Backend Engineer and Applied AI Engineer — unified as *"a backend SDE-2 who specializes in building reliable AI systems."*
**Budget:** ~15 h/week × ~24 weeks ≈ 360 h. Progression is **mastery-gated, not date-gated** (`instructions.md` §9, §A-2).
**Portfolio:** exactly three projects, in domains deliberately outside my day job — **LedgerFlow** (fintech/backend), **SearchLab** (search/IR), **RepoPilot** (AI agent, flagship).

> Redesigned 2026-08-24 from the broad 6-role / 6-project / 28-week course (archived in `../archive/`). See `../instructions.md` for the behavioral contract.

## Weekly operating system (every week)

| Activity | Hours |
|---|---|
| DSA | 3 |
| Concepts / reading | 3 |
| Projects / implementation | 6 |
| Debugging / experiments / benchmarks | 2 |
| Quizzes / explanation / review | 1 |
| **Total** | **15** |

> **Engineering craft is not a separate line item** (`instructions.md` §A-1). SOLID, clean code, refactoring, patterns, API design, AppSec, Git/tooling gates fold into the *Projects + debugging* hours and are enforced in every code review. Only additions to *Concepts* time are short **craft primers** (15–30 min) at first-introduction points.

## Phase overview

| Phase | Weeks | Main subject | Primary project |
|---|---|---|---|
| 1 | 1–4 | SDE-2 core foundations (Python, concurrency, backend/network, APIs, testing) | LedgerFlow scaffolding (M0) |
| 2 | 5–9 | Databases + practical distributed backend (PostgreSQL, Redis, Kafka) | **LedgerFlow** (core build, M1–M4) |
| 3 | 10–12 | Production SDE-2 + system design (Docker, practical K8s, cloud, observability) | LedgerFlow productionized (M5–M6) |
| 4 | 13–17 | AI engineering + information retrieval | **SearchLab** |
| 5 | 18–21 | Production AI engineering (LLM systems, agents, eval, security) | **RepoPilot** (flagship) |
| 6 | 22–24 | Interview sprint | Deep dives + weakness remediation |
| Parallel | 1–24 | DSA | ~100–120 curated problems |
| Parallel | 1–24 | Engineering craft | Applied in every project + review; consolidated Wk 22–24 |

**Design principle:** LedgerFlow anchors backend/distributed depth (Phases 1–3); SearchLab builds IR + AI-engineering; RepoPilot integrates retrieval + agents + security into the flagship. Distributed systems are taught **practically, through LedgerFlow's failure scenarios**, not as a staff-level catalog.

---

## Compact 24-week roadmap

Legend: **Concepts** · **Labs (L1, 30 min–3 h)** · **Project milestone** · **DSA**. Phase Challenges (L2, 3–8 h) sit at phase boundaries.

| Wk | Phase | Primary concepts | Labs | Project milestone | DSA |
|----|-------|------------------|------|-------------------|-----|
| 1 | 1 | Python object model, references, mutability, iterators, generators, decorators, context managers | own context manager, iterator, parametrized decorator, TTL cache | LedgerFlow **M0**: repo scaffold + tooling gates | Arrays & hashing |
| 2 | 1 | Typing, protocols, exceptions, packaging; **concurrency I** (processes, threads, GIL, races, locks) | deliberate race condition; benchmark threads vs sync | M0: FastAPI skeleton, `POST/GET /accounts` | Arrays & hashing |
| 3 | 1 | **Concurrency II** (asyncio, event loop, coroutines, tasks, cancellation, semaphores, bounded concurrency, CPU vs IO) | benchmark async vs threads for IO; bounded-concurrency limiter | M0: account model + validation + error model | Two pointers / sliding window |
| 4 | 1 | Backend/network (DNS, TCP, HTTP lifecycle, keep-alive, connection pools, TLS, proxies/LBs); API engineering; testing (unit/integration, fixtures, mocks, DI, failure testing) | "what happens when I hit a URL" trace; pytest fixtures + failure tests | M0 done: accounts API tested; **Phase-1 challenge** | Two pointers / sliding window |
| 5 | 2 | PostgreSQL I: schema, normalization/denorm, constraints, indexes (composite/partial), joins | design ledger schema; EXPLAIN a slow query | LedgerFlow **M1**: double-entry ledger core + transfers | Stack / queue / linked lists |
| 6 | 2 | PostgreSQL II: transactions, ACID, MVCC, isolation levels, locking, deadlocks, EXPLAIN ANALYZE | produce a deadlock; observe isolation anomalies | M1 done: invariant tests (entries sum to 0) | Stack / queue / linked lists |
| 7 | 2 | Concurrency control: pessimistic vs optimistic locking; idempotency keys | reproduce concurrent-spend (Scenario B); lost-response (Scenario A) | LedgerFlow **M2**: concurrent-safe transfers + idempotency | Binary search / intervals |
| 8 | 2 | Redis (structures, TTL, eviction, atomic ops, rate limiting, caching, locks — *justify first*); Kafka (topics, partitions, offsets, consumer groups, ordering, delivery semantics, DLQ) | token-bucket rate limiter; idempotent consumer | LedgerFlow **M3**: `payment.*` events + idempotent consumer (Scenario D) | Binary search / intervals |
| 9 | 2 | Practical distributed reliability: retries, backoff, jitter, timeouts, transactional outbox, reconciliation, backpressure | dual-write failure (Scenario C); outbox relay | LedgerFlow **M4**: outbox + retries/DLQ + reconciliation; **Phase-2 challenge** | Trees / BST |
| 10 | 3 | Docker (images, layers, multi-stage, networking, volumes, graceful shutdown); observability (structured logs, metrics, traces, OTel, p50/95/99, SLI/SLO) | Dockerize LedgerFlow; add tracing; load test → p95/p99 | LedgerFlow **M5**: observability + load tests | Trees / BST |
| 11 | 3 | Practical Kubernetes (pods, deployments, services, ingress, config/secrets, readiness/liveness, resources, rolling deploys, autoscaling intuition); AWS architecture intuition | deploy to local k8s; readiness/liveness probes | M5 done: containerized + deployable | Heaps |
| 12 | 3 | **System design** framework (15 steps); rate limiter, URL shortener, notification system, job scheduler | design drills (2–3 systems) | LedgerFlow **M6**: ADRs, audit history, **Phase-3 assessment** | Heaps |
| 13 | 4 | IR I: tokenization, inverted index, term frequency, IDF, TF-IDF intuition, BM25 | implement simplified inverted index + BM25 by hand | SearchLab **Stage 1**: lexical search on product dataset | Graphs / BFS / DFS |
| 14 | 4 | IR II: embeddings, cosine/dot, vector indexing, ANN, HNSW intuition; dense retrieval | benchmark vector similarity; dense vs BM25 spot-check | SearchLab **Stage 2**: dense retrieval | Graphs / BFS / DFS |
| 15 | 4 | Hybrid retrieval: weighted scoring vs RRF; reranking | measure hybrid; reranker latency | SearchLab **Stages 3–4**: hybrid + reranking | Topological sort / union-find |
| 16 | 4 | Search evaluation: Precision@K, Recall@K, Hit Rate, MRR, NDCG; labeled sets | build ~100–500 query judgments; compute metrics | SearchLab **Stage 5**: evaluation + benchmark table | Topological sort / union-find |
| 17 | 4 | Ranking vs retrieval: popularity/rating/price/availability signals; LLM fundamentals (tokenization, context, structured output, model APIs, cost) | ranking-features experiment; token accounting | SearchLab **Stage 6–7**; **Phase-4 assessment** | Recursion / backtracking |
| 18 | 5 | Code retrieval: code-aware chunking, lexical + semantic code search, context selection, attribution | index a real repo; code vs doc retrieval | RepoPilot **Stage 1**: repository intelligence (read-only) | Recursion / backtracking |
| 19 | 5 | Tool-using agents: tool schemas, structured outputs, planning, agent loops, state, retries, stopping conditions | agent loop with `run_tests`/`read_file`; deliberate tool-loop bug | RepoPilot **Stage 2**: tool-using agent | Greedy |
| 20 | 5 | Controlled editing + validation loop: sandboxing, least privilege, allowlists, audit, rollback, iteration budget, cost control | sandboxed `edit_file`; edit→test→revise loop | RepoPilot **Stages 3–4**: controlled editing + validation | Dynamic programming |
| 21 | 5 | Objective eval (task success %, tool calls, tokens, cost, latency, rollback rate); AI security (indirect prompt injection, tool poisoning, untrusted context) | build task benchmark; exploit a poisoned repo README | RepoPilot **Stages 5–6**; **Phase-5 assessment** | Dynamic programming |
| 22 | 6 | Interview sprint: DSA mocks + backend interviews; **LLD/clean-code drills**, code-review-in-interview | timed DSA; LLD exercises (cache, rate limiter) | LedgerFlow deep-dive prep | Mixed timed mocks |
| 23 | 6 | System-design mocks (45–60 min); AI Engineer interviews; behavioral/STAR | design + AI mocks | SearchLab + RepoPilot deep-dive prep | Mixed timed mocks |
| 24 | 6 | Resume deep dives (Level-4 on every claim); high-severity weakness remediation; final readiness call | full mock loops | Portfolio defense (30–60 min each) | Weak-area repair |

---

## PHASE 1 — SDE-2 Core Foundations (Weeks 1–4, ~60 h)

I already write Python. This phase is about **what Python does underneath**, the concurrency models, the network/HTTP path, API discipline, and testing — plus standing up LedgerFlow's skeleton with quality gates from commit #1.

### Weekly objectives
- **Week 1 — Python runtime & object model.** Names vs objects, identity, references, mutability, aliasing, shallow/deep copy; iterators; generators (what they actually save); context managers; decorators (incl. parametrized). *Craft primer:* clean code (naming, function size/SRP, cohesion, DRY/KISS/YAGNI) + Git workflow (feature branches, small atomic commits) + tooling gates (`ruff`, formatter, `mypy`, `pre-commit`) as LedgerFlow's scaffolding.
- **Week 2 — Typing & concurrency I.** Typing, protocols, ABCs, exceptions, packaging; then processes vs threads, the **GIL** (properly — "Python can't multithread" is misleading), race conditions, locks, deadlocks, thread/process pools. *Craft primer:* **SOLID** taught concretely against a real design; must name a real violation, not recite acronyms.
- **Week 3 — Concurrency II (async).** Event loop, coroutines, futures, tasks, cancellation, async context managers, semaphores, bounded concurrency. Internalize **CPU-bound → multiprocessing; I/O-bound → threads or asyncio, and why.** *Craft primer:* design patterns that fall out naturally (Strategy/Factory/Adapter — chosen, not memorized).
- **Week 4 — Networking, APIs, testing.** DNS, TCP, HTTP request lifecycle, keep-alive, connection pooling, TLS basics, proxies/LBs ("what happens after I type `https://…`?"); REST resource/verb semantics, status codes, consistent error contracts, idempotency keys, pagination, versioning, auth concepts; unit + integration tests, fixtures, mocks, DI, failure testing. *Craft primer:* refactoring under a green test net; code smells; test pyramid; self-review as a skill.

### Labs (Level 1)
Own context manager · own iterator · parametrized decorator · TTL cache · deliberate race condition + fix · benchmark sync vs threads vs asyncio for an IO workload · bounded-concurrency limiter · trace a full HTTPS request · pytest fixtures + a failure-injection test.

### Project milestone — LedgerFlow M0 (parallel with the Python phase; keep it light)
Repo scaffold with quality gates (ruff/format/mypy/pre-commit, meaningful commits) → FastAPI skeleton → `POST /accounts`, `GET /accounts/{id}` with validation + a consistent error model → account domain model → integration tests. **No DB internals, no Redis, no Kafka yet** (anti-cargo-cult: they aren't needed for M0).

### Phase-1 challenge (Level 2, 3–8 h)
Given a small IO-bound processing service in a naive synchronous form: make it correct and fast — add bounded concurrency, timeouts, cancellation, retries, graceful shutdown, structured logging; **measure** throughput and p95 before/after (no invented numbers); explain why unbounded concurrency hurts and what changes if the work became CPU-bound.

### Exit criteria — cannot advance until I can **defend (Level 4)**
GIL · threads vs processes vs asyncio · event loop · race conditions · CPU-bound vs I/O-bound · connection pools · p50/p95/p99 · graceful shutdown · idempotency keys (API level) · why mutable default args bite.

### Assessment
Four-part gate (`instructions.md` §25) + score /100 (§26). **Pass = 80**; a critical gap in a core concept forces remediation regardless of score.

---

## Phases 2–6 (detailed objectives generated at each phase start)

- **Phase 2 (Wk 5–9) — Databases + practical distributed backend.** PG fundamentals → PG internals (ACID, MVCC, isolation, locks, deadlocks, EXPLAIN ANALYZE) → concurrency control (pessimistic vs optimistic, idempotency) → Redis (structures, patterns, cache invalidation, rate limiting — *justified*) → Kafka (partitions, offsets, consumer groups, delivery semantics, DLQ, idempotent consumers) → practical distributed reliability (retries/backoff/jitter/timeouts, transactional outbox, reconciliation, backpressure). **Project: LedgerFlow M1–M4** with all four failure scenarios. *Craft:* Repository/Unit-of-Work; entity vs value object; AppSec intro + **OWASP Top 10**; authn/authz on the payments API. **Not** Paxos/Raft/consensus internals.
- **Phase 3 (Wk 10–12) — Production SDE-2 + system design.** Docker; practical Kubernetes (SDE-2 depth only); AWS architecture intuition; observability (logs/metrics/traces, OTel, p50/95/99, SLI/SLO); **system-design framework** across ~5–7 systems. **Project: LedgerFlow M5–M6** (observability, load tests, ADRs, audit history). *Craft:* resilience patterns (circuit breaker, bulkhead, saga) as *design patterns*; composition over inheritance; CI quality gates.
- **Phase 4 (Wk 13–17) — AI engineering + IR.** Inverted index/TF-IDF/BM25 → embeddings/ANN/HNSW → hybrid + RRF → reranking → evaluation (P@K, R@K, MRR, NDCG on a labeled set) → ranking vs retrieval → LLM fundamentals. **Project: SearchLab** with a real benchmark table. *Craft:* API-design discipline (versioning, pagination, OpenAPI, consistent errors).
- **Phase 5 (Wk 18–21) — Production AI engineering.** Code retrieval → tool-using agents → controlled editing + validation loop → objective evaluation → AI security. Model-serving *intuition* only. **Project: RepoPilot (flagship).** *Craft:* least-privilege/authorization enforced in architecture, not prompts; audit logging.
- **Phase 6 (Wk 22–24) — Interview sprint.** DSA mocks, backend/system-design/AI-Engineer mocks, project + resume deep dives, weakness remediation, **LLD/clean-code drills + behavioral/STAR** consolidation. Almost no new tech.

---

## DSA schedule (parallel, ~3 h/week, ~100–120 problems)

Wk1–2 arrays/hashing · 3–4 two-pointers/sliding window · 5–6 stack/queue/linked lists · 7–8 binary search/intervals · 9–10 trees/BST · 11–12 heaps · 13–14 graphs/BFS/DFS · 15–16 topo sort/union-find · 17–18 recursion/backtracking · 19 greedy · 20–21 DP · 22–24 mixed timed mocks + weak-area repair.

Loop: **Attempt (30–35 min) → explain reasoning → hint if needed → solve → analyze → re-solve 2–3 days & weeks later.** Optimize for pattern recognition, not count. A problem you watched solved is **not** solved. Tracked in `../trackers/DSA_TRACKER.md`.

---

## Engineering Craft (parallel track, Weeks 1–24) — `instructions.md` §A-1

Systems knowledge makes me *dangerous*; craft makes me *hireable at SDE-2*. Applied on real project code, enforced in every review (`instructions.md` §21/§27). First exposure early → apply for ~18 weeks → **defend in Phase 6**.

| Weeks | Craft focus | Applied on |
|---|---|---|
| 1 | Clean code; Git workflow; tooling gates (ruff/format/mypy/pre-commit) | LedgerFlow M0 scaffold |
| 2 | **SOLID** — concretely, against a real design | Concurrency design |
| 3 | Patterns as needed (Strategy/Factory/Adapter) | Concurrency variants |
| 4 | Refactoring under tests; code smells; test pyramid; self-review | Phase-1 challenge cleanup |
| 5–9 | Repository/Unit-of-Work; entity vs value object; **OWASP Top 10**; authn/authz | LedgerFlow |
| 10–12 | Resilience patterns; composition > inheritance; CI gates; 12-factor-lite | LedgerFlow productionization |
| 13–17 | API-design discipline (versioning, pagination, OpenAPI, error contracts) | SearchLab |
| 18–21 | Architecture-level authorization/least-privilege; audit logging | RepoPilot |
| 22–24 | **Consolidate & defend** — SOLID, patterns, coupling/cohesion via LLD drills; behavioral/STAR | Mock interviews |

**Interview-critical (Level 4):** SOLID (SRP/OCP/DIP) · coupling vs cohesion · when a pattern *is* vs *isn't* justified · refactoring/code-smell recognition · REST/API design & idempotency · OWASP Top 10 & authz. Others (12-factor, DDD-lite, specific patterns) target Level 3 unless a resume claim demands more.

---

## Repository structure (portfolio)

Keep tutoring files here in `basic_course/`. Build the **portfolio** in a separate repo, e.g. `engineering-systems-lab/`:

```
engineering-systems-lab/
  ledgerflow/        # Project 1 — payments & double-entry ledger
  searchlab/         # Project 2 — search / IR
  repopilot/         # Project 3 — secure AI agent (flagship)
  docs/
    architecture/    # design docs / diagrams
    adr/             # Architecture Decision Records
  benchmarks/        # measured results, never invented
  infra/             # Docker, k8s manifests
```

Per-project layout: `src/{api,domain,services,repositories,workers}`, `tests/{unit,integration}`, `infra/`, `docs/`, `benchmarks/`. Every significant tech choice needs an ADR (Context / Decision / Alternatives / Advantages / Disadvantages / Consequences). **Complexity must be justified** — don't explode into dozens of files either. Craft gates apply from LedgerFlow M0 (`../trackers/PROJECT_TRACKER.md`).
