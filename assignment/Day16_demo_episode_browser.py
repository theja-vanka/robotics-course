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

def index_for_search(client):
    """TODO 1: Create collection 'browser' and insert EXAMPLE_VECTORS (instruction+observation embeddings). Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: index_for_search() not written yet")


def find_episodes(client, query=QUERY, k=5):
    """TODO 2: Return ids of the k episodes best matching `query` — your CLI 'find' command."""
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
