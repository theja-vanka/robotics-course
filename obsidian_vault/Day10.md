# Day 10 — Grasp Detection

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 2 · Thu**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Grasp detection | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Grasp pose library | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ TensorRT FP16 | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Read a CUDA kernel (understand, don't write) | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Graphs: BFS & DFS | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Grasp detection
- 🗄️ Milvus *(supporting tool)*: Grasp pose library
- 🗜️ Compression: TensorRT FP16
- ⚙️ C++ *(literacy — read & modify)*: Read a CUDA kernel (understand, don't write)
- 🧩 DSA: Graphs: BFS & DFS

**🤖 Capstone today →** Grasp detection — awareness; see how a policy's action could ground to a grasp.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~335 min (~5.6 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 FoundationGrasp — task-oriented grasping w/ foundation models — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Quiz: MegaPose vs FoundPose — differences and use cases.

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
## 🧠 New Concept | 9:30–11:00 | GraspNet, AnyGrasp, Affordance Detection
**Task:** Grasp quality metrics, force closure, antipodal grasps, learning from point clouds.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand GraspNet, AnyGrasp, Affordance Detection.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**GraspNet Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 10 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **GraspNet, AnyGrasp, Affordance Detection** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain GraspNet, AnyGrasp, Affordance Detection aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [GraspNet Paper](https://www.google.com/search?q=GraspNet+Paper) — ⏱️ ~15 min
- [ ] 📄 [AnyGrasp Paper](https://www.google.com/search?q=AnyGrasp+Paper) — ⏱️ ~15 min
- [ ] 📦 [AnyGrasp SDK GitHub](https://www.google.com/search?q=AnyGrasp+SDK+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [Robot Grasping Explained](https://www.youtube.com/results?search_query=Robot+Grasping+Explained) — ⏱️ ~25 min
- [ ] 📝 [Force Closure Grasps — Tutorial](https://www.google.com/search?q=Force+Closure+Grasps+%E2%80%94+Tutorial) — ⏱️ ~15 min
- [ ] 🔥 📄 [FoundationGrasp — task-oriented grasping w/ foundation models](https://www.google.com/search?q=FoundationGrasp+%E2%80%94+task-oriented+grasping+w%2F+foundation+models) — ⏱️ ~15 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run AnyGrasp on Point Cloud
**Task:** Run AnyGrasp on the Day-8 point cloud; rank grasps by score. Deliverable: top-5 grasp poses in Open3D + their scores. Paper: AnyGrasp (arXiv 2212.08333).

**🎯 Outcome:** Working code plus saved output for Run AnyGrasp on Point Cloud.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day10_run_anygrasp_on_point_cloud.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day10_run_anygrasp_on_point_cloud.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day10_run_anygrasp_on_point_cloud.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day10_run_anygrasp_on_point_cloud.py -q` until **everything is green**. That completes: Run AnyGrasp on the Day-8 point cloud; rank grasps by score. Deliverable: top-5 grasp poses in Open3D + their scores. Paper: AnyGrasp (arXiv 2212.08333).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [AnyGrasp SDK GitHub](https://www.google.com/search?q=AnyGrasp+SDK+GitHub) — ⏱️ ~10 min
- [ ] 📦 [Open3D GitHub](https://www.google.com/search?q=Open3D+GitHub) — ⏱️ ~10 min
- [ ] 📄 [GraspNet Benchmark](https://www.google.com/search?q=GraspNet+Benchmark) — ⏱️ ~15 min

*⏱️ Resource time this block: ~35 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Grasp Pose Library
**Task:** Store (object embedding + grasp config) pairs. Query: given new object, retrieve most similar past grasp.

**🎯 Outcome:** A working Milvus operation for Milvus — Grasp Pose Library.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day10_grasp_pose_library.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day10_grasp_pose_library.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day10_grasp_pose_library.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day10_grasp_pose_library.py -q` until **everything is green**. That completes: Store (object embedding + grasp config) pairs. Query: given new object, retrieve most similar past grasp.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Hybrid Search](https://www.google.com/search?q=Milvus+Hybrid+Search) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📝 [Vector Similarity for Robotics](https://www.google.com/search?q=Vector+Similarity+for+Robotics) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | TensorRT FP16
**Task:** Convert model to FP16 TRT engine. Benchmark vs FP32 TRT. Calculate speedup ratio.

**🎯 Outcome:** A before/after measurement for Compression — TensorRT FP16.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day10_tensorrt_fp16.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install onnxruntime torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day10_tensorrt_fp16.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day10_tensorrt_fp16.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day10_tensorrt_fp16.py -q` until **everything is green**. That completes: Convert model to FP16 TRT engine. Benchmark vs FP32 TRT. Calculate speedup ratio.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [TensorRT FP16 Precision Guide](https://www.google.com/search?q=TensorRT+FP16+Precision+Guide) — ⏱️ ~15 min
- [ ] 📦 [TensorRT GitHub](https://www.google.com/search?q=TensorRT+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [TensorRT FP16 Optimization](https://www.youtube.com/results?search_query=TensorRT+FP16+Optimization) — ⏱️ ~25 min

*⏱️ Resource time this block: ~50 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Read a CUDA kernel (understand, don't write)
**Task:** Read & understand: read a cuda kernel (understand, don't write). The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Read a CUDA kernel (understand, don't write) — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**CUDA C++ Guide — read a kernel**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: read a cuda kernel (understand, don't write). The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [CUDA C++ Guide — read a kernel](https://www.google.com/search?q=CUDA+C%2B%2B+Guide+%E2%80%94+read+a+kernel) — ⏱️ ~15 min
- [ ] 🎥 [CUDA explained](https://www.youtube.com/results?search_query=CUDA+explained) — ⏱️ ~25 min
- [ ] 🎥 [HelloC++ YouTube Channel](https://www.youtube.com/results?search_query=HelloC%2B%2B+YouTube+Channel) — ⏱️ ~25 min

*⏱️ Resource time this block: ~65 min*

---
## 🧩 DSA | 19:00–20:30 | Graphs: BFS & DFS
**Task:** Name the pattern, then solve 3–5 Graphs: BFS & DFS problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Graphs: BFS & DFS problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Graphs: BFS & DFS**).
**Step 3.** Solve each in the site's built-in editor — **name the pattern first**, then code.
**Step 4.** For each: test one edge case, and say its **Big-O** (time/space) out loud.
**Step 5.** Star the hardest one to re-solve from memory tomorrow. Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] 3+ problems solved without peeking at the solution
- [ ] You can name the pattern + its Big-O in one sentence
- [ ] The hardest one is queued for a spaced re-solve tomorrow

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [HelloC++ DSA Roadmap](https://www.google.com/search?q=HelloC%2B%2B+DSA+Roadmap) — ⏱️ ~15 min
- [ ] 🎥 [NeetCode — patterns & solutions](https://www.youtube.com/results?search_query=NeetCode+%E2%80%94+patterns+%26+solutions) — ⏱️ ~25 min
- [ ] 📦 [LeetCode problem set](https://www.google.com/search?q=LeetCode+problem+set) — ⏱️ ~10 min

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

[[Day09|← Day 9]]  |  [[Day11|Day 11 →]]

---

*[[Index|🏠 Back to Index]]*
