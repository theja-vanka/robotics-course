"""
Day 09 · 🔧 Build + Milvus — Object Pose Library
TASK:    Store template embeddings + known poses. At inference: embed crop → find nearest template → retrieve pose.
OUTCOME: A working Milvus operation for Milvus — Object Pose Library.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day09_object_pose_library.py     (or just:  python Day09_object_pose_library.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  6-DoF pose — optional observation enrichment; awareness-level for your target.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day09.md
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

def build_pose_library(client):
    """TODO 1: Create collection 'templates' and insert EXAMPLE_VECTORS, each with a dummy 7-float pose stored alongside (a dynamic field 'pose'). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_pose_library() not written yet")


def lookup_pose(client, query=QUERY):
    """TODO 2: Find the nearest template to `query` and return its stored 7-float pose."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: lookup_pose() not written yet")


# ════ TESTS — run `pytest Day09_object_pose_library.py` (or `python Day09_object_pose_library.py`). All green = you're done. ════

def test_library_built():
    c = fresh_client()
    assert build_pose_library(c) == N

def test_lookup_returns_pose():
    c = fresh_client(); build_pose_library(c)
    p = lookup_pose(c, EXAMPLE_VECTORS[0])
    assert p is not None and len(p) == 7, "should return the matched template's 7-DoF pose"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
