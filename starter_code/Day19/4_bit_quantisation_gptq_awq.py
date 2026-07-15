"""
Day 19 · 🗜️ Compression — 4-bit Quantisation (GPTQ/AWQ)
TASK:    Apply GPTQ to OpenVLA. Compare 4-bit vs 8-bit vs 16-bit speed and action quality.
OUTCOME: A before/after measurement for Compression — 4-bit Quantisation (GPTQ/AWQ).

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day19_4_bit_quantisation_gptq_awq.py     (or just:  python Day19_4_bit_quantisation_gptq_awq.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ⭐ compress.py: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day19.md
Setup:  pip install torch pytest
"""
from __future__ import annotations

import torch
torch.manual_seed(0)
W = torch.randn(256, 256)   # weights to quantize (GPTQ/AWQ operate per-layer like this)



# ════ FILL IN — each function raises until you write it ════

def quantize(weight, bits):
    """TODO 1: Simulate `bits`-bit quantization: map weight to 2**bits evenly-spaced levels across [min,max], then back. Return the quantized weight (same shape, float)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: quantize() not written yet")


def quant_error(weight, bits):
    """TODO 2: Return the relative error ||W - quantize(W,bits)|| / ||W||."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: quant_error() not written yet")


def compare_bits(weight, bits_list=(16, 8, 4)):
    """TODO 3: Return {bits: quant_error(weight,bits)} for each width — your 4 vs 8 vs 16-bit table."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: compare_bits() not written yet")


# ════ TESTS — run `pytest Day19_4_bit_quantisation_gptq_awq.py` (or `python Day19_4_bit_quantisation_gptq_awq.py`). All green = you're done. ════

def test_more_bits_less_error():
    assert quant_error(W, 8) < quant_error(W, 4), "8-bit is finer than 4-bit"

def test_compare_is_monotonic():
    d = compare_bits(W)
    assert set(d) == {16, 8, 4} and d[16] <= d[8] <= d[4], "error grows as bit-width shrinks"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
