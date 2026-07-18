"""
Day 08 · 🔧 Build + Milvus — Multi-modal (RGB + Depth)
TASK:    Store both CLIP (RGB) and depth feature vectors in a Milvus collection. Query by either modality.
OUTCOME: A working Milvus operation for Milvus — Multi-modal (RGB + Depth).

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest multi_modal_rgb_depth.py     (or just:  python multi_modal_rgb_depth.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  observe.py: add Depth Anything depth → richer observation / conditioning.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day08.md
Setup:  pip install "pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
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

def create_frames(client):
    """TODO 1: Create collection 'frames' with a vector field (dim DIM) plus a string field 'modality'."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: create_frames() not written yet")


def insert_multimodal(client):
    """TODO 2: Insert each EXAMPLE_VECTOR TWICE — once tagged modality='rgb', once modality='depth'. Return the total row count (2*N)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: insert_multimodal() not written yet")


def search_by_modality(client, modality, query=QUERY, k=5):
    """TODO 3: Search 'frames' filtering to the given modality ('rgb' or 'depth'); return result ids."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: search_by_modality() not written yet")


# ════ TESTS — run `pytest multi_modal_rgb_depth.py` (or `python multi_modal_rgb_depth.py`). All green = you're done. ════

def test_inserted_both_modalities():
    c = fresh_client(); create_frames(c)
    assert insert_multimodal(c) == 2 * N

def test_search_either_modality():
    c = fresh_client(); create_frames(c); insert_multimodal(c)
    assert len(list(search_by_modality(c, "rgb", EXAMPLE_VECTORS[0], 5))) == 5
    assert len(list(search_by_modality(c, "depth", EXAMPLE_VECTORS[0], 5))) == 5


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
