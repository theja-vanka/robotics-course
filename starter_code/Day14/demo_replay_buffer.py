"""
Day 14 · 🔧 Build + Milvus — Demo Replay Buffer
TASK:    After fine-tuning, index new demo embeddings. Build retrieval for hardest negative examples.
OUTCOME: A working Milvus operation for Milvus — Demo Replay Buffer.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest demo_replay_buffer.py     (or just:  python demo_replay_buffer.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ⭐ train_lora.py: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day14.md
Setup:  pip install pymilvus numpy transformers torch pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
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

def index_replay(client):
    """TODO 1: Create collection 'replay' and insert EXAMPLE_VECTORS — CLIP embeddings of SO-100 demo key-frames. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_replay() not written yet")


def hardest_negatives(client, anchor=QUERY, k=5):
    """TODO 2: Return ids of the k demos FARTHEST from `anchor` in CLIP space (hardest negatives for contrastive fine-tuning)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: hardest_negatives() not written yet")


# ════ TESTS — run `pytest demo_replay_buffer.py` (or `python demo_replay_buffer.py`). All green = you're done. ════

def test_indexed():
    c = fresh_client()
    assert index_replay(c) == N

def test_negatives_exclude_anchor():
    c = fresh_client(); index_replay(c)
    ids = list(hardest_negatives(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] != 0, "the anchor itself is the EASIEST positive, not a hard negative"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
