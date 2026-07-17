"""
Day 21 · 🗜️ Compression — Speculative Decoding Hands-on
TASK:    Implement simple speculative decoding loop with small draft + large target VLM.
OUTCOME: A before/after measurement for Compression — Speculative Decoding Hands-on.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest speculative_decoding_hands_on.py     (or just:  python speculative_decoding_hands_on.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] Baseline and post-change numbers are both recorded
  [ ] The accuracy-vs-speed trade-off is written down
  [ ] Your benchmark table is updated

CAPSTONE TODAY:  ML refresh (skim) — solidify the eval math behind your benchmarks.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day21.md
Setup:  pip install  pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

def target_next(seq):
    """PROVIDED: the large target model's 'true' next token (here: previous + 1)."""
    return seq[-1] + 1



# ════ FILL IN — each function raises until you write it ════

def draft_propose(prefix, n=4):
    """TODO 1: Cheap draft policy: propose n next tokens, each = previous + 1 (a fast guess). Return a list of n ints."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: draft_propose() not written yet")


def speculative_decode(prefix, steps=3):
    """TODO 2: Loop: draft_propose, then accept the longest run where proposed[i] == target_next(prefix+accepted); append the accepted tokens PLUS one corrected target token; repeat. Return the final sequence. (target_next is PROVIDED.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: speculative_decode() not written yet")


# ════ TESTS — run `pytest speculative_decoding_hands_on.py` (or `python speculative_decoding_hands_on.py`). All green = you're done. ════

def test_decode_matches_autoregressive():
    # draft (+1) agrees with the target rule (+1), so speculation reproduces plain decoding.
    out = speculative_decode([0], steps=5)
    assert out[:6] == [0, 1, 2, 3, 4, 5], "accepted speculation must equal the autoregressive sequence"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
