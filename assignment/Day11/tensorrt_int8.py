"""
Day 11 · 🗜️ Compression — TensorRT INT8
TASK:    INT8 calibration with calibration dataset. Compare INT8 vs FP16 vs FP32 accuracy and speed.
OUTCOME: A before/after measurement for Compression — TensorRT INT8.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day11_tensorrt_int8.py     (or just:  python Day11_tensorrt_int8.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  SLAM — awareness only, don't build. It's the 'where am I' layer, noted for context.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day11.md
Setup:  pip install onnxruntime torch torchvision datasets numpy pillow pytest
"""
from __future__ import annotations

import os
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
EXAMPLE_INPUT = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])(_IMG).unsqueeze(0).to(DEVICE)



# ════ FILL IN — each function raises until you write it ════

def export_to_onnx():
    """TODO 1: Export resnet18(weights='DEFAULT').eval() to 'model.onnx'. Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: export_to_onnx() not written yet")


def calibrate(onnx_path, n=100):
    """TODO 2: Run a calibration pass over n EXAMPLE_INPUT copies to collect per-tensor activation min/max for INT8. Return the ranges (a dict or calibrator)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: calibrate() not written yet")


def compare_precisions(onnx_path):
    """TODO 3: Build + time engines at fp32, fp16 and int8; return {'fp32': ms, 'fp16': ms, 'int8': ms}."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare_precisions() not written yet")


# ════ TESTS — run `pytest Day11_tensorrt_int8.py` (or `python Day11_tensorrt_int8.py`). All green = you're done. ════

def test_calibration_returns_ranges():
    r = calibrate(export_to_onnx(), n=8)
    assert r is not None and len(r) >= 1, "calibration must collect at least one activation range"

def test_three_precisions_timed():
    d = compare_precisions(export_to_onnx())
    assert set(d) == {"fp32", "fp16", "int8"} and all(v > 0 for v in d.values())


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
