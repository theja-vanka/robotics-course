"""Latency benchmark + edge deploy.  Capstone W8 ⭐   Run: python src/deploy.py

This file RUNS today on a dummy workload so you can see the harness work,
then you swap in your compressed policy. The timing pattern here is exactly
what you'll quote in an interview.
"""
from __future__ import annotations
import sys, os, time, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def benchmark(infer_fn, warmup=None, runs=None, budget_ms=None) -> dict:
    """Warm up, then time `runs` calls. Returns p50/p95 latency in ms."""
    warmup = warmup if warmup is not None else CFG.warmup
    runs = runs if runs is not None else CFG.timed_runs
    budget_ms = budget_ms if budget_ms is not None else CFG.latency_budget_ms

    for _ in range(warmup):
        infer_fn()
    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        infer_fn()
        times.append((time.perf_counter() - t0) * 1000)

    times.sort()
    p50 = statistics.median(times)
    p95 = times[min(int(0.95 * len(times)), len(times) - 1)]
    print(f"latency: p50={p50:.2f}ms  p95={p95:.2f}ms  (budget {budget_ms}ms)")
    print("✅ within budget" if p95 <= budget_ms else "❌ over budget — compress more / shrink inputs")
    return {"p50_ms": round(p50, 2), "p95_ms": round(p95, 2), "within_budget": p95 <= budget_ms}


def _get_obs_for_benchmark():
    """PROVIDED: one real observation from lerobot/svla_so100_pickplace for latency benchmarking.

    Using the same dataset the model was fine-tuned on keeps the input distribution honest.
    Returns a dict matching what VLAPolicy.predict() expects.
    """
    from datasets import load_dataset
    ds  = load_dataset("lerobot/svla_so100_pickplace", split="train")
    cam = next(k for k in ds.column_names if k.startswith("observation.images."))
    row = ds[0]
    return {
        cam:                  row[cam].convert("RGB"),
        "observation.state":  row["observation.state"],
        "instruction":        CFG.task,
    }


def deploy_policy():
    """TODO ⭐: benchmark YOUR compressed policy and prove it hits the latency budget.

    Use _get_obs_for_benchmark() (PROVIDED above) so the benchmark uses real data:

        from policy import VLAPolicy
        pol = VLAPolicy(adapter_dir=CFG.adapter_dir)
        pol.load()

        obs = _get_obs_for_benchmark()          # real SO-100 observation
        result = benchmark(lambda: pol.predict(obs))   # benchmark() is PROVIDED

        from eval import log_row
        log_row("compressed_deploy", result)    # writes to benchmarks/results.csv
        return result

    Target: p95 < {CFG.latency_budget_ms} ms.

    Fast path to hit budget:
        • Export to ONNX → TensorRT FP16/INT8 (see Day09-11 starter exercises).
        • On Apple Silicon: Core ML conversion (coremltools) + MPS backend.
        • No TensorRT? torch.compile(pol.model, mode="reduce-overhead") gives ~1.5× on MPS.
    No Jetson? Run on a cloud GPU (Colab/Lambda), paste the number here and note it in README.
    benchmark() is PROVIDED — you only need to wire your policy.
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO ⭐: benchmark your real policy — see hint above")


def main():
    print("Benchmark-harness check on a DUMMY workload (proves benchmark() works — runs today):")
    benchmark(lambda: sum(i * i for i in range(20_000)))   # provided helper
    deploy_policy()  # ← stops here until you wire your policy


if __name__ == "__main__":
    main()
