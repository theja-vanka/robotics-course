"""
Day 18 · 🔧 Build + Milvus — World Model State Memory
TASK:    Store RSSM belief vectors in Milvus. Retrieve similar past states to warm-start planning.
OUTCOME: A working Milvus operation for Milvus — World Model State Memory.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day18_world_model_state_memory.py     (or just:  python Day18_world_model_state_memory.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  World models + Jetson context → fixes your deploy target and latency budget.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day18.md
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

def store_beliefs(client):
    """TODO 1: Create collection 'beliefs' and insert EXAMPLE_VECTORS (stand-ins for RSSM belief states). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_beliefs() not written yet")


def similar_states(client, state=QUERY, k=5):
    """TODO 2: Return ids of the k stored states most similar to `state` (to warm-start planning)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: similar_states() not written yet")


# ════ TESTS — run `pytest Day18_world_model_state_memory.py` (or `python Day18_world_model_state_memory.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_beliefs(c) == N

def test_similar_self():
    c = fresh_client(); store_beliefs(c)
    ids = list(similar_states(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
