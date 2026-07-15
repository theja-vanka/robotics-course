# Day 04 — Vision Transformers + SAM

> **Phase:** 🧱 Phase 1 — Foundations  ·  **📅 Week 1 · Thu**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 ViT, DINOv2, SAM 2 | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ DINOv2 object store | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Pruning theory | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Classes, headers & interfaces | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Stacks & queues | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: ViT, DINOv2, SAM 2
- 🗄️ Milvus *(supporting tool)*: DINOv2 object store
- 🗜️ Compression: Pruning theory
- ⚙️ C++ *(literacy — read & modify)*: Classes, headers & interfaces
- 🧩 DSA: Stacks & queues

**🤖 Capstone today →** `observe.py`: add SAM/ViT segmentation to turn frames into structured observations.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~410 min (~6.8 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 DINOv3 — SOTA self-supervised vision features (2025) — [open](https://www.google.com/search?q=open)
- 🔥 SAM 3 — Segment Anything with Concepts (Meta, 2025) — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Draw diffusion forward/reverse process from memory.

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
## 🧠 New Concept | 9:30–11:00 | ViT, DINOv2, SAM 2
**Task:** Patch embeddings, MHSA in vision, self-supervised features, SAM zero-shot segmentation.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand ViT, DINOv2, SAM 2.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**ViT Paper (Dosovitskiy et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 04 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **ViT, DINOv2, SAM 2** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain ViT, DINOv2, SAM 2 aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [ViT Paper (Dosovitskiy et al.)](https://www.google.com/search?q=ViT+Paper+%28Dosovitskiy+et+al.%29) — ⏱️ ~15 min
- [ ] 📄 [DINOv2 Paper](https://www.google.com/search?q=DINOv2+Paper) — ⏱️ ~15 min
- [ ] 📄 [SAM Paper (Kirillov et al.)](https://www.google.com/search?q=SAM+Paper+%28Kirillov+et+al.%29) — ⏱️ ~15 min
- [ ] 🎥 [ViT Explained — Yannic Kilcher](https://www.youtube.com/results?search_query=ViT+Explained+%E2%80%94+Yannic+Kilcher) — ⏱️ ~25 min
- [ ] 📝 [DINOv2 Blog — Meta AI](https://www.google.com/search?q=DINOv2+Blog+%E2%80%94+Meta+AI) — ⏱️ ~15 min
- [ ] 🔥 📄 [DINOv3 — SOTA self-supervised vision features (2025)](https://www.google.com/search?q=DINOv3+%E2%80%94+SOTA+self-supervised+vision+features+%282025%29) — ⏱️ ~15 min

*⏱️ Resource time this block: ~100 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run SAM 2 on Robot Scene
**Task:** Run SAM 2.1 on a tabletop image; extract per-object masks. Deliverable: at least 3 masks saved as an overlay PNG + the mask count printed. Paper: SAM (arXiv 2304.02643).

**🎯 Outcome:** Working code plus saved output for Run SAM 2 on Robot Scene.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_sam_2_on_robot_scene.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day04/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install ultralytics datasets pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_sam_2_on_robot_scene.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_sam_2_on_robot_scene.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_sam_2_on_robot_scene.py -q` until **everything is green**. That completes: Run SAM 2.1 on a tabletop image; extract per-object masks. Deliverable: at least 3 masks saved as an overlay PNG + the mask count printed. Paper: SAM (arXiv 2304.02643).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [SAM 2 GitHub (Meta)](https://www.google.com/search?q=SAM+2+GitHub+%28Meta%29) — ⏱️ ~10 min
- [ ] 📄 [SAM 2 HuggingFace Docs](https://www.google.com/search?q=SAM+2+HuggingFace+Docs) — ⏱️ ~15 min
- [ ] 🎥 [SAM 2 Demo & Tutorial](https://www.youtube.com/results?search_query=SAM+2+Demo+%26+Tutorial) — ⏱️ ~25 min
- [ ] 🔥 📦 [SAM 3 — Segment Anything with Concepts (Meta, 2025)](https://www.google.com/search?q=SAM+3+%E2%80%94+Segment+Anything+with+Concepts+%28Meta%2C+2025%29) — ⏱️ ~10 min

*⏱️ Resource time this block: ~60 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | DINOv2 Object Store
**Task:** Encode SAM-segmented object crops with DINOv2. Store in Milvus. Query: find similar objects.

**🎯 Outcome:** A working Milvus operation for Milvus — DINOv2 Object Store.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`dinov2_object_store.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day04/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest dinov2_object_store.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`dinov2_object_store.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest dinov2_object_store.py -q` until **everything is green**. That completes: Encode SAM-segmented object crops with DINOv2. Store in Milvus. Query: find similar objects.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Multi-Vector Search](https://www.google.com/search?q=Milvus+Multi-Vector+Search) — ⏱️ ~15 min
- [ ] 📄 [DINOv2 HuggingFace](https://www.google.com/search?q=DINOv2+HuggingFace) — ⏱️ ~15 min
- [ ] 📝 [Image Similarity Search Tutorial — Milvus](https://www.google.com/search?q=Image+Similarity+Search+Tutorial+%E2%80%94+Milvus) — ⏱️ ~15 min

*⏱️ Resource time this block: ~45 min*

---
## 🗜️ Compression | 15:45–17:15 | Pruning Theory
**Task:** Magnitude pruning, L1/L2 unstructured, structured channel pruning.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Compression — Pruning Theory.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**PyTorch Pruning Tutorial**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 04 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Compression — Pruning Theory** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Compression — Pruning Theory aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PyTorch Pruning Tutorial](https://www.google.com/search?q=PyTorch+Pruning+Tutorial) — ⏱️ ~15 min
- [ ] 📄 [torch.nn.utils.prune Docs](https://www.google.com/search?q=torch.nn.utils.prune+Docs) — ⏱️ ~15 min
- [ ] 🎥 [Neural Network Pruning Explained](https://www.youtube.com/results?search_query=Neural+Network+Pruning+Explained) — ⏱️ ~25 min
- [ ] 📄 [Pruning Paper Survey](https://www.google.com/search?q=Pruning+Paper+Survey) — ⏱️ ~15 min

*⏱️ Resource time this block: ~70 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Classes, headers & interfaces
**Task:** Read & understand: classes, headers & interfaces. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Classes, headers & interfaces — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Fundamentals Course**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: classes, headers & interfaces. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 🎓 [HelloC++ — C++ Fundamentals Course](https://www.google.com/search?q=HelloC%2B%2B+%E2%80%94+C%2B%2B+Fundamentals+Course) — ⏱️ ~45 min
- [ ] 📄 [cppreference — read C++](https://www.google.com/search?q=cppreference+%E2%80%94+read+C%2B%2B) — ⏱️ ~15 min
- [ ] 🎥 [C++ — The Cherno (read-along)](https://www.youtube.com/results?search_query=C%2B%2B+%E2%80%94+The+Cherno+%28read-along%29) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Stacks & queues
**Task:** Name the pattern, then solve 3–5 Stacks & queues problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Stacks & queues problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Stacks & queues**).
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

[[Day03|← Day 3]]  |  [[Day05|Day 5 →]]

---

*[[Index|🏠 Back to Index]]*
