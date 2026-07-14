"""
Day 05 · 🔧 Build + Milvus — Production Schema Design
TASK:    Design schema for robot data: image_id, object_class, embedding, timestamp, metadata. Implement it.
OUTCOME: A working Milvus operation for Milvus — Production Schema Design.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day05_production_schema_design.py     (or just:  python Day05_production_schema_design.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  3D representations — awareness; note where 3DGS could enrich observations later.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day05.md
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

def build_schema():
    """TODO 1: Return your field design for robot detections: a primary key 'image_id', a float-vector 'embedding' (dim DIM), and scalar fields 'object_class' and 'timestamp'. Any representation (list of dicts / pymilvus FieldSchema) is fine."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_schema() not written yet")


def create_from_schema(client):
    """TODO 2: Create collection 'detections' implementing your schema (image_id PK + embedding + object_class + timestamp)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: create_from_schema() not written yet")


def insert_rows(client):
    """TODO 3: Insert EXAMPLE_VECTORS as rows (image_id 0..N-1, the vector, a dummy object_class + timestamp). Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: insert_rows() not written yet")


# ════ TESTS — run `pytest Day05_production_schema_design.py` (or `python Day05_production_schema_design.py`). All green = you're done. ════

def test_schema_names_all_fields():
    blob = str(build_schema()).lower()
    assert all(x in blob for x in ["image_id", "embedding", "object_class", "timestamp"]), "schema must name all four fields"

def test_rows_inserted():
    c = fresh_client(); create_from_schema(c)
    assert insert_rows(c) == N


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
