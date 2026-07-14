"""
Day 23 · 🛠️ Hands-on — Custom PyTorch Dataset
TASK:    Implement a PyTorch Dataset + DataLoader for robot trajectory data (image + action + metadata); batch it. Deliverable: a DataLoader yielding correctly-shaped batches + a self_test() asserting batch shapes.
OUTCOME: Working code plus saved output for Custom PyTorch Dataset.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day23_custom_pytorch_dataset.py     (or just:  python Day23_custom_pytorch_dataset.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  eval.py: implement your metrics (success rate, IoU/NMS helpers) cleanly.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day23.md
Setup:  pip install torch pytest
"""
from __future__ import annotations

import torch
from torch.utils.data import Dataset, DataLoader

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def make_dataset(n=64):
    """TODO 1: Return a torch Dataset of n samples; each item = (image tensor [3,8,8], action tensor [7], meta dict). Define a Dataset subclass with __len__ + __getitem__ and return an instance."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: make_dataset() not written yet")


def make_loader(ds, batch_size=8):
    """TODO 2: Wrap `ds` in a DataLoader with the given batch_size; return it."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: make_loader() not written yet")


def batch_shapes(loader):
    """TODO 3: Pull ONE batch and return (tuple(image_batch.shape), tuple(action_batch.shape))."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: batch_shapes() not written yet")


# ════ TESTS — run `pytest Day23_custom_pytorch_dataset.py` (or `python Day23_custom_pytorch_dataset.py`). All green = you're done. ════

def test_batches_have_right_shape():
    img, act = batch_shapes(make_loader(make_dataset()))
    assert img[0] == 8 and act == (8, 7), "DataLoader should yield image [8,3,8,8] + action [8,7] batches"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
