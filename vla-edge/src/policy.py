"""Load + run the VLA policy.  Capstone W1 (run it) & W5 (defend it)   Run: python src/policy.py

Fill in load() then predict(). Each raises NotImplementedError until you write it,
so running the file shows you exactly which step is next.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


class VLAPolicy:
    def __init__(self, model_id: str | None = None, adapter_dir=None):
        self.model_id = model_id or CFG.base_model
        self.adapter_dir = adapter_dir
        self.model = None

    def load(self):
        """TODO 1: load the VLA (SmolVLA via LeRobot); if adapter_dir is set, attach the LoRA adapter."""
        # Hints:
        #   from lerobot.common.policies.factory import make_policy
        #   self.model = make_policy(name="smolvla", ...)
        #   if self.adapter_dir:
        #       from peft import PeftModel
        #       self.model = PeftModel.from_pretrained(self.model, self.adapter_dir)
        # 👇 write your code here, then DELETE the line below
        raise NotImplementedError("TODO 1: load the VLA policy (SmolVLA via LeRobot)")

    def predict(self, observation: dict):
        """TODO 2: format the observation for the policy and return its action.

        `observation` has this shape (matches observe.py output):
            {
              "instruction": "pick up the cube and place it in the box",
              "image": "scene.jpg",          # path OR PIL.Image from lerobot/svla_so100_pickplace
              "objects": ["cup", "block"],   # from detect_objects()
              "depth": <PIL.Image>,          # from estimate_depth()
            }

        LeRobot SmolVLA expects a LeRobotDataset batch dict:
            from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
            ds  = LeRobotDataset("lerobot/svla_so100_pickplace")
            obs = ds[0]   # {'observation.images.laptop': tensor, 'observation.state': tensor, ...}
            action = self.model.select_action(obs)   # returns a 6-DoF action tensor

        Simplest working stub (after load()):
            import torch
            from PIL import Image
            from transformers import AutoProcessor
            img   = Image.open(observation["image"]).convert("RGB") if isinstance(observation["image"], str) else observation["image"]
            proc  = AutoProcessor.from_pretrained(self.model_id)
            inputs = proc(images=img, text=observation["instruction"], return_tensors="pt")
            with torch.no_grad():
                out = self.model(**inputs)
            return out.logits if hasattr(out, "logits") else out
        """
        if self.model is None:
            self.load()
        # 👇 write your code here, then DELETE the line below
        raise NotImplementedError("TODO 2: run the policy on the observation and return the action")


def main():
    pol = VLAPolicy()
    action = pol.predict({"instruction": CFG.task, "image": None, "objects": []})
    print("action:", action)


if __name__ == "__main__":
    main()
