"""
Day 02 · 🔧 Build + Milvus — Store CLIP Embeddings
TASK:    Encode 100 robot images with CLIP. Insert 512-d vectors. Run similarity search. Log top-5.
OUTCOME: A working Milvus operation for Milvus — Store CLIP Embeddings.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest store_clip_embeddings.py     (or just:  python store_clip_embeddings.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Add CLIP→Milvus retrieval over observations (the policy's memory).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day02.md
Setup:  pip install pymilvus numpy transformers torch pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from pymilvus import MilvusClient  # noqa: F401  — you'll use this inside the functions below
from helpers.milvus import fresh_client
from helpers.embeddings import clip_bridge_embeddings

# Real CLIP ViT-B/32 embeddings of BridgeData V2 robot scenes (WidowX arm), computed once and
# cached to starter_code/clip_bridge_embeddings.npy.  (See helpers/embeddings.py.)
EXAMPLE_VECTORS, QUERY, DIM, N = clip_bridge_embeddings()   # (200, 512)



# ════ FILL IN — each function raises until you write it ════

def build_image_index(client):
    """TODO 1: Create collection 'clip_images' (vector dim DIM) and insert the FIRST 100 EXAMPLE_VECTORS — these stand in for 100 CLIP image embeddings. Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_image_index() not written yet")


def search_similar(client, query=QUERY, k=5):
    """TODO 2: Return the ids of the k most similar images to `query` (your top-5 log)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: search_similar() not written yet")


# ════ TESTS — run `pytest store_clip_embeddings.py` (or `python store_clip_embeddings.py`). All green = you're done. ════

def test_indexed_100():
    c = fresh_client()
    assert build_image_index(c) == 100, "should index exactly the 100 image embeddings"

def test_topk_self():
    c = fresh_client(); build_image_index(c)
    ids = list(search_similar(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0, "image 0 must be its own nearest neighbour"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
