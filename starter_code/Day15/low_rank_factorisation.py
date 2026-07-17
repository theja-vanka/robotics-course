"""
Day 15 · 🗜️ Compression — Low-rank Factorisation
TASK:    SVD decomposition of conv layer weight tensor. Measure accuracy vs compression rate.
OUTCOME: A before/after measurement for Compression — Low-rank Factorisation.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest low_rank_factorisation.py     (or just:  python low_rank_factorisation.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  Generate & inspect your first synthetic demo episodes (MimicGen) — the (obs, instruction, action) data train_lora.py will consume.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day15.md
Setup:  pip install torch pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import torch
torch.manual_seed(0)
W = torch.randn(128, 256)   # a conv/linear weight matrix to factor



# ════ FILL IN — each function raises until you write it ════

def low_rank_approx(weight, rank):
    """TODO 1: Use torch.linalg.svd to return the rank-`rank` approximation of `weight` (SAME shape)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: low_rank_approx() not written yet")


def param_counts(weight, rank):
    """TODO 2: Return (full, factored): full = weight.numel(); factored = rank*(rows+cols) for the two SVD factors."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: param_counts() not written yet")


def reconstruction_error(weight, rank):
    """TODO 3: Return the relative Frobenius error ||W - W_rank|| / ||W|| of the rank-`rank` approximation."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: reconstruction_error() not written yet")


# ════ TESTS — run `pytest low_rank_factorisation.py` (or `python low_rank_factorisation.py`). All green = you're done. ════

def test_shape_preserved():
    assert low_rank_approx(W, 8).shape == W.shape

def test_error_drops_with_more_rank():
    assert reconstruction_error(W, 64) < reconstruction_error(W, 4), "higher rank = lower error"

def test_factored_is_smaller():
    full, fac = param_counts(W, 8)
    assert fac < full, "the two low-rank factors hold fewer params than the dense weight"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
