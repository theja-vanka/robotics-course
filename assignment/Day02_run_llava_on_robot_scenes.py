"""
Day 02 · 🛠️ Hands-on — Run LLaVA on Robot Scenes
TASK:    Encode a tabletop image with CLIP (openai/clip-vit-base-patch32) into a 512-d vector; run LLaVA-1.5 to list graspable objects as JSON. Deliverable: a 512-d embedding + JSON with at least 3 objects. Paper: CLIP (arXiv 2103.00020).
OUTCOME: Working code plus saved output for Run LLaVA on Robot Scenes.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day02_run_llava_on_robot_scenes.py     (or just:  python Day02_run_llava_on_robot_scenes.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Add CLIP→Milvus retrieval over observations (the policy's memory).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day02.md
Setup:  pip install transformers datasets torch pillow pytest
"""
from __future__ import annotations

import json
import torch
from datasets import load_dataset   # OPEN dataset
from transformers import CLIPModel, CLIPProcessor

IMAGE = load_dataset("huggingface/cats-image", split="test")[0]["image"].convert("RGB")   # a REAL sample image

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def load_clip():
    """TODO 1: Load CLIPModel + CLIPProcessor ('openai/clip-vit-base-patch32') onto DEVICE; return (model, processor)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_clip() not written yet")


def encode_image(model, processor):
    """TODO 2: Encode IMAGE with model.get_image_features(...); return the 512-d tensor."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: encode_image() not written yet")


def list_objects(image=IMAGE):
    """TODO 3: Run a VLM (LLaVA-1.5, or any captioner) and return a JSON-serialisable LIST of >=3 graspable object names, e.g. ['cup','bottle','block']."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: list_objects() not written yet")


# ════ TESTS — run `pytest Day02_run_llava_on_robot_scenes.py` (or `python Day02_run_llava_on_robot_scenes.py`). All green = you're done. ════

def test_embedding_is_512d():
    model, proc = load_clip()
    emb = encode_image(model, proc)
    assert emb.shape[-1] == 512 and torch.isfinite(emb).all()

def test_objects_are_json_list():
    objs = list_objects()
    json.dumps(objs)   # must be JSON-serialisable
    assert isinstance(objs, list) and len(objs) >= 3, "LLaVA should list at least 3 graspable objects"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
