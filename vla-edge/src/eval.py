"""Eval harness: success rate + a benchmark CSV.  Capstone W10   Run: python src/eval.py

Runs today: prints an IoU self-test and writes a demo row to benchmarks/results.csv.
"""
from __future__ import annotations
import sys, os, csv, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def iou(a, b) -> float:
    """IoU of two [x1,y1,x2,y2] boxes — classic eval + interview helper."""
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    union = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / union if union else 0.0


def evaluate(policy, episodes: int = 20) -> dict:
    """TODO: roll out the policy over `episodes` and return its success rate.
    Wire to your sim (LIBERO / Meta-World) or dataset replay + a success check."""
    # Hint:
    #   obs = env.reset(); done = False
    #   while not done: obs, reward, done, info = env.step(policy.predict(obs))
    #   successes += int(info["success"])
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO: roll out the policy and count successes")


def log_row(tag: str, metrics: dict) -> None:
    """Append one row to the benchmark CSV — call it for baseline / tuned / compressed."""
    CFG.bench_csv.parent.mkdir(parents=True, exist_ok=True)
    is_new = not CFG.bench_csv.exists()
    with open(CFG.bench_csv, "a", newline="") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["when", "tag", *metrics.keys()])
        w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), tag, *metrics.values()])
    print(f"logged '{tag}' → {CFG.bench_csv}")


def main():
    # iou() and log_row() are PROVIDED helpers — these two lines run today:
    print("IoU self-test:", round(iou([0, 0, 2, 2], [1, 1, 3, 3]), 3), "(expect 0.143)")
    log_row("baseline", {"success_rate": 0.0, "p50_ms": 0.0, "size_MB": 0.0})  # demo row
    evaluate(policy=None)  # ← stops here until you implement evaluate()


if __name__ == "__main__":
    main()
