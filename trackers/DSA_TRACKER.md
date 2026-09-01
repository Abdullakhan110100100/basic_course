# DSA Tracker

Target ~100–120 curated problems across 24 weeks. Optimize for **pattern recognition**, not count. Loop: Attempt (30–35 min) → analyze → hint if needed → solve → explain → **re-solve in 2–3 days and again in weeks**. If you saw the solution, it's scheduled for an independent re-attempt.

> **DSA is rusty (2026-08-24) and front-loaded** — the biggest risk to the 6–8 month cap. Hours: **Wk 1–4 = 5 h/wk** (rebuild fundamentals thoroughly), **Wk 5–21 = 3 h/wk**, **Wk 22–24 = ~5 h/wk** (timed mocks). If pattern recognition isn't landing by ~Wk 6, we bump hours again and/or extend the ramp — and I'll say so. Watching a solution ≠ solving it.

## Pattern mastery
| Pattern | Weeks | Status (Weak / Developing / Solid) | Re-solve due |
|---|---|---|---|
| Arrays & hashing | 1–2 (front-loaded, 5 h/wk) | Developing→Solid | 2026-09-08 |
| Two pointers / sliding window | 3–4 (front-loaded, 5 h/wk) | Not started | — |
| Stack / queue / linked lists | 5–6 | Not started | — |
| Binary search / intervals | 7–8 | Not started | — |
| Trees / BST | 9–10 | Not started | — |
| Heaps | 11–12 | Not started | — |
| Graphs / BFS / DFS | 13–14 | Not started | — |
| Topological sort / union-find | 15–16 | Not started | — |
| Recursion / backtracking | 17–18 | Not started | — |
| Greedy | 19 | Not started | — |
| Dynamic programming | 20–21 | Not started | — |
| Mixed timed mocks + weak-area repair | 22–24 | Not started | — |

## Problem log
| # | Problem | Pattern | First attempt | Result (unaided / hinted / saw solution) | Re-solve 1 | Re-solve 2 |
|---|---------|---------|---------------|------------------------------------------|-----------|-----------|
| 1 | Contains Duplicate (LC 217) | Arrays & hashing | 2026-08-27 | Unaided — solved set+len approach first, then iterated to early-exit version with hint | 2026-08-30 | — |
| 2 | Valid Anagram (LC 242) | Arrays & hashing | 2026-08-27 | Unaided — freq dict correct; missed KeyError on unseen char (self-fixed); good Unicode follow-up | 2026-08-30 | — |
| 3 | Two Sum (LC 1) | Arrays & hashing | 2026-08-27 | Partial — O(n²) first; hash map needed iterations (.values() bug, overwrite bug, check-before-add insight); final solution clean | 2026-08-30 | — |
| 4 | Group Anagrams (LC 49) | Arrays & hashing | 2026-08-27 | Partial — O(n²·k) nested loops first (bug: == vs =, self-fixed); H1 hint → sorting solution O(n·k log k) correct; H1-H2 hints → frequency tuple O(n·k) with off-by-one bug (self-fixed); key insight: engineering tradeoff simple vs optimal | 2026-08-30 | — |
| 5 | Product of Array Except Self (LC 238) | Arrays & hashing | 2026-08-27 | Partial — O(n) time O(n) space prefix+suffix arrays correct first try; H1 hint → O(1) space optimization (reuse answer array, running suffix variable); key insight: values needed immediately vs later determines storage | 2026-08-30 | — |
