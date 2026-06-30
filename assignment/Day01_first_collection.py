"""
Day 01 · 🔧 Build + Milvus — First Collection
TASK:    Install Milvus via Docker, connect pymilvus, create collection, insert dummy vectors, run search.
OUTCOME: A working Milvus operation for Milvus — First Collection.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day01_first_collection.py     (or just:  python Day01_first_collection.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Stub the vla-edge repo + env; get SmolVLA running on one sample observation.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day01.md
Setup:  pip install pymilvus numpy scikit-learn pytest
"""
from __future__ import annotations

import os
from sklearn.datasets import load_digits   # OPEN dataset: 1797 handwritten digits (64-d), bundled with scikit-learn
from pymilvus import MilvusClient

_DIGITS = load_digits()
EXAMPLE_VECTORS = _DIGITS.data.astype("float32")   # (1797, 64) REAL vectors — nothing to provide
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

def create_collection(client):
    """TODO 1: Create a collection named 'demo' with a vector field of dimension DIM (=64 for this dataset)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_collection() not written yet")


def insert_vectors(client):
    """TODO 2: Insert all EXAMPLE_VECTORS (N=1797 digit vectors, ids 0..N-1) into 'demo'. Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: insert_vectors() not written yet")


def run_search(client):
    """TODO 3: Search 'demo' for QUERY (the first digit) with limit=5. Return the list of result ids (length 5)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: run_search() not written yet")


# ════ TESTS — run `pytest Day01_first_collection.py` (or `python Day01_first_collection.py`). All green = you're done. ════

def test_insert_count():
    c = fresh_client(); create_collection(c)
    assert insert_vectors(c) == N, f"should insert all {N} vectors"

def test_search_finds_itself():
    c = fresh_client(); create_collection(c); insert_vectors(c)
    ids = list(run_search(c))
    assert len(ids) == 5, f"top-5 expected, got {len(ids)}"
    assert ids[0] == 0, "the nearest neighbour of vector 0 (the query) must be itself (id 0)"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
