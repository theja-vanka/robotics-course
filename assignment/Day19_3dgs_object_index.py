"""
Day 19 · 🔧 Build + Milvus — 3DGS Object Index
TASK:    Compute shape descriptor per Gaussian cluster. Store in Milvus. Query: given new scene, retrieve similar past object + known grasp.
OUTCOME: A working Milvus operation for Milvus — 3DGS Object Index.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day19_3dgs_object_index.py     (or just:  python Day19_3dgs_object_index.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ⭐ compress.py: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day19.md
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

def store_descriptors(client):
    """TODO 1: Create collection 'shapes' and insert EXAMPLE_VECTORS (per-Gaussian-cluster shape descriptors). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_descriptors() not written yet")


def match_objects(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k stored shapes matching `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: match_objects() not written yet")


# ════ TESTS — run `pytest Day19_3dgs_object_index.py` (or `python Day19_3dgs_object_index.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_descriptors(c) == N

def test_match_self():
    c = fresh_client(); store_descriptors(c)
    ids = list(match_objects(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
