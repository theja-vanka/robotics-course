"""
Day 01 · 🔧 Build + Milvus — First Collection
TASK:    Install Milvus via Docker, connect pymilvus, create collection, insert dummy vectors, run search.
OUTCOME: A working Milvus operation for Milvus — First Collection.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day01_first_collection.py     (or just:  python Day01_first_collection.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Stub the vla-edge repo + env; get SmolVLA running on one sample observation.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day01.md
Setup:  pip install pymilvus numpy datasets transformers torch pillow pytest
"""

from __future__ import annotations

import os

import numpy as np
import torch
from datasets import load_dataset
from pymilvus import MilvusClient
from transformers import CLIPModel, CLIPProcessor

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

# Real CLIP embeddings of BridgeData V2 robot manipulation scenes (WidowX arm, real robot).
# 200 frames encoded with openai/clip-vit-base-patch32 → 512-d vectors.
# First run: downloads CLIP model + computes embeddings (~1 min). Subsequent runs: instant.
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_CACHE = os.path.join(_ROOT, "clip_bridge_embeddings.npy")


def _build_clip_cache(path: str, n: int = 200) -> None:
    """Compute CLIP embeddings of BridgeData V2 (WidowX) robot scenes and save to `path`."""
    import io

    from PIL import Image

    print("[setup] computing CLIP embeddings — one-time, ~1 min…")
    ds = load_dataset("jesbu1/bridge_v2_lerobot", split="train")
    cam = next(k for k in ds.column_names if "images" in k)

    def to_pil(r):
        if hasattr(r, "convert"):
            return r.convert("RGB")
        b = (r.get("bytes") or r.get("data")) if isinstance(r, dict) else None
        return (
            Image.open(io.BytesIO(b)).convert("RGB")
            if b
            else Image.open(r["path"]).convert("RGB")
        )

    imgs = [to_pil(ds[i][cam]) for i in range(n)]
    proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    mdl = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(DEVICE)
    mdl.eval()
    vecs = []
    with torch.no_grad():
        for i in range(0, len(imgs), 32):
            b = proc(images=imgs[i : i + 32], return_tensors="pt", padding=True)
            b = {k: v.to(DEVICE) for k, v in b.items()}
            feat = mdl.get_image_features(**b)
            vecs.append(
                (feat if isinstance(feat, torch.Tensor) else feat.pooler_output)
                .cpu()
                .numpy()
            )
    np.save(path, np.vstack(vecs).astype("float32"))
    print(f"[setup] cached {n} embeddings → {path}")


def _load_embeddings():
    if not os.path.exists(_CACHE):
        _build_clip_cache(_CACHE)
    vecs = np.load(_CACHE)
    return vecs, vecs[0], vecs.shape[1], len(vecs)


EXAMPLE_VECTORS, QUERY, DIM, N = _load_embeddings()  # (N,512) CLIP vectors; N≈200


def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    import shutil

    _db = os.path.join(_ROOT, "milvus_demo.db")
    if os.path.exists(_db):
        shutil.rmtree(_db)  # MilvusClient stores data as a folder, not a file
    return MilvusClient(_db)


# ════ FILL IN — each function raises until you write it ════


def create_collection(client):
    """TODO 1: Create a collection named 'demo' with a vector field of dimension DIM (=512)."""
    # 👇 write your code here, then DELETE the line below
    client.drop_collection(collection_name="demo")
    client.create_collection(
        collection_name="demo",
        dimension=DIM,
    )
    # raise NotImplementedError("Step 1: create_collection() not written yet")


def insert_vectors(client):
    """TODO 2: Insert all EXAMPLE_VECTORS (N=200 CLIP robot-scene embeddings, ids 0..N-1) into 'demo'. Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    import time

    data = []
    for i, vector in enumerate(EXAMPLE_VECTORS.tolist()):
        data.append({"id": i, "vector": vector, "dataset": "digits"})
    res = client.insert(collection_name="demo", data=data)
    time.sleep(2)
    return len(res["ids"])
    # raise NotImplementedError("Step 2: insert_vectors() not written yet")


def run_search(client):
    """TODO 3: Search 'demo' for QUERY (the first robot scene embedding) with limit=5. Return the list of result ids (length 5)."""
    # 👇 write your code here, then DELETE the line below
    search_results = client.search(
        collection_name="demo",
        data=[QUERY.tolist()],
        limit=5,
        Output_fields=["id", "dataset"],
    )
    return [result.id for result in search_results[0]]
    # raise NotImplementedError("Step 3: run_search() not written yet")


# ════ TESTS — run `pytest Day01_first_collection.py` (or `python Day01_first_collection.py`). All green = you're done. ════


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
