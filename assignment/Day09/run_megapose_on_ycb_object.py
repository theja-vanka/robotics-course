"""
Day 09 · 🛠️ Hands-on — Run MegaPose on YCB Object
TASK:    Run FoundationPose (or MegaPose) on a YCB object; overlay the 6-DoF axes. Deliverable: an axis-overlay image + the 4x4 pose matrix printed, reprojection aligned. Paper: FoundationPose (arXiv 2312.08344).
OUTCOME: Working code plus saved output for Run MegaPose on YCB Object.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day09_run_megapose_on_ycb_object.py     (or just:  python Day09_run_megapose_on_ycb_object.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  6-DoF pose — optional observation enrichment; awareness-level for your target.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day09.md
Setup:  pip install # clone the pose repo (see resources) pytest
"""
from __future__ import annotations

import pytest
# 6-DoF pose: clone FoundationPose (NVIDIA) or MegaPose; follow its README.



# ════ FILL IN — each function raises until you write it ════

def run_pose():
    """TODO 1: Run the pose estimator on a YCB object; return the 6-DoF pose."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: run_pose() not written yet")


# ════ TESTS — run `pytest Day09_run_megapose_on_ycb_object.py` (or `python Day09_run_megapose_on_ycb_object.py`). All green = you're done. ════

@pytest.mark.skip(reason="needs an external repo + GPU — verify by hand, see the Day note")
def test_run_pose():
    assert run_pose() is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
