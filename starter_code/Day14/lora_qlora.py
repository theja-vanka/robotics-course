"""
Day 14 · 🗜️ Compression — LoRA + QLoRA
TASK:    Apply 4-bit QLoRA to OpenVLA with bitsandbytes. Compare memory vs full fine-tune.
OUTCOME: A before/after measurement for Compression — LoRA + QLoRA.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest lora_qlora.py     (or just:  python lora_qlora.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ⭐ train_lora.py: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day14.md
Setup:  pip install torch pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import torch
import torch.nn as nn

def make_base():
    """PROVIDED: the base Linear layer you adapt (64->64)."""
    torch.manual_seed(0)
    return nn.Linear(64, 64)



# ════ FILL IN — each function raises until you write it ════

def count_trainable(model):
    """TODO 1: Return the number of parameters with requires_grad=True in `model`."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: count_trainable() not written yet")


def add_lora(base, r=8):
    """TODO 2: Return a LoRA-wrapped version of `base` (a Linear): FREEZE base.weight/bias, add two trainable low-rank matrices A (in_features x r) and B (r x out_features). (QLoRA = this on a 4-bit base.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: add_lora() not written yet")


def compare_trainable(base, lora):
    """TODO 3: Return (full_trainable, lora_trainable) — trainable params of the full model vs the LoRA model. LoRA should be far fewer."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare_trainable() not written yet")


# ════ TESTS — run `pytest lora_qlora.py` (or `python lora_qlora.py`). All green = you're done. ════

def test_lora_has_fewer_trainable():
    base = make_base()
    full, lora_n = compare_trainable(make_base(), add_lora(base))
    assert lora_n < full, "LoRA trains far fewer params than full fine-tune"

def test_lora_param_count_exact():
    lora = add_lora(make_base(), r=8)
    assert count_trainable(lora) == 2 * 64 * 8, "A(64x8) + B(8x64) = 1024 trainable params at r=8"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
