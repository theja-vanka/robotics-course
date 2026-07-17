"""
Day 18 · 🗜️ Compression — Flash Attention & Speculative Decoding
TASK:    Memory-efficient attention, KV cache, draft + target model speculative decoding.
OUTCOME: A before/after measurement for Compression — Flash Attention & Speculative Decoding.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest flash_attention_speculative_decoding.py     (or just:  python flash_attention_speculative_decoding.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  World models + Jetson context → fixes your deploy target and latency budget.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day18.md
Setup:  pip install torch pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import torch
import torch.nn.functional as F  # noqa: F401
torch.manual_seed(0)
Q = torch.randn(1, 4, 8); K = torch.randn(1, 4, 8); V = torch.randn(1, 4, 8)   # (batch, seq, dim)



# ════ FILL IN — each function raises until you write it ════

def naive_attention(q, k, v):
    """TODO 1: Standard attention: softmax(q @ k^T / sqrt(d)) @ v. Return the output (shape of v)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: naive_attention() not written yet")


def blocked_attention(q, k, v, block=2):
    """TODO 2: Same result as naive_attention but iterate over KEY/VALUE blocks with an online (running max + renormalised) softmax — never materialise the full score matrix. Return the output."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: blocked_attention() not written yet")


def speculative_accept(draft_tokens, target_tokens):
    """TODO 3: Return how many LEADING draft tokens the target accepts = length of the common prefix of the two lists."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: speculative_accept() not written yet")


# ════ TESTS — run `pytest flash_attention_speculative_decoding.py` (or `python flash_attention_speculative_decoding.py`). All green = you're done. ════

def test_flash_matches_naive():
    import torch
    assert torch.allclose(naive_attention(Q, K, V), blocked_attention(Q, K, V), atol=1e-5), "blocked == naive attention"

def test_speculative_prefix_length():
    assert speculative_accept([1, 2, 3, 9], [1, 2, 3, 4]) == 3, "accept the matching prefix, stop at the first mismatch"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
