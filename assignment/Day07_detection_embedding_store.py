"""
Day 07 · 🔧 Build + Milvus — Detection Embedding Store
TASK:    After each detection, extract RoI → embed with CLIP → upsert into Milvus with class label. Build 'seen objects' index.
OUTCOME: A working Milvus operation for Milvus — Detection Embedding Store.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day07_detection_embedding_store.py     (or just:  python Day07_detection_embedding_store.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: plug in YOLO26 detection → an object list the policy can use.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day07.md
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


# ════ TESTS — run `pytest Day07_detection_embedding_store.py` (or `python Day07_detection_embedding_store.py`). All green = you're done. ════

def test_upsert_grows():
    c = fresh_client(); create_seen_index(c)
    n1 = upsert_detection(c, EXAMPLE_VECTORS[0], 3)
    n2 = upsert_detection(c, EXAMPLE_VECTORS[1], 7)
    assert n2 > n1, "each detection grows the 'seen objects' index"

def test_query_returns_labels():
    c = fresh_client(); create_seen_index(c)
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
