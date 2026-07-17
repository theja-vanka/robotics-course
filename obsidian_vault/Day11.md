# Day 11 — SLAM & Spatial Mapping

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 2 · Fri**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 SLAM & mapping | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Semantic SLAM map | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ TensorRT INT8 | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Read a TensorRT/ONNX C++ sample | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Graphs: shortest path | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: SLAM & mapping
- 🗄️ Milvus *(supporting tool)*: Semantic SLAM map
- 🗜️ Compression: TensorRT INT8
- ⚙️ C++ *(literacy — read & modify)*: Read a TensorRT/ONNX C++ sample
- 🧩 DSA: Graphs: shortest path

**🤖 Capstone today →** SLAM — **awareness only, don't build**. It's the 'where am I' layer, noted for context.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~315 min (~5.2 hr)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Recite AnyGrasp pipeline and grasp quality metrics.

**🎯 Outcome:** Yesterday's key ideas recalled cold; today's gaps surfaced.

**▶️ DO THIS — every step (Anki + Obsidian):**

**Step 1.** Notes **closed**. Out loud (or on paper), recall yesterday's main idea — plus one topic from ~3 and ~7 days ago.
**Step 2.** Open the **Anki** app and clear today's due cards (~10 min). *(First time? [[Setup_Guide]] §1 — install Anki + import `Flashcards.csv`.)*
**Step 3.** Open yesterday's Day-note; check what you forgot. Jot 1–2 gaps to fix today.
**Step 4.** Tick the ✅ boxes and check **Block complete**.

**✅ Done when:**
- [ ] You did the recall **before** peeking at notes
- [ ] Any gaps are written down, each tagged to a block to fix it

- [ ] Block complete

### 📚 Resources

---
## 🧠 New Concept | 9:30–11:00 | ORB-SLAM3, 3DGS-SLAM
**Task:** Feature tracking, pose graph optimisation, loop closure, bundle adjustment.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand ORB-SLAM3, 3DGS-SLAM.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**ORB-SLAM3 GitHub**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 11 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **ORB-SLAM3, 3DGS-SLAM** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain ORB-SLAM3, 3DGS-SLAM aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [ORB-SLAM3 GitHub](https://github.com/UZ-SLAMLab/ORB_SLAM3) — ⏱️ ~10 min
- [ ] 📄 [ORB-SLAM3 Paper](https://arxiv.org/abs/2007.11898) — ⏱️ ~15 min
- [ ] 🎥 [SLAM Explained — Cyrill Stachniss](https://www.youtube.com/watch?v=saVZtgPyyJQ) — ⏱️ ~25 min
- [ ] 📝 [3DGS-SLAM Survey](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — ⏱️ ~15 min
- [ ] 🎥 [Loop Closure in SLAM](https://www.youtube.com/watch?v=NH-DC8STxeo) — ⏱️ ~25 min

*⏱️ Resource time this block: ~90 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run ORB-SLAM3 on TUM RGB-D
**Task:** Build ORB-SLAM3; run on the TUM RGB-D fr1/desk sequence. Deliverable: estimated trajectory vs ground truth (ATE RMSE reported) + a map screenshot. Paper: ORB-SLAM3 (arXiv 2007.11898).

**🎯 Outcome:** Working code plus saved output for Run ORB-SLAM3 on TUM RGB-D.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_orb_slam3_on_tum_rgb_d.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day11/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_orb_slam3_on_tum_rgb_d.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_orb_slam3_on_tum_rgb_d.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_orb_slam3_on_tum_rgb_d.py -q` until **everything is green**. That completes: Build ORB-SLAM3; run on the TUM RGB-D fr1/desk sequence. Deliverable: estimated trajectory vs ground truth (ATE RMSE reported) + a map screenshot. Paper: ORB-SLAM3 (arXiv 2007.11898).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [ORB-SLAM3 GitHub](https://github.com/UZ-SLAMLab/ORB_SLAM3) — ⏱️ ~10 min
- [ ] 📄 [TUM RGB-D Dataset](https://cvg.cit.tum.de/data/datasets/rgbd-dataset) — ⏱️ ~15 min
- [ ] 📝 [ORB-SLAM3 Setup Guide](https://github.com/UZ-SLAMLab/ORB_SLAM3#getting-started) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Semantic SLAM Map
**Task:** Store SLAM keyframe position + CLIP embedding in Milvus. Query: find all keyframes showing the red mug.

**🎯 Outcome:** A working Milvus operation for Milvus — Semantic SLAM Map.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`semantic_slam_map.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day11/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest semantic_slam_map.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`semantic_slam_map.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest semantic_slam_map.py -q` until **everything is green**. That completes: Store SLAM keyframe position + CLIP embedding in Milvus. Query: find all keyframes showing the red mug.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Metadata Filtering](https://milvus.io/docs/boolean.md) — ⏱️ ~15 min
- [ ] 📄 [Milvus Query Docs](https://milvus.io/docs/query.md) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | TensorRT INT8
**Task:** INT8 calibration with calibration dataset. Compare INT8 vs FP16 vs FP32 accuracy and speed.

**🎯 Outcome:** A before/after measurement for Compression — TensorRT INT8.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`tensorrt_int8.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day11/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install onnxruntime torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest tensorrt_int8.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`tensorrt_int8.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest tensorrt_int8.py -q` until **everything is green**. That completes: INT8 calibration with calibration dataset. Compare INT8 vs FP16 vs FP32 accuracy and speed.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [TensorRT INT8 Calibration Guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#optimizing_int8) — ⏱️ ~15 min
- [ ] 🎥 [INT8 Calibration with TensorRT](https://www.youtube.com/watch?v=AOHkAh3fj_M) — ⏱️ ~25 min
- [ ] 📦 [TensorRT GitHub](https://github.com/NVIDIA/TensorRT) — ⏱️ ~10 min

*⏱️ Resource time this block: ~50 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Read a TensorRT/ONNX C++ sample
**Task:** Read & understand: read a tensorrt/onnx c++ sample. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Read a TensorRT/ONNX C++ sample — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**TensorRT C++ samples — read the flow**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: read a tensorrt/onnx c++ sample. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [TensorRT C++ samples — read the flow](https://github.com/NVIDIA/TensorRT/tree/main/samples) — ⏱️ ~10 min
- [ ] 📦 [ONNX Runtime](https://github.com/microsoft/onnxruntime) — ⏱️ ~10 min
- [ ] 🎥 [HelloC++ YouTube Channel](https://www.youtube.com/@HelloCppOrg) — ⏱️ ~25 min

*⏱️ Resource time this block: ~45 min*

---
## 🧩 DSA | 19:00–20:30 | Graphs: shortest path
**Task:** Name the pattern, then solve 3–5 Graphs: shortest path problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Graphs: shortest path problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Graphs: shortest path**).
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

[[Day10|← Day 10]]  |  [[Day12|Day 12 →]]

---

*[[Index|🏠 Back to Index]]*
