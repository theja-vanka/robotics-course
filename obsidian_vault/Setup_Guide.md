# 🧰 Setup Guide — read this ONCE before Day 1

> You're on a **Mac**, and you'll run the heavy code in **Google Colab** (free GPU in your browser). This page explains every tool the day-blocks tell you to use. Keep it open in a tab. Every block's **▶️ DO THIS** section assumes you've skimmed this once.

---

## 1. The two places you'll "run" things

| Where | What it's for | How to open it |
|---|---|---|
| **🌐 Google Colab** | Running Python / AI models on a free cloud GPU (no install on your Mac). **Use this for anything that loads a model or trains/compresses.** | Browser → **https://colab.research.google.com** → **New notebook** |
| **🖥️ Terminal** (Mac app) | Small local commands (git, looking at files). Rarely needed — only when a block says "Terminal". | Press **⌘ (Command) + Space**, type **Terminal**, press **Return** |
| **📓 Obsidian** | Reading these day-notes and writing your summaries/answers. | The app you're reading this in right now |
| **🦉 Anki** | 15-min daily flashcard review (memory). | Download once: **https://apps.ankiweb.net** |

> 👉 **Rule of thumb:** if a step shows `python ...` or loads a model → do it in **Colab**. If it says "read" / "write" / "explain" → do it in your **browser + Obsidian**.

---

## 2. Colab in 6 clicks (you'll repeat this each session)

1. Open **https://colab.research.google.com** → **New notebook**.
2. Turn on the free GPU: top menu **Runtime → Change runtime type → Hardware accelerator: T4 GPU → Save**.
3. A **cell** is a grey box. Click it, type or paste code, then press **▶** (or **Shift + Return**) to run it.
4. To add another cell, click **+ Code**.
5. A line starting with **`!`** runs a terminal command (e.g. `!pip install ...`). A line starting with **`%cd`** changes folder. Normal Python needs no prefix.
6. Save your work: **File → Save a copy in Drive**.

---

## 2½. Checking your work with a starter file's tests

Every per-day starter (inside `starter_code/DayNN/`) **loads an open dataset for you** (BridgeData V2 robot scenes via `jesbu1/bridge_v2_lerobot`, SO-100 demos via `lerobot/svla_so100_pickplace` — nothing to provide) and ships its own **pytest tests**. In Colab:

1. Upload it: left sidebar **📁 → Upload** → navigate into `intensive study/starter_code/DayNN/` and pick the file.
2. Install its tools — the quickest is the shared, pinned list (covers every day); or use the file's own `Setup:` line:
   ```python
   !pip install -q -r intensive\ study/starter_code/requirements.txt   # ← everything, pinned
   # ...or just the file's Setup line, e.g.:  !pip install -q pymilvus transformers torch pillow av huggingface_hub pytest
   ```
   *(The shared setup — dataset download, CLIP/DINOv2, Milvus client — lives in `starter_code/helpers/`; the day files just import it.)*
3. Run the tests:
   ```python
   !pytest whatever.py -q
   ```
   **Red / FAILED** tests are your to-do list — each names the function to write. Double-click the file in the 📁 panel to edit it, fill the function, delete its `raise` line, and re-run until **all green**.

---

## 3. Getting the capstone code (`vla-edge`) into Colab

Your capstone repo lives in your `intensive study/vla-edge` folder. To use it in Colab you have two options:

**Option A — push it to GitHub once (recommended), then clone it anywhere:**
```
# one time, in Terminal, inside the vla-edge folder:
cd ~/Documents/"intensive study"/vla-edge
git init && git add . && git commit -m "first commit"
# create an empty repo on github.com called vla-edge, then:
git remote add origin https://github.com/YOUR-USERNAME/vla-edge.git
git push -u origin main
```
Then in any Colab notebook:
```python
!git clone https://github.com/YOUR-USERNAME/vla-edge.git
%cd vla-edge
!pip install -r requirements.txt
```

**Option B — upload (no GitHub):** in Colab, click the **📁 folder icon** on the left → **upload** → drag your `vla-edge` folder in. Slower, but works.

> The per-day **starter files** (inside `starter_code/DayXX/`) are NOT in the repo. When a block points to one, open it on your Mac (in Obsidian or TextEdit), **copy all of it**, and **paste it into a Colab cell**.

---

## 4. The 5 errors you WILL see (and the fix)

| Error message | What it means | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'X'` | A library isn't installed | New cell: `!pip install X` → run → retry |
| `CUDA out of memory` | Model too big for the GPU | **Runtime → Disconnect and delete runtime**, reconnect with GPU; use the smaller model (SmolVLA, fp16) noted in `src/config.py` |
| `FileNotFoundError` / `No such file` | You're in the wrong folder | Run `%cd vla-edge` (or re-clone); check the filename spelling |
| `repository not found` (git clone) | Repo isn't on GitHub yet | Do Option A above, or use Option B (upload) |
| Colab "session disconnected" | Idle too long / free limit | Reconnect (top-right), re-run your setup cell. Save to Drive often |

> 🧯 **Golden rule:** stuck more than **90 minutes** on an error? Write down where you're stuck in the day-note and move on. Being stuck is not the same as being behind — see each block's fix-it notes.

---

## 5. What you do NOT need to install on your Mac

You will **not** install CUDA, TensorRT, ROS2, or a C++ compiler locally. The C++ blocks are **read-only literacy** (you read code in the browser / an online compiler), and all GPU work happens in Colab. This keeps your Mac clean and avoids days lost to setup.

*Back to [[Index|🏠 Index]] · [[Capstone_VLA|🤖 Capstone]]*
