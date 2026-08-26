# Mastery Tracker

Levels: **1 Recognize** (understand when explained) · **2 Explain** (from memory) · **3 Apply** (use in a new problem) · **4 Defend** (why, alternatives, failure modes, trade-offs, follow-ups). Interview-critical concepts require **Level 4**. One correct quiz ≠ mastered. Downgrade a level if a later check reveals shallow understanding.

Tracks: **[SDE-2]** backend/distributed · **[AI]** AI-engineering · **[Craft]** engineering craft. Rows are added as concepts are introduced.

## SDE-2 core (Phases 1–3)

| Concept | Phase | Interview-critical? | Level | Last assessed | Notes |
|---|---|---|---|---|---|
| Python object model (names vs objects, identity) | 1 | Yes | 3 | 2026-08-14 | Carried from pre-redesign; explained + applied; not yet defended under follow-up |
| Mutability & aliasing | 1 | Yes | 3 | 2026-08-14 | Carried; shallow vs deep copy confirmed; mutable-default demonstrated |
| Shallow vs deep copy | 1 | Yes | 3 | 2026-08-14 | Carried (see W003) |
| `None` sentinel pattern | 1 | No | 3 | 2026-08-27 | Reproduced unaided; W004 resolved |
| Iterators / generators | 1 | Yes | 3 | 2026-08-27 | Built iterator class + generator fn; explained memory savings correctly |
| Decorators / context managers | 1 | Yes | 3 | 2026-08-27 | Built `@log_call`, `@retry(times=N)`, `SuppressError` class, `@contextmanager` timer; caught `try/finally` gap |
| Typing / protocols / ABCs | 1 | Yes | — | — | |
| GIL | 1 | Yes | — | — | |
| Threads vs processes vs asyncio | 1 | Yes | — | — | |
| Event loop / coroutines / tasks / cancellation | 1 | Yes | — | — | |
| CPU-bound vs I/O-bound | 1 | Yes | — | — | |
| Race conditions / locks / deadlocks | 1 | Yes | — | — | |
| Bounded concurrency / semaphores | 1 | Yes | — | — | |
| DNS / TCP / HTTP lifecycle / keep-alive | 1 | Yes | — | — | |
| Connection pools | 1 | Yes | — | — | |
| p50/p95/p99 | 1 | Yes | — | — | |
| Graceful shutdown | 1 | Yes | — | — | |
| REST / API design / error contracts | 1 | Yes | — | — | |
| Idempotency keys (API) | 1 | Yes | — | — | |
| Testing (unit/integration, fixtures, mocks, DI) | 1 | Yes | — | — | |
| PostgreSQL schema/constraints/indexes | 2 | Yes | — | — | |
| Transactions / ACID / MVCC / isolation | 2 | Yes | — | — | core — critical gap forces remediation |
| Locking (pessimistic vs optimistic) / deadlocks | 2 | Yes | — | — | |
| EXPLAIN ANALYZE / query planner | 2 | Yes | — | — | |
| Redis (structures, TTL, atomic ops, rate limiting) | 2 | Yes | — | — | justify before use |
| Kafka (partitions, offsets, consumer groups, delivery semantics, DLQ) | 2 | Yes | — | — | |
| Idempotent consumers | 2 | Yes | — | — | core |
| Retries / backoff / jitter / timeouts | 2 | Yes | — | — | |
| Transactional outbox | 2 | Yes | — | — | dual-write problem |
| Eventual consistency / reconciliation | 2 | Yes | — | — | |
| Backpressure / bounded queues | 2 | Yes | — | — | |
| Docker (images, layers, multi-stage, graceful shutdown) | 3 | Yes | — | — | |
| Practical Kubernetes (SDE-2 depth) | 3 | Yes | — | — | not cert depth |
| Observability (logs/metrics/traces, OTel, SLI/SLO) | 3 | Yes | — | — | |
| System-design framework | 3 | Yes | — | — | |

## AI engineering (Phases 4–5)

| Concept | Phase | Interview-critical? | Level | Last assessed | Notes |
|---|---|---|---|---|---|
| Inverted index / TF-IDF intuition | 4 | Yes | — | — | |
| BM25 (math + intuition, length norm, k1/b) | 4 | Yes | — | — | must explain, not just use |
| Embeddings / cosine / dot product | 4 | Yes | — | — | |
| Vector search / ANN / HNSW intuition | 4 | Yes | — | — | |
| Hybrid retrieval / RRF | 4 | Yes | — | — | |
| Reranking | 4 | Yes | — | — | |
| Retrieval evaluation (P@K, R@K, MRR, NDCG) | 4 | Yes | — | — | |
| Ranking vs retrieval | 4 | Yes | — | — | |
| LLM fundamentals (tokens, context, structured output, cost) | 4 | Yes | — | — | |
| Code retrieval / context selection | 5 | Yes | — | — | |
| Agents vs deterministic workflows | 5 | Yes | — | — | |
| Tool schemas / agent loops / stopping conditions | 5 | Yes | — | — | |
| Model routing / fallback / caching | 5 | Yes | — | — | |
| Model-serving intuition (batching, KV cache, TTFT) | 5 | No | — | — | intuition only |
| AI evaluation (objective task eval, LLM-as-judge + limits) | 5 | Yes | — | — | |
| AI security (prompt injection, tool authz, sandboxing, least privilege) | 5 | Yes | — | — | architecture, not prompt |

## Engineering craft (parallel track — `instructions.md` §A-1)

| Concept | Phase | Interview-critical? | Level | Last assessed | Notes |
|---|---|---|---|---|---|
| Clean code (naming, function design, cohesion) | 1 | Yes | — | — | |
| DRY / KISS / YAGNI | 1 | Yes | — | — | over-abstraction is a failure too |
| SOLID (SRP, OCP, LSP, ISP, DIP) | 1–2 | Yes | — | — | must name a real violation, not recite |
| Coupling vs cohesion | 1–2 | Yes | — | — | |
| Design patterns (Strategy/Factory/Adapter/Repository/…) | 1–3 | Yes | — | — | when it IS vs ISN'T justified |
| Refactoring & code-smell recognition | 1 | Yes | — | — | safe refactor under tests |
| Git workflow / commit hygiene / code review | 1 | No | — | — | reviewer AND reviewee |
| Quality tooling (lint/format/type/pre-commit) | 1 | No | — | — | CI gate |
| API design (REST, versioning, idempotency, pagination, OpenAPI) | 1–4 | Yes | — | — | |
| Repository / Unit of Work | 2 | No | — | — | |
| AppSec / OWASP Top 10 / authz / secrets | 2 | Yes | — | — | security ≠ model behaving |
| Resilience patterns (circuit breaker, bulkhead, saga) | 3 | No | — | — | Level 3 target |
