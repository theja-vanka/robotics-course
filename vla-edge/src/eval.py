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
    """TODO: evaluate the policy over `episodes` and return {"success_rate": float}.

    Two paths — pick one:

    ── PATH A: offline dataset replay (no sim needed, good for Day-13 VLA eval) ──
        from datasets import load_dataset
        ds  = load_dataset("lerobot/svla_so100_pickplace", split="train")
        cam = next(k for k in ds.column_names if k.startswith("observation.images."))

        # Group frames into episodes
        from collections import defaultdict
        eps = defaultdict(list)
        for row in ds:
            eps[row["episode_index"]].append(row)

        successes = 0
        for ep_id, frames in list(eps.items())[:episodes]:
            # Feed the last frame of the episode to the policy
            obs = {
                cam:                  frames[-1][cam].convert("RGB"),
                "observation.state":  frames[-1]["observation.state"],
                "instruction":        CFG.task,
            }
            predicted_action = policy.predict(obs)
            gt_action        = frames[-1]["action"]
            # Simple proxy: action error < 0.1 rad → "success"
            import numpy as np
            err = float(np.mean(np.abs(np.array(predicted_action) - np.array(gt_action))))
            successes += int(err < 0.1)

        return {"success_rate": successes / episodes}

    ── PATH B: live sim rollout (LIBERO / Meta-World / your robot) ──
        import gymnasium as gym
        env = gym.make("your-sim-id")
        successes = 0
        for _ in range(episodes):
            obs, _ = env.reset()
            done   = False
            while not done:
                action        = policy.predict(obs)
                obs, _, done, _, info = env.step(action)
            successes += int(info.get("success", False))
        return {"success_rate": successes / episodes}
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO: evaluate the policy — see PATH A (dataset replay) above")


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
