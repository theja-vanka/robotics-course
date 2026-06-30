"""
Day 12 · 🔧 Build + Milvus — Pipeline + Milvus Integration
TASK:    Wire all pipeline stages into main.py. Every detection/pose result upserted into Milvus. Smoke test.
OUTCOME: A working Milvus operation for Pipeline + Milvus Integration.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day12_pipeline_milvus_integration.py     (or just:  python Day12_pipeline_milvus_integration.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Wire observe.py end-to-end + run your first baseline pass (the 'before' number).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day12.md
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

def create_results_store(client):
    """TODO 1: Create collection 'pipeline_results' with a vector field (dim DIM) plus a string field 'stage'."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_results_store() not written yet")


def log_result(client, vec, stage):
    """TODO 2: Upsert one pipeline result tagged with its stage ('detect'/'pose'/...). Return the new entity count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: log_result() not written yet")


def query_recent(client, query=QUERY, k=5):
    """TODO 3: Return ids of the k logged results most similar to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: query_recent() not written yet")


# ════ TESTS — run `pytest Day12_pipeline_milvus_integration.py` (or `python Day12_pipeline_milvus_integration.py`). All green = you're done. ════

def test_logging_grows():
    c = fresh_client(); create_results_store(c)
    n1 = log_result(c, EXAMPLE_VECTORS[0], "detect")
    n2 = log_result(c, EXAMPLE_VECTORS[1], "pose")
    assert n2 > n1

def test_query_recent():
    c = fresh_client(); create_results_store(c)
    log_result(c, EXAMPLE_VECTORS[0], "detect")
    assert len(list(query_recent(c, EXAMPLE_VECTORS[0], 1))) >= 1


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
