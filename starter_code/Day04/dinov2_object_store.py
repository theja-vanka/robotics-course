"""
Day 04 · 🔧 Build + Milvus — DINOv2 Object Store
TASK:    Encode SAM-segmented object crops with DINOv2. Store in Milvus. Query: find similar objects.
OUTCOME: A working Milvus operation for Milvus — DINOv2 Object Store.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day04_dinov2_object_store.py     (or just:  python Day04_dinov2_object_store.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: add SAM/ViT segmentation to turn frames into structured observations.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day04.md
Setup:  pip install pymilvus numpy datasets transformers torch pillow pytest
"""
from __future__ import annotations

import os
import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModel, AutoImageProcessor
from pymilvus import MilvusClient

# DINOv2 embeddings of ALOHA robot scene images (LeRobot / HuggingFace).
# 200 top-camera frames encoded with facebook/dinov2-base → 768-d CLS token.
# In production feed real SAM-segmented object crops; the Milvus API is identical.
# First run: ~1 min on CPU / ~20 s on MPS. Subsequent runs: instant.
_ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_CACHE = os.path.join(_ROOT, "dinov2_robot_embeddings.npy")
def _build_dinov2_cache(path: str, n: int = 200) -> None:
    """Compute DINOv2 CLS embeddings of ALOHA robot scenes and save to `path`."""
    from PIL import Image
    import io
    print("[setup] computing DINOv2 embeddings — one-time, ~1 min…")
    ds     = load_dataset("lerobot/aloha_sim_insertion_human_image", split="train")
    cam    = next(k for k in ds.column_names if "images" in k)
    def to_pil(r):
        if hasattr(r, "convert"): return r.convert("RGB")
        b = (r.get("bytes") or r.get("data")) if isinstance(r, dict) else None
        return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(r["path"]).convert("RGB")
    imgs   = [to_pil(ds[i][cam]) for i in range(n)]
    proc   = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    mdl    = AutoModel.from_pretrained("facebook/dinov2-base").to(device)
    mdl.eval()
    vecs   = []
    with torch.no_grad():
        for i in range(0, len(imgs), 16):
            b = proc(images=imgs[i:i+16], return_tensors="pt")
            b = {k: v.to(device) for k, v in b.items()}
            vecs.append(mdl(**b).last_hidden_state[:, 0].cpu().numpy())
    np.save(path, np.vstack(vecs).astype("float32"))
    print(f"[setup] cached {n} embeddings → {path}")

if not os.path.exists(_CACHE):
    _build_dinov2_cache(_CACHE)
EXAMPLE_VECTORS = np.load(_CACHE)   # (200, 768) — DINOv2 CLS features of robot object crops
QUERY = EXAMPLE_VECTORS[0]
DIM   = EXAMPLE_VECTORS.shape[1]    # 768  (DINOv2-base)
N     = len(EXAMPLE_VECTORS)        # 200

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    _db = os.path.join(_ROOT, "milvus_demo.db")
    if os.path.exists(_db):
        os.remove(_db)
    return MilvusClient(_db)



# ════ FILL IN — each function raises until you write it ════

def store_objects(client):
    """TODO 1: Create collection 'objects' (vector dim DIM=768) and insert EXAMPLE_VECTORS — real DINOv2 CLS features of ALOHA robot scene crops. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_objects() not written yet")


def find_similar_objects(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k object crops most similar to `query` (your SAM-segmented object lookup)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_similar_objects() not written yet")


# ════ TESTS — run `pytest Day04_dinov2_object_store.py` (or `python Day04_dinov2_object_store.py`). All green = you're done. ════

def test_store_count():
    c = fresh_client()
    assert store_objects(c) == N

def test_find_self():
    c = fresh_client(); store_objects(c)
    ids = list(find_similar_objects(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
