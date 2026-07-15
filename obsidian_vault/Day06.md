# Day 06 — Robot Perception Pipeline Overview

> **Phase:** 🤖 Phase 2 — Robotics Perception Stack  ·  **📅 Week 1 · Sat**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Perception pipeline | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Scene retrieval service | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Knowledge distillation | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Read & modify an OpenCV C++ program | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Binary search | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Perception pipeline
- 🗄️ Milvus *(supporting tool)*: Scene retrieval service
- 🗜️ Compression: Knowledge distillation
- ⚙️ C++ *(literacy — read & modify)*: Read & modify an OpenCV C++ program
- 🧩 DSA: Binary search

**🤖 Capstone today →** Draft `observe.py` architecture — the perception front-end of your policy.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~380 min (~6.3 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 NVIDIA GR00T N1.5 — open humanoid foundation model — [open](https://www.google.com/search?q=open)

> 🌴 **Tomorrow is your rest day (Sunday).** No study — let memory consolidate off-screen.

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Draw 3DGS pipeline from scratch in 5 min.

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
## 🧠 New Concept | 9:30–11:00 | Perception Pipeline — Theory
**Task:** Sensor modalities: RGB, RGB-D, LiDAR, tactile. Pipeline: detect→segment→pose→grasp→plan.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Perception Pipeline — Theory.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**VLA Survey — Perception Section**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 06 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Perception Pipeline — Theory** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Perception Pipeline — Theory aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [VLA Survey — Perception Section](https://www.google.com/search?q=VLA+Survey+%E2%80%94+Perception+Section) — ⏱️ ~15 min
- [ ] 📝 [Robot Perception Overview — Towards Robotics](https://www.google.com/search?q=Robot+Perception+Overview+%E2%80%94+Towards+Robotics) — ⏱️ ~15 min
- [ ] 🎥 [Robot Perception Pipeline — MIT OpenCourseWare](https://www.youtube.com/results?search_query=Robot+Perception+Pipeline+%E2%80%94+MIT+OpenCourseWare) — ⏱️ ~25 min
- [ ] 📄 [ROS2 Perception Docs](https://www.google.com/search?q=ROS2+Perception+Docs) — ⏱️ ~15 min
- [ ] 🔥 📄 [NVIDIA GR00T N1.5 — open humanoid foundation model](https://www.google.com/search?q=NVIDIA+GR00T+N1.5+%E2%80%94+open+humanoid+foundation+model) — ⏱️ ~15 min

*⏱️ Resource time this block: ~85 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Build RobotPerceptionPipeline Class
**Task:** Write a RobotPerceptionPipeline class chaining today's models — detect() → segment() → estimate_pose() → plan_grasp() → plan_motion() — on one image. Deliverable: pipeline.run(img) returns a dict {detections, masks}, unit-tested end-to-end.

**🎯 Outcome:** A working, committed increment of the product for Build RobotPerceptionPipeline Class.

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
!python src/observe.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Write a RobotPerceptionPipeline class chaining today's models — detect() → segment() → estimate_pose() → plan_grasp() → plan_motion() — on one image. Deliverable: pipeline.run(img) returns a dict {detections, masks}, unit-tested end-to-end.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Python OOP Guide](https://www.google.com/search?q=Python+OOP+Guide) — ⏱️ ~15 min
- [ ] 📝 [Designing a Robot Perception System](https://www.google.com/search?q=Designing+a+Robot+Perception+System) — ⏱️ ~15 min
- [ ] 📦 [Open3D GitHub](https://www.google.com/search?q=Open3D+GitHub) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Scene Retrieval Service
**Task:** Build SceneRetriever class: encode frame with CLIP → query Milvus → return top-5 similar scenes.

**🎯 Outcome:** A working Milvus operation for Milvus — Scene Retrieval Service.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`scene_retrieval_service.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day06/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest scene_retrieval_service.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`scene_retrieval_service.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest scene_retrieval_service.py -q` until **everything is green**. That completes: Build SceneRetriever class: encode frame with CLIP → query Milvus → return top-5 similar scenes.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Python Search Tutorial](https://www.google.com/search?q=Milvus+Python+Search+Tutorial) — ⏱️ ~15 min
- [ ] 📝 [Build a Scene Search Engine — Zilliz Blog](https://www.google.com/search?q=Build+a+Scene+Search+Engine+%E2%80%94+Zilliz+Blog) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Milvus Official Docs](https://www.google.com/search?q=Milvus+Official+Docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🗜️ Compression | 15:45–17:15 | Knowledge Distillation Theory
**Task:** Teacher-student framework, soft labels, temperature scaling. Read DistilBERT paper.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Compression — Knowledge Distillation Theory.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**Knowledge Distillation Paper (Hinton et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 06 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Compression — Knowledge Distillation Theory** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Compression — Knowledge Distillation Theory aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Knowledge Distillation Paper (Hinton et al.)](https://www.google.com/search?q=Knowledge+Distillation+Paper+%28Hinton+et+al.%29) — ⏱️ ~15 min
- [ ] 📄 [DistilBERT Paper](https://www.google.com/search?q=DistilBERT+Paper) — ⏱️ ~15 min
- [ ] 🎥 [Knowledge Distillation Explained](https://www.youtube.com/results?search_query=Knowledge+Distillation+Explained) — ⏱️ ~25 min
- [ ] 📝 [KD Tutorial — PyTorch](https://www.google.com/search?q=KD+Tutorial+%E2%80%94+PyTorch) — ⏱️ ~15 min

*⏱️ Resource time this block: ~70 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Read & modify an OpenCV C++ program
**Task:** Read & understand: read & modify an opencv c++ program. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Read & modify an OpenCV C++ program — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Plus (Intermediate)**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: read & modify an opencv c++ program. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 🎓 [HelloC++ — C++ Plus (Intermediate)](https://www.google.com/search?q=HelloC%2B%2B+%E2%80%94+C%2B%2B+Plus+%28Intermediate%29) — ⏱️ ~45 min
- [ ] 📦 [OpenCV GitHub](https://www.google.com/search?q=OpenCV+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [C++ — The Cherno (read-along)](https://www.youtube.com/results?search_query=C%2B%2B+%E2%80%94+The+Cherno+%28read-along%29) — ⏱️ ~25 min

*⏱️ Resource time this block: ~80 min*

---
## 🧩 DSA | 19:00–20:30 | Binary search
**Task:** Name the pattern, then solve 3–5 Binary search problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Binary search problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Binary search**).
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

[[Day05|← Day 5]]  |  [[Day07|Day 7 →]]

---

*[[Index|🏠 Back to Index]]*
