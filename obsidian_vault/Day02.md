# Day 02 — Vision-Language Models + Milvus Embedding Store

> **Phase:** 🧱 Phase 1 — Foundations  ·  **📅 Week 1 · Tue**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 VLMs: CLIP, LLaVA | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ CLIP embeddings → Milvus | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ FP16 quantization | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Pointers & references | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Hashing & hash maps | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: VLMs: CLIP, LLaVA
- 🗄️ Milvus *(supporting tool)*: CLIP embeddings → Milvus
- 🗜️ Compression: FP16 quantization
- ⚙️ C++ *(literacy — read & modify)*: Pointers & references
- 🧩 DSA: Hashing & hash maps

**🤖 Capstone today →** Add CLIP→Milvus retrieval over observations (the policy's memory).

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~410 min (~6.8 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 Gemini Robotics 1.5 — DeepMind VLA — [open](https://deepmind.google/models/gemini-robotics/)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Confirm Milvus is running. Recap Day 1 summary notes.

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
- [ ] 📄 [Milvus Connection Guide](https://milvus.io/docs/manage-collections.md) — ⏱️ ~15 min

*⏱️ Resource time this block: ~15 min*

---
## 🧠 New Concept | 9:30–11:00 | CLIP, BLIP-2, LLaVA
**Task:** Contrastive loss, image-text alignment, how vision encoders attach to LLMs.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand CLIP, BLIP-2, LLaVA.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**CLIP Paper (Radford et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 02 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **CLIP, BLIP-2, LLaVA** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain CLIP, BLIP-2, LLaVA aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [CLIP Paper (Radford et al.)](https://arxiv.org/abs/2103.00020) — ⏱️ ~15 min
- [ ] 📄 [BLIP-2 Paper](https://arxiv.org/abs/2301.12597) — ⏱️ ~15 min
- [ ] 🎥 [CLIP Explained — Yannic Kilcher](https://www.youtube.com/watch?v=T9XSU0pKX2E) — ⏱️ ~25 min
- [ ] 📝 [Understanding CLIP — LearnOpenCV](https://learnopencv.com/clip-what-it-is-how-it-works-applications/) — ⏱️ ~15 min
- [ ] 📦 [LLaVA GitHub](https://github.com/haotian-liu/LLaVA) — ⏱️ ~10 min
- [ ] 🔥 📝 [Gemini Robotics 1.5 — DeepMind VLA](https://deepmind.google/models/gemini-robotics/) — ⏱️ ~15 min

*⏱️ Resource time this block: ~95 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run LLaVA on Robot Scenes
**Task:** Encode a tabletop image with CLIP (openai/clip-vit-base-patch32) into a 512-d vector; run LLaVA-1.5 to list graspable objects as JSON. Deliverable: a 512-d embedding + JSON with at least 3 objects. Paper: CLIP (arXiv 2103.00020).

**🎯 Outcome:** Working code plus saved output for Run LLaVA on Robot Scenes.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_llava_on_robot_scenes.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day02/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install transformers datasets torch pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_llava_on_robot_scenes.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_llava_on_robot_scenes.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_llava_on_robot_scenes.py -q` until **everything is green**. That completes: Encode a tabletop image with CLIP (openai/clip-vit-base-patch32) into a 512-d vector; run LLaVA-1.5 to list graspable objects as JSON. Deliverable: a 512-d embedding + JSON with at least 3 objects. Paper: CLIP (arXiv 2103.00020).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [LLaVA HuggingFace Model Card](https://huggingface.co/llava-hf/llava-1.5-7b-hf) — ⏱️ ~15 min
- [ ] 📄 [Transformers Pipeline Docs](https://huggingface.co/docs/transformers/main_classes/pipelines) — ⏱️ ~15 min
- [ ] 🎥 [Run LLaVA Locally Tutorial](https://www.youtube.com/watch?v=MqMAnO8yJGQ) — ⏱️ ~25 min

*⏱️ Resource time this block: ~55 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Store CLIP Embeddings
**Task:** Encode 100 robot images with CLIP. Insert 512-d vectors. Run similarity search. Log top-5.

**🎯 Outcome:** A working Milvus operation for Milvus — Store CLIP Embeddings.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`store_clip_embeddings.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day02/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest store_clip_embeddings.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`store_clip_embeddings.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest store_clip_embeddings.py -q` until **everything is green**. That completes: Encode 100 robot images with CLIP. Insert 512-d vectors. Run similarity search. Log top-5.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Image Search Tutorial](https://milvus.io/docs/image_similarity_search.md) — ⏱️ ~15 min
- [ ] 📝 [CLIP + Milvus Reverse Image Search](https://zilliz.com/blog/building-a-reverse-image-search-with-milvus-and-clip) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📄 [Milvus Insert Docs](https://milvus.io/docs/insert-update.md) — ⏱️ ~15 min

*⏱️ Resource time this block: ~55 min*

---
## 🗜️ Compression | 15:45–17:15 | FP16
**Task:** Convert model to FP16 with model.half(). Benchmark vs FP32. Log latency.

**🎯 Outcome:** A before/after measurement for Compression — FP16.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`fp16.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day02/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest fp16.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`fp16.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest fp16.py -q` until **everything is green**. That completes: Convert model to FP16 with model.half(). Benchmark vs FP32. Log latency.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PyTorch AMP (Automatic Mixed Precision)](https://pytorch.org/docs/stable/amp.html) — ⏱️ ~15 min
- [ ] 📝 [FP16 vs FP32 Training — PyTorch Blog](https://pytorch.org/blog/accelerating-training-on-nvidia-gpus-with-pytorch-automatic-mixed-precision/) — ⏱️ ~15 min
- [ ] 🎥 [Mixed Precision Training Explained](https://www.youtube.com/watch?v=UK8IMfgEMhs) — ⏱️ ~25 min

*⏱️ Resource time this block: ~55 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Pointers & references
**Task:** Read & understand: pointers & references. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Pointers & references — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Fundamentals Course**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: pointers & references. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
**Step 4.** Change **one** thing, run again, predict-then-check what changed.
**Step 5.** Write one sentence: *when would I touch this in a real robot codebase?* Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You can read this kind of C++ and explain it
- [ ] You modified one thing and it still built / ran
- [ ] You did NOT try to write it from scratch — that's not the goal

- [ ] Block complete

### 📚 Resources
- [ ] 🎓 [HelloC++ — C++ Fundamentals Course](https://www.hellocpp.dev/course/cpp-programming-fundamentals) — ⏱️ ~45 min
- [ ] 📄 [cppreference — read C++](https://en.cppreference.com/w/) — ⏱️ ~15 min
- [ ] 🎥 [C++ — The Cherno (read-along)](https://www.youtube.com/@TheCherno) — ⏱️ ~25 min

*⏱️ Resource time this block: ~85 min*

---
## 🧩 DSA | 19:00–20:30 | Hashing & hash maps
**Task:** Name the pattern, then solve 3–5 Hashing & hash maps problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Hashing & hash maps problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Hashing & hash maps**).
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

[[Day01|← Day 1]]  |  [[Day03|Day 3 →]]

---

*[[Index|🏠 Back to Index]]*
