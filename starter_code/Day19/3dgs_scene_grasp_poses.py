"""
Day 19 · 🛠️ Hands-on — 3DGS Scene + Grasp Poses
TASK:    Reconstruct a tabletop with 3DGS; export Gaussians; compute grasp poses on the geometry. Deliverable: a .ply + top-5 grasps overlaid. Paper: 3D Gaussian Splatting (arXiv 2308.04079).
OUTCOME: Working code plus saved output for 3DGS Scene + Grasp Poses.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest 3dgs_scene_grasp_poses.py     (or just:  python 3dgs_scene_grasp_poses.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  ⭐ compress.py: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day19.md
Setup:  pip install nerfstudio pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import pytest
import subprocess  # nerfstudio is CLI-driven



# ════ FILL IN — each function raises until you write it ════

def train_splat():
    """TODO 1: Shell out to `ns-process-data` then `ns-train splatfacto` on your captured video; return the run dir."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: train_splat() not written yet")


# ════ TESTS — run `pytest 3dgs_scene_grasp_poses.py` (or `python 3dgs_scene_grasp_poses.py`). All green = you're done. ════

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
