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
