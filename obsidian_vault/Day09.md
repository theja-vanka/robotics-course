# Day 09 — 6-DoF Pose Estimation

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 2 · Wed**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 6-DoF pose estimation | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Object pose library | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ TensorRT FP32 | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | ROS2 messages & data flow | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Heaps / priority queue | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: 6-DoF pose estimation
- 🗄️ Milvus *(supporting tool)*: Object pose library
- 🗜️ Compression: TensorRT FP32
- ⚙️ C++ *(literacy — read & modify)*: ROS2 messages & data flow
- 🧩 DSA: Heaps / priority queue

**🤖 Capstone today →** 6-DoF pose — optional observation enrichment; awareness-level for your target.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~405 min (~6.8 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 FoundationPose — unified 6D pose for novel objects (NVIDIA) — [open](https://www.google.com/search?q=open)
- 🔥 FoundationPose in Isaac ROS — deploy on a robot — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Draw depth-to-pointcloud pipeline from memory.

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
## 🧠 New Concept | 9:30–11:00 | PnP, RANSAC, MegaPose, FoundPose
**Task:** Correspondences, DLT, EPnP, iterative refinement. Template vs learning-based pose.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand PnP, RANSAC, MegaPose, FoundPose.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**MegaPose Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 09 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **PnP, RANSAC, MegaPose, FoundPose** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain PnP, RANSAC, MegaPose, FoundPose aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [MegaPose Paper](https://www.google.com/search?q=MegaPose+Paper) — ⏱️ ~15 min
- [ ] 📦 [MegaPose GitHub](https://www.google.com/search?q=MegaPose+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [6-DoF Pose Estimation Explained](https://www.youtube.com/results?search_query=6-DoF+Pose+Estimation+Explained) — ⏱️ ~25 min
- [ ] 📝 [PnP Algorithm — LearnOpenCV](https://www.google.com/search?q=PnP+Algorithm+%E2%80%94+LearnOpenCV) — ⏱️ ~15 min
- [ ] 📄 [FoundPose Paper](https://www.google.com/search?q=FoundPose+Paper) — ⏱️ ~15 min
- [ ] 🔥 📄 [FoundationPose — unified 6D pose for novel objects (NVIDIA)](https://www.google.com/search?q=FoundationPose+%E2%80%94+unified+6D+pose+for+novel+objects+%28NVIDIA%29) — ⏱️ ~15 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run MegaPose on YCB Object
**Task:** Run FoundationPose (or MegaPose) on a YCB object; overlay the 6-DoF axes. Deliverable: an axis-overlay image + the 4x4 pose matrix printed, reprojection aligned. Paper: FoundationPose (arXiv 2312.08344).

**🎯 Outcome:** Working code plus saved output for Run MegaPose on YCB Object.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day09_run_megapose_on_ycb_object.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day09_run_megapose_on_ycb_object.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day09_run_megapose_on_ycb_object.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day09_run_megapose_on_ycb_object.py -q` until **everything is green**. That completes: Run FoundationPose (or MegaPose) on a YCB object; overlay the 6-DoF axes. Deliverable: an axis-overlay image + the 4x4 pose matrix printed, reprojection aligned. Paper: FoundationPose (arXiv 2312.08344).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [MegaPose GitHub](https://www.google.com/search?q=MegaPose+GitHub) — ⏱️ ~10 min
- [ ] 📄 [MegaPose HuggingFace Demo](https://www.google.com/search?q=MegaPose+HuggingFace+Demo) — ⏱️ ~15 min
- [ ] 📄 [YCB Dataset Download](https://www.google.com/search?q=YCB+Dataset+Download) — ⏱️ ~15 min
- [ ] 🔥 📄 [FoundationPose in Isaac ROS — deploy on a robot](https://www.google.com/search?q=FoundationPose+in+Isaac+ROS+%E2%80%94+deploy+on+a+robot) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Object Pose Library
**Task:** Store template embeddings + known poses. At inference: embed crop → find nearest template → retrieve pose.

**🎯 Outcome:** A working Milvus operation for Milvus — Object Pose Library.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day09_object_pose_library.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day09_object_pose_library.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day09_object_pose_library.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day09_object_pose_library.py -q` until **everything is green**. That completes: Store template embeddings + known poses. At inference: embed crop → find nearest template → retrieve pose.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Metadata Filtering](https://www.google.com/search?q=Milvus+Metadata+Filtering) — ⏱️ ~15 min
- [ ] 📝 [Build a Pose Retrieval System](https://www.google.com/search?q=Build+a+Pose+Retrieval+System) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Milvus Official Docs](https://www.google.com/search?q=Milvus+Official+Docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🗜️ Compression | 15:45–17:15 | TensorRT Basics
**Task:** Install TensorRT. Convert ONNX → TRT engine. Run FP32 inference. Log latency.

**🎯 Outcome:** A before/after measurement for Compression — TensorRT Basics.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day09_tensorrt_basics.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install onnxruntime torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day09_tensorrt_basics.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day09_tensorrt_basics.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day09_tensorrt_basics.py -q` until **everything is green**. That completes: Install TensorRT. Convert ONNX → TRT engine. Run FP32 inference. Log latency.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [TensorRT Python Quickstart](https://www.google.com/search?q=TensorRT+Python+Quickstart) — ⏱️ ~15 min
- [ ] 📦 [TensorRT GitHub](https://www.google.com/search?q=TensorRT+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [TensorRT Tutorial — NVIDIA](https://www.youtube.com/results?search_query=TensorRT+Tutorial+%E2%80%94+NVIDIA) — ⏱️ ~25 min
- [ ] 📄 [TensorRT ONNX Workflow](https://www.google.com/search?q=TensorRT+ONNX+Workflow) — ⏱️ ~15 min

*⏱️ Resource time this block: ~65 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | ROS2 messages & data flow
**Task:** Read & understand: ros2 messages & data flow. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — ROS2 messages & data flow — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**ROS2 Custom Interfaces Tutorial**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: ros2 messages & data flow. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [ROS2 Custom Interfaces Tutorial](https://www.google.com/search?q=ROS2+Custom+Interfaces+Tutorial) — ⏱️ ~15 min
- [ ] 🎓 [HelloC++ — C++ Plus (Intermediate)](https://www.google.com/search?q=HelloC%2B%2B+%E2%80%94+C%2B%2B+Plus+%28Intermediate%29) — ⏱️ ~45 min
- [ ] 🎥 [HelloC++ YouTube Channel](https://www.youtube.com/results?search_query=HelloC%2B%2B+YouTube+Channel) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Heaps / priority queue
**Task:** Name the pattern, then solve 3–5 Heaps / priority queue problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Heaps / priority queue problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Heaps / priority queue**).
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

[[Day08|← Day 8]]  |  [[Day10|Day 10 →]]

---

*[[Index|🏠 Back to Index]]*
