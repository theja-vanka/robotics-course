"""
Day 03 · 🛠️ Hands-on — Run Stable Diffusion img2img
TASK:    Run Stable Diffusion v1.5 img2img (diffusers) on a workspace photo at strength 0.3 / 0.5 / 0.7. Deliverable: 3 output images + a note on the fidelity-vs-change tradeoff. Paper: Latent Diffusion (arXiv 2112.10752).
OUTCOME: Working code plus saved output for Run Stable Diffusion img2img.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest run_stable_diffusion_img2img.py     (or just:  python run_stable_diffusion_img2img.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day03.md
Setup:  pip install diffusers transformers accelerate pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from diffusers import AutoPipelineForImage2Image
from helpers.images import load_scene_image
from helpers.runtime import DEVICE  # noqa: F401
from PIL import Image  # noqa: F401

INIT_IMAGE = load_scene_image((512, 512))  # real robot scene, resized for SD


# ════ FILL IN — each function raises until you write it ════


def load_pipeline():
    """TODO 1: Load AutoPipelineForImage2Image ('runwayml/stable-diffusion-v1-5') onto DEVICE; return the pipe."""
    # 👇 write your code here, then DELETE the line below
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    ).to(DEVICE)
    return pipe
    # raise NotImplementedError("Step 1: load_pipeline() not written yet")


def run_img2img(pipe):
    """TODO 2: Run the pipe (prompt + INIT_IMAGE + strength=0.6). Return the output PIL.Image."""
    # 👇 write your code here, then DELETE the line below
    prompt = "A futuristic robot in a sci-fi environment"
    output = pipe(prompt=prompt, image=INIT_IMAGE, strength=0.6).images[0]
    return output
    # raise NotImplementedError("Step 2: run_img2img() not written yet")


# ════ TESTS — run `pytest run_stable_diffusion_img2img.py` (or `python run_stable_diffusion_img2img.py`). All green = you're done. ════


def test_output_is_image():
    out = run_img2img(load_pipeline())
    assert isinstance(out, Image.Image), "run_img2img() must return a PIL image"


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
