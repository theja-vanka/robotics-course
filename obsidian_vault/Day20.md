# Day 20 — PRODUCT BUILD DAY #1

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 4 · Tue**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Product Build #1 | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Milvus pipeline backbone | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Compress pipeline | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Union-Find (DSU) | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Product Build #1
- 🗄️ Milvus *(supporting tool)*: Milvus pipeline backbone
- 🗜️ Compression: Compress pipeline
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Union-Find (DSU)

**🤖 Capstone today →** ⭐ **Deploy day**: TensorRT/NVFP4 → run on edge (or edge-sim). Ship `vla-edge` v0.1.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~245 min (~4.1 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 π0.5 on Jetson Thor with NVFP4 — real edge VLA inference — [open](https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/)

---

## 🌅 Warm-up | 9:00–9:30 | Plan
**Task:** Write exactly what you're building before touching code. Spec all inputs/outputs.

**🎯 Outcome:** A short written spec you can execute against for the rest of the day.

**▶️ DO THIS — every step (Obsidian):**

**Step 1.** In Obsidian, make a new note `Day 20 — Plan`.
**Step 2.** Write it out: Write exactly what you're building before touching code. Spec all inputs/outputs.
**Step 3.** Mark the ONE thing that must work by tonight. Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] The spec is written down, not just held in your head
- [ ] Inputs, outputs, and a clear 'done' bar are all defined

- [ ] Block complete

### 📚 Resources

---
## 🧠 New Concept | 9:30–11:00 | Build — Full Python Pipeline
**Task:** Image → SAM 2 segments → Depth Anything depth → MegaPose 6-DoF → AnyGrasp pose → JSON.

**🎯 Outcome:** A working, committed increment of the product for Build — Full Python Pipeline.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get your capstone repo into Colab — paste this in a cell and press **▶**:

```python
!git clone https://github.com/YOUR-USERNAME/vla-edge.git
%cd vla-edge
!pip install -r requirements.txt
```

*(Repo not on GitHub yet? See [[Setup_Guide]] §3 — upload the folder instead.)*
**Step 4.** Run today's module — **+ Code**, paste, **▶**:

