# 🗓️ Part-Time Roadmap — ~3.5 hrs/day, ~12 Weeks

> [!note] This is your **fallback**, not the primary plan.
> You chose the **30-Day Intensive** (12 hr/day · Mon–Sat · Sunday rest) — start there: [[Index|🏠 Index]] + [[Capstone_VLA|🤖 Capstone]]. Keep this page in your pocket: if 12-hour days stop being sustainable, switch to this ~3.5 hr/day re-pace **without losing any structure** — same files, same capstone, just stretched over ~12 weeks.

> A sustainable re-pacing of the 30-day intensive. **Same content, same files** — just spread out so it sticks, and sequenced for someone **solid in ML but new to robotics, diffusion, and SLAM**.
>
> Suggested start: **Mon 29 Jun 2026**. 5 study days/week, weekends = optional catch-up + rest.

---

## 🎯 How to use this

- The original [[Index|30-day plan]] packs **7 blocks (~12 hrs) into one day**. That's great for a sabbatical, brutal for real life — and cramming hurts retention.
- This roadmap keeps every original day/block, but runs **four lanes in parallel** at a humane pace:
  - 🤖 **Spine** — Gen AI × Robotics CV (the **🧠 New Concept + 🛠️ Hands-on** blocks). *This is your priority.*
  - ⚙️ **C++ & DSA** — the **C++ Literacy** (→ Capstone Lab after Day 12) and **DSA** blocks (evening craft).
  - 🗄️ **Milvus** — the **🔧 Build + Milvus** block.
  - 🗜️ **Compression** — the **🗜️ Compression** block.
- Each calendar day you do **one lane focus (~2.5–3 hr) + a 30-min sidecar** (C++/DSA drills or review). You are **not** doing every track every day anymore.
- Open the linked **Day** file and follow its **🎯 Outcome → ▶️ DO THIS → ✅ Done when** for the relevant block. Tick **Done when** boxes — the [[Dashboard]] reads them.

---

## 🧭 Calibrated for *you* (solid ML, new to robotics/diffusion/SLAM)

| Topic | Your move | Why |
|---|---|---|
| **Day 21 — ML fundamentals refresh** (backprop, optimisers, attention) | **Skim / use as reference.** Do the "implement attention from scratch" only if rusty. | You already have this. Don't spend a full session here. |
| **Day 03 + Day 17 — Diffusion / ControlNet** | **Slow down — budget 1.5×.** Read the Illustrated Stable Diffusion first, *then* the DDPM paper. | New for you; the forward/reverse + score-function intuition takes a beat. |
| **Day 11 — SLAM** | **Slow down — budget 1.5×.** Watch Cyrill Stachniss first for intuition before ORB-SLAM3. | New for you; lots of moving parts (tracking, loop closure, BA). |
| **Days 06–10 — Perception stack** (detect → depth → pose → grasp) | **Core. Full attention.** | This is the robotics bridge you're here for. |
| **Days 13–14 — VLA models** | **Core. Full attention.** | The payoff topic; ties ML you know to robot action. |
| **C++** | Treat as a **steady side-habit**, 30–45 min most days. Don't let it block the spine. | Beginner C++ + advanced robotics at once is the #1 burnout trap. |

> 🔑 **Rule of thumb:** if a session runs long, protect the **Spine** and the **Done-when checks**. Defer the C++ sidecar, not the core learning.

---

## ⏱️ Daily rhythm (~3.5 hr template)

```
00:00–00:15   Warm-up: recall yesterday's "Done when" out loud (the Day's 🌅 block)
00:15–01:45   Spine — 🧠 New Concept (read + from-memory sketch)           [90 min]
01:45–03:15   Spine — 🛠️ Hands-on (run the starter, hit the outcome)        [90 min]
03:15–03:45   Sidecar — C++ drills / DSA OR review flashcards               [30 min]
```

On **lane days** (Milvus / Compression), swap the two Spine slots for that lane's 🔧 Build + Milvus / 🗜️ Compression task + its starter.

---

## 📅 12-Week Plan

> Each week = **5 sessions**. "Spine" cells link the original day's **A+B**. Lanes advance independently. Milestones are the things worth screenshotting for your portfolio.

### 🧱 Phase 1 — Foundations (Weeks 1–2)

| Wk | Spine (A+B) | ⚙️ C++ sidecar | 🗄️ Milvus | 🗜️ Compression | 🏁 Milestone |
|---|---|---|---|---|---|
| **1** | [[Day01]] Landscape + setup · [[Day02]] VLMs (CLIP/LLaVA) | [[Day01]] syntax → [[Day02]] pointers | [[Day01]] first collection | [[Day01]] overview + metrics | Env works; first Milvus search returns top-5 |
| **2** | [[Day03]] **Diffusion (1.5×)** · [[Day04]] ViT + SAM 2/3 · [[Day05]] NeRF→3DGS | [[Day03]] OOP → [[Day04]] smart ptrs | [[Day02]] CLIP→Milvus | [[Day02]] FP16 · [[Day03]] INT8 PTQ | Generate an img2img variant; store 100 CLIP vectors |

