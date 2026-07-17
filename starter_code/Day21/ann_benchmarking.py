"""
Day 21 · 🔧 Build + Milvus — ANN Benchmarking
TASK:    Benchmark HNSW vs IVF_PQ vs IVF_FLAT on your robot dataset. Plot recall@10 vs QPS.
OUTCOME: A working Milvus operation for Milvus — ANN Benchmarking.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest ann_benchmarking.py     (or just:  python ann_benchmarking.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  ML refresh (skim) — solidify the eval math behind your benchmarks.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day21.md
Setup:  pip install pymilvus numpy transformers torch pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from pymilvus import MilvusClient  # noqa: F401  — you'll use this inside the functions below
from helpers.milvus import fresh_client
from helpers.embeddings import clip_bridge_embeddings

# Real CLIP ViT-B/32 embeddings of BridgeData V2 robot scenes (WidowX arm), computed once and
# cached to starter_code/clip_bridge_embeddings.npy.  (See helpers/embeddings.py.)
EXAMPLE_VECTORS, QUERY, DIM, N = clip_bridge_embeddings()   # (200, 512)



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


# ════ TESTS — run `pytest ann_benchmarking.py` (or `python ann_benchmarking.py`). All green = you're done. ════

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
