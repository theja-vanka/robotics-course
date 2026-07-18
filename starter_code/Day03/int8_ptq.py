"""
Day 03 · 🗜️ Compression — INT8 PTQ
TASK:    Apply torch.quantization.quantize_dynamic. Compare accuracy, size, latency vs FP32.
OUTCOME: A before/after measurement for Compression — INT8 PTQ.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest int8_ptq.py     (or just:  python int8_ptq.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day03.md
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

def load_model():
    """TODO 1: Return ResNet-18 in fp32, eval mode:  resnet18(weights='DEFAULT').eval()  (weights download once). (Day 19+ on the VLA: load your fine-tuned SmolVLA like vla-edge/src/policy.py instead.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_model() not written yet")


def compress(model):
    """TODO 2: Apply THIS block's technique and return the new model. fp16 -> model.half(); int8 -> torch.quantization.quantize_dynamic(model, dtype=torch.qint8); prune -> torch.nn.utils.prune.l1_unstructured(...); 4-bit -> bitsandbytes. (The Task line says which.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: compress() not written yet")


def compare(model, compressed):
    """TODO 3: Measure BEFORE and AFTER, print the win, and LOG both rows to RESULTS_CSV (= results.csv).
    HOW (measure() and log_metrics() are PROVIDED by helpers.compress):
        before = measure(model);            log_metrics("baseline", before)
        after  = measure(compressed);       log_metrics("compressed", after)
        print("baseline:", before, "-> compressed:", after)
    Return (before, after).
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare() not written yet")


# ════ TESTS — run `pytest int8_ptq.py` (or `python int8_ptq.py`). All green = you're done. ════

def test_measure_reports_size_and_latency():
    m = measure(load_model())
    assert m["size_MB"] > 0 and m["latency_ms"] > 0, "baseline should report a real size AND latency"

def test_compress_shrinks_or_prunes():
    m = load_model()
    before = sum(p.numel() * p.element_size() for p in m.parameters())
    c = compress(m)
    after = sum(p.numel() * p.element_size() for p in c.parameters())
    zeros = sum(int((p == 0).sum()) for p in c.parameters())
    assert after < before or zeros > 0, "expected a smaller model or pruned (zeroed) weights"

def test_compare_logs_baseline_and_compressed():
    import csv as _csv
    if os.path.exists(RESULTS_CSV):
        os.remove(RESULTS_CSV)
    compare(load_model(), compress(load_model()))
    assert os.path.exists(RESULTS_CSV), "compare() must log metrics to results.csv"
    rows = list(_csv.reader(open(RESULTS_CSV)))
    assert len(rows) >= 3, "expected a header + a baseline row + a compressed row"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
