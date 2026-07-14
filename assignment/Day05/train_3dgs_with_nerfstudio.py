"""
Day 05 · 🛠️ Hands-on — Train 3DGS with Nerfstudio
TASK:    Capture a 30-frame video; train splatfacto (Nerfstudio) to a stable loss; render 3 novel views. Deliverable: a .ply of Gaussians + 3 rendered views. Paper: 3D Gaussian Splatting (arXiv 2308.04079).
OUTCOME: Working code plus saved output for Train 3DGS with Nerfstudio.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day05_train_3dgs_with_nerfstudio.py     (or just:  python Day05_train_3dgs_with_nerfstudio.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  3D representations — awareness; note where 3DGS could enrich observations later.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day05.md
Setup:  pip install nerfstudio pytest
"""
from __future__ import annotations

import pytest
import subprocess  # nerfstudio is CLI-driven

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def train_splat():
    """TODO 1: Shell out to `ns-process-data` then `ns-train splatfacto` on your captured video; return the run dir."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: train_splat() not written yet")


# ════ TESTS — run `pytest Day05_train_3dgs_with_nerfstudio.py` (or `python Day05_train_3dgs_with_nerfstudio.py`). All green = you're done. ════

@pytest.mark.skip(reason="needs an external repo + GPU — verify by hand, see the Day note")
def test_train_splat():
    assert train_splat() is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
