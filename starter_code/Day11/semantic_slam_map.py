"""
Day 11 · 🔧 Build + Milvus — Semantic SLAM Map
TASK:    Store SLAM keyframe position + CLIP embedding in Milvus. Query: find all keyframes showing the red mug.
OUTCOME: A working Milvus operation for Milvus — Semantic SLAM Map.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest semantic_slam_map.py     (or just:  python semantic_slam_map.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  SLAM — awareness only, don't build. It's the 'where am I' layer, noted for context.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day11.md
Setup:  pip install "pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
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

def store_keyframes(client):
    """TODO 1: Create collection 'keyframes' and insert EXAMPLE_VECTORS, each with a dummy (x,y,z) position in a dynamic field 'pos'. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_keyframes() not written yet")


def find_similar_keyframes(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k keyframes whose scene embedding is closest to `query` (loop-closure candidates)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_similar_keyframes() not written yet")


# ════ TESTS — run `pytest semantic_slam_map.py` (or `python semantic_slam_map.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_keyframes(c) == N

def test_find_self():
    c = fresh_client(); store_keyframes(c)
    ids = list(find_similar_keyframes(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
