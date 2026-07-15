"""
Day 22 · 🛠️ Hands-on — Add Latency Profiler
TASK:    Add per-stage timing to the Day-20 pipeline; log to CSV; find the bottleneck. Deliverable: a CSV of per-stage ms + the slowest stage named + one optimization tried (before/after).
OUTCOME: Working code plus saved output for Add Latency Profiler.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day22_add_latency_profiler.py     (or just:  python Day22_add_latency_profiler.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  System-design the vla-edge service; write the architecture section of the README.
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day22.md
Setup:  pip install  pytest
"""
from __future__ import annotations

import os
import time
import csv



# ════ FILL IN — each function raises until you write it ════

def time_stages(stages):
    """TODO 1: Given a list of (name, callable) stages, run each, time it, and return {name: elapsed_ms}."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 1: time_stages() not written yet")


def log_csv(timings, path='latency.csv'):
    """TODO 2: Write the per-stage timings to a CSV (columns: stage, ms). Return the path."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 2: log_csv() not written yet")


def bottleneck(timings):
    """TODO 3: Return the NAME of the slowest stage."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("Step 3: bottleneck() not written yet")


# ════ TESTS — run `pytest Day22_add_latency_profiler.py` (or `python Day22_add_latency_profiler.py`). All green = you're done. ════

def test_finds_bottleneck():
    stages = [("fast", lambda: None), ("slow", lambda: time.sleep(0.02))]
    t = time_stages(stages)
    assert bottleneck(t) == "slow", "the slowest stage is the bottleneck"

def test_csv_written():
    p = log_csv(time_stages([("a", lambda: None)]))
    assert os.path.exists(p)


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
