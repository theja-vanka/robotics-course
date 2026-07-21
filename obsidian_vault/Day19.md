# Day 19 — 3DGS Hands-on + Robotics Integration

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 4 · Mon**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 3DGS for manipulation | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ 3DGS object index | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ 4-bit GPTQ/AWQ | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Tries | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: 3DGS for manipulation
- 🗄️ Milvus *(supporting tool)*: 3DGS object index
- 🗜️ Compression: 4-bit GPTQ/AWQ
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Tries

**🤖 Capstone today →** ⭐ `compress.py`: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~280 min (~4.7 hr)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Flashcard: DreamerV3 RSSM components.

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
## 🧠 New Concept | 9:30–11:00 | 3DGS for Manipulation
**Task:** Gaussian scene editing, deformable 3DGS, GaussianGrasper, 3DGS as robot map.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand 3DGS for Manipulation.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**3DGS Robotics Survey**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 19 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **3DGS for Manipulation** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain 3DGS for Manipulation aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [3DGS Robotics Survey](https://arxiv.org/abs/2410.12262) — ⏱️ ~15 min
- [ ] 📄 [GaussianGrasper Paper](https://arxiv.org/abs/2403.09637) — ⏱️ ~15 min
- [ ] 📦 [NeRF and 3DGS for Robotics — Curated Resources](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — ⏱️ ~15 min
- [ ] 📦 [awesome-representation-for-robotics](https://github.com/dtc111111/awesome-representation-for-robotics) — ⏱️ ~10 min

*⏱️ Resource time this block: ~65 min*

---
## 🛠️ Hands-on | 11:15–13:00 | 3DGS Scene + Grasp Poses
**Task:** Reconstruct a tabletop with 3DGS; export Gaussians; compute grasp poses on the geometry. Deliverable: a .ply + top-5 grasps overlaid. Paper: 3D Gaussian Splatting (arXiv 2308.04079).

**🎯 Outcome:** Working code plus saved output for 3DGS Scene + Grasp Poses.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`3dgs_scene_grasp_poses.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day19/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest 3dgs_scene_grasp_poses.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`3dgs_scene_grasp_poses.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest 3dgs_scene_grasp_poses.py -q` until **everything is green**. That completes: Reconstruct a tabletop with 3DGS; export Gaussians; compute grasp poses on the geometry. Deliverable: a .ply + top-5 grasps overlaid. Paper: 3D Gaussian Splatting (arXiv 2308.04079).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [Nerfstudio GitHub](https://github.com/nerfstudio-project/nerfstudio) — ⏱️ ~10 min
- [ ] 📦 [Open3D GitHub](https://github.com/isl-org/Open3D) — ⏱️ ~10 min
- [ ] 📄 [Nerfstudio 3DGS Export](https://docs.nerf.studio/quickstart/export_geometry.html) — ⏱️ ~15 min

*⏱️ Resource time this block: ~35 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | 3DGS Object Index
**Task:** Compute shape descriptor per Gaussian cluster. Store in Milvus. Query: given new scene, retrieve similar past object + known grasp.

**🎯 Outcome:** A working Milvus operation for Milvus — 3DGS Object Index.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`3dgs_object_index.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day19/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest 3dgs_object_index.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`3dgs_object_index.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest 3dgs_object_index.py -q` until **everything is green**. That completes: Compute shape descriptor per Gaussian cluster. Store in Milvus. Query: given new scene, retrieve similar past object + known grasp.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📄 [Milvus Official Docs](https://milvus.io/docs) — ⏱️ ~15 min
- [ ] 📝 [3D Shape Search with Vector DBs](https://zilliz.com/blog) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | 4-bit Quantisation (GPTQ/AWQ)
**Task:** Apply GPTQ to OpenVLA. Compare 4-bit vs 8-bit vs 16-bit speed and action quality.

**🎯 Outcome:** A before/after measurement for Compression — 4-bit Quantisation (GPTQ/AWQ).

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`4_bit_quantisation_gptq_awq.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day19/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest 4_bit_quantisation_gptq_awq.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`4_bit_quantisation_gptq_awq.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest 4_bit_quantisation_gptq_awq.py -q` until **everything is green**. That completes: Apply GPTQ to OpenVLA. Compare 4-bit vs 8-bit vs 16-bit speed and action quality.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [GPTQ Paper](https://arxiv.org/abs/2210.17323) — ⏱️ ~15 min
- [ ] 📄 [AWQ Paper](https://arxiv.org/abs/2306.00978) — ⏱️ ~15 min
- [ ] 📦 [AutoGPTQ GitHub](https://github.com/AutoGPTQ/AutoGPTQ) — ⏱️ ~10 min
- [ ] 📦 [AWQ GitHub](https://github.com/mit-han-lab/llm-awq) — ⏱️ ~10 min

*⏱️ Resource time this block: ~50 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: ⭐ `compress.py`: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
!python src/compress.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: ⭐ `compress.py`: 4-bit (GPTQ/AWQ) on the fine-tuned policy — measure the deltas. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | Tries
**Task:** Name the pattern, then solve 3–5 Tries problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Tries problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Tries**).
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

[[Day18|← Day 18]]  |  [[Day20|Day 20 →]]

---

*[[Index|🏠 Back to Index]]*
