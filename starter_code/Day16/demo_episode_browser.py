"""
Day 16 · 🔧 Build + Milvus — Demo-Episode Browser
TASK:    Index every generated episode by instruction + observation embedding. Build a CLI: 'find episodes where the arm grasps from the left' → top-10. Use it to spot gaps in your synthetic set.
OUTCOME: A working Milvus operation for Milvus — Demo-Episode Browser.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day16_demo_episode_browser.py     (or just:  python Day16_demo_episode_browser.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Scale to ~200+ episodes in LeRobot format — the set you'll re-fine-tune on for robustness (baseline fine-tune was Day 14).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day16.md
Setup:  pip install pymilvus numpy datasets transformers torch pillow pytest
"""
from __future__ import annotations

import os
import numpy as np
import torch
from datasets import load_dataset
from transformers import CLIPModel, CLIPProcessor
from pymilvus import MilvusClient

# CLIP embeddings of SO-100 pick-place demo episode key-frames (lerobot/svla_so100_pickplace).
# One frame per episode (frame_index==0) → 512-d CLIP vector = trajectory-level embedding.
# First run: ~1 min. Subsequent runs: instant.
_ROOT     = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_CACHE    = os.path.join(_ROOT, "demo_traj_embeddings.npy")
_EP_CACHE = os.path.join(_ROOT, "demo_episode_ids.npy")
def _build_demo_cache(path: str, ep_path: str, max_eps: int = 100) -> None:
    """Encode SO-100 pick-place demo key-frames with CLIP and save to `path`."""
    from PIL import Image
    import io
    print("[setup] encoding SO-100 demo episodes with CLIP — one-time, ~1 min…")
    ds  = load_dataset("lerobot/svla_so100_pickplace", split="train")
    cam = next(k for k in ds.column_names if k.startswith("observation.images."))
    def to_pil(r):
        if hasattr(r, "convert"): return r.convert("RGB")
        b = (r.get("bytes") or r.get("data")) if isinstance(r, dict) else None
        return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(r["path"]).convert("RGB")
    seen, imgs, eps = set(), [], []
    for row in ds:
        ep = row["episode_index"]
        if row["frame_index"] == 0 and ep not in seen:
            seen.add(ep)
            imgs.append(to_pil(row[cam]))
            eps.append(ep)
        if len(imgs) >= max_eps:
            break
    proc   = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    mdl    = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
    mdl.eval()
    vecs   = []
    with torch.no_grad():
        for i in range(0, len(imgs), 16):
            b    = proc(images=imgs[i:i+16], return_tensors="pt", padding=True)
            b    = {k: v.to(device) for k, v in b.items()}
            feat = mdl.get_image_features(**b)
            vecs.append((feat if isinstance(feat, torch.Tensor) else feat.pooler_output).cpu().numpy())
    arr = np.vstack(vecs).astype("float32")
    np.save(path,    arr)
    np.save(ep_path, np.array(eps[:len(arr)]))
    print(f"[setup] cached {len(eps)} demo embeddings → {path}")

if not os.path.exists(_CACHE):
    _build_demo_cache(_CACHE, _EP_CACHE)
EXAMPLE_VECTORS = np.load(_CACHE)              # (≤100, 512) — CLIP of demo first frames
EPISODE_IDS     = np.load(_EP_CACHE).tolist()  # matching SO-100 episode IDs
QUERY = EXAMPLE_VECTORS[0]
DIM   = EXAMPLE_VECTORS.shape[1]   # 512
N     = len(EXAMPLE_VECTORS)       # ≤ 100

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    _db = os.path.join(_ROOT, "milvus_demo.db")
    if os.path.exists(_db):
        os.remove(_db)
    return MilvusClient(_db)



# ════ FILL IN — each function raises until you write it ════

def index_for_search(client):
    """TODO 1: Create collection 'browser' and insert EXAMPLE_VECTORS — CLIP embeddings of SO-100 demo key-frames (one per episode). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_for_search() not written yet")


def find_episodes(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k episodes whose CLIP embedding best matches `query` — your CLI 'find episodes where the arm grasps from the left' command."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_episodes() not written yet")


# ════ TESTS — run `pytest Day16_demo_episode_browser.py` (or `python Day16_demo_episode_browser.py`). All green = you're done. ════

def test_indexed():
    c = fresh_client()
    assert index_for_search(c) == N

def test_find():
    c = fresh_client(); index_for_search(c)
    ids = list(find_episodes(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
