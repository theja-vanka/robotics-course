"""Frame → structured observation for the policy.  Capstone W3-4   Run: python src/observe.py

Fill in detect_objects() then estimate_depth(). observe() composes them. Each raises
until written, so the file stops at the next step you need to do.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def _get_test_frame(path: str = "scene.jpg") -> str:
    """PROVIDED: download frame 0 from lerobot/svla_so100_pickplace and save as `path`.

    This gives you a real robot tabletop scene (SO-100 arm, object to pick up) — the exact
    kind of image detect_objects() and estimate_depth() should process in production.
    The image is cached after the first download.
    """
    if not os.path.exists(path):
        from datasets import load_dataset
        print(f"[observe] downloading SO-100 test frame → {path} …")
        ds  = load_dataset("lerobot/svla_so100_pickplace", split="train")
        cam = next(k for k in ds.column_names if k.startswith("observation.images."))
        ds[0][cam].convert("RGB").save(path)
        print(f"[observe] saved {ds[0][cam].size} frame from camera '{cam}'")
    return path


def detect_objects(image_path: str) -> list:
    """TODO 1 (W3): run YOLO on the SO-100 tabletop scene; return a list of detected object names.

    Hint:
        from ultralytics import YOLO
        m = YOLO("yolo11n.pt")            # downloads once (~6 MB)
        r = m(image_path)[0]
        return sorted({m.names[int(b.cls)] for b in r.boxes})

    On the SO-100 pick-place scene you should see at least: 'cup', 'bowl', or 'bottle'
    depending on the episode.  Swap YOLO for SAM2 to get per-pixel masks instead.
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO 1: detect objects in the SO-100 tabletop frame")


def estimate_depth(image_path: str):
    """TODO 2 (W4): run Depth Anything V2-Small on the tabletop scene; return the depth PIL image.

    Hint:
        from transformers import pipeline as hf_pipeline
        est = hf_pipeline("depth-estimation",
                          model="depth-anything/Depth-Anything-V2-Small-hf")
        return est(image_path)["depth"]   # PIL.Image, same size as input

    You can save it with:  depth_map.save("depth.png")
    Then back-project to a point cloud (see Day08_run_depth_anything_v2_point_cloud.py).
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO 2: estimate depth for the SO-100 tabletop frame")


def observe(image_path: str) -> dict:
    """Turn a raw frame into the dict the policy conditions on (provided — composes the steps above)."""
    return {
        "instruction": CFG.task,
        "image": image_path,
        "objects": detect_objects(image_path),
        "depth": estimate_depth(image_path),
    }


def main():
    img = _get_test_frame("scene.jpg")   # real SO-100 tabletop frame
    print("Observation:", observe(img))


if __name__ == "__main__":
    main()
