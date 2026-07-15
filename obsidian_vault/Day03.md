# Day 03 — Diffusion Models

> **Phase:** 🧱 Phase 1 — Foundations  ·  **📅 Week 1 · Wed**
> **Schedule:** 9:00 AM – 9:00 PM | **Total:** ~12 hours  ·  🌴 Sundays = rest

---

## ✅ Daily Timetable  *(ordered for retention)*

| When | Block | Focus | Status |
|---|---|---|---|
| 9:00–9:30 | 🌅 Warm-up | Spaced recall (yesterday + ~3 & ~7 days ago) + 🧠 Anki | - [ ] Done |
| 9:30–11:00 | 🧠 **New Concept** | 🤖 Diffusion Models | - [ ] Done |
| 11:00–11:15 | ☕ Break | — | — |
| 11:15–13:00 | 🛠️ **Hands-on** | 🤖 apply it → capstone | - [ ] Done |
| 13:00–14:00 | 🍽️ Lunch | Step away from screens | — |
| 14:00–15:30 | 🔧 **Build + Milvus** | 🗄️ Milvus index types | - [ ] Done |
| 15:30–15:45 | ☕ Break | — | — |
| 15:45–17:15 | 🗜️ **Compression** | 🗜️ INT8 PTQ | - [ ] Done |
| 17:15–18:30 | ⚙️ C++ Literacy | RAII & smart pointers | - [ ] Done |
| 18:30–19:00 | 🍵 Dinner | Step away | — |
| 19:00–20:30 | 🧩 **DSA** | Strings & sliding window | - [ ] Done |
| 20:30–21:00 | 🔁 Wind-down | Teach-back + preview tomorrow + Anki | - [ ] Done |

> 🧠 **Why this order:** the hardest *new* idea runs while you're freshest, then you **apply it immediately** to lock it in. Applied capstone work (Build + Milvus, then Compression) fills the post-lunch dip; the lighter *craft* tracks — C++ literacy (→ Capstone Lab after Day 12) and DSA — sit in the evening; a 30-min **wind-down** lets the day consolidate in your sleep. Recall bookends the day.

**🎯 Today's focus:**
- 🤖 AI/Robotics: Diffusion Models
- 🗄️ Milvus *(supporting tool)*: Milvus index types
- 🗜️ Compression: INT8 PTQ
- ⚙️ C++ *(literacy — read & modify)*: RAII & smart pointers
- 🧩 DSA: Strings & sliding window

**🤖 Capstone today →** Diffusion literacy — context for diffusion policies + synthetic aug (no repo code today).

**🧠 Retention:** warm-up = recall yesterday + a card from ~3 and ~7 days ago · wind-down = teach back today's big idea in 3 sentences, no notes. Anki daily. → [[Retention]]

**⏱️ Estimated resource time today:** ~405 min (~6.8 hr)