```python
!python src/deploy.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Image → SAM 2 segments → Depth Anything depth → MegaPose 6-DoF → AnyGrasp pose → JSON.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [SAM 2 GitHub (Meta)](https://github.com/facebookresearch/segment-anything-2) — ⏱️ ~10 min
- [ ] 📦 [Open3D GitHub](https://github.com/isl-org/Open3D) — ⏱️ ~10 min
- [ ] 📦 [AnyGrasp SDK](https://github.com/graspnet/anygrasp_sdk) — ⏱️ ~10 min
- [ ] 📦 [MegaPose GitHub](https://github.com/megapose6d/megapose6d) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Build — Milvus as Pipeline Backbone
**Task:** Upsert every inference result into Milvus; on startup query for similar past scenes to pre-warm. Deliverable: persists at least 100 results and retrieves top-5 similar scenes in under 50 ms.

**🎯 Outcome:** A working, committed increment of the product for Build — Milvus as Pipeline Backbone.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get your capstone repo into Colab — paste this in a cell and press **▶**:

```python
!git clone https://github.com/YOUR-USERNAME/vla-edge.git
%cd vla-edge
!pip install -r requirements.txt
```

*(Repo not on GitHub yet? See [[Setup_Guide]] §3 — upload the folder instead.)*
**Step 4.** Run today's module — **+ Code**, paste, **▶**:

```python
!python src/deploy.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Upsert every inference result into Milvus; on startup query for similar past scenes to pre-warm. Deliverable: persists at least 100 results and retrieves top-5 similar scenes in under 50 ms.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📄 [Milvus Official Docs](https://milvus.io/docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~25 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Build — FastAPI Server
**Task:** POST image → GET grasp plan JSON. Milvus powers the 'have I seen this before?' check.

**🎯 Outcome:** A working, committed increment of the product for Build — FastAPI Server.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get your capstone repo into Colab — paste this in a cell and press **▶**:

```python
!git clone https://github.com/YOUR-USERNAME/vla-edge.git
%cd vla-edge
!pip install -r requirements.txt
```

*(Repo not on GitHub yet? See [[Setup_Guide]] §3 — upload the folder instead.)*
**Step 4.** Run today's module — **+ Code**, paste, **▶**:

```python
!python src/deploy.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: POST image → GET grasp plan JSON. Milvus powers the 'have I seen this before?' check.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [FastAPI Docs](https://fastapi.tiangolo.com/) — ⏱️ ~15 min
- [ ] 📦 [FastAPI GitHub](https://github.com/tiangolo/fastapi) — ⏱️ ~10 min
- [ ] 🎥 [FastAPI Tutorial — TechWithTim](https://www.youtube.com/watch?v=cbASjoZZGIw) — ⏱️ ~25 min

*⏱️ Resource time this block: ~50 min*

---
## 🗜️ Compression | 15:45–17:15 | Compress the Pipeline
**Task:** Quantise each model to INT8/FP16 TRT. Measure total end-to-end latency. Target: <100ms.

**🎯 Outcome:** A before/after measurement for Compress the Pipeline.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`compress_the_pipeline.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day20/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install onnxruntime torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest compress_the_pipeline.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`compress_the_pipeline.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest compress_the_pipeline.py -q` until **everything is green**. That completes: Quantise each model to INT8/FP16 TRT. Measure total end-to-end latency. Target: <100ms.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [TensorRT Workflow Guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/) — ⏱️ ~15 min
- [ ] 📦 [TensorRT GitHub](https://github.com/NVIDIA/TensorRT) — ⏱️ ~10 min
- [ ] 🔥 📝 [π0.5 on Jetson Thor with NVFP4 — real edge VLA inference](https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: ⭐ **Deploy day**: TensorRT/NVFP4 → run on edge (or edge-sim). Ship `vla-edge` v0.1. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

**🎯 Outcome:** One more measured rep on the capstone — a logged number, not new scaffolding.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get your capstone repo into Colab — paste this in a cell and press **▶**:

```python
!git clone https://github.com/YOUR-USERNAME/vla-edge.git
%cd vla-edge
!pip install -r requirements.txt
```

*(Repo not on GitHub yet? See [[Setup_Guide]] §3 — upload the folder instead.)*
**Step 4.** Run today's module — **+ Code**, paste, **▶**:

```python
!python src/deploy.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: ⭐ **Deploy day**: TensorRT/NVFP4 → run on edge (or edge-sim). Ship `vla-edge` v0.1. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] You ran it again and changed one variable
- [ ] A new number is in your benchmark CSV
- [ ] You can say which direction to push next

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PEFT / LoRA docs](https://huggingface.co/docs/peft) — ⏱️ ~15 min
- [ ] 📦 [LeRoBot GitHub (HuggingFace)](https://github.com/huggingface/lerobot) — ⏱️ ~10 min
- [ ] 📄 [PyTorch benchmark utils](https://pytorch.org/docs/stable/benchmark_utils.html) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🧩 DSA | 19:00–20:30 | Union-Find (DSU)
**Task:** Name the pattern, then solve 3–5 Union-Find (DSU) problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Union-Find (DSU) problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Union-Find (DSU)**).
**Step 3.** Solve each in the site's built-in editor — **name the pattern first**, then code.
**Step 4.** For each: test one edge case, and say its **Big-O** (time/space) out loud.
**Step 5.** Star the hardest one to re-solve from memory tomorrow. Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] 3+ problems solved without peeking at the solution
- [ ] You can name the pattern + its Big-O in one sentence
- [ ] The hardest one is queued for a spaced re-solve tomorrow

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [HelloC++ DSA Roadmap](https://www.hellocpp.dev/data-structures-algorithms) — ⏱️ ~15 min
- [ ] 🎥 [NeetCode — patterns & solutions](https://neetcode.io/practice) — ⏱️ ~25 min
- [ ] 📦 [LeetCode problem set](https://leetcode.com/problemset/) — ⏱️ ~10 min

*⏱️ Resource time this block: ~50 min*

---
## 🔁 Wind-down & Consolidate | 20:30–21:00
**The highest-retention 30 minutes of your day — don't skip it.**

- [ ] Teach back today's main idea in 3 sentences, no notes (can't? flag it for tomorrow's warm-up)
- [ ] Turn 1–2 confusions into Anki cards (`Flashcards.csv`)
- [ ] Skim tomorrow's Day file for 2 min — prime your brain to pre-load overnight
- [ ] One line in `vla-edge/README.md`: what the repo can do now

> Then **stop**. Sleep is when today's reps get written to long-term memory — protect it.

---


---

[[Day19|← Day 19]]  |  [[Day21|Day 21 →]]

---

*[[Index|🏠 Back to Index]]*
