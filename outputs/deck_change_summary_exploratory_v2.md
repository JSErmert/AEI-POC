# Exploratory v2 Deck — Change Summary
## `final_slide_deck_exploratory_v2.pptx`

Generated 2026-05-07. Built from `final_slide_deck_polished.pptx` as the design baseline.

**Frozen across both decks:**
- 10-slide structure
- Every numeric claim (0.8475, 0.8467, 0.8382, 0.8301, baseline 0.8424, sensitivities 9.1 / 17.3 / 22.0 %, 84.24 / 1.83 / 13.93 % class shares, 101,437 rule-out, 3,961 high-risk leaf, all rpart importance values)
- Model ranking (Tree > Logit > KNN k=9 > KNN k=5)
- Speaker-note narrative — `speaker_notes.md` requires no edits

What changed is visual storytelling: stronger headline-driven charts, section navigation, magnitude/direction encoding, and proportion context.

---

## Files produced

| File | Role |
|---|---|
| `outputs/final_slide_deck_exploratory_v2.pptx` | Exploratory recording deck |
| `outputs/final_slide_deck_polished.pptx` | Prior polished deck — kept as fallback |
| `outputs/chart_class_imbalance_v2.png` | Slide 3 — 100-dot signature grid |
| `outputs/chart_model_comparison_v2.png` | Slide 7 — gap-from-baseline bar chart |
| `outputs/chart_variable_importance_v2.png` | Slide 9 left — top-5 with EDA-callback markers |
| `outputs/chart_diabetes_sensitivity_v2.png` | Slide 9 right — refined headline |
| `outputs/deck_render_v2/Slide{1–10}.PNG` | PowerPoint COM proofs of every slide |
| `code/build_charts_v2.py` | Chart-generation script (deterministic) |
| `code/build_slides_exploratory_v2.py` | Deck-build script |

---

## Slide-by-slide change summary

| # | Title | Change vs. polished deck |
|:--:|---|---|
| 1 | Title | Unchanged. Two-column navy/white layout retained. |
| 2 | Why This Matters | Adds section tag **02 — CONTEXT** top-right. Quote card and supporting cards unchanged. |
| 3 | Dataset and Response Variable | Section tag **03 — DATA**. New signature **dot-grid class-imbalance chart** (84/2/14 dots on a 10×10) replaces the stacked bar — Prediabetes annotated below the grid. KEY TAKEAWAY callout repositioned below the fact column. |
| 4 | Variables Used | Section tag **04 — PREDICTORS**. Otherwise unchanged. |
| 5 | Preliminary Analysis | Section tag **05 — EDA**. Each EDA card now carries a **direction arrow** (↑ or ↓, color-coded RUST/TEAL) + a **3-dot magnitude indicator** (filled = strength). HighBP and GenHlth are 3 of 3 dots, BMI/Age/HighChol are 2 of 3, PhysActivity is 1 of 3 with a downward arrow. |
| 6 | Methods | Section tag **06 — MODELS**. Otherwise unchanged. |
| 7 | Model Comparison | Section tag **07 — RESULTS**. New chart with **gap-from-baseline pp annotations** next to each bar (+0.51, +0.43, −0.42, −1.23). Right-side navy panel adds a compact **"GAP FROM BASELINE" mini-table** to reinforce the chart story for Q&A. |
| 8 | Decision Tree — Structure | Section tag **08 — TREE STRUCTURE**. Tree image and caption unchanged. |
| 9 | Variable Importance and Per-Class Story | Section tag **09 — INTERPRETATION**. Variable-importance chart now shows **amber "● flagged in EDA" markers** to the right of the bar values for HighBP, GenHlth, HighChol, BMI, and Age — directly tying back to the slide-5 callout. Sensitivity chart gets a refined headline title. |
| 10 | Practical Value and Conclusion | Section tag **10 — PRACTICAL VALUE**. Adds **proportion badges** to both operational cards: "~40% of patients" (teal-tinted) on the rule-out card and "~2% of patients" (rust-filled) on the high-risk card. Honest-framing strip and AI disclosure unchanged. |

The 40 % and 2 % figures are derived from the existing frozen counts (101,437 / 253,680 = 39.99 %; 3,961 / 253,680 = 1.56 %) — no new claims introduced.

---

## Visual fixes applied during build

Two chart issues were caught in the COM render pass and fixed before this summary:

1. **Slide 3 dot grid** — first build placed the "Prediabetes 2 of 100" annotation inside the dot grid, overlapping bottom-right dots. Fixed by extending the y-limit and moving the annotation below the grid with a leader line up to the prediabetes dots.
2. **Slide 9 variable importance** — first build placed the "flagged in EDA" labels to the *left* of the y-axis labels, overlapping the variable names (HighBP, GenHlth, etc.). Fixed by moving the labels to the *right* of the numeric value labels.

Both fixes are in `code/build_charts_v2.py`. Re-running the script reproduces the corrected charts deterministically.

---

## Slides to visually inspect before recording

Open `outputs/final_slide_deck_exploratory_v2.pptx` in PowerPoint slideshow mode and confirm:

| Slide | Why to inspect |
|:--:|---|
| **3** | New signature dot-grid is a load-bearing visual. Confirm the leader line from "Prediabetes: 2 of 100" lands cleanly on the rust dots. Confirm KEY TAKEAWAY card sits below the fact column without crowding. |
| **5** | Direction arrows and magnitude dots are the most novel element in the deck. Confirm each card's arrow color matches its direction (RUST ↑ for first five, TEAL ↓ for PhysActivity) and that the magnitude dot rows aren't clipped on any card. |
| **7** | Gap-from-baseline pp annotations sit in the chart's right margin. On a 16:9 projector, confirm they're not cut off by the navy headline panel. |
| **9** | Confirm the "flagged in EDA" amber markers no longer overlap the variable names. Confirm the WHAT THIS MEANS callout sits below the sensitivity chart cleanly. |
| **10** | Confirm the proportion badges (~40 % teal, ~2 % rust) sit inside their cards without overlapping the dollar numbers (101,437 / 3,961). |

The remaining slides (1, 2, 4, 6, 8) are visually identical to the polished deck except for the section-tag kicker top-right — a quick scroll-through is enough.

---

## Recording posture

This deck is recording-eligible. The `speaker_notes.md` script applies as-is. Two optional rehearsal beats:

- **Slide 3:** lean into the dot-grid: "Imagine 100 patients in this room — only two of them have prediabetes."
- **Slide 5:** point at the magnitude dots when delivering "HighBP and GenHlth are the two strongest signals" — the visuals do the work.

If anything in the visual inspection above looks off, the polished deck (`final_slide_deck_polished.pptx`) remains a clean fallback — same numbers, same conclusions, same slide order.
