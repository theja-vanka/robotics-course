"""
Day 12 · 🗜️ Compression — Benchmark Table
TASK:    FP32 vs FP16 vs INT8 for YOLOv8. Create a table: model size, latency, mAP. Plot latency vs mAP.
OUTCOME: A before/after measurement for Compression — Benchmark Table.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest benchmark_table.py     (or just:  python benchmark_table.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Wire observe.py end-to-end + run your first baseline pass (the 'before' number).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day12.md
Setup:  pip install torch torchvision pillow av huggingface_hub pytest   (or: pip install -r ../requirements.txt)
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

def make_variants():
    """TODO 1: Return {'fp32': m, 'fp16': m2, 'int8': m3}: a resnet18(weights=None).eval() and its .half() copy and a torch.quantization.quantize_dynamic copy."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: make_variants() not written yet")


def benchmark_all(variants):
    """TODO 2: For each variant call measure() and log_metrics(name, ...); return {name: metrics}. (measure + log_metrics are PROVIDED.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: benchmark_all() not written yet")


def to_table(results):
    """TODO 3: Return rows [name, size_MB, latency_ms] sorted by size_MB — your benchmark table (the thing you plot)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: to_table() not written yet")


# ════ TESTS — run `pytest benchmark_table.py` (or `python benchmark_table.py`). All green = you're done. ════

def test_three_variants():
    assert {"fp32", "fp16", "int8"} <= set(make_variants())

def test_table_has_a_row_per_variant():
    table = to_table(benchmark_all(make_variants()))
    assert len(table) >= 3 and all(len(row) == 3 for row in table)


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
