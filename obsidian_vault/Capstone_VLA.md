# 🤖 Capstone — Fine-tune & Ship a VLA on the Edge

> **The one thing you're building.** Everything else in the plan is scaffolding for this repo. By the end you have a **fine-tuned, compressed Vision-Language-Action policy running on edge hardware**, with benchmarks and a demo — the single most credible artifact for an **Applied GenAI (robotics-leaning)** role.

**Repo (build from Day 1):** `vla-edge` → grows weekly. Don't wait for "Product Build Day" — the product *is* the course.

---

## 🎯 Why this capstone

| It proves you can… | …which the [[Target_and_SkillMap|target role]] asks for |
|---|---|
| Run + understand a VLA (action tokens, VLM backbone) | Embodied/multimodal foundation models |
| Fine-tune efficiently (LoRA/PEFT) on a real task | The core day-to-day skill |
| Compress for deployment (QLoRA → 4-bit → NVFP4) | Model optimization / inference |
| Deploy on the edge with a latency budget | Shipping, not just notebooks |
| Evaluate honestly + write it up | Communicating results |

**Default models (small-first):** **SmolVLA-450M** (runs on consumer/Colab) → graduate to π0.5 / OpenVLA only if compute allows. Don't start on a 7B model.

---

## 🧱 Repo shape (stub it Week 1)

```
vla-edge/
  README.md            # grows into the story: problem → approach → results
  data/                # LeRobot dataset(s) or sim episodes
  src/
    observe.py         # perception → structured observation (detect/depth)
    policy.py          # load / run the VLA
    train_lora.py      # fine-tune
    compress.py        # QLoRA / 4-bit / TensorRT-NVFP4
    deploy.py          # edge inference + latency benchmark
    eval.py            # success rate, ablations
  benchmarks/          # CSVs + plots (the money shots)
  demo/                # Loom / gif
```
**The scaffold already exists** → [`vla-edge/`](../vla-edge/). Each module runs its **provided** parts, then stops at your first `TODO` with a clear `NotImplementedError`. Verify your work with **`pytest tests/`**: the provided helpers (`iou`, `benchmark`, `config`, `log_row`) pass immediately, and your functions (`predict`, `observe`, `train`, `compress_model`, `deploy_policy`, `evaluate`) go green as you write them. The per-day exercises that feed it live in [`starter_code/`](../starter_code/).

---

## 🗓️ The capstone thread — what the repo *gains* each week

> **Week numbers below = the part-time cadence.** On the **30-Day Intensive** they compress to the 5-week [[Index|calendar]]: fine-tune ≈ Week 3 (Day 14), compress + deploy ≈ Week 4 (Days 19–20), package + launch ≈ Week 5. If you're on the intensive, follow **day numbers**, not these W-numbers.
>
> Spine days feed the capstone; supporting tracks (C++, Milvus, compression) are pulled in **only where they serve it**.

| Wk | Capstone milestone (commit by Friday) | Pull from |
|---|---|---|
| **1** | `policy.py` runs **SmolVLA** inference on one sample observation; you can read the action tokens. README problem statement written. | [[Day13]] (skim early), [[Day01]] setup |
| **2** | Load a **LeRobot dataset** (SO-100 / sim); visualise episodes; CLIP-embed observations into Milvus for retrieval. | [[Day13]] RAG-VLA, [[Day02]] CLIP |
| **3** | `observe.py` v1: add **detection/segmentation** (YOLO26/SAM 3) to turn raw frames into structured observations. | [[Day07]], [[Day04]] |
| **4** | `observe.py` v2: add **depth** (Depth Anything 3) → richer observation/conditioning. Pick your task + success metric. | [[Day08]] |
| **5** | **Baseline eval**: run pretrained SmolVLA on your task; log success rate + failure cases. This is your "before" number. | [[Day12]] eval mindset |
| **6** | ⭐ **Fine-tune**: `train_lora.py` — LoRA fine-tune SmolVLA on your demos. Beat the baseline. | [[Day14]] LoRA/PEFT |
| **7** | ⭐ **Compress**: `compress.py` — QLoRA → 4-bit (GPTQ/AWQ) → measure size/latency/quality deltas. | [[Day14]] QLoRA, [[Day19]] 4-bit |
| **8** | ⭐ **Deploy**: `deploy.py` — TensorRT/NVFP4, run on Jetson **or** cloud-GPU-as-edge; hit a latency budget. **v0.1 shipped.** | [[Day18]] Jetson, [[Day20]] |
| **9** | **Robustness**: generate **synthetic episodes** (BlenderProc/Cosmos) to cover edge cases; re-fine-tune. | [[Day15]], [[Day16]] |
| **10** | **Eval harness + ablations**: success vs compression level; plots in `benchmarks/`. | [[Day23]], [[Day24]] |
| **11** | **Package**: clean README (problem→approach→results), model card, demo gif. **v1.0.0 + MIT license.** | [[Day26]] packaging |
| **12** | **Launch**: writeup/LinkedIn, model on HF Hub, apply to roles. | [[Day27]], [[Day30]] |

