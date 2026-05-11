# Polished Deck — Change Summary and Recording Checklist
## `final_slide_deck_polished.pptx`

Generated 2026-05-07 from validated source-of-truth files
(`final_report.md`, `results_packet.md`, `runtime_output_full.md`).

**Same 10-slide order. All numbers frozen. Model ranking unchanged.** What changed is layout, type hierarchy, and visuals — not content.

---

## Files produced

| File | Role |
|---|---|
| `outputs/final_slide_deck_polished.pptx` | Polished recording-ready deck |
| `outputs/final_slide_deck.pptx` | Baseline submission-safe deck (kept as fallback) |
| `outputs/chart_class_imbalance.png` | Slide 3 visual |
| `outputs/chart_model_comparison.png` | Slide 7 visual |
| `outputs/chart_variable_importance.png` | Slide 9 left visual |
| `outputs/chart_diabetes_sensitivity.png` | Slide 9 right visual |
| `outputs/chart_knn_tuning.png` | Reserve visual (not used on a slide; available for backup or report appendix) |
| `outputs/decision_tree_plot.png` | Slide 8 canonical tree image (unchanged) |
| `outputs/deck_render/Slide{1–10}.PNG` | Visual proofs of every rendered slide |
| `code/build_charts.py` | Chart-generation script (deterministic from saved CSVs) |
| `code/build_slides_v2.py` | Polished-deck build script |

---

## Slide-by-slide change summary

| # | Title | What changed | Numbers / claims changed? |
|:--:|---|---|:--:|
| 1 | Title | Two-column layout: navy band on left with "FINAL PROJECT" tag + UCI x CDC; right side now carries the title, a one-line project descriptor, and the author block. Adds rust accent line. | No |
| 2 | Why This Matters | The 4 baseline bullets become a navy pull-quote card on the left ("Identify which patient indicators predict diabetes — and turn that signal into earlier screening and targeted prevention.") plus three supporting cards on the right (Public-health weight · Three classifiers, one comparison · Personal stake). | No |
| 3 | Dataset and Response Variable | Bullet list replaced by a fact column (Source / Observations / Predictors / Missing values) on the left and the new `chart_class_imbalance.png` on the right. Adds a rust-bordered "KEY TAKEAWAY" callout under the chart. | No |
| 4 | Variables Used | Same two-column structure, now in rounded grey cards with a "14 predictors" / "7 predictors" headline and footnote about factor coding vs. KNN scaling. | No |
| 5 | Preliminary Analysis | Six EDA findings now shown as a 2 × 3 card grid; "Strongest early signals" line is a navy strip with amber tag and a footnote pointing forward to slide 9. | No |
| 6 | Methods | Three method cards (Statistical · Instance-based · Rule-based) with colored top bands (navy / teal / rust). Each card carries a name, package badge, and a short description. Tree-tuning rationale preserved verbatim. | No |
| 7 | Model Comparison | Table replaced by `chart_model_comparison.png` (with a dashed baseline at 0.8424). Right-side navy panel highlights the 0.8475 headline and the "all four within ~2 points" framing. | No |
| 8 | Decision Tree — Structure | Same tree image (`decision_tree_plot.png`), now sized to fit cleanly with a rust-tinted caption strip beneath. | No |
| 9 | Variable Importance and Per-Class Story | The bullet block is now `chart_variable_importance.png` on the left + `chart_diabetes_sensitivity.png` on the right + a "WHAT THIS MEANS" callout. The 9.1 % / 17.3 % / 22.0 % sensitivity numbers are derived directly from the saved confusion matrices. | No |
| 10 | Practical Value and Conclusion | Two contrasting cards: teal "RULE-OUT BRANCH" (101,437 patients) and rust "HIGH-RISK LEAF" (3,961 patients). A navy "HONEST FRAMING" strip preserves the class-imbalance caveat. AI disclosure footer kept. | No |

**Net effect:** identical narrative, same headline numbers (0.8475, 0.8467, 0.8382, 0.8301), same model ranking, same Diabetes-leaf rule, same baseline reference (0.8424). Visual presentation is significantly more polished.

---

## Speaker notes — update needed?

**No update required.** `outputs/speaker_notes.md` was written against the slide *narrative* (opener / support / transition for each slide), and the narrative on every slide is unchanged. The polished deck simply visualizes the same content more effectively.

Two micro-adjustments you may optionally adopt during rehearsal:

