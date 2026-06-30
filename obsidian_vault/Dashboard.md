# 📊 Progress Dashboard

> **Live inside Obsidian** — needs the **Dataview** community plugin (Settings → Community plugins → search "Dataview" → install + enable; toggle on "Enable JavaScript Queries" for the % bar).
> **No plugins?** Open `Progress.html` in the project root instead — run `python dashboard.py` to refresh it.

Completion is tracked by the **`- [ ] Block complete`** toggle at the bottom of each block. Tick it when a block's ✅ *Done when* checks pass.

---

## 🔢 Overall

```dataviewjs
const pages = dv.pages('"obsidian_vault"').where(p => p.file.name.startsWith("Day"));
let done = 0, total = 0;
for (const p of pages) {
  const bc = p.file.tasks.where(t => t.text.includes("Block complete"));
  total += bc.length;
  done  += bc.where(t => t.completed).length;
}
const pct = total ? Math.round(100 * done / total) : 0;
const filled = Math.round(pct / 5);
dv.paragraph(`### ${done} / ${total} blocks · ${pct}%`);
dv.paragraph("`" + "█".repeat(filled) + "░".repeat(20 - filled) + "`");
```

---

## 📅 By day

```dataview
TABLE WITHOUT ID
  file.link AS "Day",
  length(filter(file.tasks, (t) => contains(t.text, "Block complete") AND t.completed)) + " / " +
  length(filter(file.tasks, (t) => contains(t.text, "Block complete"))) AS "Blocks ✓"
FROM "obsidian_vault"
WHERE startswith(file.name, "Day")
SORT file.name ASC
```

---

## ⏭️ What's left (tick these straight from here)

```dataview
TASK
FROM "obsidian_vault"
WHERE startswith(file.name, "Day") AND contains(text, "Block complete") AND !completed
GROUP BY file.link
```

---

*Following the sustainable pace? See the [[PartTime_Roadmap|🗓️ Part-Time Roadmap]]. Back to the [[Index|🏠 full plan]].*
