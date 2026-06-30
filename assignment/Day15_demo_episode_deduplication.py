"""
Day 15 · 🔧 Build + Milvus — Demo-Episode Deduplication
TASK:    Embed each demo episode (CLIP on key frames or a trajectory summary). Insert into Milvus. Flag near-duplicate episodes (cosine > 0.98) so your synthetic set stays diverse.
OUTCOME: A working Milvus operation for Milvus — Demo-Episode Deduplication.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day15_demo_episode_deduplication.py     (or just:  python Day15_demo_episode_deduplication.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Generate & inspect your first synthetic demo episodes (MimicGen) — the (obs, instruction, action) data train_lora.py will consume.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day15.md
Setup:  pip install pymilvus numpy scikit-learn pytest
"""
from __future__ import annotations

import os
from sklearn.datasets import load_digits   # OPEN dataset: 1797 handwritten digits (64-d), bundled with scikit-learn
from pymilvus import MilvusClient

_DIGITS = load_digits()
EXAMPLE_VECTORS = _DIGITS.data.astype("float32")   # (1797, 64) REAL vectors stand in for your embeddings
QUERY = EXAMPLE_VECTORS[0]
DIM = EXAMPLE_VECTORS.shape[1]   # 64
N = len(EXAMPLE_VECTORS)         # 1797

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    if os.path.exists("milvus_demo.db"):
        os.remove("milvus_demo.db")
    return MilvusClient("milvus_demo.db")

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def index_episodes(client):
    """TODO 1: Create collection 'episodes' and insert EXAMPLE_VECTORS. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_episodes() not written yet")


def near_duplicates(client, vec, threshold):
    """TODO 2: Return ids of episodes whose distance to `vec` is BELOW `threshold` (the near-duplicates to drop)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: near_duplicates() not written yet")


# ════ TESTS — run `pytest Day15_demo_episode_deduplication.py` (or `python Day15_demo_episode_deduplication.py`). All green = you're done. ════

def test_self_is_duplicate():
    c = fresh_client(); index_episodes(c)
    dups = list(near_duplicates(c, EXAMPLE_VECTORS[0], 1e9))
    assert 0 in dups, "an episode is a near-duplicate of itself (distance 0)"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
