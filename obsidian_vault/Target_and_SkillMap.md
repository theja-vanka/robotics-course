# 🎯 Target & Skill Map

> Anchor the whole plan to a concrete destination, then cut anything that doesn't serve it. Your target: **Applied GenAI Engineer — robotics-leaning** (VLA / generative-for-robotics / embodied AI).

---

## 🧭 The roles you're aiming at (3 composite JDs)

These are stitched from real postings in this niche. Print them; reverse-engineer from them.

**A. Applied AI Engineer — Robotics Foundation Models**
> Build and fine-tune vision-language-action / multimodal models for manipulation. Curate datasets, run PEFT/LoRA training, evaluate policies, and optimize models for real-time on-robot inference. Python/PyTorch; HF/LeRobot; some deployment (TensorRT/ONNX). *Nice to have: synthetic data, world models.*

**B. ML Engineer — Embodied AI / VLA**
> Own the policy-learning loop: data → train → eval → deploy. Improve success rates, reduce latency, ship to edge (Jetson). Comfort with quantization and the perception stack feeding the policy. *Nice to have: ROS2 familiarity.*

**C. Research Engineer — Generative Models for Robotics**
> Prototype with diffusion policies, world models, and VLAs; reproduce papers; build eval harnesses. Strong DL fundamentals, fast experimentation, clear writeups. *Nice to have: 3D / simulation.*

**Common denominator → your spike:** *fine-tune a VLA, compress it, deploy it, prove it works.* That's the [[Capstone_VLA|capstone]].

---

## 🗺️ Skill map — what each role wants → where the plan delivers it

| Skill the JDs ask for | Priority | Where you build it |
|---|---|---|
| VLA architecture & action decoding | 🔴 Core | [[Day13]], capstone W1–2 |
| Efficient fine-tuning (LoRA/QLoRA/PEFT) | 🔴 Core | [[Day14]], capstone W6 |
| Model compression / quantization | 🔴 Core | [[Day19]], compression track, capstone W7 |
| Edge deployment + latency | 🔴 Core | [[Day18]], [[Day20]], capstone W8 |
| Multimodal / VLM (CLIP, encoders) | 🟠 High | [[Day02]], [[Day04]] |
| Perception inputs (detect/depth) | 🟠 High | [[Day07]], [[Day08]] |
| Eval harness + experiment hygiene | 🟠 High | [[Day23]]–[[Day25]], capstone W10 |
| Diffusion / world models (literacy) | 🟡 Useful | [[Day03]], [[Day17]], [[Day18]] |
| Synthetic data | 🟡 Useful | [[Day15]], [[Day16]] |
| Vector DB (Milvus) as a *tool* | 🟢 Support | woven into capstone, not a track |
| SLAM / pose / grasp | 🟢 Awareness | [[Day09]]–[[Day11]] — know what they are |
| C++ / ROS2 | 🟢 Literacy | read & modify only — see below |

---

## ✂️ Keep / Cut — calibrated to *this* target

**Keep & go deep:** VLA fine-tuning · compression/quantization · edge deploy · VLM/multimodal · eval. *(These are the interview.)*

**Demote to literacy/awareness:**
- **C++ → literacy.** Goal: *read and modify* a ROS2/C++ node and explain RAII/pointers. **Not** production CUDA/TensorRT C++. Cap C++ at ~30–45 min/day; never let it block the capstone. (TensorRT/ONNX you'll use via **Python**.)
- **SLAM, 6-DoF pose, grasp, NeRF/3DGS → awareness.** Be able to say what they do and when you'd reach for them. Don't sink days into building them — for an Applied-GenAI role they're context, not core.
- **Milvus → supporting tool.** Use it inside the capstone for observation/demo retrieval. Drop the standalone 30-block track.

**Reclaimed time → ** more reps on fine-tuning, compression, and eval (the things you'll actually be hired to do).

---

## 🩺 Day-0 Diagnostic — skip what you already own

You're **solid in ML, new to robotics/diffusion/SLAM**. Spend ~2 hrs here before Week 1 and **skip or compress** anything you pass.

Rate yourself 1–5. **If ≥4, skip the linked day / use it only as reference.**

| Check | If you can already… | Then |
|---|---|---|
| Backprop & optimizers | derive the chain rule, explain Adam vs SGD | **Skip [[Day21]]** theory |
| Attention | implement multi-head attention from scratch | Skip the Day 21 attention block |
| Transformers/LLMs | explain tokenization, KV cache | Skim only |
| CLIP / VLMs | explain contrastive image-text training | Light pass on [[Day02]] |
| PyTorch fluency | write a custom Dataset + training loop blind | Skip the boilerplate, keep the robotics parts |
| **Diffusion** | *new for you* → **do [[Day03]] fully (1.5×)** | study |
| **SLAM** | *new for you* → **[[Day11]] = awareness only** | watch, don't build |
| **VLA** | *new for you* → **[[Day13]]–[[Day14]] = full depth** | study |

> Write your scores in a `diagnostic.md` in the repo. Re-take the diffusion/VLA rows at Week 6 to see movement — that delta is a great interview story.

---

## 🏁 Program-level definition of done

You're ready to apply when **all** are true:

- [ ] **Capstone shipped:** fine-tuned + compressed VLA running on (simulated-)edge, with a baseline-vs-tuned-vs-compressed benchmark table
- [ ] **One strong repo + 2-min demo + writeup** telling problem → approach → results
- [ ] **Interview-fluent** on: VLA architecture, LoRA vs QLoRA, quantization trade-offs, your eval methodology
- [ ] **Targeted applications out** to ~10 roles matching JDs A/B/C, résumé bullets mapped to the skill table above

*See [[Capstone_VLA|🤖 Capstone]] · [[PartTime_Roadmap|🗓️ Roadmap]] · [[Retention|🧠 Retention]] · [[Index|🏠 Index]]*
