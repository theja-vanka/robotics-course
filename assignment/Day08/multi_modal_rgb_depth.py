"""
Day 08 · 🔧 Build + Milvus — Multi-modal (RGB + Depth)
TASK:    Store both CLIP (RGB) and depth feature vectors in a Milvus collection. Query by either modality.
OUTCOME: A working Milvus operation for Milvus — Multi-modal (RGB + Depth).

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day08_multi_modal_rgb_depth.py     (or just:  python Day08_multi_modal_rgb_depth.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: add Depth Anything depth → richer observation / conditioning.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day08.md
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

def create_frames(client):
    """TODO 1: Create collection 'frames' with a vector field (dim DIM) plus a string field 'modality'."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_frames() not written yet")


def insert_multimodal(client):
    """TODO 2: Insert each EXAMPLE_VECTOR TWICE — once tagged modality='rgb', once modality='depth'. Return the total row count (2*N)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: insert_multimodal() not written yet")


def search_by_modality(client, modality, query=QUERY, k=5):
    """TODO 3: Search 'frames' filtering to the given modality ('rgb' or 'depth'); return result ids."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: search_by_modality() not written yet")


# ════ TESTS — run `pytest Day08_multi_modal_rgb_depth.py` (or `python Day08_multi_modal_rgb_depth.py`). All green = you're done. ════

def test_inserted_both_modalities():
    c = fresh_client(); create_frames(c)
    assert insert_multimodal(c) == 2 * N

def test_search_either_modality():
    c = fresh_client(); create_frames(c); insert_multimodal(c)
    assert len(list(search_by_modality(c, "rgb", EXAMPLE_VECTORS[0], 5))) == 5
    assert len(list(search_by_modality(c, "depth", EXAMPLE_VECTORS[0], 5))) == 5


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
