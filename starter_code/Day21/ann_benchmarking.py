"""
Day 21 · 🔧 Build + Milvus — ANN Benchmarking
TASK:    Benchmark HNSW vs IVF_PQ vs IVF_FLAT on your robot dataset. Plot recall@10 vs QPS.
OUTCOME: A working Milvus operation for Milvus — ANN Benchmarking.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day21_ann_benchmarking.py     (or just:  python Day21_ann_benchmarking.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ML refresh (skim) — solidify the eval math behind your benchmarks.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day21.md
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
def _build_clip_cache(path: str, n: int = 200) -> None:
    """Compute CLIP embeddings of ALOHA robot scenes and save to `path`."""
    from PIL import Image
    import io
    print("[setup] computing CLIP embeddings — one-time, ~1 min…")
    ds     = load_dataset("lerobot/aloha_sim_insertion_human_image", split="train")
    cam    = next(k for k in ds.column_names if "images" in k)
    def to_pil(r):
        if hasattr(r, "convert"): return r.convert("RGB")
        b = (r.get("bytes") or r.get("data")) if isinstance(r, dict) else None
        return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(r["path"]).convert("RGB")
    imgs   = [to_pil(ds[i][cam]) for i in range(n)]
    proc   = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    mdl    = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
    mdl.eval()
    vecs   = []
    with torch.no_grad():
        for i in range(0, len(imgs), 32):
            b    = proc(images=imgs[i:i+32], return_tensors="pt", padding=True)
            b    = {k: v.to(device) for k, v in b.items()}
            feat = mdl.get_image_features(**b)
            vecs.append((feat if isinstance(feat, torch.Tensor) else feat.pooler_output).cpu().numpy())
    np.save(path, np.vstack(vecs).astype("float32"))
    print(f"[setup] cached {n} embeddings → {path}")

if not os.path.exists(_CACHE):
    _build_clip_cache(_CACHE)
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

def build_index(client, index_type):
    """TODO 1: Create collection 'bench' and insert EXAMPLE_VECTORS with the given index_type ('FLAT'/'IVF_FLAT'/'HNSW'). Return the collection name."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_index() not written yet")


def measure_qps(client, n_queries=100):
    """TODO 2: Run n_queries searches; return queries-per-second (float)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: measure_qps() not written yet")


def benchmark(client):
    """TODO 3: Build with each of ['FLAT','IVF_FLAT','HNSW'], measure QPS for each, and return {index_type: qps}."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: benchmark() not written yet")


# ════ TESTS — run `pytest Day21_ann_benchmarking.py` (or `python Day21_ann_benchmarking.py`). All green = you're done. ════

def test_qps_positive():
    c = fresh_client(); build_index(c, "FLAT")
    assert measure_qps(c, 10) > 0

def test_benchmark_covers_all():
    d = benchmark(fresh_client())
    assert {"FLAT", "IVF_FLAT", "HNSW"} <= set(d), "benchmark every index type"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
