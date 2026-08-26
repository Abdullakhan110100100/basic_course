# 28-Week Curriculum — Backend / Distributed Systems / AI Platform

**Goal:** Be strong enough to clear SDE-2 Backend / AI Platform interviews and defend every important claim on the resume under aggressive questioning.
**Budget:** 15 hrs/week × 28 weeks ≈ 420 hrs. Progression is **mastery-gated**, not date-gated.

## Weekly operating system (every week)

| Activity | Hours |
|---|---|
| DSA | 3 |
| Concepts / reading / experimentation | 3 |
| Building | 6 |
| Testing, benchmarking, debugging | 2 |
| Technical write-up / explaining aloud (record 10–15 min, no notes) | 1 |
| **Total** | **15** |

> **Engineering craft is not a separate line item.** SOLID, clean code, refactoring, patterns, Git hygiene, API design, and AppSec fold into the **Building + Testing + Write-up** hours — they are *how* the project work is done and how it is reviewed, not an extra subject. The only additions to *Concepts* time are short **craft primers** (15–30 min) at first-introduction points. See the [Engineering Craft & Best Practices track](#engineering-craft--best-practices-parallel-track-weeks-128) below.

## Phase overview

| Phase | Weeks | Main subject | Portfolio project |
|---|---|---|---|
| 1 | 1–4 | Python & computer-systems fundamentals | High-performance async processing service |
| 2 | 5–8 | PostgreSQL, Redis, Kafka | Distributed job scheduler |
| 3 | 9–14 | Distributed systems (highest priority) | Workflow orchestration engine |
| 4 | 15–18 | Docker, Kubernetes, cloud, observability | Productionize workflow platform + Chaos Day |
| 5 | 19–23 | AI systems: retrieval, eval, LLM serving, agents, security | Enterprise AI Support Platform (flagship) |
| 6 | 24–26 | LLD + system design | Architecture portfolio (≥5 design docs) |
| 7 | 27–28 | Interview sprint | Interview-ready capstone + portfolio |
| Parallel | 1–28 | DSA | ~120–150 curated problems |
| Parallel | 1–28 | Engineering craft & best practices | Applied in every project + review; consolidated Wk 24–26 |

**Design principle:** projects build on each other into one ecosystem. Projects 2→4 can be one evolving repo. The AI platform (Project 5) integrates the earlier work.

---

## PHASE 1 — Python as an engineering language (Weeks 1–4, ~60h)

You already write Python. This phase is about **what Python does underneath your code** and the systems concepts around it.

### Week 1 — Python runtime & object model
Object model; references vs values; mutability; stack/heap intuition; reference counting + GC; iterators; generators; context managers; decorators (incl. with args); descriptors; dataclasses; typing; protocols; ABCs; dependency injection.
**Build (no libraries where practical):** your own context manager, iterator, parametrized decorator, tiny DI container, TTL cache.
**Must be able to explain:** why mutable default args are dangerous; what generators actually save; when copying bites you; what happens when Python creates/frees an object.
**Craft primer:** clean-code fundamentals (naming, function size/single-responsibility, cohesion, DRY / KISS / YAGNI, self-documenting code vs comments) + Git workflow (feature branches, small atomic commits, meaningful messages) + repo quality tooling as Project 1's scaffolding (`ruff` lint, `black`/formatter, `mypy`, `pre-commit`). Every commit from here on passes the gates.

### Week 2 — Concurrency
Threads (scheduling, race conditions, locks, deadlocks, thread pools); processes (multiprocessing, IPC, serialization, process pools); async (event loop, coroutines, futures, tasks, cancellation, async CMs, semaphores, bounded concurrency). Study the **GIL properly** — "Python can't multithread" is misleading. Internalize CPU-bound → multiprocessing; I/O-bound → threads OR asyncio, **and why**.
**Craft primer:** **SOLID** taught concretely (not as acronyms) against the concurrency design — SRP, OCP, LSP, ISP, DIP; where coupling/cohesion actually bite; dependency inversion vs the DI container you built in Wk1. Must be able to name a real SOLID violation in your own code and the smell it produces.

### Week 3 — Networking & HTTP
DNS; TCP + connection establishment; HTTP request lifecycle; HTTP/1.1; HTTP/2 concepts; keep-alive; connection pooling; TLS basics; sockets; proxies; load balancers.
**Must be able to answer (no hand-waving):** "What happens after I type `https://example.com`?"
**Craft primer:** design patterns that fall out of Project 1 naturally — **Strategy** (your sync/threaded/async variants *are* interchangeable strategies), **Factory**, **Adapter** — chosen because they solve a real problem, never memorized. Plus **API design basics**: REST resource/verb semantics, status codes, consistent error contracts, idempotency keys, pagination.

### Week 4 — Performance & testing
Profiling (CPU, memory); benchmarking; p50/p95/p99; load testing; unit + integration tests; mocks; fixtures; contract-testing concepts; failure testing.
**Craft primer:** **refactoring under a test net** — identify code smells (long functions, primitive obsession, feature envy, shotgun surgery) in your own Project 1 code and refactor safely with tests green; the test pyramid; **code review as a skill** (self-review first per the Code-Review Protocol, then review as if it were a teammate's PR).

### Project 1 — Async Processing Service (spec)
Build a service that accepts thousands of document/URL processing jobs, in **three implementations**: synchronous, threaded, asyncio (add a multiprocessing variant for CPU-bound comparison where relevant).
**Measure:** throughput, CPU, memory, p50, p95, p99.
**Add:** concurrency limits, cancellation, timeouts, retries, graceful shutdown, structured logging, integration tests.
**README must explain (with evidence, not assertions):**
- Why async improved — or didn't improve — performance.
- Why increasing concurrency indefinitely hurts throughput.
- What happens when downstream services become slow.
- What would change if processing became CPU-bound.
**Require benchmark evidence — no invented numbers.**

### Phase 1 assessment & passing criteria
Four-part gate (instructions.md §19): (A) Knowledge exam, (B) debugging challenge, (C) project review, (D) oral interview on the project.
**Exit criteria — cannot advance until you can confidently *defend* (Level 4):** GIL · threads vs processes vs asyncio · event loop · race conditions · connection pools · CPU-bound vs I/O-bound · p50/p95/p99 · graceful shutdown.
**Score /100** (Conceptual 25 / Implementation 20 / Architecture 20 / Testing 15 / Performance 10 / Explanation 10). **Pass = 80**; a critical gap in any core concept forces remediation regardless of score.

---

## Phases 2–7 (summary — detailed objectives generated at each phase start)

- **Phase 2 (Wk 5–8):** PG fundamentals → PG internals (ACID, MVCC, isolation levels, locks, deadlocks, WAL, EXPLAIN ANALYZE) → Redis (structures, patterns, cache invalidation) → Kafka (partitions, offsets, consumer groups, delivery semantics, DLQ, idempotency). **Project 2:** distributed job scheduler (FastAPI + PG + Redis + Kafka) with failure tests. *Craft:* **Repository pattern + Unit of Work** for data access; **DDD-lite** (entities vs value objects) in schema design; **AppSec intro** — SQL injection, input validation, secrets management, authn/authz + **OWASP Top 10** overview on the scheduler API.
- **Phase 3 (Wk 9–14):** partial failure, CAP/PACELC, replication/quorum, idempotency/retries/backoff/jitter, circuit breakers/bulkheads, scaling/sharding/consistent hashing, distributed transactions/sagas/CQRS/event sourcing, backpressure/load shedding, crash recovery/leases/heartbeats/consensus intuition. Taught **through failure scenarios**. **Project 3:** workflow orchestration engine; must state explicit execution guarantees. *Craft:* resilience **as design patterns** — circuit breaker, bulkhead, saga; **composition over inheritance** and **interface-driven pluggable executors** (OCP/DIP in anger); refactor Project 2's data layer as you reuse it.
- **Phase 4 (Wk 15–18):** Linux, Docker internals, Kubernetes (practical), AWS architecture, Terraform, observability (logs/metrics/traces, OTel, Prometheus, Grafana, RED/USE, SLI/SLO/SLA, error budgets). **Project 4:** productionize + mandatory **Chaos Day** + incident postmortem. *Craft:* **12-Factor app** principles (config, statelessness, disposability, logs as streams); **CI/CD quality gates** — lint + type-check + coverage threshold + dependency/security scan wired into the pipeline; secrets & **least-privilege** (IAM / K8s Secrets).
- **Phase 5 (Wk 19–23):** IR (inverted index, TF-IDF, BM25, embeddings, ANN/HNSW, hybrid, RRF, reranking) → retrieval eval (P@K, R@K, MRR, NDCG on a labeled set) → LLM systems (tokenization, context, inference latency/cost, caching, batching, gateways, routing, fallbacks, KV cache, TTFT, vLLM concepts) → agents vs workflows + tool auth → AI eval + security (prompt injection, least privilege, PII). **Project 5:** Enterprise AI Support Platform (flagship) with real benchmark tables. *Craft:* full **API-design discipline** (versioning, pagination, consistent error contracts, OpenAPI); **multi-tenant authorization** and general AppSec layered onto the AI-specific security work.
- **Phase 6 (Wk 24–26):** LLD **consolidate & defend** — SOLID, composition, DI, patterns, DDD are now *review-and-drill*, not first exposure (you've applied them across Projects 1–5 for 20 weeks); LLD coding exercises + system-design framework (14 steps) across ~15–20 systems. **Behavioral/ownership (STAR) prep begins.** **Project 6:** architecture portfolio (≥5 full design docs incl. rejected alternatives).
- **Phase 7 (Wk 27–28):** interview sprint — coding, backend, AI-platform, system-design mocks + **LLD / clean-code interview drills** + **code-review-in-interview** + **behavioral/STAR** stories + **resume deep-dive interrogation** to Level-4 depth on every claim.

### DSA schedule (parallel, ~3h/wk, 120–150 problems)
Wk1–2 arrays/hashing · 3–4 two-pointers/sliding window · 5–6 stack/queue/linked lists · 7–8 binary search/intervals · 9–10 trees/BST · 11–12 heaps/tries · 13–14 graphs/BFS/DFS · 15–16 topo sort/union-find · 17–18 recursion/backtracking · 19–20 greedy · 21–23 DP · 24–25 mixed medium · 26 weak-area repair · 27–28 timed mocks.
Loop: Attempt (30–35m) → analyze → hint if needed → solve → explain → **re-solve 2–3 days & weeks later**. A problem you watched someone solve is not solved.

---

## Engineering Craft & Best Practices (parallel track, Weeks 1–28)

The systems knowledge above makes you *dangerous*; craft makes you *hireable at SDE-2*. Interviewers and teammates judge you daily on how you structure code, design APIs, and reason about maintainability — not just whether the system scales. This track runs the whole way through, is **applied on real project code**, and is **enforced in every code review** (see `instructions.md` §13/§15). First exposure is early so it compounds: apply for ~20 weeks → *defend* in Phase 6.

**Anti-cargo-cult applies here too.** A pattern or abstraction is only "right" if it removes a real, present problem. "I added a Factory / interface / event bus" without a problem it solves is a finding, not a win. YAGNI beats speculative flexibility.

### Schedule (folds into Building + Testing + Write-up hours; ~15–30 min primers in Concepts time)

| Weeks | Craft focus | Applied on |
|---|---|---|
| 1 | Clean code (naming, function design, cohesion, DRY/KISS/YAGNI); Git workflow (branches, atomic commits); tooling gates (ruff, formatter, mypy, pre-commit) | Project 1 scaffolding |
| 2 | **SOLID** — concretely, against a real design | Project 1 concurrency design |
| 3 | Design patterns as needed (Strategy, Factory, Adapter); API-design basics (REST, error contracts, idempotency, pagination) | Project 1 API + variants |
| 4 | Refactoring under a test net; code smells; test pyramid; code review as a skill | Project 1 cleanup |
| 5–8 | Repository / Unit of Work; DDD-lite (entity vs value object); AppSec intro + **OWASP Top 10**; authn/authz | Project 2 |
| 9–14 | Resilience patterns (circuit breaker, bulkhead, saga); composition > inheritance; interface-driven design (OCP/DIP) | Project 3 |
| 15–18 | **12-Factor app**; CI/CD quality gates (lint/type/coverage/security scan); least-privilege & secrets | Project 4 |
| 19–23 | Full API-design discipline (versioning, OpenAPI); multi-tenant authorization; general AppSec | Project 5 |
| 24–26 | **Consolidate & defend** — SOLID, patterns, DDD, coupling/cohesion via LLD exercises; behavioral/STAR prep begins | Portfolio + LLD drills |
| 27–28 | LLD + clean-code interview drills; code-review-in-interview; behavioral/STAR | Mock interviews |

**Interview-critical (require Level 4 — Defend):** SOLID (esp. SRP, OCP, DIP) · coupling vs cohesion · when a design pattern *is* vs *isn't* justified · refactoring/code-smell recognition · REST/API design & idempotency · OWASP Top 10 & authz. Others (12-Factor, DDD-lite, specific patterns) target Level 3 (Apply) unless a resume claim demands more.

**Loop (mirrors DSA):** apply on project code → I review against the craft dimensions (§13) → **you fix your own code first** → I give feedback → the *next* project must show you internalized it. Watching a clean refactor ≠ being able to produce one.

---

## Repository structure (portfolio monorepo)

Keep tutoring files here in `basic_course/`. Build the **portfolio** in a separate repo, e.g. `engineering-systems-lab/`:

```
engineering-systems-lab/
  async-service/        # Project 1
  job-scheduler/        # Project 2
  workflow-engine/      # Projects 3 & 4 (evolves)
  ai-platform/          # Project 5 (flagship)
  docs/
    architecture/       # design docs / diagrams
    adr/                # Architecture Decision Records
    incidents/          # postmortems (Chaos Day, etc.)
  benchmarks/           # measured results, never invented
  infra/                # Docker, k8s manifests, Terraform
```

Per-project layout: `src/{api,domain,services,repositories,workers}`, `tests/{unit,integration}`, `infra/`, `docs/`, `benchmarks/`. Every significant tech choice needs an ADR (Context / Decision / Alternatives / Advantages / Disadvantages / Consequences). Complexity must be justified — don't explode into 75 files either.

**Craft gates (every project, enforced from Project 1):** passes `ruff` + formatter + `mypy` clean via `pre-commit`; meaningful commit history (small, atomic, well-described — not one "final" commit); at least one design decision justified as a pattern/ADR (and simpler alternatives it beat); a security checklist appropriate to the project (input validation, authz, secrets handling, dependency scan). Code that "works" but is poorly structured does **not** pass review.
