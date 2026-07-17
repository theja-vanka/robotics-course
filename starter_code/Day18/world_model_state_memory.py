"""
Day 18 · 🔧 Build + Milvus — World Model State Memory
TASK:    Store RSSM belief vectors in Milvus. Retrieve similar past states to warm-start planning.
OUTCOME: A working Milvus operation for Milvus — World Model State Memory.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest world_model_state_memory.py     (or just:  python world_model_state_memory.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  World models + Jetson context → fixes your deploy target and latency budget.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day18.md
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

def store_beliefs(client):
    """TODO 1: Create collection 'beliefs' and insert EXAMPLE_VECTORS (stand-ins for RSSM belief states). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_beliefs() not written yet")


def similar_states(client, state=QUERY, k=5):
    """TODO 2: Return ids of the k stored states most similar to `state` (to warm-start planning)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: similar_states() not written yet")


# ════ TESTS — run `pytest world_model_state_memory.py` (or `python world_model_state_memory.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_beliefs(c) == N

def test_similar_self():
    c = fresh_client(); store_beliefs(c)
    ids = list(similar_states(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
