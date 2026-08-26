# Mastery Tracker

Levels: **1 Recognize** (understand when explained) · **2 Explain** (from memory) · **3 Apply** (use in a new problem) · **4 Defend** (why, alternatives, failure modes, trade-offs, follow-ups). Interview-critical concepts require **Level 4**. One correct quiz ≠ mastered.

| Concept | Phase | Interview-critical? | Level | Last assessed | Notes |
|---|---|---|---|---|---|
| Python object model (names vs objects, identity) | 1 | Yes | 3 | 2026-08-14 | Explained + applied; not yet defended under follow-up pressure |
| Mutability & aliasing | 1 | Yes | 3 | 2026-08-14 | Shallow vs deep copy confirmed; mutable default args demonstrated |
| Reference counting & GC | 1 | No | — | — | |
| Generators vs iterators | 1 | Yes | — | — | |
| Decorators / context managers | 1 | Yes | — | — | |
| GIL | 1 | Yes | — | — | |
| Threads vs processes vs asyncio | 1 | Yes | — | — | |
| Event loop | 1 | Yes | — | — | |
| CPU-bound vs I/O-bound | 1 | Yes | — | — | |
| Race conditions / locks / deadlocks | 1 | Yes | — | — | |
| Connection pools | 1 | Yes | — | — | |
| p50/p95/p99 | 1 | Yes | — | — | |
| Graceful shutdown | 1 | Yes | — | — | |

## Engineering craft & best practices (parallel track)

| Concept | Phase | Interview-critical? | Level | Last assessed | Notes |
|---|---|---|---|---|---|
| Clean code (naming, function design, cohesion) | 1 | Yes | — | — | |
| DRY / KISS / YAGNI | 1 | Yes | — | — | over-abstraction is a failure too |
| SOLID (SRP, OCP, LSP, ISP, DIP) | 1 | Yes | — | — | must name a real violation, not recite |
| Coupling vs cohesion | 1 | Yes | — | — | |
| Design patterns (Strategy/Factory/Adapter/Repository/…) | 1 | Yes | — | — | when it IS vs ISN'T justified |
| Refactoring & code-smell recognition | 1 | Yes | — | — | safe refactor under tests |
| Git workflow / commit hygiene / PR & code review | 1 | No | — | — | reviewer AND reviewee |
| Quality tooling (lint/format/type/pre-commit) | 1 | No | — | — | CI gate |
| API design (REST, versioning, idempotency, pagination, OpenAPI) | 1 | Yes | — | — | |
| Repository / Unit of Work | 2 | No | — | — | |
| DDD-lite (entity vs value object, bounded context) | 2 | No | — | — | Level 3 target |
| AppSec / OWASP Top 10 / authz / secrets | 2 | Yes | — | — | security ≠ model behaving |
| 12-Factor app principles | 4 | No | — | — | Level 3 target |

_Add rows as concepts are introduced. Downgrade a level if a later check reveals the understanding was shallow._
