"""
Day 14 · 🛠️ Hands-on — Fine-tune a VLA (SmolVLA) with LoRA
TASK:    LoRA fine-tune SmolVLA (r=16, target q_proj/v_proj) on the SO-100 pick-place set for ~2k steps. Deliverable: a saved adapter + train-loss curve; success-rate lift vs zero-shot reported (target at least +10pp). Paper: LoRA (arXiv 2106.09685).
OUTCOME: Working code plus saved output for Fine-tune a VLA (SmolVLA) with LoRA.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day14_fine_tune_a_vla_smolvla_with_lora.py     (or just:  python Day14_fine_tune_a_vla_smolvla_with_lora.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  ⭐ train_lora.py: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day14.md
Setup:  pip install lerobot transformers peft pytest
"""
from __future__ import annotations

import pytest
# LoRA fine-tune SmolVLA on a Colab GPU. (The full training also lives in vla-edge/src/train_lora.py.)
DATASET_ID = "lerobot/svla_so100_pickplace"
ADAPTER_DIR = "adapter"



# ════ FILL IN — each function raises until you write it ════

def build_lora_config():
    """TODO 1: Return a PEFT LoraConfig with r=16, lora_alpha=32, target_modules=['q_proj','v_proj'] (SmolVLA's attention projections)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: build_lora_config() not written yet")


def finetune():
    """TODO 2: Load SmolVLA via LeRobot, wrap it with get_peft_model(model, build_lora_config()), train ~2k steps on DATASET_ID, and save the adapter to ADAPTER_DIR. Return the adapter path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: finetune() not written yet")


# ════ TESTS — run `pytest Day14_fine_tune_a_vla_smolvla_with_lora.py` (or `python Day14_fine_tune_a_vla_smolvla_with_lora.py`). All green = you're done. ════

def test_lora_config_is_r16():
    cfg = build_lora_config()
    assert cfg.r == 16, "task asks for LoRA rank r=16"
    assert "q_proj" in cfg.target_modules, "target the attention projections (q_proj / v_proj)"

@pytest.mark.skip(reason="real fine-tuning is slow — run finetune() on a GPU, then check the adapter dir exists")
def test_finetune_saves_adapter():
    import os
    finetune()
    assert os.path.isdir(ADAPTER_DIR)


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
