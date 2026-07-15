"""
Day 23 · 🔧 Build + Milvus — Anomaly Detection
TASK:    Store nominal scene embeddings. Flag queries with nearest-neighbour distance > threshold as OOD.
OUTCOME: A working Milvus operation for Milvus — Anomaly Detection.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day23_anomaly_detection.py     (or just:  python Day23_anomaly_detection.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  eval.py: implement your metrics (success rate, IoU/NMS helpers) cleanly.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day23.md
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
_ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_CACHE = os.path.join(_ROOT, "clip_robot_embeddings.npy")
if not os.path.exists(_CACHE):
    print("[setup] computing CLIP embeddings of robot scenes — one-time, ~1 min…")
    _ds   = load_dataset("lerobot/aloha_sim_insertion_human_image", split="train")
    _cam  = next(k for k in _ds.column_names if "images" in k)
    def _to_pil(_r):
        from PIL import Image; import io
        if hasattr(_r, "convert"): return _r.convert("RGB")
        b = (_r.get("bytes") or _r.get("data")) if isinstance(_r, dict) else None
        return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(_r["path"]).convert("RGB")
    _imgs = [_to_pil(_ds[i][_cam]) for i in range(200)]
    _proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    _device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    _mdl  = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(_device)
    _mdl.eval()
    _vecs = []
    with torch.no_grad():
        for i in range(0, len(_imgs), 32):
            _b = _proc(images=_imgs[i:i+32], return_tensors="pt", padding=True)
            _b = {k: v.to(_device) for k, v in _b.items()}
            _feat = _mdl.get_image_features(**_b)
            _vecs.append((_feat if isinstance(_feat, torch.Tensor) else _feat.pooler_output).cpu().numpy())
    np.save(_CACHE, np.vstack(_vecs).astype("float32"))
    print(f"[setup] cached → {_CACHE}")
EXAMPLE_VECTORS = np.load(_CACHE)   # (200, 512) — real CLIP embeddings of robot scenes
QUERY = EXAMPLE_VECTORS[0]
DIM   = EXAMPLE_VECTORS.shape[1]    # 512  (CLIP ViT-B/32)
N     = len(EXAMPLE_VECTORS)        # 200

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    _db = os.path.join(_ROOT, "milvus_demo.db")
    if os.path.exists(_db):
        os.remove(_db)
    return MilvusClient(_db)



# ════ FILL IN — each function raises until you write it ════

def store_nominal(client):
    """TODO 1: Create collection 'nominal' and insert EXAMPLE_VECTORS (the normal scenes). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_nominal() not written yet")


def nn_distance(client, vec):
    """TODO 2: Return the distance from `vec` to its nearest nominal neighbour (a float)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: nn_distance() not written yet")


def is_anomaly(client, vec, threshold):
    """TODO 3: Return True if nn_distance(vec) > threshold."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: is_anomaly() not written yet")


# ════ TESTS — run `pytest Day23_anomaly_detection.py` (or `python Day23_anomaly_detection.py`). All green = you're done. ════

def test_nominal_not_anomaly():
    c = fresh_client(); store_nominal(c)
    assert is_anomaly(c, EXAMPLE_VECTORS[0], 1.0) is False, "a stored nominal scene is not anomalous"

def test_outlier_flagged():
    c = fresh_client(); store_nominal(c)
    far = EXAMPLE_VECTORS[0] * 0.0 + 999.0
    assert is_anomaly(c, far, 1.0) is True


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
