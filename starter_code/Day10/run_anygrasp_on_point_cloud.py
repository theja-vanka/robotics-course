"""
Day 10 · 🛠️ Hands-on — Run AnyGrasp on Point Cloud
TASK:    Run AnyGrasp on the Day-8 point cloud; rank grasps by score. Deliverable: top-5 grasp poses in Open3D + their scores. Paper: AnyGrasp (arXiv 2212.08333).
OUTCOME: Working code plus saved output for Run AnyGrasp on Point Cloud.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day10_run_anygrasp_on_point_cloud.py     (or just:  python Day10_run_anygrasp_on_point_cloud.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Grasp detection — awareness; see how a policy's action could ground to a grasp.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day10.md
Setup:  pip install # clone the grasp repo (see resources) pytest
"""
from __future__ import annotations

import pytest
# Grasping: clone AnyGrasp / GraspNet; needs a point cloud + license.



# ════ FILL IN — each function raises until you write it ════

def run_grasp():
    """TODO 1: Run the grasp model on a point cloud; return the top grasps."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: run_grasp() not written yet")


# ════ TESTS — run `pytest Day10_run_anygrasp_on_point_cloud.py` (or `python Day10_run_anygrasp_on_point_cloud.py`). All green = you're done. ════

@pytest.mark.skip(reason="needs an external repo + GPU — verify by hand, see the Day note")
def test_run_grasp():
    assert run_grasp() is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
