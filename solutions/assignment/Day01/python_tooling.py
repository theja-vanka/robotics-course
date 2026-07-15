"""
Day 01 · 🛠️ Hands-on — Python Tooling
TASK:    Verify the GPU and import diffusers, transformers, open3d, pymilvus, ultralytics. Deliverable: torch.cuda.is_available()==True, every library version printed with no MISSING, and a 1-line CUDA tensor op runs.
OUTCOME: Working code plus saved output for Python Tooling.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day01_python_tooling.py     (or just:  python Day01_python_tooling.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Stub the vla-edge repo + env; get SmolVLA running on one sample observation.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day01.md
Setup:  pip install torch pytest
"""

from __future__ import annotations

import importlib

import torch

# ════ FILL IN — each function raises until you write it ════


def report_env() -> dict:
    """Return {'cuda': bool, 'mps': bool, 'torch': version_str}."""
    return {
        "cuda": torch.cuda.is_available(),
        "mps": torch.backends.mps.is_available(),
        "torch": torch.__version__,
    }


def check_libraries() -> dict:
    """Return {name: version_or_None} for the core CV/robotics stack."""
    libs = ["torch", "transformers", "diffusers", "pymilvus", "ultralytics"]
    result = {}
    for name in libs:
        try:
            m = importlib.import_module(name)
            result[name] = getattr(m, "__version__", "installed")
        except ImportError:
            result[name] = None
    return result


# ════ TESTS — run `pytest Day01_python_tooling.py` (or `python Day01_python_tooling.py`). All green = you're done. ════


def test_report_env():
    e = report_env()
    assert isinstance(e, dict) and "cuda" in e and "torch" in e


def test_torch_present():
    libs = check_libraries()
    assert isinstance(libs, dict) and libs.get("torch") is not None, (
        "torch should be installed"
    )


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
