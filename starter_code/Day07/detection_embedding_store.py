"""
Day 07 · 🔧 Build + Milvus — Detection Embedding Store
TASK:    After each detection, extract RoI → embed with CLIP → upsert into Milvus with class label. Build 'seen objects' index.
OUTCOME: A working Milvus operation for Milvus — Detection Embedding Store.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest detection_embedding_store.py     (or just:  python detection_embedding_store.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: plug in YOLO26 detection → an object list the policy can use.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day07.md
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


def create_seen_index(client):
    """TODO 1: Create collection 'seen_objects' with a vector field (dim DIM) plus an int64 'label' field."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_seen_index() not written yet")


def upsert_detection(client, vec, label):
    """TODO 2: Upsert one detection (its RoI embedding + class label). Return the new total entity count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: upsert_detection() not written yet")


def query_seen(client, query=QUERY, k=5):
    """TODO 3: Return (ids, labels) of the k nearest seen objects to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: query_seen() not written yet")


# ════ TESTS — run `pytest detection_embedding_store.py` (or `python detection_embedding_store.py`). All green = you're done. ════


def test_upsert_grows():
    c = fresh_client()
    create_seen_index(c)
    n1 = upsert_detection(c, EXAMPLE_VECTORS[0], 3)
    n2 = upsert_detection(c, EXAMPLE_VECTORS[1], 7)
    assert n2 > n1, "each detection grows the 'seen objects' index"


def test_query_returns_labels():
    c = fresh_client()
    create_seen_index(c)
    upsert_detection(c, EXAMPLE_VECTORS[0], 3)
    ids, labels = query_seen(c, EXAMPLE_VECTORS[0], 5)
    assert len(ids) >= 1 and len(labels) == len(ids)


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
