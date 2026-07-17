"""
Day 17 · 🛠️ Hands-on — Depth-conditioned ControlNet Augmentation
TASK:    Use depth-ControlNet (SDv1.5) to generate 20 photorealistic variants of your synthetic scenes, conditioned on their depth maps. Deliverable: 20 images + a CLIP-diversity score vs the originals. Paper: ControlNet (arXiv 2302.05543).
OUTCOME: Working code plus saved output for Depth-conditioned ControlNet Augmentation.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest depth_conditioned_controlnet_augmentation.py     (or just:  python depth_conditioned_controlnet_augmentation.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  ControlNet photorealism pass on synthetic data — shrink the sim-to-real gap.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day17.md
Setup:  pip install diffusers transformers accelerate pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PIL import Image  # noqa: F401
from helpers.runtime import DEVICE  # noqa: F401
from helpers.images import load_scene_image
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel

CONDITION = load_scene_image((512, 512))   # real robot scene — use a depth/edge map in prod



# ════ FILL IN — each function raises until you write it ════

def load_pipeline():
    """TODO 1: Load a ControlNet (e.g. 'lllyasviel/sd-controlnet-depth') + SD ControlNet pipeline onto DEVICE; return the pipe."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_pipeline() not written yet")


def generate(pipe):
    """TODO 2: Run the pipe with a text prompt + CONDITION (num_inference_steps=20). Return the output PIL.Image."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: generate() not written yet")


# ════ TESTS — run `pytest depth_conditioned_controlnet_augmentation.py` (or `python depth_conditioned_controlnet_augmentation.py`). All green = you're done. ════

def test_generate_returns_image():
    img = generate(load_pipeline())
    assert isinstance(img, Image.Image), "generate() must return a PIL image"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
