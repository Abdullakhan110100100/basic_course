# Lesson 1 Primer — Python Object Model, Mutability & Copying

> Week 1 — Phase 1 SDE-2 Core Foundations

---

## 1. Names vs Objects

In Python, variables are **names** — labels that point to objects. The object lives in memory; the name is just a reference to it.

```python
x = 42
```

This does NOT store 42 "inside" x. It creates an integer object `42` in memory and binds the name `x` to it.

```python
y = x
```

Now both `x` and `y` point to the same object. No copy is made.

### `id()` and `is`

- `id(obj)` — returns the memory address of the object (unique identifier)
- `a is b` — checks if `a` and `b` point to the **same object** (identity)
- `a == b` — checks if `a` and `b` have the **same value** (equality, uses `__eq__`)

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b    # True  — same value
a is b    # False — different objects in memory

c = a
a is c    # True  — same object
```

---

## 2. Mutability

Python objects are either **mutable** (can be changed in place) or **immutable** (cannot).

| Mutable | Immutable |
|---|---|
| `list` | `int`, `float`, `bool` |
| `dict` | `str` |
| `set` | `tuple` |
| `bytearray` | `frozenset`, `bytes` |
| Most class instances | |

### Why it matters

When two names point to the same mutable object, mutating through one name changes what the other name sees.

```python
a = [1, 2, 3]
b = a           # b points to the same list

b.append(4)
print(a)        # [1, 2, 3, 4] — a sees the change
```

With immutable objects, you can't mutate in place — you create a new object instead.

```python
x = "hello"
y = x
y = y + " world"   # creates a NEW string object; x is unchanged
print(x)            # "hello"
```

---

## 3. Aliasing

Aliasing is when two or more names point to the same object. This is not a bug by itself, but it causes subtle bugs when you mutate through one name and forget the other name is watching.

```python
a = [1, 2, 3]
b = a           # alias — not a copy

b[0] = 99
print(a)        # [99, 2, 3]
```

**Interview trigger:** any time you pass a list to a function and modify it, the caller sees the change.

```python
def zero_first(lst):
    lst[0] = 0

nums = [1, 2, 3]
zero_first(nums)
print(nums)   # [0, 2, 3] — modified in place
```

---

## 4. Mutable Default Arguments

**One of Python's most common gotchas.**

```python
def append_item(item, collection=[]):   # BAD
    collection.append(item)
    return collection
```

The default value `[]` is created **once** when the function is defined — not on each call. Every call that omits `collection` shares the same list.

```python
append_item(1)   # [1]
append_item(2)   # [1, 2]  — not [2]!
append_item(3)   # [1, 2, 3]
```

### The fix: use `None` as sentinel

```python
def append_item(item, collection=None):   # GOOD
    if collection is None:
        collection = []
    collection.append(item)
    return collection
```

### Why `is None`, not `== None` or `not collection`

- `is None` checks **identity** — `None` is a singleton, so this is always correct.
- `== None` calls `__eq__`, which a custom class can override. Avoid it.
- `not collection` is wrong — an empty list `[]` is falsy, so a valid empty list passed by the caller would be incorrectly replaced with a new one.

PEP 8 rule: **always use `is` or `is not` when comparing to `None`.**

---

## 5. Shallow vs Deep Copy

When you copy a container (list, dict, etc.), you have two options:

### Shallow copy

Creates a **new outer container** but does **not** copy the nested objects — it copies the references.

```python
import copy

a = [[1, 2], [3, 4]]
b = a[:]             # or: b = list(a), b = copy.copy(a)

b[0].append(99)
print(a)   # [[1, 2, 99], [3, 4]] — inner list is shared!
print(b)   # [[1, 2, 99], [3, 4]]
```

`b` is a different list, but `b[0]` and `a[0]` still point to the **same inner list**.

### Deep copy

Recursively copies every nested object. No sharing.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)
print(a)   # [[1, 2], [3, 4]]   — unchanged
print(b)   # [[1, 2, 99], [3, 4]]
```

### When to use which

| Situation | Use |
|---|---|
| Flat containers (no nesting) | Shallow copy is fine |
| Nested mutable objects | Deep copy to avoid aliasing bugs |
| Large structures where nesting is safe | Shallow (cheaper) |

### Common shallow-copy methods

```python
b = a[:]            # slice — only for lists
b = list(a)         # list constructor
b = copy.copy(a)    # explicit shallow copy — works on any type
b = a.copy()        # dict/list method
```

---

## Summary

| Concept | One-liner |
|---|---|
| Name vs object | Variables are labels; assignment binds a name to an object, never copies |
| `is` vs `==` | `is` = identity (same object); `==` = equality (same value) |
| Mutable | Can change in place; mutations visible through all names pointing to it |
| Immutable | Cannot change in place; "modification" creates a new object |
| Aliasing | Two names → one object; mutation through either is visible through both |
| Mutable default arg | Default created once at definition time — use `None` sentinel instead |
| `is None` | Always use `is`, not `==`, when checking for `None` |
| Shallow copy | New container, shared inner objects |
| Deep copy | New container AND new inner objects, fully independent |
