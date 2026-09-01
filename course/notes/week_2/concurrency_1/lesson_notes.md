# Concurrency I — Lesson Notes

**Date:** 2026-09-01
**Mastery level:** 3 (Apply)

---

## Key concepts

### Processes vs Threads

| | Process | Thread |
|---|---|---|
| Memory | Isolated | Shared |
| Creation cost | Expensive | Cheap |
| Python parallelism | True (bypasses GIL) | Limited by GIL |
| Use for | CPU-bound | I/O-bound |

### The GIL

- Exists to protect **CPython's internal memory management** (reference counting)
- Ensures only one thread executes Python bytecode at a time
- Releases every **5ms** (switch interval) AND during I/O operations
- Does NOT protect your application logic
- Does NOT make your operations atomic

### CPU-bound vs I/O-bound

- **CPU-bound** (image resizing, computation) → `multiprocessing` — true parallelism
- **I/O-bound** (HTTP calls, DB queries, file reads) → `threading` or `asyncio`

### Race conditions

Occur when two threads interleave their read-modify-write steps:
```
Thread 1: LOAD counter = 0
Thread 2: LOAD counter = 0   ← GIL switched here!
Thread 1: STORE counter = 1
Thread 2: STORE counter = 1  ← lost update!
```
`counter += 1` is NOT atomic — it's 3 bytecode instructions.

**Fix:** use a lock around the critical section.

### Locks

```python
lock = threading.Lock()  # capital L!

with lock:
    # critical section — only one thread here at a time
    counter += 1
```

### Deadlocks

Two threads each hold a lock the other needs → both wait forever.

**Prevention:** always acquire locks in the same order across all threads.

**LedgerFlow application:** when transferring between acc_1 and acc_2, always acquire locks in account_id order (e.g. alphabetical). Then acc_1→acc_2 and acc_2→acc_1 transfers both acquire acc_1's lock first → no deadlock.

---

## Mistakes / gaps

- Initially unclear why the GIL still allows race conditions (needed explanation of GIL releasing between bytecode instructions)
- `threading.lock()` — lowercase doesn't exist, it's `threading.Lock()`

---

## Next

- Week 2 concepts COMPLETE (Typing ✓, Exceptions ✓, Concurrency I ✓)
- **Week 3:** Concurrency II — asyncio, event loop, coroutines, tasks, cancellation
- **URGENT: LedgerFlow M0** — must start this week
- **DSA re-solve:** W001-W005 due (overdue from 2026-08-30)
