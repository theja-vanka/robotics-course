"""
Day 01 · 🔧 Build + Milvus — First Collection
TASK:    Install Milvus via Docker, connect pymilvus, create collection, insert dummy vectors, run search.
OUTCOME: A working Milvus operation for Milvus — First Collection.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest first_collection.py     (or just:  python first_collection.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Stub the vla-edge repo + env; get SmolVLA running on one sample observation.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day01.md
Setup:  pip install pymilvus numpy transformers torch pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from helpers.embeddings import clip_bridge_embeddings
from helpers.milvus import fresh_client
from pymilvus import (
    MilvusClient,  # noqa: F401  — you'll use this inside the functions below
)

# Real CLIP ViT-B/32 embeddings of BridgeData V2 robot scenes (WidowX arm), computed once and
# cached to starter_code/clip_bridge_embeddings.npy.  (See helpers/embeddings.py.)
EXAMPLE_VECTORS, QUERY, DIM, N = clip_bridge_embeddings()  # (200, 512)


# ════ FILL IN — each function raises until you write it ════


def create_collection(client):
    """TODO 1: Create a collection named 'demo' with a vector field of dimension DIM (=512)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_collection() not written yet")


def insert_vectors(client):
    """TODO 2: Insert all EXAMPLE_VECTORS (N=200 CLIP robot-scene embeddings, ids 0..N-1) into 'demo'. Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: insert_vectors() not written yet")


def run_search(client):
    """TODO 3: Search 'demo' for QUERY (the first robot scene embedding) with limit=5. Return the list of result ids (length 5)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: run_search() not written yet")


# ════ TESTS — run `pytest first_collection.py` (or `python first_collection.py`). All green = you're done. ════


def test_insert_count():
    c = fresh_client()
    create_collection(c)
    assert insert_vectors(c) == N, f"should insert all {N} vectors"


def test_search_finds_itself():
    c = fresh_client()
    create_collection(c)
    insert_vectors(c)
    ids = list(run_search(c))
    assert len(ids) == 5, f"top-5 expected, got {len(ids)}"
    assert ids[0] == 0, (
        "the nearest neighbour of vector 0 (the query) must be itself (id 0)"
    )


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
