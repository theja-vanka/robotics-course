# Day 18 — World Models for Robotics

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 3 · Sat**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 World models / DreamerV3 | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ World model memory | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Flash Attention | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Matrix & simulation | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: World models / DreamerV3
- 🗄️ Milvus *(supporting tool)*: World model memory
- 🗜️ Compression: Flash Attention
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Matrix & simulation

**🤖 Capstone today →** World models + Jetson context → fixes your deploy target and latency budget.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~325 min (~5.4 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 Genie 3 — real-time interactive world model (DeepMind) — [open](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
- 🔥 FlashAttention-3 — async + FP8 attention (Dao-AILab) — [open](https://github.com/Dao-AILab/flash-attention)

> 🌴 **Tomorrow is your rest day (Sunday).** No study — let memory consolidate off-screen.

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Flash: ControlNet architecture in 3 sentences.

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
## 🧠 New Concept | 9:30–11:00 | UniSim, DreamerV3, DIAMOND
**Task:** Latent world models, RSSM, video prediction for robot planning.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand UniSim, DreamerV3, DIAMOND.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**DreamerV3 Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 18 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **UniSim, DreamerV3, DIAMOND** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain UniSim, DreamerV3, DIAMOND aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [DreamerV3 Paper](https://arxiv.org/abs/2301.04104) — ⏱️ ~15 min
- [ ] 📦 [DreamerV3 GitHub](https://github.com/danijar/dreamerv3) — ⏱️ ~10 min
- [ ] 📄 [UniSim Paper](https://arxiv.org/abs/2310.06114) — ⏱️ ~15 min
- [ ] 🎥 [World Models Explained — Yannic Kilcher](https://www.youtube.com/watch?v=dPmHnQ6aABQ) — ⏱️ ~25 min
- [ ] 📝 [DreamerV3 Blog — DeepMind](https://deepmind.google/discover/blog/mastering-diverse-domains-through-world-models/) — ⏱️ ~15 min
- [ ] 🔥 📝 [Genie 3 — real-time interactive world model (DeepMind)](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — ⏱️ ~15 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run DreamerV3
**Task:** Run DreamerV3 on DMControl walker-walk; visualise imagined vs real rollouts. Deliverable: a rollout GIF + a return curve reaching at least 300. Paper: DreamerV3 (arXiv 2301.04104).

**🎯 Outcome:** Working code plus saved output for Run DreamerV3.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_dreamerv3.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day18/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install # clone the repo in the resources, then: pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_dreamerv3.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_dreamerv3.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_dreamerv3.py -q` until **everything is green**. That completes: Run DreamerV3 on DMControl walker-walk; visualise imagined vs real rollouts. Deliverable: a rollout GIF + a return curve reaching at least 300. Paper: DreamerV3 (arXiv 2301.04104).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [DreamerV3 GitHub](https://github.com/danijar/dreamerv3) — ⏱️ ~10 min
- [ ] 📄 [DMControl Suite](https://github.com/google-deepmind/dm_control) — ⏱️ ~15 min
- [ ] 🎥 [DreamerV3 Demo](https://www.youtube.com/watch?v=vfpZu0R1s_Y) — ⏱️ ~25 min

*⏱️ Resource time this block: ~50 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | World Model State Memory
**Task:** Store RSSM belief vectors in Milvus. Retrieve similar past states to warm-start planning.

**🎯 Outcome:** A working Milvus operation for Milvus — World Model State Memory.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`world_model_state_memory.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day18/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest world_model_state_memory.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`world_model_state_memory.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest world_model_state_memory.py -q` until **everything is green**. That completes: Store RSSM belief vectors in Milvus. Retrieve similar past states to warm-start planning.
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
- [ ] 📝 [Vector DBs for Temporal Data](https://zilliz.com/blog) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | Flash Attention & Speculative Decoding
**Task:** Memory-efficient attention, KV cache, draft + target model speculative decoding.

**🎯 Outcome:** A before/after measurement for Compression — Flash Attention & Speculative Decoding.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`flash_attention_speculative_decoding.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day18/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest flash_attention_speculative_decoding.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`flash_attention_speculative_decoding.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest flash_attention_speculative_decoding.py -q` until **everything is green**. That completes: Memory-efficient attention, KV cache, draft + target model speculative decoding.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Flash Attention Paper](https://arxiv.org/abs/2205.14135) — ⏱️ ~15 min
- [ ] 📦 [Flash Attention GitHub](https://github.com/Dao-AILab/flash-attention) — ⏱️ ~10 min
- [ ] 📝 [Speculative Decoding Explained](https://huggingface.co/blog/assisted-generation) — ⏱️ ~15 min
- [ ] 🔥 📦 [FlashAttention-3 — async + FP8 attention (Dao-AILab)](https://github.com/Dao-AILab/flash-attention) — ⏱️ ~10 min

*⏱️ Resource time this block: ~50 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: World models + Jetson context → fixes your deploy target and latency budget. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: World models + Jetson context → fixes your deploy target and latency budget. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | Matrix & simulation
**Task:** Name the pattern, then solve 3–5 Matrix & simulation problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Matrix & simulation problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Matrix & simulation**).
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

[[Day17|← Day 17]]  |  [[Day19|Day 19 →]]

---

*[[Index|🏠 Back to Index]]*
