"""
Day 07 · 🗜️ Compression — Distillation Hands-on
TASK:    Distil YOLOv8l → YOLOv8n using soft labels. Compare mAP vs speed.
OUTCOME: A before/after measurement for Compression — Distillation Hands-on.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day07_distillation_hands_on.py     (or just:  python Day07_distillation_hands_on.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  observe.py: plug in YOLO26 detection → an object list the policy can use.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day07.md
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

def load_teacher():
    """TODO 1: Return a big pretrained teacher: resnet50(weights='DEFAULT').eval(). (Task: YOLOv8l — resnet50 stands in.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_teacher() not written yet")


def load_student():
    """TODO 2: Return a small student: resnet18(weights=None). (Task: YOLOv8n — small + untrained.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: load_student() not written yet")


def soft_labels(teacher, x=EXAMPLE_INPUT, temperature=4.0):
    """TODO 3: Return the teacher's SOFTENED probabilities: softmax(teacher(x)/temperature), shape (1,1000)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: soft_labels() not written yet")


def distill_step(student, soft_targets, x=EXAMPLE_INPUT, temperature=4.0):
    """TODO 4: One distillation step: KL-divergence between student log-softmax(x/T) and `soft_targets`. Return the scalar loss tensor."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 4: distill_step() not written yet")


# ════ TESTS — run `pytest Day07_distillation_hands_on.py` (or `python Day07_distillation_hands_on.py`). All green = you're done. ════

def test_student_smaller_than_teacher():
    ts = sum(p.numel() for p in load_teacher().parameters())
    ss = sum(p.numel() for p in load_student().parameters())
    assert ss < ts, "the student must be smaller than the teacher"

def test_soft_labels_are_a_distribution():
    s = soft_labels(load_teacher())
    assert abs(float(s.sum()) - 1.0) < 1e-2 and float(s.min()) >= 0.0, "softmax over classes sums to 1"

def test_distill_loss_is_nonneg_scalar():
    t = load_teacher(); st = load_student()
    loss = distill_step(st, soft_labels(t))
    assert loss.dim() == 0 and float(loss) >= 0.0, "KL distillation loss is a non-negative scalar"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
