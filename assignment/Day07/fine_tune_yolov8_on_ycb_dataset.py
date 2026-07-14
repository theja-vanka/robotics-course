"""
Day 07 · 🛠️ Hands-on — Fine-tune YOLOv8 on YCB Dataset
TASK:    Fine-tune YOLO11n on 10 YCB-Video classes for 30 epochs. Deliverable: mAP50 at least 0.6 on the val split + a confusion matrix. Paper: Focal Loss / RetinaNet (arXiv 1708.02002).
OUTCOME: Working code plus saved output for Fine-tune YOLOv8 on YCB Dataset.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day07_fine_tune_yolov8_on_ycb_dataset.py     (or just:  python Day07_fine_tune_yolov8_on_ycb_dataset.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  observe.py: plug in YOLO26 detection → an object list the policy can use.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day07.md
Setup:  pip install ultralytics pytest pytest
"""
from __future__ import annotations

import pytest
from ultralytics import YOLO

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def load_model():
    """TODO 1: Load YOLO('yolo11n.pt') (downloads once); return it."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: load_model() not written yet")


def fine_tune(model, data='coco8.yaml', epochs=1):
    """TODO 2: Fine-tune on a small dataset — use ultralytics' bundled 'coco8.yaml' as a stand-in for 10 YCB classes. Return the training results. (Real task: YCB, 30 epochs.)"""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: fine_tune() not written yet")


def evaluate(model):
    """TODO 3: Validate the model; return the metrics object (has .box.map50)."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: evaluate() not written yet")


# ════ TESTS — run `pytest Day07_fine_tune_yolov8_on_ycb_dataset.py` (or `python Day07_fine_tune_yolov8_on_ycb_dataset.py`). All green = you're done. ════

def test_model_loads_pretrained():
    assert len(load_model().names) == 80, "yolo11n starts COCO-pretrained (80 classes)"

@pytest.mark.skip(reason="fine-tuning downloads a dataset + wants a GPU — run it by hand, see the Day note")
def test_fine_tune_then_eval():
    m = load_model(); fine_tune(m); r = evaluate(m)
    assert r is not None


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
