"""
Compression-benchmark helpers: one real example input plus the two metrics that matter.

``measure()`` and ``log_metrics()`` are PROVIDED — call them for the baseline AND each
compressed variant, then screenshot ``results.csv`` for your notes.
"""

from __future__ import annotations

import csv
import os
import time

import torch
from torchvision import transforms

from .datasets import BRIDGE, scene_frames
from .runtime import DEVICE

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # starter_code/
RESULTS_CSV = os.path.join(_ROOT, "results.csv")

_PREP = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
_EXAMPLE = None  # lazily built + reused across measure() calls


def example_input() -> torch.Tensor:
    """A (1,3,224,224) tensor from one real BridgeData V2 frame, on DEVICE."""
    img = scene_frames(BRIDGE, 1)[0]
    return _PREP(img).unsqueeze(0).to(DEVICE)


def _default_input() -> torch.Tensor:
    global _EXAMPLE
    if _EXAMPLE is None:
        _EXAMPLE = example_input()
    return _EXAMPLE


def measure(model, example_input=None, runs: int = 50) -> dict:
    """PROVIDED — size_MB (param bytes / 1e6) + latency_ms (avg forward pass)."""
    model.eval()
    x = example_input if example_input is not None else _default_input()
    size_mb = sum(p.numel() * p.element_size() for p in model.parameters()) / 1e6
    latency_ms = -1.0
    try:
        with torch.no_grad():
            for _ in range(5):
                model(x)  # warm-up
            t0 = time.perf_counter()
            for _ in range(runs):
                model(x)
        latency_ms = round((time.perf_counter() - t0) / runs * 1000, 2)
    except Exception as exc:
        print(
            f"[measure] latency skipped ({type(exc).__name__}) — put model + input on the "
            f"same device/dtype to time it"
        )
    return {"size_MB": round(size_mb, 1), "latency_ms": latency_ms}


def log_metrics(tag: str, metrics: dict) -> str:
    """PROVIDED — append one row to RESULTS_CSV (call for 'baseline' AND each variant)."""
    is_new = not os.path.exists(RESULTS_CSV)
    with open(RESULTS_CSV, "a", newline="") as fh:
        writer = csv.writer(fh)
        if is_new:
            writer.writerow(["tag", "size_MB", "latency_ms"])
        writer.writerow([tag, metrics["size_MB"], metrics["latency_ms"]])
    return RESULTS_CSV
