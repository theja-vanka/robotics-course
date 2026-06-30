"""Frame → structured observation for the policy.  Capstone W3-4   Run: python src/observe.py

Fill in detect_objects() then estimate_depth(). observe() composes them. Each raises
until written, so the file stops at the next step you need to do.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def detect_objects(image_path: str) -> list:
    """TODO 1 (W3): run a detector (YOLO/SAM) on the image and return the list of object names."""
    # Hint: from ultralytics import YOLO; m = YOLO("yolo11n.pt"); r = m(image_path)[0]
    #       return sorted({m.names[int(b.cls)] for b in r.boxes})
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO 1: detect objects in the frame")


def estimate_depth(image_path: str):
    """TODO 2 (W4): run a depth model (Depth Anything) and return the depth map."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO 2: estimate depth for the frame")


def observe(image_path: str) -> dict:
    """Turn a raw frame into the dict the policy conditions on (provided — composes the steps above)."""
    return {
        "instruction": CFG.task,
        "image": image_path,
        "objects": detect_objects(image_path),
        "depth": estimate_depth(image_path),
    }


def main():
    print("Observation:", observe("scene.jpg"))


if __name__ == "__main__":
    main()