**🔥 Bleeding-edge picks today:**
- 🔥 FLUX.1 — frontier open-weight diffusion (Black Forest Labs) — [open](https://www.google.com/search?q=open)

---

## 🌅 Warm-up | 9:00–9:30 | Review
**Task:** Draw CLIP architecture from memory. Check Milvus collection item count.

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
## 🧠 New Concept | 9:30–11:00 | DDPM, DDIM, Stable Diffusion
**Task:** Forward/reverse process, score function, UNet denoiser, VAE, CLIP text encoder.

**🎯 Outcome:** A written artifact (summary + from-memory sketch) that proves you understand DDPM, DDIM, Stable Diffusion.

**▶️ DO THIS — every step (read in browser → write in Obsidian):**

**Step 1.** Click the first resource below (**DDPM Paper (Ho et al.)**) — it opens in your browser.
**Step 2.** Read it for ~15 min. You don't need every word — get the big picture and the main diagram.
**Step 3.** In Obsidian, make a new note (click the 📄 **New note** icon, name it `Day 03 — notes`).
**Step 4.** With the article **closed**, write 5–8 sentences explaining **DDPM, DDIM, Stable Diffusion** in your own words, and sketch the main flow.
**Step 5.** Re-open the article, compare, fix mistakes, and write down **2 questions** you still have.
**Step 6.** Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] You can explain DDPM, DDIM, Stable Diffusion aloud in ~2 min with notes closed
- [ ] Your summary + from-memory sketch both exist
- [ ] 2 open questions are logged for a later block

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [DDPM Paper (Ho et al.)](https://www.google.com/search?q=DDPM+Paper+%28Ho+et+al.%29) — ⏱️ ~15 min
- [ ] 📄 [DDIM Paper](https://www.google.com/search?q=DDIM+Paper) — ⏱️ ~15 min
- [ ] 📝 [The Illustrated Stable Diffusion — Jay Alammar](https://www.google.com/search?q=The+Illustrated+Stable+Diffusion+%E2%80%94+Jay+Alammar) — ⏱️ ~15 min
- [ ] 🎥 [Diffusion Models Explained — Yannic Kilcher](https://www.youtube.com/results?search_query=Diffusion+Models+Explained+%E2%80%94+Yannic+Kilcher) — ⏱️ ~25 min
- [ ] 🎥 [Stable Diffusion Deep Dive — Fast.ai](https://www.youtube.com/results?search_query=Stable+Diffusion+Deep+Dive+%E2%80%94+Fast.ai) — ⏱️ ~25 min
- [ ] 🔥 📦 [FLUX.1 — frontier open-weight diffusion (Black Forest Labs)](https://www.google.com/search?q=FLUX.1+%E2%80%94+frontier+open-weight+diffusion+%28Black+Forest+Labs%29) — ⏱️ ~10 min

*⏱️ Resource time this block: ~105 min*

---
## 🛠️ Hands-on | 11:15–13:00 | Run Stable Diffusion img2img
**Task:** Run Stable Diffusion v1.5 img2img (diffusers) on a workspace photo at strength 0.3 / 0.5 / 0.7. Deliverable: 3 output images + a note on the fidelity-vs-change tradeoff. Paper: Latent Diffusion (arXiv 2112.10752).

**🎯 Outcome:** Working code plus saved output for Run Stable Diffusion img2img.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`run_stable_diffusion_img2img.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day03/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install diffusers transformers accelerate datasets pillow pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest run_stable_diffusion_img2img.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`run_stable_diffusion_img2img.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest run_stable_diffusion_img2img.py -q` until **everything is green**. That completes: Run Stable Diffusion v1.5 img2img (diffusers) on a workspace photo at strength 0.3 / 0.5 / 0.7. Deliverable: 3 output images + a note on the fidelity-vs-change tradeoff. Paper: Latent Diffusion (arXiv 2112.10752).
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The script runs start-to-finish with no errors
- [ ] Output is saved to disk and committed to git
- [ ] You can describe one thing that broke or surprised you

- [ ] Block complete

### 📚 Resources
- [ ] 📦 [HuggingFace Diffusers GitHub](https://www.google.com/search?q=HuggingFace+Diffusers+GitHub) — ⏱️ ~10 min
- [ ] 📄 [Diffusers img2img Pipeline](https://www.google.com/search?q=Diffusers+img2img+Pipeline) — ⏱️ ~15 min
- [ ] 🎥 [Diffusers Library Tutorial](https://www.youtube.com/results?search_query=Diffusers+Library+Tutorial) — ⏱️ ~25 min

*⏱️ Resource time this block: ~50 min*

---
## 🔧 Build + Milvus | 14:00–15:30 | Index Types
**Task:** Learn IVF_FLAT, HNSW, IVF_PQ. Rebuild collection with HNSW. Compare speed vs recall.

**🎯 Outcome:** A working Milvus operation for Milvus — Index Types.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`index_types.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day03/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install pymilvus numpy scikit-learn pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest index_types.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`index_types.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest index_types.py -q` until **everything is green**. That completes: Learn IVF_FLAT, HNSW, IVF_PQ. Rebuild collection with HNSW. Compare speed vs recall.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] The insert / query / operation completes without error
- [ ] Top-k results are sensible for your query
- [ ] Entity count + latency are written into your notes

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [Milvus Index Guide](https://www.google.com/search?q=Milvus+Index+Guide) — ⏱️ ~15 min
- [ ] 📝 [HNSW Explained — Zilliz](https://www.google.com/search?q=HNSW+Explained+%E2%80%94+Zilliz) — ⏱️ ~15 min
- [ ] 📝 [ANN Benchmarks — ann-benchmarks.com](https://www.google.com/search?q=ANN+Benchmarks+%E2%80%94+ann-benchmarks.com) — ⏱️ ~15 min
- [ ] 📄 [Milvus Official Docs](https://www.google.com/search?q=Milvus+Official+Docs) — ⏱️ ~15 min

*⏱️ Resource time this block: ~60 min*

---
## 🗜️ Compression | 15:45–17:15 | INT8 PTQ
**Task:** Apply torch.quantization.quantize_dynamic. Compare accuracy, size, latency vs FP32.

**🎯 Outcome:** A before/after measurement for Compression — INT8 PTQ.

**▶️ DO THIS — every step (macOS · Google Colab):**

**Step 1.** In your browser, open **https://colab.research.google.com** → click **New notebook**. *(First time? Read [[Setup_Guide]] once — it explains every tool below.)*
**Step 2.** Turn on the free GPU: top menu **Runtime → Change runtime type → T4 GPU → Save**.
**Step 3.** Get the starter file **`int8_ptq.py`** into Colab: click the **📁 folder icon** (left sidebar) → **Upload**, and pick it from `intensive study/starter_code/Day03/`. *(It's pre-written — a specific model + an open-source dataset are loaded for you; you only fill the functions.)*
**Step 4.** Install its tools — new cell, **▶** (the file's `Setup:` line lists the exact ones):

```python
!pip install torch torchvision pytest   # ← or whatever the file's own Setup line lists
```

**Step 5.** Run the tests — new cell, **▶**:  `!pytest int8_ptq.py -q`  →  the **red / FAILED** tests are your to-do list (each one names the function to write).
**Step 6.** Double-click **`int8_ptq.py`** in the 📁 panel to edit it. Fill in each function and DELETE its `raise` line, then re-run `!pytest int8_ptq.py -q` until **everything is green**. That completes: Apply torch.quantization.quantize_dynamic. Compare accuracy, size, latency vs FP32.
   ❌ `ModuleNotFoundError: X` → new cell, run `!pip install X`, then retry.  ❌ `CUDA out of memory` → **Runtime → Disconnect and delete runtime**, reconnect with GPU, use the smaller model in `src/config.py`.  ❌ Anything else for >90 min → write down where you're stuck and move on (that's not 'behind').
**Step 7.** All tests green? Tick the ✅ boxes below and check **Block complete**.

**✅ Done when:**
- [ ] Baseline **and** post-change numbers are both recorded
- [ ] The accuracy-vs-speed trade-off is written down
- [ ] Your benchmark table is updated

- [ ] Block complete

### 📚 Resources
- [ ] 📄 [PyTorch PTQ Tutorial](https://www.google.com/search?q=PyTorch+PTQ+Tutorial) — ⏱️ ~15 min
- [ ] 📝 [Intro to Quantization — PyTorch Blog](https://www.google.com/search?q=Intro+to+Quantization+%E2%80%94+PyTorch+Blog) — ⏱️ ~15 min
- [ ] 🎥 [INT8 Quantization Explained](https://www.youtube.com/results?search_query=INT8+Quantization+Explained) — ⏱️ ~25 min

*⏱️ Resource time this block: ~55 min*

---
## ⚙️ C++ Literacy | 17:15–18:30 | RAII & smart pointers
**Task:** Read & understand: raii & smart pointers. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.

**🎯 Outcome:** You can read and modify C++ Literacy — RAII & smart pointers — explain it, not reproduce it from scratch.

**▶️ DO THIS — every step (browser + online C++ compiler):**

**Step 1.** Click the first resource (**HelloC++ — C++ Fundamentals Course**) and read the example C++. This is **read & modify** — you are NOT writing it from scratch.
**Step 2.** To *run* a small C++ snippet with **nothing installed**, use an online compiler: **https://www.programiz.com/cpp-programming/online-compiler/** (paste code, press **Run**).
**Step 3.** Do it: Read & understand: raii & smart pointers. The goal is to READ and MODIFY, not write from scratch — trace what the code does, change one thing, rebuild/run, predict the effect.
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
## 🧩 DSA | 19:00–20:30 | Strings & sliding window
**Task:** Name the pattern, then solve 3–5 Strings & sliding window problems. Test edge cases, state time/space complexity, and queue the hardest to re-solve from memory tomorrow.

**🎯 Outcome:** A few DSA — Strings & sliding window problems solved cold, with the pattern named.

**▶️ DO THIS — every step (browser — NeetCode / LeetCode):**

**Step 1.** Open the first resource (**HelloC++ DSA Roadmap**) in your browser (NeetCode or LeetCode — no install needed).
**Step 2.** Pick **3–5** problems on today's pattern (**Strings & sliding window**).
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

[[Day02|← Day 2]]  |  [[Day04|Day 4 →]]

---

*[[Index|🏠 Back to Index]]*
