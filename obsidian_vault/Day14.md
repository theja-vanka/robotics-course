# Day 14 — Fine-tuning VLA Models

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 3 · Tue**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 LoRA / QLoRA fine-tuning | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Demo replay buffer | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ QLoRA compression | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | DP II — grids / 2D | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: LoRA / QLoRA fine-tuning
- 🗄️ Milvus *(supporting tool)*: Demo replay buffer
- 🗜️ Compression: QLoRA compression
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: DP II — grids / 2D

**🤖 Capstone today →** ⭐ `train_lora.py`: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16).

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~340 min (~5.7 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 SmolVLA — 450M open VLA that runs on consumer hardware (HF) — [open](https://www.google.com/search?q=open)
- 🔥 FP4 (NVFP4/MXFP4) on Blackwell — when it's worth it — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Draw VLA encoder + action decoder from memory.

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
## 🧠 New Concept | 9:30–11:00 | LoRA, QLoRA, PEFT
**Task:** Low-rank matrices, rank selection, target modules, merge vs unmerge.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand LoRA, QLoRA, PEFT.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**LoRA Paper**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 14 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **LoRA, QLoRA, PEFT** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain LoRA, QLoRA, PEFT aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [LoRA Paper](https://www.google.com/search?q=LoRA+Paper) — ⏱️ ~15 min
- [ ] 📦 [PEFT Library GitHub](https://www.google.com/search?q=PEFT+Library+GitHub) — ⏱️ ~10 min
- [ ] 🎥 [LoRA Explained — Andrej Karpathy Style](https://www.youtube.com/results?search_query=LoRA+Explained+%E2%80%94+Andrej+Karpathy+Style) — ⏱️ ~25 min
- [ ] 📝 [PEFT Quickstart Docs](https://www.google.com/search?q=PEFT+Quickstart+Docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~65 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Fine-tune a VLA (SmolVLA) with LoRA
**Task:** LoRA fine-tune SmolVLA (r=16, target q_proj/v_proj) on the SO-100 pick-place set for ~2k steps. Deliverable: a saved adapter + train-loss curve; success-rate lift vs zero-shot reported (target at least +10pp). Paper: LoRA (arXiv 2106.09685).

**🎯 Outcome:** Working code plus saved output for Fine-tune a VLA (SmolVLA) with LoRA.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day14_fine_tune_a_vla_smolvla_with_lora.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install lerobot transformers numpy pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day14_fine_tune_a_vla_smolvla_with_lora.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day14_fine_tune_a_vla_smolvla_with_lora.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day14_fine_tune_a_vla_smolvla_with_lora.py -q` until **everything is green**. That completes: LoRA fine-tune SmolVLA (r=16, target q_proj/v_proj) on the SO-100 pick-place set for ~2k steps. Deliverable: a saved adapter + train-loss curve; success-rate lift vs zero-shot reported (target at least +10pp). Paper: LoRA (arXiv 2106.09685).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [SmolVLA — fine-tune on consumer HW](https://www.google.com/search?q=SmolVLA+%E2%80%94+fine-tune+on+consumer+HW) — ⏱️ ~15 min
- [ ] 📦 [OpenVLA GitHub](https://www.google.com/search?q=OpenVLA+GitHub) — ⏱️ ~10 min
- [ ] 📦 [LeRoBot GitHub (HuggingFace)](https://www.google.com/search?q=LeRoBot+GitHub+%28HuggingFace%29) — ⏱️ ~10 min
- [ ] 📄 [PEFT LoRA Docs](https://www.google.com/search?q=PEFT+LoRA+Docs) — ⏱️ ~15 min
- [ ] 🎥 [Fine-tuning LLMs with LoRA](https://www.youtube.com/results?search_query=Fine-tuning+LLMs+with+LoRA) — ⏱️ ~25 min
- [ ] 🔥 📝 [SmolVLA — 450M open VLA that runs on consumer hardware (HF)](https://www.google.com/search?q=SmolVLA+%E2%80%94+450M+open+VLA+that+runs+on+consumer+hardware+%28HF%29) — ⏱️ ~15 min

*⏱️ Resource time this block: ~90 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Demo Replay Buffer
**Task:** After fine-tuning, index new demo embeddings. Build retrieval for hardest negative examples.

**🎯 Outcome:** A working Milvus operation for Milvus — Demo Replay Buffer.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day14_demo_replay_buffer.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day14_demo_replay_buffer.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day14_demo_replay_buffer.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day14_demo_replay_buffer.py -q` until **everything is green**. That completes: After fine-tuning, index new demo embeddings. Build retrieval for hardest negative examples.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Partition Docs](https://www.google.com/search?q=Milvus+Partition+Docs) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📝 [Contrastive Learning + Milvus](https://www.google.com/search?q=Contrastive+Learning+%2B+Milvus) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | LoRA + QLoRA
**Task:** Apply 4-bit QLoRA to OpenVLA with bitsandbytes. Compare memory vs full fine-tune.

**🎯 Outcome:** A before/after measurement for Compression — LoRA + QLoRA.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day14_lora_qlora.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day14_lora_qlora.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day14_lora_qlora.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day14_lora_qlora.py -q` until **everything is green**. That completes: Apply 4-bit QLoRA to OpenVLA with bitsandbytes. Compare memory vs full fine-tune.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [QLoRA Paper](https://www.google.com/search?q=QLoRA+Paper) — ⏱️ ~15 min
- [ ] 📦 [bitsandbytes GitHub](https://www.google.com/search?q=bitsandbytes+GitHub) — ⏱️ ~10 min
- [ ] 📝 [QLoRA Fine-tuning Guide](https://www.google.com/search?q=QLoRA+Fine-tuning+Guide) — ⏱️ ~15 min
- [ ] 🔥 📝 [FP4 (NVFP4/MXFP4) on Blackwell — when it's worth it](https://www.google.com/search?q=FP4+%28NVFP4%2FMXFP4%29+on+Blackwell+%E2%80%94+when+it%27s+worth+it) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: ⭐ `train_lora.py`: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
!python src/train_lora.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: ⭐ `train_lora.py`: LoRA fine-tune SmolVLA on a public LeRobot dataset — beat the zero-shot baseline (your own synthetic demos come Days 15–16). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | DP II — grids / 2D
**Task:** Name the pattern, then solve 3–5 DP II — grids / 2D problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — DP II — grids / 2D problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**DP II — grids / 2D**).
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

[[Day13|← Day 13]]  |  [[Day15|Day 15 →]]

---

*[[Index|🏠 Back to Index]]*
