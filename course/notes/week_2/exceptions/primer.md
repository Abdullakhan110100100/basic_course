# Exceptions in Python — Primer

## Why exceptions matter

You're building a payments API. What happens when:
- A user tries to transfer from an account that doesn't exist?
- An account has insufficient funds?
- The database is unreachable?
- Someone passes `amount = -100`?

You need a **systematic way to signal, propagate, and handle failure**. That's exceptions.

---

## The exception hierarchy

Python's built-in exceptions form a tree:

```
BaseException
├── SystemExit           ← sys.exit() — don't catch this
├── KeyboardInterrupt    ← Ctrl+C — don't catch this
└── Exception            ← catch THIS as your base
    ├── ValueError       ← bad value ("amount must be positive")
    ├── TypeError        ← wrong type
    ├── KeyError         ← dict key missing
    ├── IndexError       ← list index out of range
    ├── AttributeError   ← object has no attribute
    ├── RuntimeError     ← general runtime error
    ├── OSError          ← file/network errors
    │   └── FileNotFoundError
    └── ...
```

**Key rule:** Always catch `Exception` or a subclass, never `BaseException`. `SystemExit` and `KeyboardInterrupt` should propagate.

---

## raise, try, except, else, finally

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Bad input: {e}")
except ZeroDivisionError:
    print("Division error")
else:
    print(f"Result: {result}")  # runs ONLY if no exception
finally:
    print("Always runs")  # cleanup goes here
```

**`else` block:** runs only when NO exception was raised in the `try` block. Useful for code that should only run on success.

**`finally` block:** runs ALWAYS — success, exception, or even `return`. Use it for cleanup (closing files, releasing locks, etc.).

---

## Custom exceptions

For a production system, define your own exceptions. This lets callers handle specific failure modes:

```python
# base exception for your whole application
class LedgerError(Exception):
    pass

# specific subclasses
class InsufficientFundsError(LedgerError):
    def __init__(self, account_id: str, required: float, available: float):
        self.account_id = account_id
        self.required = required
        self.available = available
        super().__init__(
            f"Account {account_id} has insufficient funds: "
            f"required {required}, available {available}"
        )

class AccountNotFoundError(LedgerError):
    def __init__(self, account_id: str):
        self.account_id = account_id
        super().__init__(f"Account not found: {account_id}")

class DuplicateTransactionError(LedgerError):
    def __init__(self, idempotency_key: str):
        self.idempotency_key = idempotency_key
        super().__init__(f"Duplicate transaction: {idempotency_key}")
```

**Usage:**
```python
def transfer(from_id: str, to_id: str, amount: float) -> None:
    account = get_account(from_id)
    if account is None:
        raise AccountNotFoundError(from_id)
    if account.balance < amount:
        raise InsufficientFundsError(from_id, amount, account.balance)
    # ... proceed with transfer

# Caller can handle specifically:
try:
    transfer("acc_1", "acc_2", 500.0)
except InsufficientFundsError as e:
    return {"error": "insufficient_funds", "available": e.available}
except AccountNotFoundError as e:
    return {"error": "account_not_found", "account_id": e.account_id}
except LedgerError as e:
    return {"error": "ledger_error", "message": str(e)}
```

---

## Exception chaining

When you catch one exception and raise another, **chain them** to preserve context:

```python
try:
    result = db.query("SELECT * FROM accounts WHERE id = ?", account_id)
except DatabaseError as e:
    raise AccountNotFoundError(account_id) from e
    # ↑ the original DatabaseError is preserved as __cause__
```

**Without chaining:**
```
AccountNotFoundError: Account not found: acc_123
```

**With chaining:**
```
DatabaseError: Connection refused
The above exception was the direct cause of the following exception:
AccountNotFoundError: Account not found: acc_123
```

Chaining gives you a **full traceback** — critical for debugging in production.

---

## Common mistakes

### 1. Catching too broadly
```python
# WRONG — hides every possible error
try:
    do_something()
except Exception:
    pass  # silent failure — the worst kind

# RIGHT — catch specifically, at least log it
try:
    do_something()
except ValueError as e:
    logger.error("Bad input: %s", e)
    raise  # re-raise after logging
```

### 2. Using exceptions for control flow
```python
# WRONG — exceptions are for exceptional cases
try:
    value = my_dict[key]
except KeyError:
    value = default

# RIGHT — use .get()
value = my_dict.get(key, default)
```

### 3. Losing the original exception (no chaining)
```python
# WRONG — loses DatabaseError context
try:
    db.query(...)
except DatabaseError:
    raise AccountNotFoundError(id)  # where did the DB error go?

# RIGHT — preserve it
try:
    db.query(...)
except DatabaseError as e:
    raise AccountNotFoundError(id) from e
```

### 4. Catching `BaseException`
```python
# WRONG — catches KeyboardInterrupt, SystemExit
try:
    long_operation()
except BaseException:  # ← don't do this
    cleanup()

# RIGHT
try:
    long_operation()
except Exception:
    cleanup()
    raise
```

---

## Exceptions in FastAPI (preview)

FastAPI converts exceptions to HTTP responses. You'll use this in LedgerFlow M0:

```python
from fastapi import HTTPException

@app.get("/accounts/{account_id}")
async def get_account(account_id: str):
    account = db.find(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
```

You can also register **custom exception handlers**:
```python
@app.exception_handler(AccountNotFoundError)
async def handle_not_found(request, exc: AccountNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "account_not_found", "account_id": exc.account_id}
    )
```

This maps your domain exceptions directly to HTTP responses — clean separation.

---

**Read this primer. Let me know when you're ready and we'll drill it.**
