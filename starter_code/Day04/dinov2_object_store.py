"""
Day 04 · 🔧 Build + Milvus — DINOv2 Object Store
TASK:    Encode SAM-segmented object crops with DINOv2. Store in Milvus. Query: find similar objects.
OUTCOME: A working Milvus operation for Milvus — DINOv2 Object Store.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest dinov2_object_store.py     (or just:  python dinov2_object_store.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: add SAM/ViT segmentation to turn frames into structured observations.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day04.md
Setup:  pip install pymilvus numpy transformers torch pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from pymilvus import MilvusClient  # noqa: F401
from helpers.milvus import fresh_client
from helpers.embeddings import dinov2_bridge_embeddings

# Real DINOv2-base CLS features of BridgeData V2 robot scenes → 768-d vectors, cached to
# starter_code/dinov2_bridge_embeddings.npy.  In production feed SAM-segmented object crops.
EXAMPLE_VECTORS, QUERY, DIM, N = dinov2_bridge_embeddings()   # (200, 768)



# ════ FILL IN — each function raises until you write it ════

def store_objects(client):
    """TODO 1: Create collection 'objects' (vector dim DIM=768) and insert EXAMPLE_VECTORS — real DINOv2 CLS features of BridgeData V2 robot scene crops. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_objects() not written yet")


def find_similar_objects(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k object crops most similar to `query` (your SAM-segmented object lookup)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_similar_objects() not written yet")


# ════ TESTS — run `pytest dinov2_object_store.py` (or `python dinov2_object_store.py`). All green = you're done. ════

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
