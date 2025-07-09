### Prioritization

**Worst UX inconsistency (highest priority):** Unlabeled chart gap (#4)

1. **Unlabeled chart gap** (#4) — breaks data interpretation, highest friction
2. **Number-formatting** (#3) — impedes rapid comparison across cards
3. **Nav-icon color clash** (#2) — draws distracting attention
4. **Non-clickable logo** (#1) — mild annoyance but easily fixed

---

# UX Audit Summary

## 1. Non-clickable logo
<img width="1508" alt="Screenshot 2025-07-09 at 08 35 12" src="https://github.com/user-attachments/assets/2e35d814-4f89-4f3f-98d5-4e2fcdff0ed1" />



* **Issue:** The brand logo in the top-left isn’t a clickable "home" link.
* **Impact:** Users expect the logo to take them back to dashboard or home. Lacking that breaks a common navigation convention.
* **Recommendation:** Make the logo a link to the primary landing page (dashboard/home).

---

## 2. Nav‑icon color clash

<img width="1512" alt="Screenshot 2025-07-09 at 08 25 01" src="https://github.com/user-attachments/assets/46871439-84ee-45df-9840-cd069ff48197" />

* **Issue:** One nav icon uses bright green, while the rest are monochrome.
* **Impact:** That lone splash of color draws unintended attention and feels visually out of place.
* **Recommendation:** Either tint that icon to match the others, or introduce a consistent accent color across all active icons.

---

## 3. Number‑formatting inconsistencies

<img width="1512" alt="Screenshot 2025-07-09 at 08 14 43" src="https://github.com/user-attachments/assets/19711bc7-8e5c-4425-a4e4-202ebf698aa3" />


* **Issue A:** Cost‑Per‑Conversion decimals vary (sometimes two places, sometimes one).
* **Issue B:** “K” suffix appears on some spend values but not others of similar magnitude.
* **Impact:** Forces users into mental math to compare values, slows down quick scannability.
* **Recommendation:**

  * Always show two decimal places (`$0.60`, not `$0.6`).
  * Define a clear “when to abbreviate” rule (e.g. “≥1,000 → K; otherwise show full number”), and apply it uniformly.

---

## 4. Unlabeled chart gap

<img width="1512" alt="Screenshot 2025-07-09 at 08 25 01" src="https://github.com/user-attachments/assets/f11d076f-99c3-483c-a2b5-01f221df4777" />

* **Issue:** The empty space splitting the two date ranges in the line chart has no axis break marker or segment label.
* **Impact:** Users assume a continuous timeline and get confused—“Did data fail to load? Are these the same scale?”—breaking their flow and costing time.
* **Recommendation:**

  * Insert a vertical “break” indicator (zig-zag or dashed line).
  * Label each segment ("Primary: Dec 5–17" vs. "Compare: Dec 19–31").
