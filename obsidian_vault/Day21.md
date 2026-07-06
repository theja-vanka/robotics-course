# Day 21 — ML Fundamentals Refresh

> **Phase:** 🎯 Phase 4 — Interview Mastery + Second Product  ·  **📅 Week 4 · Wed**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 ML fundamentals refresh | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ ANN benchmarking | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Speculative decoding | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Sliding window (advanced) | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: ML fundamentals refresh
- 🗄️ Milvus *(supporting tool)*: ANN benchmarking
- 🗜️ Compression: Speculative decoding
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Sliding window (advanced)

**🤖 Capstone today →** ML refresh (skim) — solidify the eval math behind your benchmarks.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~305 min (~5.1 hr)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Watch your Day 20 Loom. Note 3 things to improve.

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
## 🧠 New Concept | 9:30–11:00 | Backprop, Optimisers, Losses
**Task:** Chain rule, Adam vs SGD, focal loss, contrastive loss, diffusion ELBO, score matching.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Backprop, Optimisers, Losses.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**Backpropagation Calculus — 3Blue1Brown**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 21 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Backprop, Optimisers, Losses** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Backprop, Optimisers, Losses aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 🎥 [Backpropagation Calculus — 3Blue1Brown](https://www.youtube.com/results?search_query=Backpropagation+Calculus+%E2%80%94+3Blue1Brown) — ⏱️ ~25 min
- [ ] 📝 [Adam Optimizer Explained](https://www.google.com/search?q=Adam+Optimizer+Explained) — ⏱️ ~15 min
- [ ] 🎥 [Loss Functions in Deep Learning](https://www.youtube.com/results?search_query=Loss+Functions+in+Deep+Learning) — ⏱️ ~25 min
- [ ] 📄 [Diffusion ELBO Derivation](https://www.google.com/search?q=Diffusion+ELBO+Derivation) — ⏱️ ~15 min

*⏱️ Resource time this block: ~80 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Implement Attention from Scratch
**Task:** Implement multi-head self-attention in pure PyTorch (no nn.MultiheadAttention); match torch's output within 1e-4 on a random input. Deliverable: a passing self_test() asserting allclose. Paper: Attention Is All You Need (arXiv 1706.03762).

**🎯 Outcome:** Working code plus saved output for Implement Attention from Scratch.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day21_implement_attention_from_scratch.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch numpy pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day21_implement_attention_from_scratch.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day21_implement_attention_from_scratch.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day21_implement_attention_from_scratch.py -q` until **everything is green**. That completes: Implement multi-head self-attention in pure PyTorch (no nn.MultiheadAttention); match torch's output within 1e-4 on a random input. Deliverable: a passing self_test() asserting allclose. Paper: Attention Is All You Need (arXiv 1706.03762).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 🎥 [Attention from Scratch — Andrej Karpathy](https://www.youtube.com/results?search_query=Attention+from+Scratch+%E2%80%94+Andrej+Karpathy) — ⏱️ ~25 min
- [ ] 📄 [Attention is All You Need Paper](https://www.google.com/search?q=Attention+is+All+You+Need+Paper) — ⏱️ ~15 min
- [ ] 📝 [Illustrated Transformer — Jay Alammar](https://www.google.com/search?q=Illustrated+Transformer+%E2%80%94+Jay+Alammar) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | ANN Benchmarking
**Task:** Benchmark HNSW vs IVF_PQ vs IVF_FLAT on your robot dataset. Plot recall@10 vs QPS.

**🎯 Outcome:** A working Milvus operation for Milvus — ANN Benchmarking.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day21_ann_benchmarking.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day21_ann_benchmarking.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day21_ann_benchmarking.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day21_ann_benchmarking.py -q` until **everything is green**. That completes: Benchmark HNSW vs IVF_PQ vs IVF_FLAT on your robot dataset. Plot recall@10 vs QPS.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [ANN Benchmarks Site](https://www.google.com/search?q=ANN+Benchmarks+Site) — ⏱️ ~15 min
- [ ] 📄 [Milvus Benchmark Docs](https://www.google.com/search?q=Milvus+Benchmark+Docs) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🗜️ Compression | 15:45–17:15 | Speculative Decoding Hands-on
**Task:** Implement simple speculative decoding loop with small draft + large target VLM.

**🎯 Outcome:** A before/after measurement for Compression — Speculative Decoding Hands-on.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`Day21_speculative_decoding_hands_on.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from your `intensive study/starter_code` folder. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest Day21_speculative_decoding_hands_on.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`Day21_speculative_decoding_hands_on.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest Day21_speculative_decoding_hands_on.py -q` until **everything is green**. That completes: Implement simple speculative decoding loop with small draft + large target VLM.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [Speculative Decoding — HuggingFace Blog](https://www.google.com/search?q=Speculative+Decoding+%E2%80%94+HuggingFace+Blog) — ⏱️ ~15 min
- [ ] 📄 [Speculative Decoding Paper](https://www.google.com/search?q=Speculative+Decoding+Paper) — ⏱️ ~15 min
- [ ] 📦 [transformers assisted generation](https://www.google.com/search?q=transformers+assisted+generation) — ⏱️ ~10 min

*⏱️ Resource time this block: ~40 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: ML refresh (skim) — solidify the eval math behind your benchmarks. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: ML refresh (skim) — solidify the eval math behind your benchmarks. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | Sliding window (advanced)
**Task:** Name the pattern, then solve 3–5 Sliding window (advanced) problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Sliding window (advanced) problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Sliding window (advanced)**).
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

[[Day20|← Day 20]]  |  [[Day22|Day 22 →]]

---

*[[Index|🏠 Back to Index]]*
