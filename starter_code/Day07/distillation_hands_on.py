"""
Day 07 · 🗜️ Compression — Distillation Hands-on
TASK:    Distil YOLOv8l → YOLOv8n using soft labels. Compare mAP vs speed.
OUTCOME: A before/after measurement for Compression — Distillation Hands-on.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest distillation_hands_on.py     (or just:  python distillation_hands_on.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  observe.py: plug in YOLO26 detection → an object list the policy can use.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day07.md
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


# ════ TESTS — run `pytest distillation_hands_on.py` (or `python distillation_hands_on.py`). All green = you're done. ════

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
