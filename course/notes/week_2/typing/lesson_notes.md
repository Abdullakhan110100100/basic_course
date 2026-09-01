# Typing — Lesson Notes

**Date:** 2026-08-28  
**Mastery level:** 3 (Apply)  
**Status:** Interview-critical concept, need Level 4 by Phase 6

---

## What I learned

### Core concepts

**Type hints are optional at runtime** — Python ignores them, but `mypy` checks them at development time (before code runs).

**Development time vs runtime:**
- Development time = writing code, mypy checks types, no execution
- Runtime = actually running `python file.py`, Python ignores type hints

**Basic syntax:**
```python
def transfer(from_id: str, to_id: str, amount: Decimal) -> str:
    ...
```

**Collection types:**
```python
from typing import List, Dict, Optional, Union

numbers: List[int] = [1, 2, 3]
scores: Dict[str, int] = {"Alice": 95}
name: Optional[str] = None  # same as Union[str, None]
```

---

### Protocols — structural subtyping

**Protocol** = define what methods/attributes an object must have, WITHOUT requiring inheritance.

```python
from typing import Protocol

class HasStatus(Protocol):
    status: str  # just declare the attribute

def filter_by_status(items: List[HasStatus], target: str) -> List[HasStatus]:
    return [item for item in items if item.status == target]
```

Any class with a `.status: str` attribute works — no inheritance needed.

**When to use Protocol vs ABC:**
- **Protocol:** don't control all classes, third-party code, more flexible, no inheritance
- **ABC:** you control the hierarchy, want runtime `isinstance()`, want shared implementation

---

### TypeVar — generics

Preserve type information through a function:

```python
from typing import TypeVar, List

T = TypeVar('T')  # ← parentheses, not brackets!

def get_last(items: List[T]) -> T:
    return items[-1]

numbers: List[int] = [1, 2, 3]
result = get_last(numbers)  # mypy knows result is int
```

---

### Why `Any` is dangerous

Using `Any` disables type checking:

```python
def process(data: Any) -> Any:
    result = data.transform()  # unchecked — .transform() might not exist
    return result.upper()      # unchecked — result might not be str
```

Three problems:
1. Input method calls unchecked (`.transform()` might not exist)
2. Return value method calls unchecked (`.upper()` might fail)
3. Caller gets no type info (return type `Any` tells them nothing)

---

## What I can now do

✓ Write type-hinted functions with proper signatures  
✓ Use Protocols to define structural interfaces  
✓ Explain when to use Protocol vs ABC  
✓ Use TypeVar for generic functions  
✓ Explain development time vs runtime  
✓ Predict what mypy will catch vs miss  

---

## Mistakes I made

- Initially tried to import `str` from `typing` (it's a built-in)
- Put `__init__` in a Protocol (Protocols just declare attributes, no implementation)
- Wrote `TypeVar['T']` with brackets instead of `TypeVar('T')` with parentheses
- Thought `Optional[X]` was different from `Union[X, None]` (they're identical)

---

## Questions I still have

- None yet — will surface during concurrency (async type hints) and project work

---

## Next: Exceptions, then Concurrency I

Week 2 continues with:
1. Exceptions — raising, catching, custom exceptions, finally/else
2. Concurrency I — processes vs threads, GIL, race conditions, locks
