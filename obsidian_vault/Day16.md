# Day 16 — Synthetic Demos for VLA — At Scale

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 3 · Thu**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Synthetic VLA demos — at scale | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Demo-episode browser | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ EfficientDet/NAS | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Intervals & sorting | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Synthetic VLA demos — at scale
- 🗄️ Milvus *(supporting tool)*: Demo-episode browser
- 🗜️ Compression: EfficientDet/NAS
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Intervals & sorting

**🤖 Capstone today →** Scale to ~200+ episodes in LeRobot format — the set you'll re-fine-tune on for robustness (baseline fine-tune was Day 14).

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~300 min (~5.0 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 Cosmos-Predict 2.5 — improved world simulation (NVIDIA) — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Flashcard: the 4-stage GR00T data blueprint (Teleop → MimicGen → Neural Trajectory → Fine-tune).

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
## 🧠 New Concept | 9:30–11:00 | GR00T-Dreams & Neural-Trajectory Pipelines
**Task:** World foundation models (Cosmos-Predict2) generate action videos → inverse dynamics → 'neural trajectories'. The 4-stage GR00T blueprint compresses ~6,500 human hours into ~11 GPU-hours. Decide which stages you'll run vs. use pre-generated data.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand GR00T-Dreams & Neural-Trajectory Pipelines.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**NVIDIA GR00T-Dreams (DreamGen)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 16 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **GR00T-Dreams & Neural-Trajectory Pipelines** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain GR00T-Dreams & Neural-Trajectory Pipelines aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [NVIDIA GR00T-Dreams (DreamGen)](https://www.google.com/search?q=NVIDIA+GR00T-Dreams+%28DreamGen%29) — ⏱️ ~10 min
- [ ] 📄 [NVIDIA Isaac GR00T — Synthetic Manipulation Blueprint](https://www.google.com/search?q=NVIDIA+Isaac+GR00T+%E2%80%94+Synthetic+Manipulation+Blueprint) — ⏱️ ~15 min
- [ ] 📝 [NVIDIA — Synthetic Trajectory Data via World Foundation Models](https://www.google.com/search?q=NVIDIA+%E2%80%94+Synthetic+Trajectory+Data+via+World+Foundation+Models) — ⏱️ ~15 min
- [ ] 📄 [Isaac Lab — GPU robot-learning sim (paper)](https://www.google.com/search?q=Isaac+Lab+%E2%80%94+GPU+robot-learning+sim+%28paper%29) — ⏱️ ~15 min
- [ ] 🔥 📄 [Cosmos-Predict 2.5 — improved world simulation (NVIDIA)](https://www.google.com/search?q=Cosmos-Predict+2.5+%E2%80%94+improved+world+simulation+%28NVIDIA%29) — ⏱️ ~15 min

*⏱️ Resource time this block: ~70 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Build a Training-Ready Demo Set
**Task:** Generate ~200–500 episodes (MimicGen, or pre-generated GR00T/RoboCasa data); export in LeRobot format; point train_lora.py at it. Deliverable: at least 200 episodes that train_lora.py loads without error; count + avg length printed. Paper: DreamGen / GR00T-Dreams (arXiv 2505.12705).

**🎯 Outcome:** A working, committed increment of the product for Build a Training-Ready Demo Set.

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
!python src/train_lora.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Generate ~200–500 episodes (MimicGen, or pre-generated GR00T/RoboCasa data); export in LeRobot format; point train_lora.py at it. Deliverable: at least 200 episodes that train_lora.py loads without error; count + avg length printed. Paper: DreamGen / GR00T-Dreams (arXiv 2505.12705).
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [MimicGen — code & docs](https://www.google.com/search?q=MimicGen+%E2%80%94+code+%26+docs) — ⏱️ ~10 min
- [ ] 📦 [LeRoBot GitHub (HuggingFace)](https://www.google.com/search?q=LeRoBot+GitHub+%28HuggingFace%29) — ⏱️ ~10 min
- [ ] 📄 [RoboCasa365 — large-scale sim demos](https://www.google.com/search?q=RoboCasa365+%E2%80%94+large-scale+sim+demos) — ⏱️ ~15 min

*⏱️ Resource time this block: ~35 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Demo-Episode Browser
**Task:** Index every generated episode by instruction + observation embedding. Build a CLI: 'find episodes where the arm grasps from the left' → top-10. Use it to spot gaps in your synthetic set.

**🎯 Outcome:** A working Milvus operation for Milvus — Demo-Episode Browser.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day16_demo_episode_browser.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day16_demo_episode_browser.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day16_demo_episode_browser.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day16_demo_episode_browser.py -q` until **everything is green**. That completes: Index every generated episode by instruction + observation embedding. Build a CLI: 'find episodes where the arm grasps from the left' → top-10. Use it to spot gaps in your synthetic set.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Text Search Tutorial](https://www.google.com/search?q=Milvus+Text+Search+Tutorial) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📝 [Build a Semantic Search Engine](https://www.google.com/search?q=Build+a+Semantic+Search+Engine) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | EfficientDet Study
**Task:** BiFPN, compound scaling, EfficientNet backbone — understand the design principles.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Compression — EfficientDet Study.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**EfficientDet Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 16 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Compression — EfficientDet Study** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Compression — EfficientDet Study aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [EfficientDet Paper](https://www.google.com/search?q=EfficientDet+Paper) — ⏱️ ~15 min
- [ ] 📄 [EfficientNet Paper](https://www.google.com/search?q=EfficientNet+Paper) — ⏱️ ~15 min
- [ ] 🎥 [EfficientDet Explained](https://www.youtube.com/results?search_query=EfficientDet+Explained) — ⏱️ ~25 min
- [ ] 📦 [EfficientDet PyTorch](https://www.google.com/search?q=EfficientDet+PyTorch) — ⏱️ ~10 min

*⏱️ Resource time this block: ~65 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: Scale to ~200+ episodes in LeRobot format — the set you'll re-fine-tune on for robustness (baseline fine-tune was Day 14). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: Scale to ~200+ episodes in LeRobot format — the set you'll re-fine-tune on for robustness (baseline fine-tune was Day 14). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | Intervals & sorting
**Task:** Name the pattern, then solve 3–5 Intervals & sorting problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Intervals & sorting problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Intervals & sorting**).
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

[[Day15|← Day 15]]  |  [[Day17|Day 17 →]]

---

*[[Index|🏠 Back to Index]]*