- **Slide 7:** the polished slide foregrounds "0.8475" as a callout, so you can lean into "Here's the headline — 0.8475" before walking through the bar chart.
- **Slide 9:** because both charts (variable importance + Diabetes sensitivity) are now visible at once, you can tighten the per-class section by pointing at the sensitivity chart directly: "Tree 9 percent, Logit 17, KNN 22 — that's the trade-off."

Neither change shifts any wording in `speaker_notes.md`; they're delivery options, not script edits.

---

## Recording Checklist

### Pre-recording (do these once)

- [ ] Open `outputs/final_slide_deck_polished.pptx` in PowerPoint and click through all 10 slides in slideshow mode. Confirm:
  - [ ] Tree image on slide 8 is fully visible above the caption strip.
  - [ ] All charts on slides 3, 7, 9 render at full resolution.
  - [ ] Footer slide numbers read 1/10 through 10/10.
  - [ ] No text overlaps anywhere; colors look correct (navy + rust + teal).
- [ ] Open `outputs/speaker_notes.md` in a second window or printed.
- [ ] Time one full read-through aloud against the slides. Target **10–12 minutes**.
  - If under 10 min: slow down on slides 7, 8, 9 (the substantive ones).
  - If over 13 min: drop the parenthetical detail under each Support block; keep headlines.
- [ ] Set system audio: external mic preferred, otherwise built-in. Test record 30 sec to confirm levels.
- [ ] Close all non-essential windows / notifications / chat apps.

### Recording (one clean take ideal; multiple OK)

- [ ] Launch slideshow from slide 1.
- [ ] Use **PowerPoint → Record** *or* **Zoom local recording with screen share** of slideshow.
- [ ] Speak directly to slide content — opener for each slide should land within 2 seconds of the slide appearing.
- [ ] Pause briefly between slides; let the new slide register before talking.
- [ ] On slide 8 (Decision Tree): pause an extra beat so viewers can read the leaves.
- [ ] On slide 9 (Per-Class Story): physically point to the sensitivity chart when you say "9 / 17 / 22 percent."
- [ ] Closing line: "Thanks — happy to take questions."

### Post-recording

- [ ] Save the recording. Confirm:
  - [ ] Audio levels audible end-to-end (no long silences, no clipping).
  - [ ] Slide changes are visible in the recording.
  - [ ] Total length is between 10 and 13 minutes.
- [ ] Upload / share. Copy the share link.
- [ ] Open `outputs/submission_checklist.md`. Update the Recording Link row in Section 1 with the URL.
- [ ] Update Section 7 (Submission Package Manifest) so the recording link is captured in the package.

### Submission package final assembly

- [ ] Export `outputs/final_report.md` → `Ermert_MIS401_Final_Report.pdf` (Word "Save As PDF" or Pandoc).
- [ ] Rename `outputs/final_slide_deck_polished.pptx` → `Ermert_MIS401_Final_Deck.pptx` for submission.
  - Keep `final_slide_deck.pptx` (baseline) as a local backup, do not submit.
- [ ] Copy `code/diabetes_modeling_script.R` and `data/diabetes_012_health_indicators_BRFSS2015_PRO.csv` into the submission folder.
- [ ] Add `recording_link.txt` containing the URL.
- [ ] Zip and submit. Mark `submission_checklist.md` Section 8 → **YES — submission ready.**

---

## What is intentionally not in the polished deck

- **The KNN tuning chart** (`chart_knn_tuning.png`). Slide 6 already mentions tuning over k ∈ {3, 5, 7, 9} with best K = 9, and slide 7 reports the resulting accuracy. Adding a separate KNN-tuning slide would push the deck to 11 slides and break the 10–12 minute pacing target. The chart is exported and available if you want to add an appendix slide for Q&A.
- **A summary statistics table** for BMI / Age / MentHlth / PhysHlth. The EDA findings on slide 5 capture the directional story; a numeric summary table is in the report (Section 4) where the rubric expects it. Keeping it off the deck protects density.
- **A confusion-matrix visualization for each model.** The full confusion matrices are in the report (Section 6.3) and the saved CSVs. The deck instead foregrounds the consequence of the matrices (per-class sensitivity) on slide 9, which is what the audience actually needs in 12 minutes.

If the recording rehearsal reveals empty time, the KNN tuning chart is the most natural addition — slot it between slide 6 and slide 7 as an interstitial, and update the speaker-note ordering accordingly.
