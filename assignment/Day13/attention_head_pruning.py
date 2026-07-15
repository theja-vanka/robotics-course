"""
Day 13 · 🗜️ Compression — Attention Head Pruning
TASK:    Remove least-important heads in ViT using Taylor expansion importance scores.
OUTCOME: A before/after measurement for Compression — Attention Head Pruning.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day13_attention_head_pruning.py     (or just:  python Day13_attention_head_pruning.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ⭐ policy.py: understand the VLA you'll fine-tune (action tokens, VLM backbone).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day13.md
Setup:  pip install torch pytest
"""
from __future__ import annotations

import torch
import torch.nn as nn

EMBED_DIM, NUM_HEADS = 32, 4
X = torch.randn(1, 5, EMBED_DIM)   # (batch, seq, dim)

def make_mha():
    """PROVIDED: a fresh small multi-head attention block to prune."""
    torch.manual_seed(0)
    return nn.MultiheadAttention(EMBED_DIM, NUM_HEADS, batch_first=True)



# ════ FILL IN — each function raises until you write it ════

def head_importance(mha, x=X):
    """TODO 1: Score each of the NUM_HEADS heads by Taylor-style importance: run mha(x,x,x), backprop a scalar loss (e.g. output.sum()), then per head sum |grad * weight| over that head's slice of in_proj_weight. Return a tensor of length NUM_HEADS."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: head_importance() not written yet")


def prune_heads(mha, importance, k):
    """TODO 2: Zero the in_proj/out_proj weights belonging to the k LEAST-important heads. Return the modified module."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: prune_heads() not written yet")


# ════ TESTS — run `pytest Day13_attention_head_pruning.py` (or `python Day13_attention_head_pruning.py`). All green = you're done. ════

def test_importance_one_per_head():
    imp = head_importance(make_mha())
    assert imp.shape[0] == NUM_HEADS, "one importance score per attention head"

def test_pruning_zeros_weights():
    mha = make_mha()
    before = sum(int((p == 0).sum()) for p in mha.parameters())
    prune_heads(mha, head_importance(mha), 1)
    after = sum(int((p == 0).sum()) for p in mha.parameters())
    assert after > before, "pruning the least-important head must zero some weights"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
