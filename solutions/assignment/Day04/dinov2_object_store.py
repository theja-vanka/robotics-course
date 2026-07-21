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
Setup:  pip install "pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from helpers.embeddings import dinov2_bridge_embeddings
from helpers.milvus import fresh_client
from pymilvus import MilvusClient  # noqa: F401

# Real DINOv2-base CLS features of BridgeData V2 robot scenes → 768-d vectors, cached to
# starter_code/dinov2_bridge_embeddings.npy.  In production feed SAM-segmented object crops.
EXAMPLE_VECTORS, QUERY, DIM, N = dinov2_bridge_embeddings()  # (200, 768)


# ════ FILL IN — each function raises until you write it ════


def store_objects(client):
    """TODO 1: Create collection 'objects' (vector dim DIM=768) and insert EXAMPLE_VECTORS — real DINOv2 CLS features of BridgeData V2 robot scene crops. Return the count."""
    # 👇 write your code here, then DELETE the line below
    import time

    collection_name = "objects"
    if client.has_collection(collection_name):
        client.drop_collection(collection_name)

    client.create_collection(
        collection_name=collection_name,
        dimension=DIM,
        primary_field_name="id",
        vector_field_name="embeddings",
        auto_id=False,
        enable_dynamic_field=True,
    )

    data = [
        {
            "id": i,
            "embeddings": vector,
            "dataset": "digits",
        }
        for i, vector in enumerate(EXAMPLE_VECTORS[:200].tolist())
    ]

    result = client.insert(
        collection_name=collection_name,
        data=data,
    )
    time.sleep(2)  # wait for Milvus to finish inserting
    return len(result["ids"])
    # raise NotImplementedError("Step 1: store_objects() not written yet")


def find_similar_objects(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k object crops most similar to `query` (your SAM-segmented object lookup)."""
    # 👇 write your code here, then DELETE the line below
    collection_name = "objects"
    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
    }
    search_results = client.search(
        collection_name=collection_name,
        data=[query.tolist()],
        limit=k,
        params=search_params,
        output_fields=["id", "dataset"],
    )
    return [result.id for result in search_results[0]]
    # raise NotImplementedError("Step 2: find_similar_objects() not written yet")


# ════ TESTS — run `pytest dinov2_object_store.py` (or `python dinov2_object_store.py`). All green = you're done. ════


def test_store_count():
    c = fresh_client()
    assert store_objects(c) == N


def test_find_self():
    c = fresh_client()
    store_objects(c)
    ids = list(find_similar_objects(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
