"""
Day 10 · 🔧 Build + Milvus — Grasp Pose Library
TASK:    Store (object embedding + grasp config) pairs. Query: given new object, retrieve most similar past grasp.
OUTCOME: A working Milvus operation for Milvus — Grasp Pose Library.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest grasp_pose_library.py     (or just:  python grasp_pose_library.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Grasp detection — awareness; see how a policy's action could ground to a grasp.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day10.md
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

def store_grasps(client):
    """TODO 1: Create collection 'grasps' and insert EXAMPLE_VECTORS, each paired with a dummy 7-float grasp config (x,y,z,qx,qy,qz,width) in a dynamic field 'grasp'. Return the count."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: store_grasps() not written yet")


def retrieve_grasp(client, query=QUERY):
    """TODO 2: Return the grasp config of the most similar stored object to `query`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: retrieve_grasp() not written yet")


# ════ TESTS — run `pytest grasp_pose_library.py` (or `python grasp_pose_library.py`). All green = you're done. ════

def test_stored():
    c = fresh_client()
    assert store_grasps(c) == N

def test_retrieve_grasp():
    c = fresh_client(); store_grasps(c)
    g = retrieve_grasp(c, EXAMPLE_VECTORS[0])
    assert g is not None and len(g) == 7


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
