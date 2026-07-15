"""
Day 04 · 🛠️ Hands-on — Run SAM 2 on Robot Scene
TASK:    Run SAM 2.1 on a tabletop image; extract per-object masks. Deliverable: at least 3 masks saved as an overlay PNG + the mask count printed. Paper: SAM (arXiv 2304.02643).
OUTCOME: Working code plus saved output for Run SAM 2 on Robot Scene.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day04_run_sam_2_on_robot_scene.py     (or just:  python Day04_run_sam_2_on_robot_scene.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  observe.py: add SAM/ViT segmentation to turn frames into structured observations.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day04.md
Setup:  pip install ultralytics datasets pillow pytest
"""
from __future__ import annotations

from datasets import load_dataset   # OPEN dataset
from ultralytics import SAM

_ds_r = load_dataset("lerobot/aloha_sim_insertion_human_image", split="train")
_cam_r = next(k for k in _ds_r.column_names if "images" in k)
_raw_r = _ds_r[0][_cam_r]
def _to_pil_r(_r):
    from PIL import Image; import io
    if hasattr(_r, "convert"): return _r.convert("RGB")
    b = (_r.get("bytes") or _r.get("data")) if isinstance(_r, dict) else None
    return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(_r["path"]).convert("RGB")
IMAGE = _to_pil_r(_raw_r)   # real robot scene image (ALOHA top-view camera)
IMAGE.save("scene.jpg")



# ════ FILL IN — each function raises until you write it ════

def load_model():
    """TODO 1: Load SAM('sam2.1_b.pt') (downloads once); return it."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_model() not written yet")


def segment(model):
    """TODO 2: Run the model on 'scene.jpg' and return the results object (the first element)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: segment() not written yet")


# ════ TESTS — run `pytest Day04_run_sam_2_on_robot_scene.py` (or `python Day04_run_sam_2_on_robot_scene.py`). All green = you're done. ════

def test_segment_returns_masks():
    r = segment(load_model())
    assert r is not None and getattr(r, "masks", None) is not None, "segment() should return masks"
    assert len(r.masks) >= 1, "expected at least one object mask on the scene"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
