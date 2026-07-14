"""
Day 20 · 🗜️ Compression — Compress the Pipeline
TASK:    Quantise each model to INT8/FP16 TRT. Measure total end-to-end latency. Target: <100ms.
OUTCOME: A before/after measurement for Compress the Pipeline.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day20_compress_the_pipeline.py     (or just:  python Day20_compress_the_pipeline.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ⭐ Deploy day: TensorRT/NVFP4 → run on edge (or edge-sim). Ship vla-edge v0.1.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day20.md
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

_IMG = load_dataset("lerobot/aloha_sim_insertion_human", split="train")[0]["observation.images.top"].convert("RGB")   # real robot scene image (ALOHA top-view camera)
EXAMPLE_INPUT = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])(_IMG).unsqueeze(0)  # (1,3,224,224)
RESULTS_CSV = "results.csv"

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

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


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


# ════ TESTS — run `pytest Day20_compress_the_pipeline.py` (or `python Day20_compress_the_pipeline.py`). All green = you're done. ════

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
