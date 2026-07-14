"""
Day 15 · 🛠️ Hands-on — Load & Amplify Demo Episodes
TASK:    Load a LeRobot/LIBERO demo set; visualise 3 episodes; map the (image, instruction, action) schema; run MimicGen to amplify ~10 demos → ~100. Deliverable: 100 episodes in LeRobot format + the schema printed. Paper: MimicGen (arXiv 2310.17596).
OUTCOME: Working code plus saved output for Load & Amplify Demo Episodes.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day15_load_amplify_demo_episodes.py     (or just:  python Day15_load_amplify_demo_episodes.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Generate & inspect your first synthetic demo episodes (MimicGen) — the (obs, instruction, action) data train_lora.py will consume.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day15.md
Setup:  pip install lerobot numpy pytest
"""
from __future__ import annotations

import importlib
import pytest
# OPEN robot dataset (LeRobot): real teleop episodes you amplify with MimicGen.
DATASET_ID = "lerobot/svla_so100_pickplace"

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def load_episodes():
    """TODO 1: Load LeRobotDataset(DATASET_ID) and return it."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_episodes() not written yet")


def inspect_schema(ds):
    """TODO 2: Return one frame's schema as {field_name: shape}; it should include the image and the action."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: inspect_schema() not written yet")


def amplify(ds):
    """TODO 3: Amplify the demos with MimicGen (or note the command) and return the NEW episode count (int)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: amplify() not written yet")


# ════ TESTS — run `pytest Day15_load_amplify_demo_episodes.py` (or `python Day15_load_amplify_demo_episodes.py`). All green = you're done. ════

def test_schema_has_action():
    if importlib.util.find_spec("lerobot") is None:
        pytest.skip("pip install lerobot to load the dataset")
    schema = inspect_schema(load_episodes())
    assert any("action" in str(k).lower() for k in schema), "schema should include an action field"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
