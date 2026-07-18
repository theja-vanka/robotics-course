"""
Day 13 · 🔧 Build + Milvus — Retrieval-Augmented VLA
TASK:    Store robot demo trajectories as embeddings. At inference: encode observation → retrieve top-3 demos → prepend as context.
OUTCOME: A working Milvus operation for Milvus — Retrieval-Augmented VLA.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest retrieval_augmented_vla.py     (or just:  python retrieval_augmented_vla.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ⭐ policy.py: understand the VLA you'll fine-tune (action tokens, VLM backbone).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day13.md
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

def index_demos(client):
    """TODO 1: Create collection 'demos' and insert EXAMPLE_VECTORS — real CLIP embeddings of SO-100 pick-place demo key-frames (one per episode). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_demos() not written yet")


def retrieve_demos(client, observation=QUERY, k=3):
    """TODO 2: Return ids of the k demos most similar to `observation` — the context you prepend for the VLA."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: retrieve_demos() not written yet")


# ════ TESTS — run `pytest retrieval_augmented_vla.py` (or `python retrieval_augmented_vla.py`). All green = you're done. ════

def test_indexed():
    c = fresh_client()
    assert index_demos(c) == N

def test_retrieve_k():
    c = fresh_client(); index_demos(c)
    ids = list(retrieve_demos(c, EXAMPLE_VECTORS[0], 3))
    assert len(ids) == 3 and ids[0] == 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