### 🤖 Phase 2 — Robotics Perception Stack (Weeks 3–5)

| Wk | Spine (A+B) | ⚙️ C++ sidecar | 🗄️ Milvus | 🗜️ Compression | 🏁 Milestone |
|---|---|---|---|---|---|
| **3** | [[Day06]] Perception pipeline · [[Day07]] Detection (YOLO) | [[Day05]] CMake · [[Day06]] OpenCV | [[Day04]] DINOv2 store | [[Day04]] pruning theory | YOLO fine-tuned on YCB; mAP logged |
| **4** | [[Day08]] Depth · [[Day09]] 6-DoF pose | [[Day07]] ROS2 publisher | [[Day06]] scene retrieval | [[Day08]] ONNX export | Depth→point cloud; FoundationPose axes overlaid |
| **5** | [[Day10]] Grasp · [[Day11]] **SLAM (1.5×)** · [[Day12]] integrate + Mock #1 | [[Day08]] ROS2 images | [[Day11]] semantic SLAM map | [[Day09]] TensorRT FP32 | End-to-end perception pipeline runs once |

### 🧠 Phase 3 — Generative AI for Robotics (Weeks 6–8)

| Wk | Spine (A+B) | ⚙️ C++ sidecar | 🗄️ Milvus | 🗜️ Compression | 🏁 Milestone |
|---|---|---|---|---|---|
| **6** | [[Day13]] VLA deep dive · [[Day14]] Fine-tune VLA (LoRA) | [[Day13]] CUDA intro | [[Day13]] RAG-VLA | [[Day14]] QLoRA | OpenVLA / SmolVLA runs; LoRA fine-tune started |
| **7** | [[Day15]] Synthetic data · [[Day16]] Synthetic pipeline · [[Day17]] **ControlNet (1.5×)** | [[Day14]] TensorRT C++ | [[Day15]] dedup | [[Day15]] low-rank | 500-image synthetic set with COCO labels |
| **8** | [[Day18]] World models · [[Day19]] 3DGS hands-on · [[Day20]] **Product Build #1** | [[Day16]] multi-thread TRT | [[Day20]] pipeline backbone | [[Day20]] compress pipeline | **Product #1 shipped to GitHub + Loom demo** |

### 🎯 Phase 4 — Consolidate, Build #2, Job-Ready (Weeks 9–12)

| Wk | Spine (A+B) | ⚙️ C++ sidecar | 🗄️ Milvus | 🗜️ Compression | 🏁 Milestone |
|---|---|---|---|---|---|
| **9** | [[Day21]] ML refresh *(skim)* · [[Day22]] System design · [[Day23]] Coding patterns | [[Day21]] DSA · [[Day23]] IoU/NMS | [[Day21]] ANN benchmark | [[Day22]] 30ms budget | System-design 1-pager; IoU/NMS from scratch |
| **10** | [[Day24]] Papers speed-run · [[Day25]] **Mock #2** | [[Day22]] design patterns | [[Day24]] Milvus paper | [[Day24]] compression papers | Honest mock score + ranked weakness list |
| **11** | [[Day26]] **Product Build #2 (CLI)** · [[Day28]] Gap-fill weak areas | [[Day26]] gtest wrapper | [[Day26]] auto-index | [[Day26]] `--quantize` | **Product #2 (synthetic-data CLI) shipped** |
| **12** | [[Day27]] Freelance positioning · [[Day29]] Mock #3 · [[Day30]] Launch | [[Day27]]/[[Day30]] profile + tag | [[Day28]] weakness fix | [[Day29]] final benchmark | Portfolio live; applications out |

---

## 🔁 If you fall behind (you will, some weeks)

- **Protect the Spine.** Skipping a C++ or Milvus sidecar for a week is fine. Skipping the robotics core compounds.
- **Half-session option:** do only the **🧠 New Concept block + its Done-when checks**, defer the **🛠️ Hands-on** block to the weekend.
- **Reset, don't spiral:** a missed week just shifts the calendar. The dashboard tracks *blocks done*, not dates.

---

## ➡️ Next steps

- **Starter code** for each 🛠️ Hands-on block lives in `starter_code/` — open the matching `DayNN_*.py`, then `pytest` it until green.
- Track everything on the [[Dashboard]] (live in Obsidian) or open `Progress.html` for a visual snapshot.

*[[Index|🏠 Back to the full 30-day Index]]*
