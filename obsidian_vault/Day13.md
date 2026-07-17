# Day 13 — VLA Models Deep Dive

> **Phase:** 🧠 Phase 3 — Generative AI for Robotics  ·  **📅 Week 3 · Mon**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 VLA models deep dive | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Retrieval-Augmented VLA | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Attention head pruning | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | DP I — 1D | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: VLA models deep dive
- 🗄️ Milvus *(supporting tool)*: Retrieval-Augmented VLA
- 🗜️ Compression: Attention head pruning
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: DP I — 1D

**🤖 Capstone today →** ⭐ `policy.py`: understand the VLA you'll fine-tune (action tokens, VLM backbone).

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~345 min (~5.8 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 openpi — π0 / π0.5 open VLA (Physical Intelligence) — [open](https://github.com/Physical-Intelligence/openpi)
- 🔥 Run GR00T N1.5 in LeRobot — hands-on — [open](https://huggingface.co/blog/nvidia/nvidia-isaac-gr00t-in-lerobot)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Summarise mock interview weaknesses. Commit to fixing this week.

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
## 🧠 New Concept | 9:30–11:00 | RT-2, OpenVLA, π0, GR00T N1
**Task:** VLM backbone + action decoder. Discrete vs diffusion action heads. Action tokenisation.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand RT-2, OpenVLA, π0, GR00T N1.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**RT-2 Paper (Brohan et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 13 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **RT-2, OpenVLA, π0, GR00T N1** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain RT-2, OpenVLA, π0, GR00T N1 aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [RT-2 Paper (Brohan et al.)](https://arxiv.org/abs/2307.15818) — ⏱️ ~15 min
- [ ] 📄 [OpenVLA Paper](https://arxiv.org/abs/2406.09246) — ⏱️ ~15 min
- [ ] 📄 [π0 Paper — Physical Intelligence](https://www.physicalintelligence.company/blog/pi0) — ⏱️ ~15 min
- [ ] 📄 [State of VLA at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html) — ⏱️ ~15 min
- [ ] 🎥 [VLA Models Explained](https://www.youtube.com/watch?v=Ow1_k5ysM6A) — ⏱️ ~25 min
- [ ] 🔥 📦 [openpi — π0 / π0.5 open VLA (Physical Intelligence)](https://github.com/Physical-Intelligence/openpi) — ⏱️ ~10 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Load & Run a VLA (SmolVLA-first)
**Task:** Load SmolVLA-450M via LeRobot; run inference on one frame from the SO-100 pick-place dataset; print the 7-DoF action + decode the action tokens. Deliverable: an action vector + a 2-sentence note on the VLM→action flow. Paper: π0 (arXiv 2410.24164).

**🎯 Outcome:** Working code plus saved output for Load & Run a VLA (SmolVLA-first).

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`load_run_a_vla_smolvla_first.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day13/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install lerobot transformers numpy pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest load_run_a_vla_smolvla_first.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`load_run_a_vla_smolvla_first.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest load_run_a_vla_smolvla_first.py -q` until **everything is green**. That completes: Load SmolVLA-450M via LeRobot; run inference on one frame from the SO-100 pick-place dataset; print the 7-DoF action + decode the action tokens. Deliverable: an action vector + a 2-sentence note on the VLM→action flow. Paper: π0 (arXiv 2410.24164).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [SmolVLA — 450M VLA, start here](https://huggingface.co/blog/smolvla) — ⏱️ ~15 min
- [ ] 📦 [OpenVLA GitHub](https://github.com/openvla/openvla) — ⏱️ ~10 min
- [ ] 📄 [OpenVLA-7B HuggingFace (heavier alt)](https://huggingface.co/openvla/openvla-7b) — ⏱️ ~15 min
- [ ] 📦 [LeRoBot GitHub (HuggingFace)](https://github.com/huggingface/lerobot) — ⏱️ ~10 min
- [ ] 📝 [LeRobot Quickstart](https://github.com/huggingface/lerobot#quick-start) — ⏱️ ~15 min
- [ ] 🔥 📝 [Run GR00T N1.5 in LeRobot — hands-on](https://huggingface.co/blog/nvidia/nvidia-isaac-gr00t-in-lerobot) — ⏱️ ~15 min

*⏱️ Resource time this block: ~80 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Retrieval-Augmented VLA
**Task:** Store robot demo trajectories as embeddings. At inference: encode observation → retrieve top-3 demos → prepend as context.

**🎯 Outcome:** A working Milvus operation for Milvus — Retrieval-Augmented VLA.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`retrieval_augmented_vla.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day13/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest retrieval_augmented_vla.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`retrieval_augmented_vla.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest retrieval_augmented_vla.py -q` until **everything is green**. That completes: Store robot demo trajectories as embeddings. At inference: encode observation → retrieve top-3 demos → prepend as context.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📝 [RAG with Milvus — Tutorial](https://milvus.io/docs/integrate_with_langchain.md) — ⏱️ ~15 min
- [ ] 📝 [Retrieval-Augmented Robot Learning](https://zilliz.com/blog) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | Attention Head Pruning
**Task:** Remove least-important heads in ViT using Taylor expansion importance scores.

**🎯 Outcome:** A before/after measurement for Compression — Attention Head Pruning.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`attention_head_pruning.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day13/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest attention_head_pruning.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`attention_head_pruning.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest attention_head_pruning.py -q` until **everything is green**. That completes: Remove least-important heads in ViT using Taylor expansion importance scores.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Are Sixteen Heads Really Better Than One?](https://arxiv.org/abs/1905.10650) — ⏱️ ~15 min
- [ ] 📝 [Attention Head Pruning Tutorial](https://towardsdatascience.com/pruning-attention-heads-dba4d8aa9db4) — ⏱️ ~15 min
- [ ] 📦 [transformers GitHub](https://github.com/huggingface/transformers) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: ⭐ `policy.py`: understand the VLA you'll fine-tune (action tokens, VLM backbone). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
!python src/policy.py
```

   ✅ **You should see:** it runs and prints results / `TODO`s with no red error.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: ⭐ `policy.py`: understand the VLA you'll fine-tune (action tokens, VLM backbone). Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | DP I — 1D
**Task:** Name the pattern, then solve 3–5 DP I — 1D problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — DP I — 1D problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**DP I — 1D**).
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

[[Day12|← Day 12]]  |  [[Day14|Day 14 →]]

---

*[[Index|🏠 Back to Index]]*
