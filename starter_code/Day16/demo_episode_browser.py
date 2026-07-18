"""
Day 16 · 🔧 Build + Milvus — Demo-Episode Browser
TASK:    Index every generated episode by instruction + observation embedding. Build a CLI: 'find episodes where the arm grasps from the left' → top-10. Use it to spot gaps in your synthetic set.
OUTCOME: A working Milvus operation for Milvus — Demo-Episode Browser.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest demo_episode_browser.py     (or just:  python demo_episode_browser.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Scale to ~200+ episodes in LeRobot format — the set you'll re-fine-tune on for robustness (baseline fine-tune was Day 14).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day16.md
Setup:  pip install "pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from pymilvus import MilvusClient  # noqa: F401
from helpers.milvus import fresh_client
from helpers.embeddings import demo_episode_embeddings

# CLIP embeddings of SO-100 pick-place demo key-frames (lerobot/svla_so100_pickplace),
# one 512-d vector per sampled key-frame, cached to starter_code/demo_traj_embeddings.npy.
EXAMPLE_VECTORS, EPISODE_IDS, QUERY, DIM, N = demo_episode_embeddings()



# ════ FILL IN — each function raises until you write it ════

def index_for_search(client):
    """TODO 1: Create collection 'browser' and insert EXAMPLE_VECTORS — CLIP embeddings of SO-100 demo key-frames (one per episode). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_for_search() not written yet")


def find_episodes(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k episodes whose CLIP embedding best matches `query` — your CLI 'find episodes where the arm grasps from the left' command."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: find_episodes() not written yet")


# ════ TESTS — run `pytest demo_episode_browser.py` (or `python demo_episode_browser.py`). All green = you're done. ════

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
