# Weakness Ledger

Every misconception, repeated mistake, weak explanation, cargo-culted choice, missed failure mode, or poorly-answered interview question lands here — and does **not** disappear when the week changes. It leaves only when mastery is later demonstrated (record the evidence).

Columns: **ID · Topic · Date found · Type** (misconception / terminology / DSA-pattern / architecture / assumption / weak-explanation / code-quality / prod-failure-mode / interview) · **Severity** (Critical / Significant / Minor) · **Current mastery** (1–4) · **Review date** · **Status**.

| ID | Topic | Date found | Type | Severity | Mastery | Review date | Status |
|----|-------|-----------|------|----------|---------|-------------|--------|
| W001 | Aliasing: initially thought `b=a` doesn't affect `a` after mutation | 2026-08-14 | misconception | Significant | 3 | — | **Resolved** 2026-08-27 — answered correctly unaided |
| W002 | Mutable default args: believed a fresh list is created each call | 2026-08-14 | misconception | Significant | 3 | — | **Resolved** 2026-08-27 — answered correctly unaided |
| W003 | Shallow vs deep copy: conflated `c[:]` with deep copy | 2026-08-14 | terminology | Minor | 3 | **2026-08-30** | Open — regression caught 2026-08-27, self-corrected; one more round |
| W004 | `None` sentinel pattern: did not know it; needed L5 hint | 2026-08-14 | misconception | Minor | 3 | — | **Resolved** 2026-08-27 — wrote safe version unaided, explained `is` vs `==` correctly |

## Resolved (kept for history)
_(none yet)_

> Note: review dates predate the 2026-08-24 redesign; all four are now overdue and should be surfaced (as ambushes, not announced) at the next session. On successful unaided reproduction, mark Resolved with evidence and stop scheduling.
