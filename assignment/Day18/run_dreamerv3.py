"""
Day 18 · 🛠️ Hands-on — Run DreamerV3
TASK:    Run DreamerV3 on DMControl walker-walk; visualise imagined vs real rollouts. Deliverable: a rollout GIF + a return curve reaching at least 300. Paper: DreamerV3 (arXiv 2301.04104).
OUTCOME: Working code plus saved output for Run DreamerV3.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day18_run_dreamerv3.py     (or just:  python Day18_run_dreamerv3.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  World models + Jetson context → fixes your deploy target and latency budget.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day18.md
Setup:  pip install # clone DreamerV3 (see resources) pytest
"""
from __future__ import annotations

import pytest
# World models: clone danijar/dreamerv3; run on DMControl.

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def run_dreamer():
    """TODO 1: Run DreamerV3 on a DMControl task; return the log dir."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: run_dreamer() not written yet")


# ════ TESTS — run `pytest Day18_run_dreamerv3.py` (or `python Day18_run_dreamerv3.py`). All green = you're done. ════

@pytest.mark.skip(reason="needs an external repo + GPU — verify by hand, see the Day note")
def test_run_dreamer():
    assert run_dreamer() is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
