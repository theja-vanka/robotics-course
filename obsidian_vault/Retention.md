# 🧠 Retention — so Week 3 is still in your head at Week 8

> The plan is resource-heavy (~191 hrs of links). **Reading and watching is intake, not retention.** This page turns intake into memory with three cheap habits. Active recall + spacing beats re-reading by a wide margin — and it's exactly what makes you fluent in interviews.

---

## ⏱️ The three habits

**1. Daily — 15 min spaced repetition (at warm-up).**
Open Anki, clear the day's due cards from `Flashcards.csv`. That's it. The algorithm resurfaces things right before you'd forget them.

**2. Daily — teach-back (5 min, end of the concept block).**
In the Day file (or out loud), explain the day's main idea in **3 sentences, no notes**. If you can't, you didn't learn it — that's the signal to revisit, not move on. The 🌅 Warm-up blocks already prompt this; make it a habit.

**3. Weekly — Feynman one-pager (Friday, 30 min).**
Take the week's **hardest** concept and write one page explaining it to a smart non-expert. Re-do any flashcards you failed that week. Update the capstone README with "what I can do now." This page *is* portfolio evidence.

> 🔑 If you only keep one: **do the daily Anki review.** Five minutes of recall outperforms an hour of re-watching.

---

## 📥 Use the starter deck (`Flashcards.csv`)

~60 cards, weighted toward what's **new for you** (diffusion, SLAM, VLA) plus interview staples.

1. Install [Anki](https://apps.ankiweb.net/) (free).
2. **File → Import** → pick `Flashcards.csv`.
3. Confirm: separator **Comma**, field 1 → **Front**, field 2 → **Back**, field 3 → **Tags**, deck **VLA Edge Intensive**. (The file has `#` directives that set these automatically in recent Anki.)
4. Study daily. Suspend anything you already own (you're strong in ML — kill the fundamentals cards you ace).

**Tags** let you drill one area: `vla`, `diffusion`, `slam`, `compression`, `perception`, `vlm`, `3d`, `worldmodels`, `fundamentals`, `milvus`.

---

## ➕ Add your own cards (this is where real retention happens)

The deck is a seed. **Every time a Done-when check makes you realize you didn't get something, write a card.** Append a line to `Flashcards.csv`:

```
"Your question here","The tight answer here",tagname
```

Best cards are **atomic** (one fact), **phrased as a question**, and in **your own words**. Turning a confusion into a card is the single highest-retention move in this whole plan.

---

## 🔁 Closing the loop

- **Week 6 & Week 12:** re-take the diffusion / VLA rows of the [[Target_and_SkillMap#🩺 Day-0 Diagnostic — skip what you already own|Day-0 diagnostic]]. The score jump is both a confidence check and a great interview anecdote.
- Failed the same card 3×? It's a **gap, not a card problem** → schedule a real session on it (use a [[Index|gap-fill day]]).

*See [[Capstone_VLA|🤖 Capstone]] · [[PartTime_Roadmap|🗓️ Roadmap]] · [[Index|🏠 Index]]*
