"""
Day 03 · 🗜️ Compression — INT8 PTQ
TASK:    Apply torch.quantization.quantize_dynamic. Compare accuracy, size, latency vs FP32.
OUTCOME: A before/after measurement for Compression — INT8 PTQ.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day03_int8_ptq.py     (or just:  python Day03_int8_ptq.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day03.md
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

# WHERE the metrics get logged — one row per variant. (In the vla-edge capstone this is
# benchmarks/results.csv via eval.log_row(); here it's a local results.csv you screenshot.)
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS_CSV = os.path.join(_ROOT, "results.csv")

def measure(model, example_input=EXAMPLE_INPUT, runs: int = 50) -> dict:
    """PROVIDED — the two metrics that matter for compression:
         size_MB    = total parameter bytes / 1e6
         latency_ms = average wall-clock time of one forward pass."""
    model.eval()
    size_mb = sum(p.numel() * p.element_size() for p in model.parameters()) / 1e6
    latency_ms = -1.0
    try:
        with torch.no_grad():
            for _ in range(5):
                model(example_input)               # warm-up
            t0 = time.perf_counter()
            for _ in range(runs):
                model(example_input)
        latency_ms = round((time.perf_counter() - t0) / runs * 1000, 2)
    except Exception as e:
        print(f"[measure] latency skipped ({type(e).__name__}) — put model + input on the same device/dtype to time it")
    return {"size_MB": round(size_mb, 1), "latency_ms": latency_ms}

def log_metrics(tag: str, metrics: dict) -> str:
    """PROVIDED — append one row to RESULTS_CSV. Call it for 'baseline' AND each compressed variant."""
    is_new = not os.path.exists(RESULTS_CSV)
    with open(RESULTS_CSV, "a", newline="") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["tag", "size_MB", "latency_ms"])
        w.writerow([tag, metrics["size_MB"], metrics["latency_ms"]])
    return RESULTS_CSV



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
    HOW (measure() and log_metrics() are PROVIDED above):
        before = measure(model);            log_metrics("baseline", before)
        after  = measure(compressed);       log_metrics("compressed", after)
        print("baseline:", before, "-> compressed:", after)
    Return (before, after).
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare() not written yet")


# ════ TESTS — run `pytest Day03_int8_ptq.py` (or `python Day03_int8_ptq.py`). All green = you're done. ════

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
