# Exceptions — Lesson Notes

**Date:** 2026-08-31
**Mastery level:** 3 (Apply)

---

## Key concepts

**Exception hierarchy:**
```
BaseException
└── Exception          ← always catch this, never BaseException
    └── LedgerError    ← base for all domain errors (just `pass`)
        ├── AccountNotFoundError
        ├── InsufficientFundsError
        └── AccountFrozenError
```

Never catch `SystemExit` / `KeyboardInterrupt` — they are intentional signals (sys.exit, Ctrl+C), not bugs.

**Custom exceptions:**
- Base class with `pass` — groups related errors, enables `except LedgerError`
- Subclasses store domain attributes (`account_id`, `required`, `available`)
- `super().__init__(f"message {var}")` — sets the human-readable message in `Exception.args[0]`
- Always use f-strings, not multiple args to `super().__init__`

**Check order matters:**
- Check frozen BEFORE balance — a frozen account should always be rejected regardless of balance

**Exception chaining:**
```python
except DatabaseError as e:
    raise AccountNotFoundError(account_id) from e
```
- Caller gets clean domain error
- Developer gets full root cause in traceback via `e.__cause__`
- Always chain when catching one exception and raising another

**Silent swallow is the worst pattern:**
```python
except LedgerError:
    pass  # ← never do this
```
Always log at minimum. Catch specific first, base as fallback.

**`try/except/else/finally`:**
- `else` — runs only if NO exception raised
- `finally` — runs ALWAYS (success, exception, return) — use for cleanup

---

## Mistakes made

- Forgot `f` prefix on f-strings in `super().__init__` (literal `{account_id}` not interpolated)
- Checked balance before frozen — wrong order (frozen = always reject)
- Passed multiple args to `super().__init__` instead of one f-string

---

## Next: Concurrency I

Processes vs threads, GIL, race conditions, locks, deadlocks.
