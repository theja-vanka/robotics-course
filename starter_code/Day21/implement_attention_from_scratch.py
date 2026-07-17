"""
Day 21 · 🛠️ Hands-on — Implement Attention from Scratch
TASK:    Implement multi-head self-attention in pure PyTorch (no nn.MultiheadAttention); match torch's output within 1e-4 on a random input. Deliverable: a passing self_test() asserting allclose. Paper: Attention Is All You Need (arXiv 1706.03762).
OUTCOME: Working code plus saved output for Implement Attention from Scratch.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest implement_attention_from_scratch.py     (or just:  python implement_attention_from_scratch.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  ML refresh (skim) — solidify the eval math behind your benchmarks.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day21.md
Setup:  pip install torch numpy pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import torch
import numpy as np



# ════ FILL IN — each function raises until you write it ════

def implement():
    """TODO 1: Implement the function the task describes, from scratch (no high-level libraries). Return its output."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: implement() not written yet")


def self_test():
    """TODO 2: Build a small known input, run implement(), and `assert` the output is what you expect. Return True if it passes."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: self_test() not written yet")


# ════ TESTS — run `pytest implement_attention_from_scratch.py` (or `python implement_attention_from_scratch.py`). All green = you're done. ════

def test_self_test_passes():
    assert self_test() is True, "your own self_test() should return True once implement() is correct"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
