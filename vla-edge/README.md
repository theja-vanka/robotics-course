# vla-edge — fine-tune & ship a Vision-Language-Action policy on the edge

> Capstone for the [30-day intensive](../obsidian_vault/Capstone_VLA.md). One repo that grows from "run a VLA" to "fine-tuned + compressed policy hitting a latency budget on edge hardware," with benchmarks and a demo. This README *is* the portfolio piece — rewrite it as the project grows.

## Problem
*(fill in)* Robots need policies that run **in real time on limited on-board compute**. I take a small open VLA (**SmolVLA**), fine-tune it on a task, compress it, and deploy it under a latency budget — measuring quality and speed at every step.

## Approach
```
camera frame ─▶ observe.py ─▶ {instruction, objects, depth}
                                   │
                            policy.py (SmolVLA)  ──train_lora.py──▶ fine-tuned
                                   │                                   │
                                   ▼                            compress.py (4-bit/NVFP4)
                              action (7-DoF)                           │
                                                                  deploy.py ──▶ edge + latency
                                                                       │
                                                                   eval.py ──▶ benchmarks/results.csv
```

## Module map → capstone weeks
| File | Does | Week |
|---|---|---|
| `src/policy.py` | load + run SmolVLA | W1 / W5 |
| `src/observe.py` | frame → structured observation (YOLO/depth) | W3–4 |
| `src/train_lora.py` | LoRA fine-tune | **W6 ⭐** |
| `src/compress.py` | 4-bit / quantization + measure | **W7 ⭐** |
| `src/deploy.py` | latency benchmark + edge | **W8 ⭐** |
| `src/eval.py` | success rate + benchmark CSV | W10 |
| `src/config.py` | one place to tune everything | — |

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt          # install torch for your CUDA: pytorch.org/get-started
```

## How it works
Each module runs its **provided** helpers, then stops at your first `TODO` with a clear
`NotImplementedError` telling you exactly what to write. Check yourself with pytest:
```bash
pytest tests/ -q
```
- ✅ **green** = a provided helper works (`iou`, `benchmark`, `config`, `log_row`).
- ❌ **red** = a lightweight function you write next (`predict`, `observe`, `evaluate`) — these go green as you implement each module.

The three heavy ⭐ steps — `train` (`train_lora.py`), `compress_model` (`compress.py`), `deploy_policy` (`deploy.py`) — aren't unit-tested (a real `train()` is a 2000-step fine-tune). You validate those by **running the module**: `python src/train_lora.py` prints the provided config, then stops at its `NotImplementedError` until you write the loop.

Fill them in order — `policy.py` → `train_lora.py` → `compress.py` → `deploy.py` → `eval.py`; the `pytest` reds turn green and each `python src/<module>` run gets further.

## Results *(fill as you go — this is what gets you hired)*
| Variant | Success rate | p95 latency | Size |
|---|---|---|---|
| baseline (pretrained) | — | — | — |
| + LoRA fine-tune | — | — | — |
| + 4-bit compress | — | — | — |
| on edge (Jetson/sim) | — | — | — |

## Plan B (never lose a day)
No GPU → Colab. No robot → public LeRobot dataset / LIBERO sim. No Jetson → TensorRT on cloud GPU, report the number. OOM → QLoRA + batch 1 + grad-accum. Stuck >90 min → log it, move to the next module.
