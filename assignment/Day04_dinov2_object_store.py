"""
Day 04 · 🔧 Build + Milvus — DINOv2 Object Store
TASK:    Encode SAM-segmented object crops with DINOv2. Store in Milvus. Query: find similar objects.
OUTCOME: A working Milvus operation for Milvus — DINOv2 Object Store.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day04_dinov2_object_store.py     (or just:  python Day04_dinov2_object_store.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: add SAM/ViT segmentation to turn frames into structured observations.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day04.md
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

def store_objects(client):
    """TODO 1: Create collection 'objects' and insert EXAMPLE_VECTORS (stand-ins for DINOv2 crop embeddings). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_objects() not written yet")


def find_similar_objects(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k object crops most similar to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_similar_objects() not written yet")


# ════ TESTS — run `pytest Day04_dinov2_object_store.py` (or `python Day04_dinov2_object_store.py`). All green = you're done. ════

def test_store_count():
    c = fresh_client()
    assert store_objects(c) == N

def test_find_self():
    c = fresh_client(); store_objects(c)
    ids = list(find_similar_objects(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
