"""
Day 14 · 🔧 Build + Milvus — Demo Replay Buffer
TASK:    After fine-tuning, index new demo embeddings. Build retrieval for hardest negative examples.
OUTCOME: A working Milvus operation for Milvus — Demo Replay Buffer.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day14_demo_replay_buffer.py     (or just:  python Day14_demo_replay_buffer.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ⭐ train_lora.py: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day14.md
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

def index_replay(client):
    """TODO 1: Create collection 'replay' and insert EXAMPLE_VECTORS (new demo embeddings). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_replay() not written yet")


def hardest_negatives(client, anchor=QUERY, k=5):
    """TODO 2: Return ids of the k examples FARTHEST from `anchor` (the hardest negatives). Hint: search returns nearest — you want the opposite end (e.g. negate the metric or scan)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: hardest_negatives() not written yet")


# ════ TESTS — run `pytest Day14_demo_replay_buffer.py` (or `python Day14_demo_replay_buffer.py`). All green = you're done. ════

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
