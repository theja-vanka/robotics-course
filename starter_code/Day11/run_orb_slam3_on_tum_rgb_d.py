"""
Day 11 · 🛠️ Hands-on — Run ORB-SLAM3 on TUM RGB-D
TASK:    Build ORB-SLAM3; run on the TUM RGB-D fr1/desk sequence. Deliverable: estimated trajectory vs ground truth (ATE RMSE reported) + a map screenshot. Paper: ORB-SLAM3 (arXiv 2007.11898).
OUTCOME: Working code plus saved output for Run ORB-SLAM3 on TUM RGB-D.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day11_run_orb_slam3_on_tum_rgb_d.py     (or just:  python Day11_run_orb_slam3_on_tum_rgb_d.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  SLAM — awareness only, don't build. It's the 'where am I' layer, noted for context.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day11.md
Setup:  pip install # mostly C++ (ORB-SLAM3) pytest
"""
from __future__ import annotations

import pytest
# SLAM is C++: build ORB-SLAM3, run on a TUM RGB-D sequence.



# ════ FILL IN — each function raises until you write it ════

def run_slam():
    """TODO 1: Run ORB-SLAM3 on a TUM RGB-D sequence; return the trajectory path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: run_slam() not written yet")


# ════ TESTS — run `pytest Day11_run_orb_slam3_on_tum_rgb_d.py` (or `python Day11_run_orb_slam3_on_tum_rgb_d.py`). All green = you're done. ════

@pytest.mark.skip(reason="needs an external repo + GPU — verify by hand, see the Day note")
def test_run_slam():
    assert run_slam() is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
