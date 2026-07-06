# Day 05 — 3D Representations: NeRF → 3DGS

> **Phase:** 🧱 Phase 1 — Foundations  ·  **📅 Week 1 · Fri**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 NeRF → 3DGS | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Milvus schema design | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Pruning hands-on | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | CMake — build someone else's project | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Linked lists | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: NeRF → 3DGS
- 🗄️ Milvus *(supporting tool)*: Milvus schema design
- 🗜️ Compression: Pruning hands-on
- ⚙️ C++ *(literacy — read & modify)*: CMake — build someone else's project
- 🧩 DSA: Linked lists

**🤖 Capstone today →** 3D representations — awareness; note where 3DGS could enrich observations later.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~375 min (~6.2 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 Depth Anything 3 — geometry from any views (ICLR 2026) — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Quiz: ViT vs CNN, SAM architecture in 3 sentences.

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
## 🧠 New Concept | 9:30–11:00 | NeRF → 3D Gaussian Splatting
**Task:** Volume rendering, positional encoding, ray marching. 3DGS: Gaussian primitives, splatting, rasterisation.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand NeRF → 3D Gaussian Splatting.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**NeRF Paper (Mildenhall et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 05 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **NeRF → 3D Gaussian Splatting** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain NeRF → 3D Gaussian Splatting aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [NeRF Paper (Mildenhall et al.)](https://www.google.com/search?q=NeRF+Paper+%28Mildenhall+et+al.%29) — ⏱️ ~15 min
- [ ] 📄 [3DGS Paper (Kerbl et al.)](https://www.google.com/search?q=3DGS+Paper+%28Kerbl+et+al.%29) — ⏱️ ~15 min
- [ ] 📄 [3DGS in Robotics Survey](https://www.google.com/search?q=3DGS+in+Robotics+Survey) — ⏱️ ~15 min
- [ ] 🎥 [NeRF Explained — Two Minute Papers](https://www.youtube.com/results?search_query=NeRF+Explained+%E2%80%94+Two+Minute+Papers) — ⏱️ ~25 min
- [ ] 🎥 [3D Gaussian Splatting Explained](https://www.youtube.com/results?search_query=3D+Gaussian+Splatting+Explained) — ⏱️ ~25 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Train 3DGS with Nerfstudio
**Task:** Capture a 30-frame video; train splatfacto (Nerfstudio) to a stable loss; render 3 novel views. Deliverable: a .ply of Gaussians + 3 rendered views. Paper: 3D Gaussian Splatting (arXiv 2308.04079).

**🎯 Outcome:** Working code plus saved output for Train 3DGS with Nerfstudio.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day05_train_3dgs_with_nerfstudio.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day05_train_3dgs_with_nerfstudio.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day05_train_3dgs_with_nerfstudio.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day05_train_3dgs_with_nerfstudio.py -q` until **everything is green**. That completes: Capture a 30-frame video; train splatfacto (Nerfstudio) to a stable loss; render 3 novel views. Deliverable: a .ply of Gaussians + 3 rendered views. Paper: 3D Gaussian Splatting (arXiv 2308.04079).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [Nerfstudio GitHub](https://www.google.com/search?q=Nerfstudio+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Nerfstudio Getting Started](https://www.google.com/search?q=Nerfstudio+Getting+Started) — ⏱️ ~15 min
- [ ] 🎥 [Nerfstudio Tutorial](https://www.youtube.com/results?search_query=Nerfstudio+Tutorial) — ⏱️ ~25 min
- [ ] 🔥 📦 [Depth Anything 3 — geometry from any views (ICLR 2026)](https://www.google.com/search?q=Depth+Anything+3+%E2%80%94+geometry+from+any+views+%28ICLR+2026%29) — ⏱️ ~10 min

*⏱️ Resource time this block: ~60 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Production Schema Design
**Task:** Design schema for robot data: image_id, object_class, embedding, timestamp, metadata. Implement it.

**🎯 Outcome:** A working Milvus operation for Milvus — Production Schema Design.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day05_production_schema_design.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day05_production_schema_design.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day05_production_schema_design.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day05_production_schema_design.py -q` until **everything is green**. That completes: Design schema for robot data: image_id, object_class, embedding, timestamp, metadata. Implement it.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Schema Design Guide](https://www.google.com/search?q=Milvus+Schema+Design+Guide) — ⏱️ ~15 min
- [ ] 📄 [Milvus Data Types Reference](https://www.google.com/search?q=Milvus+Data+Types+Reference) — ⏱️ ~15 min
- [ ] 📝 [Milvus Best Practices — Zilliz](https://www.google.com/search?q=Milvus+Best+Practices+%E2%80%94+Zilliz) — ⏱️ ~15 min

*⏱️ Resource time this block: ~45 min*

---
## 🗜️ Compression | 15:45–17:15 | Pruning Hands-on
**Task:** Prune ResNet-50 with torch.nn.utils.prune. Measure accuracy drop vs parameter reduction.

**🎯 Outcome:** A before/after measurement for Compression — Pruning Hands-on.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day05_pruning_hands_on.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day05_pruning_hands_on.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day05_pruning_hands_on.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day05_pruning_hands_on.py -q` until **everything is green**. That completes: Prune ResNet-50 with torch.nn.utils.prune. Measure accuracy drop vs parameter reduction.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PyTorch Pruning Tutorial](https://www.google.com/search?q=PyTorch+Pruning+Tutorial) — ⏱️ ~15 min
- [ ] 📦 [torchvision Models](https://www.google.com/search?q=torchvision+Models) — ⏱️ ~10 min
- [ ] 📝 [Structured Pruning Guide](https://www.google.com/search?q=Structured+Pruning+Guide) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | CMake — build someone else's project
**Task:** Read & understand: cmake — build someone else's project. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — CMake — build someone else's project — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Fundamentals Course**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: cmake — build someone else's project. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 🎓 [HelloC++ — C++ Fundamentals Course](https://www.google.com/search?q=HelloC%2B%2B+%E2%80%94+C%2B%2B+Fundamentals+Course) — ⏱️ ~45 min
- [ ] 📝 [Modern CMake (read)](https://www.google.com/search?q=Modern+CMake+%28read%29) — ⏱️ ~15 min
- [ ] 🎥 [C++ — The Cherno (read-along)](https://www.youtube.com/results?search_query=C%2B%2B+%E2%80%94+The+Cherno+%28read-along%29) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Linked lists
**Task:** Name the pattern, then solve 3–5 Linked lists problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Linked lists problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Linked lists**).
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

[[Day04|← Day 4]]  |  [[Day06|Day 6 →]]

---

*[[Index|🏠 Back to Index]]*
