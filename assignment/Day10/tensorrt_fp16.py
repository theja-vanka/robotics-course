"""
Day 10 · 🗜️ Compression — TensorRT FP16
TASK:    Convert model to FP16 TRT engine. Benchmark vs FP32 TRT. Calculate speedup ratio.
OUTCOME: A before/after measurement for Compression — TensorRT FP16.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day10_tensorrt_fp16.py     (or just:  python Day10_tensorrt_fp16.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Grasp detection — awareness; see how a policy's action could ground to a grasp.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day10.md
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

_IMG = load_dataset("lerobot/aloha_sim_insertion_human", split="train")[0]["observation.images.top"].convert("RGB")
EXAMPLE_INPUT = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])(_IMG).unsqueeze(0)

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def export_to_onnx():
    """TODO 1: Export resnet18(weights='DEFAULT').eval() to 'model.onnx'. Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: export_to_onnx() not written yet")


def build_engine(onnx_path, half=False):
    """TODO 2: Build an engine (TRT, or ort.InferenceSession stand-in). half=True selects the FP16 path. Return it."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: build_engine() not written yet")


def speedup(onnx_path):
    """TODO 3: Build FP32 and FP16 engines, time a forward pass on each, and return fp32_ms / fp16_ms (the speedup ratio, a float > 0)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: speedup() not written yet")


# ════ TESTS — run `pytest Day10_tensorrt_fp16.py` (or `python Day10_tensorrt_fp16.py`). All green = you're done. ════

def test_speedup_is_positive_ratio():
    assert speedup(export_to_onnx()) > 0, "report the FP32/FP16 speedup ratio"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
