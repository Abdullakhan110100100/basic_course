# Revision Queue (spaced repetition)

Important mistakes and interview-critical concepts return on intervals: **~2–3 days → ~1 week → ~2–3 weeks → later mixed interviews.** Don't always announce that a question is revision; sometimes ambush with old material to force integration.

| Item | Source (weakness ID / lesson) | First seen | Next review | Interval stage | Notes |
|------|-------------------------------|-----------|-------------|----------------|-------|
| Aliasing: predict output for `b=a; b.append(x); print(a)` | W001 / Lesson 1 | 2026-08-14 | 2026-08-17 | 1 (2–3 days) | Ambush mid-lesson; don't announce |
| Mutable default arg: what does `def f(x=[]):` do across calls? | W002 / Lesson 1 | 2026-08-14 | 2026-08-17 | 1 (2–3 days) | Ask to write the safe version from scratch |
| `None` sentinel pattern: write it and explain why not `if not x` | W004 / Lesson 1 | 2026-08-14 | 2026-08-17 | 1 (2–3 days) | Must reproduce without prompting |
| Shallow vs deep copy: `a=[[1,2]]; b=a[:]`; mutation question | W003 / Lesson 1 | 2026-08-14 | 2026-08-21 | 2 (1 week) | Confirm it stuck |

## Ambush pool (surprise retrieval — pull from here mid-lesson)
- _(will fill as concepts accumulate; e.g. later during Kafka week: "A Python async service calls a blocking PostgreSQL client. What happens?")_
