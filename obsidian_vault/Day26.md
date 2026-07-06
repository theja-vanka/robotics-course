# Day 26 — PRODUCT BUILD DAY #2: Synthetic Data CLI Tool

> **Phase:** 🎯 Phase 4 — Interview Mastery + Second Product  ·  **📅 Week 5 · Tue**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Synthetic data CLI tool | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Milvus auto-index | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ --quantize flag | - [ ] Done |
| 17:15–18:30 | 🔁 Capstone Lab | extra fine-tune / compress / eval reps | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Backtracking (combinations / permutations) | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Synthetic data CLI tool
- 🗄️ Milvus *(supporting tool)*: Milvus auto-index
- 🗜️ Compression: --quantize flag
- 🔁 Capstone Lab *(reps on the capstone)*: extra fine-tune / compress / eval reps
- 🧩 DSA: Backtracking (combinations / permutations)

**🤖 Capstone today →** Package: clean README (problem→approach→results), demo gif, **v1.0.0 + license**.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~235 min (~3.9 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 NVIDIA Cosmos-Predict 2.5 — world model for synthetic data — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Plan
**Task:** Spec the CLI tool in 10 bullet points before writing code.

**🎯 Outcome:** A short written spec you can execute against for the rest of the day.

**▶️ DO THIS — every step (Obsidian):**

**Step 1.** In Obsidian, make a new note `Day 26 — Plan`.
**Step 2.** Write it out: Spec the CLI tool in 10 bullet points before writing code.
**Step 3.** Mark the ONE thing that must work by tonight. Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] The spec is written down, not just held in your head
- [ ] Inputs, outputs, and a clear 'done' bar are all defined

- [ ] Block complete

### 📚 Resources

---
## 🧠 New Concept | 9:30–11:00 | Build — CLI Core
**Task:** Python CLI (Click): .obj mesh in → BlenderProc renders N images → exports COCO JSON.

**🎯 Outcome:** A working, committed increment of the product for Build — CLI Core.

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
**Step 5.** Do the reps: Python CLI (Click): .obj mesh in → BlenderProc renders N images → exports COCO JSON.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [BlenderProc GitHub](https://www.google.com/search?q=BlenderProc+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Click CLI Docs](https://www.google.com/search?q=Click+CLI+Docs) — ⏱️ ~15 min
- [ ] 📝 [Building CLI Tools in Python](https://www.google.com/search?q=Building+CLI+Tools+in+Python) — ⏱️ ~15 min
- [ ] 🔥 📦 [NVIDIA Cosmos-Predict 2.5 — world model for synthetic data](https://www.google.com/search?q=NVIDIA+Cosmos-Predict+2.5+%E2%80%94+world+model+for+synthetic+data) — ⏱️ ~10 min

*⏱️ Resource time this block: ~50 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Build — Milvus Auto-Index
**Task:** After rendering, CLIP-embed all images → insert into Milvus → dedupe (cosine > 0.98) → log a diversity score. Deliverable: a deduped collection + the diversity score, wired behind a --dedupe CLI flag.

**🎯 Outcome:** A working, committed increment of the product for Build — Milvus Auto-Index.

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
**Step 5.** Do the reps: After rendering, CLIP-embed all images → insert into Milvus → dedupe (cosine > 0.98) → log a diversity score. Deliverable: a deduped collection + the diversity score, wired behind a --dedupe CLI flag.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Milvus Official Docs](https://www.google.com/search?q=Milvus+Official+Docs) — ⏱️ ~15 min
- [ ] 📄 [Milvus Batch Insert](https://www.google.com/search?q=Milvus+Batch+Insert) — ⏱️ ~15 min

*⏱️ Resource time this block: ~40 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Build — ControlNet + Diversity Filter
**Task:** --augment flag: ControlNet pass. Only keep images that increase Milvus diversity.

**🎯 Outcome:** A working, committed increment of the product for Build — ControlNet + Diversity Filter.

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
**Step 5.** Do the reps: --augment flag: ControlNet pass. Only keep images that increase Milvus diversity.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [ControlNet GitHub](https://www.google.com/search?q=ControlNet+GitHub) — ⏱️ ~10 min
- [ ] 📦 [HuggingFace Diffusers GitHub](https://www.google.com/search?q=HuggingFace+Diffusers+GitHub) — ⏱️ ~10 min
- [ ] 📦 [pymilvus GitHub](https://www.google.com/search?q=pymilvus+GitHub) — ⏱️ ~10 min

*⏱️ Resource time this block: ~30 min*

---
## 🗜️ Compression | 15:45–17:15 | Build — --quantize Flag
**Task:** After YOLOv8 training on output, export TRT INT8 engine automatically.

**🎯 Outcome:** A working, committed increment of the product for Build — --quantize Flag.

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
**Step 5.** Do the reps: After YOLOv8 training on output, export TRT INT8 engine automatically.
**Step 6.** **File → Save a copy in Drive**, tick the ✅ boxes, check **Block complete**.

**✅ Done when:**
- [ ] It runs on a real input and returns the expected output
- [ ] Code is committed with a meaningful message
- [ ] One edge/failure case is handled or logged as a TODO

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [Ultralytics YOLOv8 GitHub](https://www.google.com/search?q=Ultralytics+YOLOv8+GitHub) — ⏱️ ~10 min
- [ ] 📄 [TensorRT INT8 Guide](https://www.google.com/search?q=TensorRT+INT8+Guide) — ⏱️ ~15 min

*⏱️ Resource time this block: ~25 min*

---
## 🔁 Capstone Lab | 17:15–18:30 | drill today's milestone
**Task:** Deliberate-practice reps on the capstone: Package: clean README (problem→approach→results), demo gif, **v1.0.0 + license**. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.

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
**Step 5.** Do the reps: Deliberate-practice reps on the capstone: Package: clean README (problem→approach→results), demo gif, **v1.0.0 + license**. Re-run it, change ONE variable (LoRA rank, precision, prompt, batch), measure the effect, and log a number to vla-edge/benchmarks/results.csv.
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
## 🧩 DSA | 19:00–20:30 | Backtracking (combinations / permutations)
**Task:** Name the pattern, then solve 3–5 Backtracking (combinations / permutations) problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Backtracking (combinations / permutations) problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Backtracking (combinations / permutations)**).
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

[[Day25|← Day 25]]  |  [[Day27|Day 27 →]]

---

*[[Index|🏠 Back to Index]]*
