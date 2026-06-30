"""
Day 09 · 🗜️ Compression — TensorRT Basics
TASK:    Install TensorRT. Convert ONNX → TRT engine. Run FP32 inference. Log latency.
OUTCOME: A before/after measurement for Compression — TensorRT Basics.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day09_tensorrt_basics.py     (or just:  python Day09_tensorrt_basics.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  6-DoF pose — optional observation enrichment; awareness-level for your target.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day09.md
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

_IMG = load_dataset("huggingface/cats-image", split="test")[0]["image"].convert("RGB")
EXAMPLE_INPUT = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])(_IMG).unsqueeze(0)

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def export_to_onnx():
    """TODO 1: Export resnet18(weights='DEFAULT').eval() to 'model.onnx' with torch.onnx.export(EXAMPLE_INPUT). Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: export_to_onnx() not written yet")


def build_engine(onnx_path):
    """TODO 2: Build a runnable engine from the ONNX file. With TensorRT: trt.Builder. On CPU/no-TRT: return ort.InferenceSession(onnx_path) as a stand-in. Return the engine/session."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: build_engine() not written yet")


def run_and_time(engine, runs=50):
    """TODO 3: Run EXAMPLE_INPUT through the engine `runs` times; return the average latency in ms (float)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: run_and_time() not written yet")


# ════ TESTS — run `pytest Day09_tensorrt_basics.py` (or `python Day09_tensorrt_basics.py`). All green = you're done. ════

def test_onnx_created():
    assert os.path.exists(export_to_onnx())

def test_engine_latency_positive():
    eng = build_engine(export_to_onnx())
    assert run_and_time(eng) > 0


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
