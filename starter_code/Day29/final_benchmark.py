"""
Day 29 · 🗜️ Compression — Final Benchmark
TASK:    Full Day 20 pipeline FP32 vs fully compressed. Document latency, memory, throughput numbers.
OUTCOME: A before/after measurement for Compression — Final Benchmark.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day29_final_benchmark.py     (or just:  python Day29_final_benchmark.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Mock #3 — full defense; tighten the benchmark story.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day29.md
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


# ════ TESTS — run `pytest Day29_final_benchmark.py` (or `python Day29_final_benchmark.py`). All green = you're done. ════

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
