"""
Day 03 · 🔧 Build + Milvus — Index Types
TASK:    Learn IVF_FLAT, HNSW, IVF_PQ. Rebuild collection with HNSW. Compare speed vs recall.
OUTCOME: A working Milvus operation for Milvus — Index Types.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest index_types.py     (or just:  python index_types.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day03.md
Setup:  pip install "pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""

from __future__ import annotations

import os
import sys
from pydoc import cli

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


def build_with_index(client, index_type):
    """TODO 1: Create collection 'vecs', insert EXAMPLE_VECTORS, building the given index_type ('FLAT' or 'HNSW'). milvus-lite may map both to FLAT — that's fine, set the param. Return the collection name."""
    # 👇 write your code here, then DELETE the line below
    collection_name = "vecs"

    index_type = index_type.upper()
    if index_type not in {"FLAT", "HNSW"}:
        raise ValueError("index_type must be 'FLAT' or 'HNSW'")

    if client.has_collection(collection_name):
        client.drop_collection(collection_name)

    # Quick setup creates and loads the collection with a default index.
    client.create_collection(
        collection_name=collection_name,
        dimension=DIM,
        primary_field_name="id",
        vector_field_name="embeddings",
        auto_id=False,
        enable_dynamic_field=True,
        metric_type="COSINE",
    )

    # Remove the automatically created index.
    client.release_collection(collection_name)

    default_indexes = client.list_indexes(collection_name=collection_name)

    for index_name in default_indexes:
        client.drop_index(
            collection_name=collection_name,
            index_name=index_name,
        )

    data = [
        {
            "id": i,
            "embeddings": vector,
            "dataset": "digits",
        }
        for i, vector in enumerate(EXAMPLE_VECTORS[:100].tolist())
    ]

    result = client.insert(
        collection_name=collection_name,
        data=data,
    )

    print("Inserted:", result["insert_count"])

    index_params = client.prepare_index_params()

    if index_type == "HNSW":
        index_specific_params = {
            "M": 16,
            "efConstruction": 200,
        }
    else:
        index_specific_params = {}

    index_params.add_index(
        field_name="embeddings",
        index_name="embedding_idx",
        index_type=index_type,
        metric_type="COSINE",
        params=index_specific_params,
    )

    client.create_index(
        collection_name=collection_name,
        index_params=index_params,
    )

    client.load_collection(collection_name)

    return collection_name
    # raise NotImplementedError("Step 1: build_with_index() not written yet")


def timed_search(client, query=QUERY, k=5):
    """TODO 2: Run one search; return (ids, elapsed_seconds)."""
    # 👇 write your code here, then DELETE the line below
    import time

    start = time.time()
    result = client.search("vecs", [query.tolist()], limit=k)
    elapsed = time.time() - start

    return [hit["id"] for hit in result[0]], elapsed
    # raise NotImplementedError("Step 2: timed_search() not written yet")


def compare_indexes(client):
    """TODO 3: Rebuild the collection once as 'FLAT' and once as 'HNSW', time a search on each, and return {'FLAT': seconds, 'HNSW': seconds}."""
    # 👇 write your code here, then DELETE the line below
    times = {}
    for index_type in ["FLAT", "HNSW"]:
        build_with_index(client, index_type)
        _, elapsed = timed_search(client)
        times[index_type] = elapsed

    return times
    # raise NotImplementedError("Step 3: compare_indexes() not written yet")


# ════ TESTS — run `pytest index_types.py` (or `python index_types.py`). All green = you're done. ════


def test_search_after_index():
    c = fresh_client()
    build_with_index(c, "HNSW")
    ids, _ = timed_search(c)
    assert list(ids)[0] == 0, "nearest neighbour of the query is itself"


def test_compare_has_both():
    d = compare_indexes(fresh_client())
    assert {"FLAT", "HNSW"} <= set(d) and all(v >= 0 for v in d.values()), (
        "time both index types"
    )


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
