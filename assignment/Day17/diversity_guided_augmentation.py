"""
Day 17 · 🔧 Build + Milvus — Diversity-guided Augmentation
TASK:    Only keep ControlNet images that increase Milvus collection diversity (distance threshold).
OUTCOME: A working Milvus operation for Milvus — Diversity-guided Augmentation.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day17_diversity_guided_augmentation.py     (or just:  python Day17_diversity_guided_augmentation.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ControlNet photorealism pass on synthetic data — shrink the sim-to-real gap.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day17.md
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

def seed_collection(client):
    """TODO 1: Create collection 'aug' and insert the FIRST 50 EXAMPLE_VECTORS as the seed set. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: seed_collection() not written yet")


def is_diverse(client, vec, threshold):
    """TODO 2: Return True if `vec`'s nearest-neighbour distance in the collection is ABOVE `threshold` (it adds diversity)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: is_diverse() not written yet")


def add_if_diverse(client, vec, threshold):
    """TODO 3: Insert `vec` only when is_diverse() is True; return True if it was added."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: add_if_diverse() not written yet")


# ════ TESTS — run `pytest Day17_diversity_guided_augmentation.py` (or `python Day17_diversity_guided_augmentation.py`). All green = you're done. ════

def test_duplicate_not_diverse():
    c = fresh_client(); seed_collection(c)
    assert is_diverse(c, EXAMPLE_VECTORS[0], 1.0) is False, "a vector already in the set adds no diversity"

def test_far_vector_is_diverse():
    c = fresh_client(); seed_collection(c)
    far = EXAMPLE_VECTORS[0] * 0.0 + 999.0
    assert is_diverse(c, far, 1.0) is True


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
