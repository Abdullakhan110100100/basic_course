# Lesson 1 Primer — Iterators & Generators

> Week 1 — Phase 1 SDE-2 Core Foundations

---

## Iterators

### What Python does in a `for` loop

When you write:

```python
for x in [1, 2, 3]:
    print(x)
```

Python does this under the hood:

1. Calls `iter([1, 2, 3])` → returns an **iterator object**
2. Repeatedly calls `next(iterator)` → gets one value at a time
3. When the iterator is exhausted, `next()` raises `StopIteration` → loop ends

An **iterable** is anything you can pass to `iter()` — lists, tuples, strings, dicts, files, etc.
An **iterator** is the object that actually produces values one at a time. It remembers where it is.

### The iterator protocol

Any object is an iterator if it implements two dunder methods:

```python
__iter__(self)   # returns self (so iterators are also iterables)
__next__(self)   # returns the next value, or raises StopIteration
```

### Building your own iterator

```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for n in CountUp(3):
    print(n)  # 0, 1, 2
```

### Common mistake

Iterators are **single-use**. Once exhausted, calling `next()` keeps raising `StopIteration`. Lists are iterables (not iterators) — you can loop them many times. An iterator of a list is consumed after one full pass.

```python
nums = [1, 2, 3]
it = iter(nums)
list(it)   # [1, 2, 3]
list(it)   # [] — exhausted
```

---

## Generators

### What they are

A generator is a function that uses `yield` instead of `return`. Calling it returns a **generator object** — which is an iterator. You don't have to write `__iter__` / `__next__` yourself.

```python
def count_up(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

for n in count_up(3):
    print(n)  # 0, 1, 2
```

### What actually happens at `yield`

When Python hits `yield`:
1. The current value is returned to the caller
2. The function's **local state is frozen** (local variables, position in code)
3. Execution resumes from the same line on the next `next()` call

This is unlike a normal function, which throws away all state when it returns.

### What generators actually save

This is the key point — generators are not just syntactic sugar. They save **memory**.

```python
# Builds the entire list in memory before you touch a single item
big_list = [x * x for x in range(10_000_000)]

# Computes one value at a time — only one integer lives in memory at once
big_gen = (x * x for x in range(10_000_000))
```

If you only need to iterate through values once (e.g. summing, finding the first match), a generator uses O(1) memory vs O(n) for a list. For 10 million items that's the difference between ~80 MB and a few bytes.

### Generator expression vs list comprehension

```python
[x * x for x in range(5)]   # list — all in memory now
(x * x for x in range(5))   # generator — lazy, computes on demand
```

Use a list when you need random access, multiple passes, or length. Use a generator when you only need one pass.

### `return` inside a generator

A `return` inside a generator raises `StopIteration`. Anything after it never runs.

```python
def gen():
    yield 1
    return        # stops iteration here
    yield 2       # never reached
```

### Common mistakes

**1. Generators are single-use** — same as any iterator.

```python
g = (x for x in range(3))
list(g)   # [0, 1, 2]
list(g)   # [] — already exhausted
```

**2. Lazy evaluation hides bugs** — code inside a generator doesn't run until you ask for a value.

```python
def gen_with_side_effect():
    print("start")   # doesn't print until first next()
    yield 1

g = gen_with_side_effect()   # nothing printed yet
next(g)                      # prints "start", returns 1
```

---

## Summary

| Concept | One-liner |
|---|---|
| Iterable | Anything you can pass to `iter()` |
| Iterator | Produces values one at a time; single-use; raises `StopIteration` when done |
| Generator | A function with `yield`; returns an iterator automatically; freezes local state between yields |
| Memory saving | Generator = O(1) memory (lazy); list = O(n) (eager) |
| When to use generator | Single-pass, large/infinite sequences, pipeline of transformations |
| When to use list | Multiple passes, random access, need `len()`, need to mutate |
