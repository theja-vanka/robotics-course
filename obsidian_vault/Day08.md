# Day 08 — Depth Estimation & 3D Scene Understanding

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 2 · Tue**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Depth estimation | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Multi-modal RGB+depth | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ ONNX export | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Modify a ROS2 node | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Trees & BST traversals | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Depth estimation
- 🗄️ Milvus *(supporting tool)*: Multi-modal RGB+depth
- 🗜️ Compression: ONNX export
- ⚙️ C++ *(literacy — read & modify)*: Modify a ROS2 node
- 🧩 DSA: Trees & BST traversals

**🤖 Capstone today →** `observe.py`: add Depth Anything depth → richer observation / conditioning.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~370 min (~6.2 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 Depth Anything 3 — geometry from any views (ICLR 2026) — [open](https://www.google.com/search?q=open)
- 🔥 Apple Depth Pro — sharp metric depth in <1s — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Flashcard: anchor-free vs anchor-based detection differences.

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
## 🧠 New Concept | 9:30–11:00 | Depth Anything v2, ZoeDepth, Stereo
**Task:** Monocular depth, disparity, structured light, ToF. Converting depth map to point cloud.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Depth Anything v2, ZoeDepth, Stereo.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**Depth Anything v2 Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 08 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Depth Anything v2, ZoeDepth, Stereo** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Depth Anything v2, ZoeDepth, Stereo aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Depth Anything v2 Paper](https://www.google.com/search?q=Depth+Anything+v2+Paper) — ⏱️ ~15 min
- [ ] 📦 [Depth Anything v2 GitHub](https://www.google.com/search?q=Depth+Anything+v2+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [Monocular Depth Estimation Explained](https://www.youtube.com/results?search_query=Monocular+Depth+Estimation+Explained) — ⏱️ ~25 min
- [ ] 📝 [Stereo Vision Guide — LearnOpenCV](https://www.google.com/search?q=Stereo+Vision+Guide+%E2%80%94+LearnOpenCV) — ⏱️ ~15 min
- [ ] 🔥 📦 [Depth Anything 3 — geometry from any views (ICLR 2026)](https://www.google.com/search?q=Depth+Anything+3+%E2%80%94+geometry+from+any+views+%28ICLR+2026%29) — ⏱️ ~10 min

*⏱️ Resource time this block: ~75 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run Depth Anything v2 + Point Cloud
**Task:** Run Depth Anything V2-Small on a tabletop image; back-project to an Open3D point cloud. Deliverable: depth.png + a cloud with at least 10k points (intrinsics noted). Paper: Depth Anything v2 (arXiv 2406.09414).

**🎯 Outcome:** Working code plus saved output for Run Depth Anything v2 + Point Cloud.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_depth_anything_v2_point_cloud.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day08/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install transformers datasets torch pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_depth_anything_v2_point_cloud.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_depth_anything_v2_point_cloud.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_depth_anything_v2_point_cloud.py -q` until **everything is green**. That completes: Run Depth Anything V2-Small on a tabletop image; back-project to an Open3D point cloud. Deliverable: depth.png + a cloud with at least 10k points (intrinsics noted). Paper: Depth Anything v2 (arXiv 2406.09414).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Depth Anything v2 HuggingFace](https://www.google.com/search?q=Depth+Anything+v2+HuggingFace) — ⏱️ ~15 min
- [ ] 📦 [Open3D GitHub](https://www.google.com/search?q=Open3D+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Open3D Point Cloud Tutorial](https://www.google.com/search?q=Open3D+Point+Cloud+Tutorial) — ⏱️ ~15 min
- [ ] 🔥 📝 [Apple Depth Pro — sharp metric depth in <1s](https://www.google.com/search?q=Apple+Depth+Pro+%E2%80%94+sharp+metric+depth+in+%3C1s) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Multi-modal (RGB + Depth)
**Task:** Store both CLIP (RGB) and depth feature vectors in a Milvus collection. Query by either modality.

**🎯 Outcome:** A working Milvus operation for Milvus — Multi-modal (RGB + Depth).

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`multi_modal_rgb_depth.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day08/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest multi_modal_rgb_depth.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`multi_modal_rgb_depth.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest multi_modal_rgb_depth.py -q` until **everything is green**. That completes: Store both CLIP (RGB) and depth feature vectors in a Milvus collection. Query by either modality.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Multi-Vector Fields](https://www.google.com/search?q=Milvus+Multi-Vector+Fields) — ⏱️ ~15 min
- [ ] 📝 [Multi-modal Search with Milvus](https://www.google.com/search?q=Multi-modal+Search+with+Milvus) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | ONNX Export
**Task:** Export YOLOv8 PyTorch → ONNX. Run inference with onnxruntime. Validate outputs match.

**🎯 Outcome:** A before/after measurement for Compression — ONNX Export.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`onnx_export.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day08/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install onnxruntime torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest onnx_export.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`onnx_export.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest onnx_export.py -q` until **everything is green**. That completes: Export YOLOv8 PyTorch → ONNX. Run inference with onnxruntime. Validate outputs match.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [ONNX Export Docs — Ultralytics](https://www.google.com/search?q=ONNX+Export+Docs+%E2%80%94+Ultralytics) — ⏱️ ~15 min
- [ ] 📦 [ONNX Runtime GitHub](https://www.google.com/search?q=ONNX+Runtime+GitHub) — ⏱️ ~10 min
- [ ] 📄 [ONNX Runtime Python Docs](https://www.google.com/search?q=ONNX+Runtime+Python+Docs) — ⏱️ ~15 min
- [ ] 🎥 [ONNX Export Tutorial](https://www.youtube.com/results?search_query=ONNX+Export+Tutorial) — ⏱️ ~25 min

*⏱️ Resource time this block: ~65 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Modify a ROS2 node
**Task:** Read & understand: modify a ros2 node. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Modify a ROS2 node — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**ROS2 C++ Pub/Sub Tutorial**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: modify a ros2 node. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [ROS2 C++ Pub/Sub Tutorial](https://www.google.com/search?q=ROS2+C%2B%2B+Pub%2FSub+Tutorial) — ⏱️ ~15 min
- [ ] 🎓 [HelloC++ — C++ Plus (Intermediate)](https://www.google.com/search?q=HelloC%2B%2B+%E2%80%94+C%2B%2B+Plus+%28Intermediate%29) — ⏱️ ~45 min
- [ ] 🎥 [HelloC++ YouTube Channel](https://www.youtube.com/results?search_query=HelloC%2B%2B+YouTube+Channel) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Trees & BST traversals
**Task:** Name the pattern, then solve 3–5 Trees & BST traversals problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Trees & BST traversals problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Trees & BST traversals**).
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

[[Day07|← Day 7]]  |  [[Day09|Day 9 →]]

---

*[[Index|🏠 Back to Index]]*