⭐ = the three milestones an interviewer will actually probe. Everything before W6 exists to make these real.

---

## 💻 Compute plan (don't lose days to setup)

| Stage | Cheapest thing that works | Upgrade if needed |
|---|---|---|
| Run SmolVLA (inference) | **Colab free / your laptop** (450M fits) | Colab Pro |
| Fine-tune (LoRA) | **Colab Pro / a single RunPod A40 (~$0.4/hr)** | Lambda A100 for speed |
| Compress | Same GPU you trained on | Blackwell (RTX 5090/B200) for real NVFP4 tensor cores |
| "Edge" deploy | **Jetson Orin Nano** (~$249) | Borrow time on Orin AGX; or simulate edge with TensorRT on cloud + report numbers |
| Robot data | **Public LeRobot datasets + sim (LIBERO, Meta-World)** | Real SO-100 arm (~$120) only if you want the flex |

**Rule:** never block the capstone on hardware. If the ideal rig isn't there, take the "cheapest" column and note the limitation in your README.

---

## 🧯 Failure-mode playbook (when a hands-on day fights you)

| Symptom | Plan B (keep moving) |
|---|---|
| Model won't download / OOM on load | Use a smaller checkpoint (SmolVLA-450M, fp16), `device_map="auto"`, or run on Colab. |
| Fine-tune OOMs | QLoRA (4-bit base), batch size 1 + grad-accum, shorter context, freeze the vision encoder. |
| No robot / no demos | Use a **public LeRobot dataset** or a **sim task** (LIBERO). You do not need hardware to learn this. |
| No Jetson | Run TensorRT/NVFP4 on a cloud GPU, report the latency, and *say so* — interviewers care about the method. |
| A frontier repo won't build (pose/SLAM/3DGS) | Drop to the HF/`transformers` or `ultralytics` equivalent; these are **awareness** topics for your target, not blockers. |
| Whole day is stuck | Timebox debugging to 90 min → log the blocker in README → move to the next capstone increment. Stuck ≠ behind. |

---

## 🔁 Rhythm: rest + retention are part of the plan

- **5 study days + 1 light day + 1 full rest day** per week. The rest day has **no screens on this** — it's when memory consolidates. Skipping it is how you forget Week 3 by Week 5.
- **Daily (15 min):** spaced-repetition review — see [[Retention]] + `Flashcards.csv`.
- **Friday (30 min):** write a one-paragraph "what the repo can do now + what I learned" in the README. That *is* your portfolio, accruing weekly.

---

## ✅ Definition of done (the capstone is "interview-ready" when…)

- [ ] `vla-edge` runs end-to-end: observation → fine-tuned policy → action, on edge or edge-simulated hardware
- [ ] A benchmark table: **baseline vs fine-tuned vs compressed** (success rate, latency, size)
- [ ] A 2-min demo + a README that tells the story in problem → approach → results
- [ ] You can whiteboard a VLA, explain LoRA vs QLoRA, and defend your compression trade-offs out loud

*See [[Target_and_SkillMap|🎯 Target & Skill Map]] · [[PartTime_Roadmap|🗓️ Roadmap]] · [[Index|🏠 Index]]*
