# Revision Queue (spaced repetition)

Important mistakes and interview-critical concepts return on intervals: **~2–3 days → ~1 week → ~2–3 weeks → later mixed interviews.** Don't always announce that a question is revision; sometimes ambush with old material to force integration.

| Item | Source (weakness / lesson) | First seen | Next review | Interval stage | Notes |
|------|----------------------------|-----------|-------------|----------------|-------|
| Shallow vs deep copy: `a=[[1,2]]; b=a[:]`; mutation question | W003 / Lesson 1 | 2026-08-14 | **2026-08-30** | 3 | Regression caught 2026-08-27 (self-corrected); one more round to confirm |

## Ambush pool (surprise retrieval — pull mid-lesson to force integration)
- Later during the async week: *"A Python async endpoint calls a blocking (synchronous) PostgreSQL client. What happens, and why?"*
- Later during Kafka (LedgerFlow M3): *"Your consumer updates PostgreSQL and crashes before acknowledging. What happens? How do you make it safe?"*
- Later during outbox (M4): *"The DB commit succeeds but the Kafka publish fails. How do the two states diverge?"*
- (Fill more as concepts accumulate.)
