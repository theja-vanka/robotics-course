"""LoRA fine-tune the VLA.  Capstone W6 ⭐   Run: python src/train_lora.py

build_lora_config() is PROVIDED (a correct PEFT config). You write train(). It raises
until you do, so running the file shows your config then stops at the loop.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def build_lora_config():
    """A correct PEFT LoRA config. Tune r/alpha; set target_modules to your model's proj names."""
    from peft import LoraConfig
    return LoraConfig(
        r=CFG.lora_r,
        lora_alpha=CFG.lora_alpha,
        lora_dropout=CFG.lora_dropout,
        bias="none",
        target_modules=["q_proj", "v_proj"],   # TODO: confirm names (print(model) to find them)
    )


def train():
    """TODO ⭐: write the LoRA fine-tune loop:
       1. base = load policy (see policy.py)
       2. from peft import get_peft_model;  model = get_peft_model(base, build_lora_config())
       3. data = LeRobotDataset(CFG.dataset_repo_id)
       4. for step in range(CFG.steps): loss = model(**batch).loss; loss.backward(); opt.step()
       5. model.save_pretrained(CFG.adapter_dir)
    Plan B (OOM): QLoRA — load base in 4-bit (see compress.py), batch_size=1 + grad-accum,
                  freeze the vision encoder, shorten context."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO ⭐: write the LoRA fine-tune loop")


def main():
    print(f"LoRA fine-tune of {CFG.base_model}")
    try:
        print("config (provided):", build_lora_config())
    except ImportError:
        print("  (pip install peft to see the config)")
    train()  # ← stops here until you write the training loop


if __name__ == "__main__":
    main()
