# Day 01 — The Landscape + Environment Setup

> **Phase:** 🧱 Phase 1 — Foundations  ·  **📅 Week 1 · Mon**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 CV/AI Landscape | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Docker/Milvus basics | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ Compression overview | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | Reading C++ — syntax & types | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Arrays & two pointers | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: CV/AI Landscape
- 🗄️ Milvus *(supporting tool)*: Docker/Milvus basics
- 🗜️ Compression: Compression overview
- ⚙️ C++ *(literacy — read & modify)*: Reading C++ — syntax & types
- 🧩 DSA: Arrays & two pointers

**🤖 Capstone today →** Stub the `vla-edge` repo + env; get **SmolVLA** running on one sample observation.

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~510 min (~8.5 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 VLA Models Comparison 2026 — Octo · OpenVLA · π0/π0.5 · GR00T · SmolVLA — [open](https://www.roboticscenter.ai/tools/vla-models-comparison)
- 🔥 SmolVLA — 450M open VLA that runs on consumer hardware (HF) — [open](https://huggingface.co/blog/smolvla)
- 🔥 π0.5 on Jetson Thor with NVFP4 — real edge VLA inference — [open](https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/)

---

## 🌅 Warm-up | 9:00–9:30 | Setup
**Task:** First morning — get oriented: skim the Index + Setup Guide, open Google Colab once, set up Anki, and write your 30-day goal.

**🎯 Outcome:** Oriented for Day 1: you know the 30-day arc, Colab opens, Anki is ready, and your goal is written.

**▶️ DO THIS — every step (Anki + Obsidian):**

**Step 1.** It's Day 1 — nothing to recall yet. Open **[[Index]]** and skim the 30-day arc (~5 min).
**Step 2.** Read **[[Setup_Guide]]** §1–2, then open **https://colab.research.google.com** once to confirm it loads (no install needed on your Mac).
**Step 3.** Install **Anki** and import `Flashcards.csv` so daily review is ready tomorrow. *([[Setup_Guide]] §1)*
**Step 4.** In a new `Day 01 — notes`, write your one-line goal for the next 30 days. Tick ✅ and check **Block complete**.

**✅ Done when:**
- [ ] You skimmed the Index + Setup Guide and opened Colab once
- [ ] Anki is installed with Flashcards.csv imported
- [ ] Your one-line 30-day goal is written in `Day 01 — notes`

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PyTorch Install Guide](https://pytorch.org/get-started/locally/) — ⏱️ ~15 min
- [ ] 📄 [HuggingFace Hub Quickstart](https://huggingface.co/docs/huggingface_hub/quick-start) — ⏱️ ~15 min
- [ ] 📝 [RunPod GPU Setup Guide](https://docs.runpod.io/pods/overview) — ⏱️ ~15 min

*⏱️ Resource time this block: ~45 min*

---
## 🧠 New Concept | 9:30–11:00 | Gen AI × Robotics Overview
**Task:** Read CVPR 2026 trends, VLA survey intro, GR00T overview. Write a 1-page summary.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Gen AI × Robotics Overview.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**CVPR 2026 Trends — Encord**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 01 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Gen AI × Robotics Overview** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Gen AI × Robotics Overview aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📝 [CVPR 2026 Trends — Encord](https://encord.com/cvpr-2026/) — ⏱️ ~15 min
- [ ] 📄 [VLA Models Survey](https://vla-survey.github.io/) — ⏱️ ~15 min
- [ ] 📝 [NVIDIA GR00T N1 Blog](https://blogs.nvidia.com/blog/gr00t-n1-open-foundation-model-humanoid-robots/) — ⏱️ ~15 min
- [ ] 🎥 [Andrej Karpathy — Software 2.0](https://www.youtube.com/watch?v=VrBiDsYB8J0) — ⏱️ ~25 min
- [ ] 📝 [CVPR 2026 Robotics Showcase](https://cvpr.thecvf.com/Conferences/2026/News/Robotics) — ⏱️ ~15 min
- [ ] 🔥 📝 [VLA Models Comparison 2026 — Octo · OpenVLA · π0/π0.5 · GR00T · SmolVLA](https://www.roboticscenter.ai/tools/vla-models-comparison) — ⏱️ ~15 min

*⏱️ Resource time this block: ~100 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Python Tooling
**Task:** Verify the GPU and import diffusers, transformers, open3d, pymilvus, ultralytics. Deliverable: torch.cuda.is_available()==True, every library version printed with no MISSING, and a 1-line CUDA tensor op runs.

**🎯 Outcome:** Working code plus saved output for Python Tooling.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`python_tooling.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day01/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install diffusers transformers accelerate datasets pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest python_tooling.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`python_tooling.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest python_tooling.py -q` until **everything is green**. That completes: Verify the GPU and import diffusers, transformers, open3d, pymilvus, ultralytics. Deliverable: torch.cuda.is_available()==True, every library version printed with no MISSING, and a 1-line CUDA tensor op runs.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [CUDA Toolkit Install Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/) — ⏱️ ~15 min
- [ ] 📦 [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics) — ⏱️ ~10 min
- [ ] 📦 [Open3D GitHub](https://github.com/isl-org/Open3D) — ⏱️ ~10 min
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📦 [HuggingFace Diffusers GitHub](https://github.com/huggingface/diffusers) — ⏱️ ~10 min
- [ ] 🔥 📝 [SmolVLA — 450M open VLA that runs on consumer hardware (HF)](https://huggingface.co/blog/smolvla) — ⏱️ ~15 min

*⏱️ Resource time this block: ~70 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | First Collection
**Task:** Install Milvus via Docker, connect pymilvus, create collection, insert dummy vectors, run search.

**🎯 Outcome:** A working Milvus operation for Milvus — First Collection.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`first_collection.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day01/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions. Its shared setup lives in `starter_code/helpers/`.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest first_collection.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`first_collection.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest first_collection.py -q` until **everything is green**. That completes: Install Milvus via Docker, connect pymilvus, create collection, insert dummy vectors, run search.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Standalone Docker Quickstart](https://milvus.io/docs/install_standalone-docker.md) — ⏱️ ~15 min
- [ ] 📄 [pymilvus Hello Milvus Tutorial](https://milvus.io/docs/quickstart.md) — ⏱️ ~15 min
- [ ] 📦 [pymilvus GitHub](https://github.com/milvus-io/pymilvus) — ⏱️ ~10 min
- [ ] 📦 [Milvus GitHub](https://github.com/milvus-io/milvus) — ⏱️ ~10 min
- [ ] 🎥 [Milvus Getting Started](https://www.youtube.com/watch?v=P6DP3VLTNqo) — ⏱️ ~25 min

*⏱️ Resource time this block: ~75 min*

---
## 🗜️ Compression | 15:45–17:15 | Overview & Metrics
**Task:** Why compress? Latency, FLOPs, params, throughput. Survey the landscape.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand Compression — Overview & Metrics.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**TensorRT Developer Guide**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 01 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **Compression — Overview & Metrics** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain Compression — Overview & Metrics aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [TensorRT Developer Guide](https://developer.nvidia.com/tensorrt) — ⏱️ ~15 min
- [ ] 📝 [Model Compression Survey — Medium](https://towardsdatascience.com/model-compression-approaches-overview-5c0e4b0b3f4) — ⏱️ ~15 min
- [ ] 🎥 [Neural Network Quantization Explained](https://www.youtube.com/watch?v=DDelqfkYCuo) — ⏱️ ~25 min
- [ ] 📄 [PyTorch Quantization Overview](https://pytorch.org/docs/stable/quantization.html) — ⏱️ ~15 min
- [ ] 🔥 📝 [π0.5 on Jetson Thor with NVFP4 — real edge VLA inference](https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/) — ⏱️ ~15 min

*⏱️ Resource time this block: ~85 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | Reading C++ — syntax & types
**Task:** Read & understand: reading c++ — syntax & types. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — Reading C++ — syntax & types — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Fundamentals Course**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: reading c++ — syntax & types. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
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
## 🧩 DSA | 19:00–20:30 | Arrays & two pointers
**Task:** Name the pattern, then solve 3–5 Arrays & two pointers problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Arrays & two pointers problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Arrays & two pointers**).
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

[[Day02|Day 2 →]]

---

*[[Index|🏠 Back to Index]]*
