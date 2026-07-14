"""
Day 03 · 🔧 Build + Milvus — Index Types
TASK:    Learn IVF_FLAT, HNSW, IVF_PQ. Rebuild collection with HNSW. Compare speed vs recall.
OUTCOME: A working Milvus operation for Milvus — Index Types.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day03_index_types.py     (or just:  python Day03_index_types.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day03.md
Setup:  pip install pymilvus numpy datasets transformers torch pillow pytest
"""
from __future__ import annotations

import os
import numpy as np
import torch
from datasets import load_dataset
from transformers import CLIPModel, CLIPProcessor
from pymilvus import MilvusClient

# Real CLIP embeddings of ALOHA robot manipulation scenes (LeRobot / HuggingFace).
# 200 top-camera frames encoded with openai/clip-vit-base-patch32 → 512-d vectors.
# First run: downloads CLIP model + computes embeddings (~1 min on CPU, ~20 s on MPS/CUDA).
# Subsequent runs: loads instantly from cache file.
_CACHE = "clip_robot_embeddings.npy"
if not os.path.exists(_CACHE):
    print("[setup] computing CLIP embeddings of robot scenes — one-time, ~1 min…")
    _ds   = load_dataset("lerobot/aloha_sim_insertion_human", split="train")
    _imgs = [_ds[i]["observation.images.top"].convert("RGB") for i in range(200)]
    _proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    _mdl  = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    _mdl.eval()
    _vecs = []
    with torch.no_grad():
        for i in range(0, len(_imgs), 32):
            _b = _proc(images=_imgs[i:i+32], return_tensors="pt", padding=True)
            _vecs.append(_mdl.get_image_features(**_b).cpu().numpy())
    np.save(_CACHE, np.vstack(_vecs).astype("float32"))
    print(f"[setup] cached → {_CACHE}")
EXAMPLE_VECTORS = np.load(_CACHE)   # (200, 512) — real CLIP embeddings of robot scenes
QUERY = EXAMPLE_VECTORS[0]
DIM   = EXAMPLE_VECTORS.shape[1]    # 512  (CLIP ViT-B/32)
N     = len(EXAMPLE_VECTORS)        # 200

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    if os.path.exists("milvus_demo.db"):
        os.remove("milvus_demo.db")
    return MilvusClient("milvus_demo.db")

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def build_with_index(client, index_type):
    """TODO 1: Create collection 'vecs', insert EXAMPLE_VECTORS, building the given index_type ('FLAT' or 'HNSW'). milvus-lite may map both to FLAT — that's fine, set the param. Return the collection name."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_with_index() not written yet")


def timed_search(client, query=QUERY, k=5):
    """TODO 2: Run one search; return (ids, elapsed_seconds)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: timed_search() not written yet")


def compare_indexes(client):
    """TODO 3: Rebuild the collection once as 'FLAT' and once as 'HNSW', time a search on each, and return {'FLAT': seconds, 'HNSW': seconds}."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare_indexes() not written yet")


# ════ TESTS — run `pytest Day03_index_types.py` (or `python Day03_index_types.py`). All green = you're done. ════

def test_search_after_index():
    c = fresh_client(); build_with_index(c, "HNSW")
    ids, _ = timed_search(c)
    assert list(ids)[0] == 0, "nearest neighbour of the query is itself"

def test_compare_has_both():
    d = compare_indexes(fresh_client())
    assert {"FLAT", "HNSW"} <= set(d) and all(v >= 0 for v in d.values()), "time both index types"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
