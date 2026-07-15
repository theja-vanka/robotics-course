# Day 22 — System Design for Robotics CV

> **Phase:** 🎯 Phase 4 — Interview Mastery + Second Product  ·  **📅 Week 4 · Thu**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 System design | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Milvus production design | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ 30ms budget design | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Monotonic stack / queue | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: System design
- 🗄️ Milvus *(supporting tool)*: Milvus production design
- 🗜️ Compression: 30ms budget design
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Monotonic stack / queue

**🤖 Capstone today →** System-design the `vla-edge` service; write the architecture section of the README.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~265 min (~4.4 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 YOLO26 on NVIDIA Jetson — setup & benchmarks — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Flashcard: Adam update rule, diffusion ELBO three terms.

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
## 🧠 New Concept | 9:30–11:00 | Production System Design
**Task:** Data pipeline, model registry, latency budgets, failure modes, retraining loops.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Production System Design.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**ML System Design — Chip Huyen Book**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 22 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Production System Design** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Production System Design aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [ML System Design — Chip Huyen Book](https://www.google.com/search?q=ML+System+Design+%E2%80%94+Chip+Huyen+Book) — ⏱️ ~15 min
- [ ] 📝 [Designing ML Systems — Stanford CS329S](https://www.google.com/search?q=Designing+ML+Systems+%E2%80%94+Stanford+CS329S) — ⏱️ ~15 min
- [ ] 🎥 [ML System Design Interview](https://www.youtube.com/results?search_query=ML+System+Design+Interview) — ⏱️ ~25 min

*⏱️ Resource time this block: ~55 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Add Latency Profiler
**Task:** Add per-stage timing to the Day-20 pipeline; log to CSV; find the bottleneck. Deliverable: a CSV of per-stage ms + the slowest stage named + one optimization tried (before/after).

**🎯 Outcome:** Working code plus saved output for Add Latency Profiler.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`add_latency_profiler.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day22/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch numpy pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest add_latency_profiler.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`add_latency_profiler.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest add_latency_profiler.py -q` until **everything is green**. That completes: Add per-stage timing to the Day-20 pipeline; log to CSV; find the bottleneck. Deliverable: a CSV of per-stage ms + the slowest stage named + one optimization tried (before/after).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Python cProfile Docs](https://www.google.com/search?q=Python+cProfile+Docs) — ⏱️ ~15 min
- [ ] 📝 [Profiling Python Code Guide](https://www.google.com/search?q=Profiling+Python+Code+Guide) — ⏱️ ~15 min

*⏱️ Resource time this block: ~30 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Production System Design Doc
**Task:** Write design doc: how Milvus fits in a production robot perception system. Cover sharding, replication, incremental upsert.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Milvus — Production System Design Doc.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**Milvus Deployment Guide**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 22 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Milvus — Production System Design Doc** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Milvus — Production System Design Doc aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Deployment Guide](https://www.google.com/search?q=Milvus+Deployment+Guide) — ⏱️ ~15 min
- [ ] 📄 [Milvus Replica Docs](https://www.google.com/search?q=Milvus+Replica+Docs) — ⏱️ ~15 min
- [ ] 📄 [Milvus Official Docs](https://www.google.com/search?q=Milvus+Official+Docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~45 min*

---
## 🗜️ Compression | 15:45–17:15 | Real-time Constraint Design
**Task:** Design a compressed pipeline fitting 30ms latency budget. Document trade-offs per model.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Compression — Real-time Constraint Design.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**Jetson Orin Benchmarks**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 22 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Compression — Real-time Constraint Design** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Compression — Real-time Constraint Design aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Jetson Orin Benchmarks](https://www.google.com/search?q=Jetson+Orin+Benchmarks) — ⏱️ ~15 min
- [ ] 📝 [Latency Optimization for CV — Blog](https://www.google.com/search?q=Latency+Optimization+for+CV+%E2%80%94+Blog) — ⏱️ ~15 min
- [ ] 🔥 📄 [YOLO26 on NVIDIA Jetson — setup & benchmarks](https://www.google.com/search?q=YOLO26+on+NVIDIA+Jetson+%E2%80%94+setup+%26+benchmarks) — ⏱️ ~15 min

*⏱️ Resource time this block: ~45 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: System-design the `vla-edge` service; write the architecture section of the README. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: System-design the `vla-edge` service; write the architecture section of the README. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] You ran it again and changed one variable
- [ ] A new number is in your benchmark CSV
- [ ] You can say which direction to push next

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PEFT / LoRA docs](https://www.google.com/search?q=PEFT+%2F+LoRA+docs) — ⏱️ ~15 min
- [ ] 📦 [LeRoBot GitHub (HuggingFace)](https://www.google.com/search?q=LeRoBot+GitHub+%28HuggingFace%29) — ⏱️ ~10 min
- [ ] 📄 [PyTorch benchmark utils](https://www.google.com/search?q=PyTorch+benchmark+utils) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🧩 DSA | 19:00–20:30 | Monotonic stack / queue
**Task:** Name the pattern, then solve 3–5 Monotonic stack / queue problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Monotonic stack / queue problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Monotonic stack / queue**).
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

[[Day21|← Day 21]]  |  [[Day23|Day 23 →]]

---

*[[Index|🏠 Back to Index]]*
