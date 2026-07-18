"""
Day 08 · 🗜️ Compression — ONNX Export
TASK:    Export YOLOv8 PyTorch → ONNX. Run inference with onnxruntime. Validate outputs match.
OUTCOME: A before/after measurement for Compression — ONNX Export.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest onnx_export.py     (or just:  python onnx_export.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  observe.py: add Depth Anything depth → richer observation / conditioning.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day08.md
Setup:  pip install onnxruntime torch torchvision numpy pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import onnxruntime as ort  # noqa: F401
import torch
from torchvision.models import resnet18
from helpers.runtime import DEVICE
from helpers.compress import example_input

EXAMPLE_INPUT = example_input()   # (1,3,224,224) real BridgeData V2 frame on DEVICE



# ════ FILL IN — each function raises until you write it ════

def export_to_onnx():
    """TODO 1: Export a model to 'model.onnx'. WHICH MODEL? a small one: m = resnet18(weights='DEFAULT').eval(); torch.onnx.export(m, EXAMPLE_INPUT, 'model.onnx'). (Day 20 capstone: export your fine-tuned SmolVLA instead.) Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: export_to_onnx() not written yet")


def run_onnx():
    """TODO 2: Load 'model.onnx' with onnxruntime and run EXAMPLE_INPUT through it; return the output (a numpy array)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: run_onnx() not written yet")


# ════ TESTS — run `pytest onnx_export.py` (or `python onnx_export.py`). All green = you're done. ════

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
