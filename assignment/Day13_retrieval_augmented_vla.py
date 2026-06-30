"""
Day 13 · 🔧 Build + Milvus — Retrieval-Augmented VLA
TASK:    Store robot demo trajectories as embeddings. At inference: encode observation → retrieve top-3 demos → prepend as context.
OUTCOME: A working Milvus operation for Milvus — Retrieval-Augmented VLA.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day13_retrieval_augmented_vla.py     (or just:  python Day13_retrieval_augmented_vla.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ⭐ policy.py: understand the VLA you'll fine-tune (action tokens, VLM backbone).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day13.md
Setup:  pip install pymilvus numpy scikit-learn pytest
"""
from __future__ import annotations

import os
from sklearn.datasets import load_digits   # OPEN dataset: 1797 handwritten digits (64-d), bundled with scikit-learn
from pymilvus import MilvusClient

_DIGITS = load_digits()
EXAMPLE_VECTORS = _DIGITS.data.astype("float32")   # (1797, 64) REAL vectors stand in for your embeddings
QUERY = EXAMPLE_VECTORS[0]
DIM = EXAMPLE_VECTORS.shape[1]   # 64
N = len(EXAMPLE_VECTORS)         # 1797

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    if os.path.exists("milvus_demo.db"):
        os.remove("milvus_demo.db")
    return MilvusClient("milvus_demo.db")

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def index_demos(client):
    """TODO 1: Create collection 'demos' and insert EXAMPLE_VECTORS (stand-ins for demo-trajectory embeddings). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_demos() not written yet")


def retrieve_demos(client, observation=QUERY, k=3):
    """TODO 2: Return ids of the k demos most similar to `observation` — the context you feed the VLA."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: retrieve_demos() not written yet")


# ════ TESTS — run `pytest Day13_retrieval_augmented_vla.py` (or `python Day13_retrieval_augmented_vla.py`). All green = you're done. ════

def test_indexed():
    c = fresh_client()
    assert index_demos(c) == N

def test_retrieve_k():
    c = fresh_client(); index_demos(c)
    ids = list(retrieve_demos(c, EXAMPLE_VECTORS[0], 3))
    assert len(ids) == 3 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
