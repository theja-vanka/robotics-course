"""
Day 20 · 🗜️ Compression — Compress the Pipeline
TASK:    Quantise each model to INT8/FP16 TRT. Measure total end-to-end latency. Target: <100ms.
OUTCOME: A before/after measurement for Compress the Pipeline.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest compress_the_pipeline.py     (or just:  python compress_the_pipeline.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ⭐ Deploy day: TensorRT/NVFP4 → run on edge (or edge-sim). Ship vla-edge v0.1.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day20.md
Setup:  pip install torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import torch
from torchvision.models import resnet18
from helpers.runtime import DEVICE
from helpers.compress import example_input, measure, log_metrics, RESULTS_CSV

# One real BridgeData V2 frame as a (1,3,224,224) tensor on DEVICE.  measure() + log_metrics()
# are PROVIDED (helpers/compress.py) — call them for the baseline AND each compressed variant.
EXAMPLE_INPUT = example_input()



# ════ FILL IN — each function raises until you write it ════

def build_pipeline():
    """TODO 1: Return a list of 2-3 stage models (e.g. [resnet18(weights=None).eval(), resnet18(weights=None).eval()]) that each run EXAMPLE_INPUT."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_pipeline() not written yet")


def compress_pipeline(stages):
    """TODO 2: Return the stages each compressed (e.g. .half() or quantize_dynamic). A list of compressed models."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: compress_pipeline() not written yet")


def end_to_end_latency(stages):
    """TODO 3: Run EXAMPLE_INPUT through every stage in sequence; return total latency_ms (sum of per-stage measure()['latency_ms']). Target <100ms."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: end_to_end_latency() not written yet")


# ════ TESTS — run `pytest compress_the_pipeline.py` (or `python compress_the_pipeline.py`). All green = you're done. ════

def test_pipeline_runs_before_and_after():
    base = end_to_end_latency(build_pipeline())
    comp = end_to_end_latency(compress_pipeline(build_pipeline()))
    assert base > 0 and comp > 0, "measure end-to-end latency before AND after compressing every stage"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
