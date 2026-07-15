"""
Day 08 · 🗜️ Compression — ONNX Export
TASK:    Export YOLOv8 PyTorch → ONNX. Run inference with onnxruntime. Validate outputs match.
OUTCOME: A before/after measurement for Compression — ONNX Export.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day08_onnx_export.py     (or just:  python Day08_onnx_export.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  observe.py: add Depth Anything depth → richer observation / conditioning.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day08.md
Setup:  pip install onnxruntime torch torchvision datasets numpy pillow pytest
"""
from __future__ import annotations

import numpy as np
import onnxruntime as ort
import torch
from torchvision.models import resnet18
from torchvision import transforms
from datasets import load_dataset   # OPEN dataset

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")

_ds_r = load_dataset("lerobot/aloha_sim_insertion_human_image", split="train")
_cam_r = next(k for k in _ds_r.column_names if "images" in k)
_raw_r = _ds_r[0][_cam_r]
def _to_pil_r(_r):
    from PIL import Image; import io
    if hasattr(_r, "convert"): return _r.convert("RGB")
    b = (_r.get("bytes") or _r.get("data")) if isinstance(_r, dict) else None
    return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.open(_r["path"]).convert("RGB")
_IMG = _to_pil_r(_raw_r)   # real robot scene image (ALOHA top-view camera)
EXAMPLE_INPUT = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])(_IMG).unsqueeze(0).to(DEVICE)  # (1,3,224,224) on DEVICE



# ════ FILL IN — each function raises until you write it ════

def export_to_onnx():
    """TODO 1: Export a model to 'model.onnx'. WHICH MODEL? a small one: m = resnet18(weights='DEFAULT').eval(); torch.onnx.export(m, EXAMPLE_INPUT, 'model.onnx'). (Day 20 capstone: export your fine-tuned SmolVLA instead.) Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: export_to_onnx() not written yet")


def run_onnx():
    """TODO 2: Load 'model.onnx' with onnxruntime and run EXAMPLE_INPUT through it; return the output (a numpy array)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: run_onnx() not written yet")


# ════ TESTS — run `pytest Day08_onnx_export.py` (or `python Day08_onnx_export.py`). All green = you're done. ════

def test_onnx_file_created():
    p = export_to_onnx()
    import os; assert os.path.exists(p), "export_to_onnx() should write the .onnx file"

def test_onnx_runs():
    out = run_onnx()
    assert hasattr(out, "shape") and out.shape[0] == 1, "run_onnx() should return the model output"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
