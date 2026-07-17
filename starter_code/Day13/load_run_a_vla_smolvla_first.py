"""
Day 13 · 🛠️ Hands-on — Load & Run a VLA (SmolVLA-first)
TASK:    Load SmolVLA-450M via LeRobot; run inference on one frame from the SO-100 pick-place dataset; print the 7-DoF action + decode the action tokens. Deliverable: an action vector + a 2-sentence note on the VLM→action flow. Paper: π0 (arXiv 2410.24164).
OUTCOME: Working code plus saved output for Load & Run a VLA (SmolVLA-first).

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest load_run_a_vla_smolvla_first.py     (or just:  python load_run_a_vla_smolvla_first.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  ⭐ policy.py: understand the VLA you'll fine-tune (action tokens, VLM backbone).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day13.md
Setup:  pip install lerobot transformers numpy pytest   (or: pip install -r ../requirements.txt)
"""
from __future__ import annotations

import numpy as np
# OPEN robot dataset (LeRobot): https://huggingface.co/datasets/lerobot/svla_so100_pickplace
DATASET_ID = "lerobot/svla_so100_pickplace"   # real teleop episodes — see https://huggingface.co/blog/smolvla



# ════ FILL IN — each function raises until you write it ════

def load_policy():
    """TODO 1: Load a small VLA (SmolVLA via LeRobot — see resources). Return the policy object."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_policy() not written yet")


def predict_action(policy):
    """TODO 2: Build an observation by loading frame 0 from LeRobotDataset(DATASET_ID), run the policy on it, and return the action (numpy array / tensor)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: predict_action() not written yet")


# ════ TESTS — run `pytest load_run_a_vla_smolvla_first.py` (or `python load_run_a_vla_smolvla_first.py`). All green = you're done. ════

def test_action_is_vector():
    import numpy as np, torch
    a = predict_action(load_policy())
    a = a.detach().cpu().numpy() if isinstance(a, torch.Tensor) else np.asarray(a)
    assert a.ndim == 1 and a.shape[0] >= 1, f"action should be a 1-D vector, got shape {a.shape}"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
