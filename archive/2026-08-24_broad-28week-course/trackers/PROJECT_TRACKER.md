# Project Tracker

Four flagship portfolio stories by the end; later projects reuse/improve earlier ones. Every project must meet the quality standard: README · architecture diagram · setup · unit + integration tests · Docker · CI · structured logging · metrics · tracing · error handling · benchmark/load-test results · known limitations · failure scenarios · trade-offs · ADRs for significant choices.

**Craft gates (every project):** clean structure (SOLID / cohesion, no unjustified abstraction) · passes `ruff` + formatter + `mypy` via `pre-commit` · meaningful atomic commit history · ≥1 design choice justified as pattern/ADR + simpler alternative it beat · security checklist (input validation, authz, secrets, dependency scan). Code that merely "works" but is poorly structured does not pass review.

| # | Project | Phase | Status | Milestone / next step |
|---|---------|-------|--------|----------------------|
| 1 | Async Processing Service | 1 | **Not started** | Kick off in parallel with Week 1; decide job type (doc/URL processing) |
| 2 | Distributed Job Scheduler | 2 | Not started | — |
| 3 | Workflow Orchestration Engine | 3 | Not started | — |
| 4 | Productionized Workflow Platform (+ Chaos Day) | 4 | Not started | — |
| 5 | Enterprise AI Support Platform (flagship) | 5 | Not started | — |
| 6 | Architecture Portfolio (≥5 design docs) | 6 | Not started | — |

## Quality checklist per project (fill as built)
### Project 1 — Async Processing Service
- [ ] Sync / threaded / async (+ multiprocessing for CPU-bound) implementations
- [ ] Benchmarks: throughput, CPU, memory, p50/p95/p99 (measured, not invented)
- [ ] Concurrency limits · cancellation · timeouts · retries · graceful shutdown · structured logging
- [ ] Integration tests
- [ ] README explains: why async helped/didn't · why unbounded concurrency hurts · slow-downstream behavior · CPU-bound implications
- [ ] ADR(s) for key choices
- [ ] Craft: clean-code + SOLID applied; Strategy pattern for sync/threaded/async variants (or justified alternative)
- [ ] Craft: `ruff` + formatter + `mypy` clean via `pre-commit`; atomic commit history
- [ ] Craft: one refactor pass under green tests (record before/after smell)
