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


def deploy_policy():
    """TODO ⭐: benchmark YOUR compressed policy and hit the latency budget:
       from policy import VLAPolicy
       pol = VLAPolicy(adapter_dir=CFG.adapter_dir); pol.load()
       obs = {...}                       # one real observation (see observe.py)
       return benchmark(lambda: pol.predict(obs))
    benchmark() above is PROVIDED. Fast path: export ONNX -> TensorRT/NVFP4 on Jetson.
    No Jetson? Run TensorRT on a cloud GPU, report the number, say so in the README."""
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO ⭐: benchmark your real policy")


def main():
    print("Benchmark-harness check on a DUMMY workload (proves benchmark() works — runs today):")
    benchmark(lambda: sum(i * i for i in range(20_000)))   # provided helper
    deploy_policy()  # ← stops here until you wire your policy


if __name__ == "__main__":
    main()
