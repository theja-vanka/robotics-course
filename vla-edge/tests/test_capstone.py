"""Tests for the vla-edge capstone.  Run from the repo root:  pytest tests/ -q

  ✅ GREEN  = a PROVIDED helper works (iou, benchmark, config, log_row).
  ❌ RED    = a function YOU still have to write (policy.predict, observe, evaluate, ...).
The red ones are your to-do list — they go green as you implement each module.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


# ─────────────── provided helpers — these should PASS right away ───────────────

def test_iou_is_exact():
    from eval import iou
    assert abs(iou([0, 0, 2, 2], [1, 1, 3, 3]) - 1 / 7) < 1e-6, "IoU of those boxes is 1/7"
    assert iou([0, 0, 1, 1], [5, 5, 6, 6]) == 0.0


def test_config_has_fields():
    from config import CFG
    for field in ("base_model", "latency_budget_ms", "lora_r", "adapter_dir", "bench_csv"):
        assert hasattr(CFG, field), f"CFG is missing '{field}'"


def test_log_row_writes_csv():
    from eval import log_row
    from config import CFG
    log_row("test_row", {"metric": 1})
    assert CFG.bench_csv.exists(), "log_row should create the benchmark CSV"


def test_benchmark_reports_latency():
    from deploy import benchmark
    r = benchmark(lambda: sum(range(50)), warmup=2, runs=5)
    assert "p50_ms" in r and "p95_ms" in r, "benchmark should report p50/p95 latency"


# ─────────────── functions YOU write — RED until you implement them ───────────────

def test_policy_predict_returns_action():
    from policy import VLAPolicy
    action = VLAPolicy().predict({"instruction": "pick up the cube", "image": None, "objects": []})
    assert action is not None, "policy.predict() should return an action vector"


def test_observe_returns_observation():
    from observe import observe, _get_test_frame
    img = _get_test_frame("scene.jpg")   # downloads real SO-100 frame if not cached
    obs = observe(img)
    assert isinstance(obs, dict) and "objects" in obs, "observe() should return a dict with 'objects'"


def test_evaluate_returns_success_rate():
    import eval as E
    result = E.evaluate(policy=None, episodes=1)
    assert isinstance(result, dict) and "success_rate" in result, "evaluate() should return a success rate"


def test_lora_config_if_peft_installed():
    import importlib.util
    import pytest
    if importlib.util.find_spec("peft") is None:
        pytest.skip("peft not installed — install it on Colab to check this")
    from train_lora import build_lora_config
    assert build_lora_config().r > 0
