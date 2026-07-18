"""
Day 29 · 🗜️ Compression — Final Benchmark
TASK:    Full Day 20 pipeline FP32 vs fully compressed. Document latency, memory, throughput numbers.
OUTCOME: A before/after measurement for Compression — Final Benchmark.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest final_benchmark.py     (or just:  python final_benchmark.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Mock #3 — full defense; tighten the benchmark story.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day29.md
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

def baseline_pipeline():
    """TODO 1: Return the uncompressed pipeline: a list of resnet18(weights=None).eval() stages (the FP32 reference)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: baseline_pipeline() not written yet")


def compressed_pipeline():
    """TODO 2: Return the fully-compressed pipeline (each stage .half()/quantized)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: compressed_pipeline() not written yet")


def report(pipeline):
    """TODO 3: Run EXAMPLE_INPUT through the pipeline; return {'latency_ms':..., 'size_MB':...} totalled over stages. (measure() is PROVIDED.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: report() not written yet")


# ════ TESTS — run `pytest final_benchmark.py` (or `python final_benchmark.py`). All green = you're done. ════

def test_reports_both_metrics():
    r = report(baseline_pipeline())
    assert "latency_ms" in r and "size_MB" in r and r["size_MB"] > 0

def test_compressed_is_smaller():
    base = report(baseline_pipeline())
    comp = report(compressed_pipeline())
    assert comp["size_MB"] <= base["size_MB"], "the compressed pipeline should not be larger"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
