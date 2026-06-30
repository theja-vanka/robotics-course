"""
Day 06 · 🔧 Build + Milvus — Scene Retrieval Service
TASK:    Build SceneRetriever class: encode frame with CLIP → query Milvus → return top-5 similar scenes.
OUTCOME: A working Milvus operation for Milvus — Scene Retrieval Service.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day06_scene_retrieval_service.py     (or just:  python Day06_scene_retrieval_service.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Draft observe.py architecture — the perception front-end of your policy.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day06.md
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

def index_scenes(client):
    """TODO 1: Create collection 'scenes' and insert EXAMPLE_VECTORS (stand-ins for CLIP frame embeddings). Return the count. (In the capstone, wrap index_scenes + retrieve into a SceneRetriever class.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_scenes() not written yet")


def retrieve(client, query=QUERY, k=5):
    """TODO 2: Return the ids of the top-k scenes most similar to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: retrieve() not written yet")


# ════ TESTS — run `pytest Day06_scene_retrieval_service.py` (or `python Day06_scene_retrieval_service.py`). All green = you're done. ════

def test_indexed():
    c = fresh_client()
    assert index_scenes(c) == N

def test_retrieve_topk():
    c = fresh_client(); index_scenes(c)
    ids = list(retrieve(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
