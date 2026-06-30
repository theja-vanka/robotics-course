"""
Day 10 · 🔧 Build + Milvus — Grasp Pose Library
TASK:    Store (object embedding + grasp config) pairs. Query: given new object, retrieve most similar past grasp.
OUTCOME: A working Milvus operation for Milvus — Grasp Pose Library.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day10_grasp_pose_library.py     (or just:  python Day10_grasp_pose_library.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Grasp detection — awareness; see how a policy's action could ground to a grasp.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day10.md
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

def store_grasps(client):
    """TODO 1: Create collection 'grasps' and insert EXAMPLE_VECTORS, each paired with a dummy 7-float grasp config (x,y,z,qx,qy,qz,width) in a dynamic field 'grasp'. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_grasps() not written yet")


def retrieve_grasp(client, query=QUERY):
    """TODO 2: Return the grasp config of the most similar stored object to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: retrieve_grasp() not written yet")


# ════ TESTS — run `pytest Day10_grasp_pose_library.py` (or `python Day10_grasp_pose_library.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_grasps(c) == N

def test_retrieve_grasp():
    c = fresh_client(); store_grasps(c)
    g = retrieve_grasp(c, EXAMPLE_VECTORS[0])
    assert g is not None and len(g) == 7


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
