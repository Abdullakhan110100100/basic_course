# Project 2 — SearchLab (Intelligent Search & Recommendation Engine)

**Purpose:** demonstrate **information retrieval + AI engineering without building another chatbot.**
**Domain:** e-commerce / search. **Output = ranked products, not prose.**
**Runs across Phase 4 (Weeks 13–17).**

> **Design ownership:** decisions captured as ADRs — which vector index, how hybrid scores are fused (weighted vs RRF), which reranker, chunking/field strategy, evaluation-set construction.

---

## Core concept

Use a realistic public product dataset (fields such as title, description, brand, category, price, attributes, rating, availability). Users query e.g. *"lightweight black running shoes under ₹6000"*. The system returns a **ranked list of products**.

---

## Stages

1. **Lexical search.** Tokenization, inverted index, term frequency, IDF, TF-IDF intuition, **BM25**. Implement a **simplified inverted index + BM25 by hand once** — understanding is the goal; a real search library/engine can replace it later.
2. **Dense retrieval.** Embedding generation, cosine similarity, dot product, vector indexing, ANN, **HNSW intuition**. Compare against BM25 and **discover through evaluation that semantic search is not universally better.**
3. **Hybrid search.** Combine BM25 + dense; experiment with **weighted scoring** and **Reciprocal Rank Fusion (RRF)**; measure both.
4. **Reranking.** `Query → candidate retrieval → hybrid fusion → reranker → final ranking`. Measure **relevance and latency** changes.
5. **Evaluation.** Build a labeled dataset (~100–500 queries) with relevance judgments. Implement **Precision@K, Recall@K, Hit Rate, MRR, NDCG.** Require actual experiments.
6. **Ranking features.** Signals beyond text relevance — popularity, rating, price, availability, user preference. Teach the difference between **retrieval** and **ranking**.
7. **Recommendations (if time).** Similar products, light personalized ranking, interaction history. Don't let this distract from retrieval mastery.

---

## Benchmark table (measured — no invented numbers)

| Approach | Recall@10 | MRR | NDCG@10 | p95 latency |
|---|---|---|---|---|
| BM25 | measured | measured | measured | measured |
| Dense | measured | measured | measured | measured |
| Hybrid | measured | measured | measured | measured |
| Hybrid + reranking | measured | measured | measured | measured |

---

## Final learning outcomes (defend at Level 4)

Inverted indexes · BM25 (math + intuition; document-length normalization; k1/b) · embeddings · vector search · ANN/HNSW · hybrid retrieval · RRF · reranking · search evaluation metrics · ranking vs retrieval · latency/relevance trade-offs · experiment design.

**Resume tie-in:** directly builds my ability to defend the Fynd "hybrid retrieval (vector + BM25 + reranking)" claim with real numbers (see `../../CLAUDE.md`).
