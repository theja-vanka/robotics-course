"""
Day 08 · 🛠️ Hands-on — Run Depth Anything v2 + Point Cloud
TASK:    Run Depth Anything V2-Small on a tabletop image; back-project to an Open3D point cloud. Deliverable: depth.png + a cloud with at least 10k points (intrinsics noted). Paper: Depth Anything v2 (arXiv 2406.09414).
OUTCOME: Working code plus saved output for Run Depth Anything v2 + Point Cloud.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest run_depth_anything_v2_point_cloud.py     (or just:  python run_depth_anything_v2_point_cloud.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  observe.py: add Depth Anything depth → richer observation / conditioning.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day08.md
Setup:  pip install transformers pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PIL import Image  # noqa: F401
from helpers.images import load_scene_image
from transformers import pipeline as hf_pipeline

IMAGE = load_scene_image()   # real BridgeData V2 / WidowX robot scene (PIL)



# ════ FILL IN — each function raises until you write it ════

def load_estimator():
    """TODO 1: Return hf_pipeline('depth-estimation', model='depth-anything/Depth-Anything-V2-Small-hf')."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_estimator() not written yet")


def estimate_depth(est):
    """TODO 2: Run est on IMAGE; return the depth map (the ['depth'] PIL image)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: estimate_depth() not written yet")


# ════ TESTS — run `pytest run_depth_anything_v2_point_cloud.py` (or `python run_depth_anything_v2_point_cloud.py`). All green = you're done. ════

def test_depth_matches_input_size():
    d = estimate_depth(load_estimator())
    assert isinstance(d, Image.Image), "estimate_depth() should return a depth image"
    assert d.size == IMAGE.size, f"depth map {d.size} should match the input image {IMAGE.size}"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
