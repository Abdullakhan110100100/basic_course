# Concurrency I — Primer: Processes, Threads, GIL, Race Conditions, Locks

## Why concurrency matters

Your LedgerFlow payments API will receive many simultaneous requests. Two users might try to withdraw from the same account at the same time. Without understanding concurrency, you'll write code that silently corrupts data — the balance goes negative, or a transfer gets applied twice.

This is not theoretical. It's the most common class of bug in payment systems.

---

## Processes vs Threads

### Process

A **process** is an independent running program. It has its own:
- Memory space (heap, stack)
- File descriptors
- OS resources

When you run `python script.py`, you create one process. Two processes **cannot share memory** by default — they're isolated.

**Communication between processes:** files, sockets, pipes, queues (via `multiprocessing.Queue`).

```python
import multiprocessing

def worker(n):
    print(f"Process {n} running")

p = multiprocessing.Process(target=worker, args=(1,))
p.start()
p.join()
```

**Cost:** expensive to create (~milliseconds), heavy memory overhead (each process has its own Python interpreter).

---

### Thread

A **thread** is a unit of execution within a process. Multiple threads share the same memory space — they can read and write the same variables.

**Communication between threads:** shared variables (but this is dangerous — see race conditions below).

```python
import threading

def worker(n):
    print(f"Thread {n} running")

t = threading.Thread(target=worker, args=(1,))
t.start()
t.join()
```

**Cost:** cheap to create (~microseconds), share memory with the parent process.

---

### Key difference

| | Process | Thread |
|---|---|---|
| Memory | Isolated (own copy) | Shared |
| Communication | IPC (queues, pipes) | Shared variables |
| Creation cost | Expensive | Cheap |
| Crash isolation | Crash doesn't affect others | Crash can kill all threads |
| Python parallelism | True parallelism | Limited by GIL |

---

## The GIL (Global Interpreter Lock)

This is the most misunderstood Python concept.

### What it is

The **GIL** is a mutex (lock) inside the CPython interpreter. It ensures that **only one thread executes Python bytecode at a time**, even on a multi-core machine.

### What it means

```python
# You have 4 CPU cores. You create 4 threads doing CPU work.
# You expect 4x speedup.
# You get ~1x — because only one thread runs at a time.
```

**"Python can't multithread"** is misleading. Python CAN have multiple threads. They just can't run Python code simultaneously.

### What the GIL doesn't prevent

The GIL releases during **I/O operations** (network calls, file reads, database queries). While one thread is waiting for a network response, another thread can run.

So threads ARE useful for I/O-bound work:
- Making HTTP requests
- Reading files
- Querying a database
- Waiting for user input

### The rule

| Workload | Use |
|---|---|
| CPU-bound (computation, image processing, ML) | `multiprocessing` — true parallelism |
| I/O-bound (HTTP, DB, file) | `threading` or `asyncio` — concurrency |

---

## Race conditions

A **race condition** occurs when two threads access shared data simultaneously and the final result depends on the order of execution.

### Example — bank balance

```python
import threading

balance = 1000

def withdraw(amount):
    global balance
    current = balance       # step 1: read
    current -= amount       # step 2: subtract
    balance = current       # step 3: write

t1 = threading.Thread(target=withdraw, args=(100,))
t2 = threading.Thread(target=withdraw, args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)  # Should be 800. Might be 900.
```

### Why it goes wrong

```
Thread 1: reads balance = 1000
Thread 2: reads balance = 1000   ← before Thread 1 wrote back!
Thread 1: writes balance = 900
Thread 2: writes balance = 900   ← overwrites Thread 1's result!
Final balance: 900 (lost one withdrawal)
```

This is called a **lost update**. One withdrawal was silently ignored.

The problem: **read-modify-write** is not atomic. Three separate steps can be interleaved by the scheduler.

---

## Locks

A **lock** (mutex) ensures only one thread can execute a section of code at a time.

```python
import threading

balance = 1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:              # acquire lock — other threads block here
        current = balance   # safe: only one thread here at a time
        current -= amount
        balance = current
    # lock released automatically by context manager

t1 = threading.Thread(target=withdraw, args=(100,))
t2 = threading.Thread(target=withdraw, args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)  # Always 800
```

**`with lock:`** is a context manager. It acquires the lock on entry and releases it on exit — even if an exception occurs.

The protected section is called a **critical section**.

---

## Deadlocks

A **deadlock** occurs when two threads each hold a lock the other needs, and both are waiting forever.

```python
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    with lock_a:
        time.sleep(0.1)  # give thread_2 time to acquire lock_b
        with lock_b:     # waits for thread_2 to release lock_b
            print("Thread 1 done")

def thread_2():
    with lock_b:
        time.sleep(0.1)  # give thread_1 time to acquire lock_a
        with lock_a:     # waits for thread_1 to release lock_a
            print("Thread 2 done")
```

```
Thread 1 holds lock_a, waiting for lock_b
Thread 2 holds lock_b, waiting for lock_a
Both wait forever → deadlock
```

### How to avoid deadlocks

1. **Always acquire locks in the same order** — if all threads acquire `lock_a` before `lock_b`, deadlock is impossible
2. **Keep critical sections small** — hold locks for the shortest time possible
3. **Use timeouts** — `lock.acquire(timeout=1.0)` returns `False` instead of blocking forever

---

## Thread pools

Creating a thread per request doesn't scale. Use a **thread pool** — a fixed number of reusable worker threads.

```python
from concurrent.futures import ThreadPoolExecutor

def process_request(n):
    return n * 2

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(process_request, i) for i in range(10)]
    results = [f.result() for f in futures]

print(results)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**`ThreadPoolExecutor`** manages the pool. `submit()` queues work. `result()` blocks until the task completes.

---

## Summary: The mental model

```
One request → one thread (or coroutine)
Shared state → protected by a lock
CPU-bound work → multiprocessing
I/O-bound work → threading or asyncio
```

**In LedgerFlow:** every transfer request touches the same account balances. Without locks (or database-level locking), two simultaneous transfers from the same account will corrupt data. This is exactly what you'll implement in M2.

---

**Read this primer carefully — especially the race condition section. When you're done, come back and we'll reproduce a race condition live, then fix it.**
