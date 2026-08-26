# Course State Snapshot (resumable checkpoint)

> Read this FIRST every session. Update it LAST every session. If lost, this is how we resume without inventing progress.

**Last updated:** 2026-08-24 (Redesign → focused SDE-2 Backend + AI Engineer program)

## Continuity header
- **Phase:** 1 — SDE-2 Core Foundations
- **Week:** 1 → transitioning to Week 2
- **Lesson:** 1 — **COMPLETE** (object model, mutability, aliasing, mutable defaults, shallow/deep copy, iterators, generators, context managers, decorators incl. parametrized)
- **Project:** LedgerFlow — milestone **M0** (repo scaffold + `/accounts` API), not started; begin this week
- **Current milestone:** start Week 2 (typing, protocols, exceptions, concurrency I) + kick off LedgerFlow M0 scaffold
- **Revision due:** W001 ✓, W002 ✓, W004 ✓ (all passed unaided 2026-08-27); W003 — regression caught and self-corrected, re-queue in ~3 days (due ~2026-08-30)
- **DSA focus:** Weeks 1–2 = Arrays & Hashing (not started — must begin)

## What changed in the redesign (2026-08-24)
Replaced the broad 6-role / 6-project / 28-week course with a **focused 2-role / 3-project / 24-week** program (SDE-2 Backend + AI Engineer). Old files archived in `../archive/2026-08-24_broad-28week-course/`. **Carried forward:** Python object-model + mutability mastery (Level 3), weaknesses W001–W004, their revision schedule. New projects: **LedgerFlow** (Ph 1–3), **SearchLab** (Ph 4), **RepoPilot** (Ph 5). See `../instructions.md` §A for the three amendments (craft track, two-track expectation, LedgerFlow milestones).

## Where we are in the lesson
Lesson 1 **complete** (2026-08-27). All topics covered: object model, mutability, aliasing, mutable defaults, `is None`, shallow/deep copy, iterator protocol, generators, context managers (`__enter__`/`__exit__`, `@contextmanager`, `try/finally`), decorators and parametrized decorators with `@wraps`.

**Next action when resuming:** Week 2 — Typing, protocols, exceptions, packaging; then Concurrency I (processes, threads, GIL, race conditions, locks). Also: **start LedgerFlow M0** (repo scaffold + tooling gates + FastAPI skeleton). DSA Arrays & Hashing must begin.

**Process change (2026-08-27):** Primer files written to `course/notes/week_N/lesson_N_title/` before each new topic; grilling happens after reading. Retrieval-first still applies for revision of old material.

## Learner profile (fixed context)
- Abdulla Khan, Software Engineer ~2.5 YOE, Bangalore. Currently at Fynd.
- Target: **SDE-2 Backend + Applied AI Engineer** ("backend SDE-2 who specializes in reliable AI systems"). Commit: 15 hrs/week.
- **Lead track: BACKEND-FIRST** (confirmed 2026-08-24, reversible). AI hardens in the tail.
- **DSA: rusty** (learner's own words) → **front-loaded** (see timeline note + `DSA_TRACKER.md`). Biggest risk to the timeline.
- System-design baseline: TBD (ask when convenient).

## Working timeline & expectation (agreed 2026-08-24)
- **No fixed interview date; hard cap ~6–8 months.**
- Realistic ~7-month outcome under this cap: **backend SDE-2 strong/interview-capable + AI Engineer interview-capable** (NOT both "strong" simultaneously — see `../instructions.md` §A-2).
- **Deal:** hold ≥13 hrs/wk actually logged; front-load DSA vs the rust; accept the lead/secondary split. If sustained hours drift to 8–9, flag that we're off the 6–8 month track *that week*, not at month 7.
- **DSA hour rebalance (total stays 15/wk):** Wk 1–4 DSA 5h / Concepts 3 / Projects 4 / debug 2 / review 1. Wk 5–21 back to DSA 3 / Projects 6. Wk 22–24 DSA ~5 (mocks).

## Open items / to ask the learner
1. Confirm local setup: Python 3.11+, Docker available, editor. (Needed before LedgerFlow M0 *build*, not before Lesson 1 teaching.)
2. System-design self-rating (1–10) — when convenient.
3. Where should the portfolio repo `engineering-systems-lab/` live (sibling dir vs new GitHub repo)?
4. Product dataset preference for SearchLab (Phase 4) — decide by Week 12.
