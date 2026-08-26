# Lesson 1 Primer — Decorators

> Week 1 — Phase 1 SDE-2 Core Foundations

---

## Prerequisites: functions are first-class objects

In Python, functions are objects. You can:
- Assign them to variables
- Pass them as arguments
- Return them from other functions
- Store them in lists/dicts

```python
def greet(name):
    return f"Hello {name}"

say_hello = greet          # assign to another name
say_hello("Rex")           # works — same function object

def call_twice(fn, arg):   # accept a function as argument
    fn(arg)
    fn(arg)

call_twice(greet, "Rex")   # prints twice
```

---

## Closures

A closure is a function that **captures variables from its enclosing scope**, even after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiply(x):       # inner function
        return x * factor  # captures `factor` from outer scope
    return multiply        # return the inner function

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10 — factor=2 is "remembered"
triple(5)   # 15 — factor=3 is "remembered"
```

`factor` lives inside `double` and `triple` even though `make_multiplier` has returned. This is what makes decorators possible.

---

## What a decorator is

A decorator is a function that **takes a function, wraps it, and returns the wrapper**. The `@` syntax is shorthand for reassigning the function name.

```python
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)   # call the original
        print("after")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")

# @my_decorator is exactly equivalent to:
# greet = my_decorator(greet)
```

`greet` is now the `wrapper` function. The original `greet` is captured inside the closure.

---

## `functools.wraps` — always use it

The wrapper replaces the original function, which means metadata like `__name__` and `__doc__` are lost:

```python
greet.__name__   # "wrapper" — wrong
```

Fix with `functools.wraps`:

```python
from functools import wraps

def my_decorator(fn):
    @wraps(fn)              # copies __name__, __doc__, etc. from fn to wrapper
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result
    return wrapper
```

Now `greet.__name__` returns `"greet"`. Always use `@wraps` — it matters for debugging, introspection, and documentation tools.

---

## Parametrized decorators

Sometimes you want to pass arguments to the decorator itself:

```python
@retry(times=3)
def fetch_data():
    ...
```

This requires **three layers**: the outermost function takes the parameters, the middle function takes the function, the innermost function is the wrapper.

```python
from functools import wraps

def retry(times):                        # layer 1: takes decorator args
    def decorator(fn):                   # layer 2: takes the function
        @wraps(fn)
        def wrapper(*args, **kwargs):    # layer 3: the actual wrapper
            for attempt in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}, retrying...")
        return wrapper
    return decorator

@retry(times=3)
def fetch_data():
    raise ConnectionError("timeout")

# equivalent to: fetch_data = retry(times=3)(fetch_data)
```

The call `retry(times=3)` returns `decorator`. Then `@decorator` is applied to `fetch_data` — same as a regular decorator.

---

## Real-world uses

| Use case | What it does |
|---|---|
| `@property` | Turns a method into an attribute accessor |
| `@staticmethod`, `@classmethod` | Change how method receives first arg |
| `@functools.lru_cache` | Memoizes return values |
| `@app.route("/path")` | Flask/FastAPI route registration |
| `@retry(times=3)` | Retry logic without polluting business code |
| `@login_required` | Auth checks before a view |
| `@timer` | Performance measurement |

---

## Common mistakes

**1. Forgetting to call the original function**

```python
def broken(fn):
    def wrapper(*args, **kwargs):
        print("before")
        # forgot to call fn! returns None always
    return wrapper
```

**2. Forgetting `*args, **kwargs`** in the wrapper — the wrapper won't accept the same arguments as the original.

**3. Forgetting `@wraps(fn)`** — metadata is lost, debugging becomes painful.

**4. Calling the decorator instead of applying it**

```python
@my_decorator()   # wrong if my_decorator takes no args — calls it, passing fn to the result
@my_decorator     # correct for a plain decorator
```

---

## Summary

| Concept | One-liner |
|---|---|
| First-class function | Functions are objects — pass, return, assign freely |
| Closure | Inner function remembers variables from the outer scope after it returns |
| Decorator | Function that takes a function and returns a wrapper — adds behaviour without modifying the original |
| `@syntax` | Shorthand for `fn = decorator(fn)` |
| `@wraps(fn)` | Preserves `__name__`, `__doc__` on the wrapper — always use it |
| Parametrized decorator | Three layers: args → function → wrapper |
