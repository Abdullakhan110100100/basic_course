# Typing in Python — Primer

## Why typing matters (motivation)

You've written Python without type hints. It works. So why add them?

**Three reasons:**
1. **Catch bugs before runtime** — `mypy` finds type errors at development time
2. **IDE superpowers** — autocomplete, refactoring, go-to-definition work better
3. **Self-documenting code** — `def transfer(from_id: str, to_id: str, amount: Decimal)` vs `def transfer(a, b, c)`

Type hints are **optional** — Python doesn't enforce them at runtime. But `mypy` (a static type checker) does.

---

## Basic type hints

```python
# Variables
name: str = "Alice"
age: int = 30
balance: float = 100.50

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# Return None
def log(message: str) -> None:
    print(message)
```

**Key syntax:**
- Parameter: `name: type`
- Return type: `-> type`
- `None` is a type (for functions that don't return anything)

---

## Collection types (from `typing`)

```python
from typing import List, Dict, Set, Tuple, Optional

# List of integers
numbers: List[int] = [1, 2, 3]

# Dict from string to int
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Set of strings
tags: Set[str] = {"python", "typing"}

# Tuple (fixed size, heterogeneous)
point: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Alice", 30, True)

# Optional (value or None)
def find_user(id: str) -> Optional[User]:
    # might return User or None
    return users.get(id)
```

**Python 3.9+** allows using built-in types directly:
```python
numbers: list[int] = [1, 2, 3]  # instead of List[int]
scores: dict[str, int] = {}     # instead of Dict[str, int]
```

We'll use the `typing` module forms for now (more explicit).

---

## Union types

A value can be **one of several types**:

```python
from typing import Union

# Either int or float
def process(value: Union[int, float]) -> float:
    return float(value)

# Either str or None (same as Optional[str])
name: Union[str, None] = None
name: Optional[str] = None  # equivalent, more common
```

**Python 3.10+** has a shorthand:
```python
value: int | float  # instead of Union[int, float]
```

---

## The problem with duck typing

Python is **duck-typed**: "If it walks like a duck and quacks like a duck, it's a duck."

```python
def process_items(items):
    for item in items:
        print(item.name)
```

What's `items`? A list? A set? A custom iterable? What's `item`? Anything with a `.name` attribute?

**Without type hints, you can't tell.** Your IDE can't help. `mypy` can't check it.

---

## Protocols — structural subtyping

A **Protocol** defines what methods/attributes an object must have, without requiring inheritance.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

def render(obj: Drawable) -> None:
    obj.draw()

# Both work — they have .draw(), so they satisfy the Drawable protocol
render(Circle())
render(Square())
```

**Key insight:** `Circle` and `Square` don't inherit from `Drawable`. They just **happen to have** a `draw()` method. That's enough.

This is called **structural subtyping** (vs nominal subtyping with inheritance).

---

## When to use Protocol vs ABC (Abstract Base Class)

**Protocol:**
- External code you don't control (stdlib, third-party)
- Duck-typed interfaces ("anything with `.read()`")
- Lightweight contracts

**ABC (from `abc` module):**
- You control the inheritance hierarchy
- You want **runtime enforcement** (can't instantiate abstract class)
- Shared implementation in base class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2

# This would fail at instantiation:
# shape = Shape()  # TypeError: Can't instantiate abstract class
```

---

## Generics — TypeVar

What if you want to write a function that works with **any type**, but you want to preserve the type through the function?

**Wrong:**
```python
from typing import Any

def first(items: List[Any]) -> Any:
    return items[0]

names: List[str] = ["Alice", "Bob"]
result = first(names)  # mypy thinks result is Any, not str!
```

**Right — use TypeVar:**
```python
from typing import TypeVar, List

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

names: List[str] = ["Alice", "Bob"]
result = first(names)  # mypy knows result is str!
```

**Generic classes:**
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    
    def get(self) -> T:
        return self.value

box: Box[int] = Box(42)
val = box.get()  # mypy knows val is int
```

---

## Common pitfalls

### 1. Mutable default arguments (again!)

```python
# WRONG — mypy will complain
def append_to(item: int, target: List[int] = []) -> List[int]:
    target.append(item)
    return target
```

**Fix:**
```python
from typing import Optional, List

def append_to(item: int, target: Optional[List[int]] = None) -> List[int]:
    if target is None:
        target = []
    target.append(item)
    return target
```

### 2. Forgetting to import from `typing`

`List`, `Dict`, `Optional` are in `typing`, not built-in (before Python 3.9).

### 3. Using `Any` everywhere

`Any` turns off type checking. Use it sparingly (untyped third-party libraries, truly dynamic code).

---

## Running mypy

Install:
```bash
pip install mypy
```

Check a file:
```bash
mypy your_file.py
```

Check a project (with config):
```bash
mypy .
```

**Common mypy errors:**
- `Incompatible return value type` — you said `-> int` but returned `str`
- `Argument has incompatible type` — you passed `str` where `int` expected
- `Missing type parameters` — you wrote `List` instead of `List[int]`

---

## Your task after reading this

I'll ask you to:
1. **Explain** key concepts (Protocol, TypeVar, Optional)
2. **Predict** what `mypy` will say about code snippets
3. **Write** type-hinted functions and fix type errors
4. **Defend** when to use Protocol vs ABC

This is **Level 4 mastery** territory — you need to be able to explain *why*, not just *how*.

---

**Read this primer now. When you're done, let me know and we'll start the lesson.**
