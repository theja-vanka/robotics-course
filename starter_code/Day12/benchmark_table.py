"""
Day 12 · 🗜️ Compression — Benchmark Table
TASK:    FP32 vs FP16 vs INT8 for YOLOv8. Create a table: model size, latency, mAP. Plot latency vs mAP.
OUTCOME: A before/after measurement for Compression — Benchmark Table.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day12_benchmark_table.py     (or just:  python Day12_benchmark_table.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Wire observe.py end-to-end + run your first baseline pass (the 'before' number).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day12.md
Setup:  pip install torch torchvision datasets pillow pytest
"""
from __future__ import annotations

import csv
import os
import time
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
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS_CSV = os.path.join(_ROOT, "results.csv")

def measure(model, example_input=EXAMPLE_INPUT, runs: int = 50) -> dict:
    """PROVIDED — size_MB (param bytes/1e6) + latency_ms (avg forward pass)."""
    model.eval()
    size_mb = sum(p.numel() * p.element_size() for p in model.parameters()) / 1e6
    latency_ms = -1.0
    try:
        with torch.no_grad():
            for _ in range(5):
                model(example_input)
            t0 = time.perf_counter()
            for _ in range(runs):
                model(example_input)
        latency_ms = round((time.perf_counter() - t0) / runs * 1000, 2)
    except Exception as e:
        print(f"[measure] latency skipped ({type(e).__name__}) — same device/dtype to time it")
    return {"size_MB": round(size_mb, 1), "latency_ms": latency_ms}

def log_metrics(tag: str, metrics: dict) -> str:
    """PROVIDED — append one row to RESULTS_CSV (call for baseline AND each variant)."""
    is_new = not os.path.exists(RESULTS_CSV)
    with open(RESULTS_CSV, "a", newline="") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["tag", "size_MB", "latency_ms"])
        w.writerow([tag, metrics["size_MB"], metrics["latency_ms"]])
    return RESULTS_CSV



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


# ════ TESTS — run `pytest Day12_benchmark_table.py` (or `python Day12_benchmark_table.py`). All green = you're done. ════

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
