# Day 07 — Object Detection (Production-grade)

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 2 · Mon**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 YOLOv8 detection | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Detection embedding store | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Distillation hands-on | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | ROS2 node anatomy — read a pub/sub | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Recursion & backtracking | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: YOLOv8 detection
- 🗄️ Milvus *(supporting tool)*: Detection embedding store
- 🗜️ Compression: Distillation hands-on
- ⚙️ C++ *(literacy — read & modify)*: ROS2 node anatomy — read a pub/sub
- 🧩 DSA: Recursion & backtracking

**🤖 Capstone today →** `observe.py`: plug in YOLO26 detection → an object list the policy can use.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~395 min (~6.6 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 YOLO26 — NMS-free real-time detector (Jan 2026) — [open](https://www.ultralytics.com/yolo/yolo26)
- 🔥 YOLO26 on NVIDIA Jetson — setup & benchmarks — [open](https://docs.ultralytics.com/guides/nvidia-jetson)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Recite the full perception pipeline without notes.

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
## 🧠 New Concept | 9:30–11:00 | YOLOv8–v10, Anchor-free Detection
**Task:** FCOS, CenterPoint, NMS, focal loss, task-aligned head architecture.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand YOLOv8–v10, Anchor-free Detection.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**YOLOv8 Docs — Ultralytics**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 07 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **YOLOv8–v10, Anchor-free Detection** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain YOLOv8–v10, Anchor-free Detection aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [YOLOv8 Docs — Ultralytics](https://docs.ultralytics.com/) — ⏱️ ~15 min
- [ ] 📄 [FCOS Paper](https://arxiv.org/abs/1904.01355) — ⏱️ ~15 min
- [ ] 📄 [Focal Loss Paper (RetinaNet)](https://arxiv.org/abs/1708.02002) — ⏱️ ~15 min
- [ ] 🎥 [YOLOv8 Explained](https://www.youtube.com/watch?v=ag3DLKsl2vk) — ⏱️ ~25 min
- [ ] 📝 [Anchor-Free Detection Overview](https://towardsdatascience.com/anchor-free-object-detection-b8a4c3f9dc7c) — ⏱️ ~15 min
- [ ] 🔥 📝 [YOLO26 — NMS-free real-time detector (Jan 2026)](https://www.ultralytics.com/yolo/yolo26) — ⏱️ ~15 min

*⏱️ Resource time this block: ~100 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Fine-tune YOLOv8 on YCB Dataset
**Task:** Fine-tune YOLO11n on 10 YCB-Video classes for 30 epochs. Deliverable: mAP50 at least 0.6 on the val split + a confusion matrix. Paper: Focal Loss / RetinaNet (arXiv 1708.02002).

**🎯 Outcome:** Working code plus saved output for Fine-tune YOLOv8 on YCB Dataset.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day07_fine_tune_yolov8_on_ycb_dataset.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install ultralytics datasets pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day07_fine_tune_yolov8_on_ycb_dataset.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day07_fine_tune_yolov8_on_ycb_dataset.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day07_fine_tune_yolov8_on_ycb_dataset.py -q` until **everything is green**. That completes: Fine-tune YOLO11n on 10 YCB-Video classes for 30 epochs. Deliverable: mAP50 at least 0.6 on the val split + a confusion matrix. Paper: Focal Loss / RetinaNet (arXiv 1708.02002).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics) — ⏱️ ~10 min
- [ ] 📄 [YCB Object Dataset](https://www.ycbbenchmarks.com/) — ⏱️ ~15 min
- [ ] 📄 [YOLOv8 Training Docs](https://docs.ultralytics.com/modes/train/) — ⏱️ ~15 min
- [ ] 🎥 [YOLOv8 Custom Training Tutorial](https://www.youtube.com/watch?v=gRAyOPjQ9_s) — ⏱️ ~25 min
- [ ] 🔥 📄 [YOLO26 on NVIDIA Jetson — setup & benchmarks](https://docs.ultralytics.com/guides/nvidia-jetson) — ⏱️ ~15 min

*⏱️ Resource time this block: ~80 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Detection Embedding Store
**Task:** After each detection, extract RoI → embed with CLIP → upsert into Milvus with class label. Build 'seen objects' index.

**🎯 Outcome:** A working Milvus operation for Milvus — Detection Embedding Store.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day07_detection_embedding_store.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day07_detection_embedding_store.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day07_detection_embedding_store.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day07_detection_embedding_store.py -q` until **everything is green**. That completes: After each detection, extract RoI → embed with CLIP → upsert into Milvus with class label. Build 'seen objects' index.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Upsert Docs](https://milvus.io/docs/upsert_entities.md) — ⏱️ ~15 min
- [ ] 📝 [Milvus with Object Detection — Tutorial](https://milvus.io/docs/integrate_with_pytorch.md) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | Distillation Hands-on
**Task:** Distil YOLOv8l → YOLOv8n using soft labels. Compare mAP vs speed.

**🎯 Outcome:** A before/after measurement for Compression — Distillation Hands-on.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day07_distillation_hands_on.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day07_distillation_hands_on.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day07_distillation_hands_on.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day07_distillation_hands_on.py -q` until **everything is green**. That completes: Distil YOLOv8l → YOLOv8n using soft labels. Compare mAP vs speed.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Knowledge Distillation PyTorch Tutorial](https://pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) — ⏱️ ~15 min
- [ ] 📝 [Distilling YOLOv8 — Blog](https://learnopencv.com/knowledge-distillation/) — ⏱️ ~15 min
- [ ] 📦 [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | ROS2 node anatomy — read a pub/sub
**Task:** Read & understand: ros2 node anatomy — read a pub/sub. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — ROS2 node anatomy — read a pub/sub — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**ROS2 C++ Pub/Sub Tutorial**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: ros2 node anatomy — read a pub/sub. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [ROS2 C++ Pub/Sub Tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html) — ⏱️ ~15 min
- [ ] 🎓 [HelloC++ — C++ Plus (Intermediate)](https://www.hellocpp.dev/course/cpp-plus) — ⏱️ ~45 min
- [ ] 🎥 [HelloC++ YouTube Channel](https://www.youtube.com/@HelloCppOrg) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Recursion & backtracking
**Task:** Name the pattern, then solve 3–5 Recursion & backtracking problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Recursion & backtracking problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Recursion & backtracking**).
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

[[Day06|← Day 6]]  |  [[Day08|Day 8 →]]

---

*[[Index|🏠 Back to Index]]*
