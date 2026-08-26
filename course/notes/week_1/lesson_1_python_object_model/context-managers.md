# Lesson 1 Primer — Context Managers

> Week 1 — Phase 1 SDE-2 Core Foundations

---

## The problem they solve

Some resources need to be cleaned up after use — files closed, locks released, DB connections returned to a pool, transactions committed or rolled back. The naive approach:

```python
f = open("data.txt")
data = f.read()
f.close()   # never runs if f.read() raises an exception
```

If an exception fires between `open` and `close`, the file handle leaks. Context managers make cleanup **guaranteed**, even when exceptions occur.

---

## The `with` statement

```python
with open("data.txt") as f:
    data = f.read()
# f is closed here — always, even if f.read() raises
```

`with` guarantees the cleanup runs. This is the correct way to handle any resource that needs teardown.

---

## The context manager protocol

An object is a context manager if it implements two dunder methods:

```python
__enter__(self)          # runs when entering the `with` block; return value binds to `as` target
__exit__(self, exc_type, exc_val, exc_tb)   # runs on exit, even if an exception occurred
```

- If no exception: `exc_type`, `exc_val`, `exc_tb` are all `None`.
- If `__exit__` returns a **truthy value**, the exception is suppressed. If it returns `None` / `False`, the exception propagates.

### Building your own

```python
class ManagedFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        return self.file          # this is what `as f` receives

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False              # don't suppress exceptions

with ManagedFile("data.txt") as f:
    data = f.read()
```

### Suppressing exceptions selectively

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    self.file.close()
    if exc_type is FileNotFoundError:
        return True   # suppress this specific exception
    return False      # let everything else propagate
```

---

## `contextlib.contextmanager` — the generator shortcut

Writing a full class for a simple resource is verbose. `contextlib.contextmanager` lets you write it as a generator with one `yield`:

```python
from contextlib import contextmanager

@contextmanager
def managed_file(path):
    f = open(path)
    try:
        yield f           # everything before yield = __enter__
    finally:
        f.close()         # everything after yield = __exit__

with managed_file("data.txt") as f:
    data = f.read()
```

The `try/finally` is what guarantees cleanup — `finally` always runs, whether or not an exception occurred. This is the pattern you'll use most often in practice.

---

## Real-world uses (things you'll see in backend code)

| Use case | What gets cleaned up |
|---|---|
| `open()` | file handle closed |
| `threading.Lock()` | lock released even on exception |
| DB session (SQLAlchemy) | transaction committed or rolled back; connection returned to pool |
| `unittest.mock.patch` | mock removed after the test |
| Custom timer | records elapsed time on exit |

### Timer example

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{label}: {elapsed:.3f}s")

with timer("DB query"):
    results = db.execute(query)
```

---

## Common mistakes

**1. Forgetting `finally` in the generator form** — if you use `try/except` without `finally`, cleanup won't run on exceptions you don't catch.

```python
@contextmanager
def bad_managed_file(path):
    f = open(path)
    try:
        yield f
    except Exception:
        f.close()   # only closes on exception — misses the normal path!
```

**2. Returning a value from `__exit__` accidentally** — any truthy return suppresses the exception silently.

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    # implicit return None — fine, exceptions propagate
```

**3. Not using `with` at all** — manual `try/finally` works but is more code and easier to get wrong. Prefer `with`.

---

## Summary

| Concept | One-liner |
|---|---|
| Why context managers | Guaranteed cleanup even when exceptions occur |
| `__enter__` | Runs on entry; return value goes to `as` target |
| `__exit__` | Runs on exit (always); return truthy to suppress exception |
| `@contextmanager` | Generator shortcut; code before `yield` = enter, `finally` block = exit |
| `finally` | Always runs — the mechanism that makes cleanup guaranteed |
| When to use | Any resource with setup + teardown: files, locks, connections, timers, mocks |
