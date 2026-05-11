# Submission Checklist
## Diabetes Risk Prediction by Patient Health Indicators
### Final Package Readiness Artifact

Generated 2026-05-07. Source-of-truth files: validated R run (`runtime_output_full.md`), report (`final_report.md`), deck (`final_slide_deck.pptx`), notes (`speaker_notes.md`).

---

## 1. Required Deliverables (per `10_Deliverable_Targets_and_Submission_Requirements.md`)

| # | Deliverable | Source file | Status |
|:--:|---|---|:--:|
| 1 | Final report | `outputs/final_report.md` (export to .pdf or .docx for submission) | [ ] Confirmed |
| 2 | Slide deck / presentation file | `outputs/final_slide_deck.pptx` | [x] File exists |
| 3 | Recording link | (record from `final_slide_deck.pptx` using `speaker_notes.md`) | [ ] Recorded · [ ] Link saved |
| 4 | R code | `code/diabetes_modeling_script.R` | [x] File exists |
| 5 | Data file | `data/diabetes_012_health_indicators_BRFSS2015_PRO.csv` | [x] File exists |

## 2. Supporting Evidence Files (recommended, not strictly required)

| File | Status |
|---|:--:|
| `outputs/results_packet.md` (validated evidence digest) | [x] Exists |
| `outputs/runtime_output_full.md` (complete R runtime log) | [x] Exists |
| `outputs/decision_tree_plot.png` (canonical tree visual) | [x] Exists |
| `outputs/model_comparison_results.csv` | [x] Exists |
| `outputs/logit_confusion_matrix.csv` | [x] Exists |
| `outputs/knn_confusion_matrix.csv` | [x] Exists |
| `outputs/knn_k_tuning_results.csv` | [x] Exists |
| `outputs/tree_confusion_matrix.csv` | [x] Exists |
| `outputs/slide_deck_design_brief.md` (for optional design polish) | [x] Exists |

## 3. Filename Consistency

- [x] Code filename matches what the report's Reproducibility appendix references: `diabetes_modeling_script.R`.
- [x] Data filename matches what the R script reads: `diabetes_012_health_indicators_BRFSS2015_PRO.csv`.
- [x] Tree image filename matches what the deck embeds: `decision_tree_plot.png`.
- [ ] Confirm final report export filename, e.g., `Ermert_MIS401_Final_Report.pdf`.
- [ ] Confirm final deck filename for submission, e.g., `Ermert_MIS401_Final_Deck.pptx`.

## 4. Numerical Consistency Across Artifacts (audit)

All four artifacts must agree on these values. They were cross-checked against `runtime_output_full.md` while writing each file.

| Claim | Value | report | deck | notes | packet |
|---|---:|:--:|:--:|:--:|:--:|
| Total observations | 253,680 | ✓ | ✓ | ✓ | ✓ |
| Train / test split | 177,576 / 76,104 | ✓ | ✓ | ✓ | ✓ |
| Random seed | 401 | ✓ | ✓ | ✓ | ✓ |
| Class share NoDiabetes | 84.24 % | ✓ | ✓ | ✓ | ✓ |
| Class share Prediabetes | 1.83 % | ✓ | ✓ | ✓ | ✓ |
| Class share Diabetes | 13.93 % | ✓ | ✓ | ✓ | ✓ |
| Logit accuracy | 0.8467 | ✓ | ✓ | ✓ | ✓ |
| KNN k = 5 accuracy | 0.8301 | ✓ | ✓ | ✓ | ✓ |
| KNN best K | 9 | ✓ | ✓ | ✓ | ✓ |
| KNN best accuracy | 0.8382 | ✓ | ✓ | ✓ | ✓ |
| Decision tree accuracy | 0.8475 | ✓ | ✓ | ✓ | ✓ |
| Tree depth | ≤ 5 | ✓ | ✓ | ✓ | ✓ |
| Tree-control: cp / minsplit / minbucket / maxdepth | 0.001 / 2000 / 1000 / 5 | ✓ | ✓ | ✓ | ✓ |
| Top tree variable | HighBP | ✓ | ✓ | ✓ | ✓ |
| Diabetes-leaf rule | HighBP=1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol=1 ∧ BMI ≥ 35 | ✓ | ✓ | ✓ | ✓ |
| Diabetes-leaf size / probability | 3,961 obs / ~60 % | ✓ | ✓ | ✓ | ✓ |

If any of these change in a subsequent run, every artifact above must be updated together.

## 5. Cross-Artifact Alignment Checks

- [x] Model ranking in deck slide 7 matches the report's Section 6.1 table.
- [x] Speaker-note ordering matches deck slide order 1–10.
- [x] Tree image embedded in `final_slide_deck.pptx` is the same file referenced by the report and packet.
- [x] R script filename in the report appendix matches the actual file in `code/`.
- [x] AI disclosure present in **report** (Section 9) and in **speaker notes** (Slide 10 closing) — required by course.

## 6. Final Review Actions (must do before submitting)

- [ ] Open `outputs/final_slide_deck.pptx` in PowerPoint and click through every slide; confirm tree image renders, no overlapping text, no missing footers.
- [ ] Open `outputs/final_report.md`, export to `.pdf` or `.docx`, and re-skim for layout / pagination.
- [ ] Open `code/diabetes_modeling_script.R` and confirm it is the version with the tuned `rpart.control` and hardened `rpart.plot` `tryCatch`. (Do not submit `diabetes_tree_only_emergency.R` — that was a fallback; remove or label it before zipping.)
- [ ] Open `data/diabetes_012_health_indicators_BRFSS2015_PRO.csv` and verify 253,681 lines (1 header + 253,680 rows).
- [ ] Run a 12-minute timed pass of `speaker_notes.md` against the deck on the second monitor.
- [ ] Record the presentation; verify the recording opens and audio is clean before submitting the link.

## 7. Submission Package Manifest

When zipping or uploading, include exactly:

1. `Ermert_MIS401_Final_Report.pdf` (exported from `final_report.md`)
2. `Ermert_MIS401_Final_Deck.pptx` (rename `final_slide_deck.pptx`)
3. Recording link (paste into the submission form / a `recording_link.txt` file in the package)
4. `diabetes_modeling_script.R` (from `code/`)
5. `diabetes_012_health_indicators_BRFSS2015_PRO.csv` (from `data/`)

**Do not include:**
- `diabetes_tree_only_emergency.R` (fallback, never executed)
- `build_slides.py` (build tool, not a project deliverable)
- `model_runtime_output_partial_with_decision_tree_plot_error.md` (superseded; keep locally as audit trail only)
- `slide_deck_design_brief.md` (for your optional design pass, not the rubric)
- `Rplots.pdf` (auto-generated artifact, removed)

## 8. Submission-Ready Status

- [ ] All boxes in Section 1 are checked **including the recording link**.
- [ ] Section 6 review actions are all confirmed.
- [ ] Files in Section 7 are renamed and bundled.
- [ ] When the three lines above are all true, declare: **YES — submission ready.**

Until then: **NOT YET — last items remaining are the report export, the timed rehearsal, the recording, and the recording-link confirmation.**

---

## Outstanding User Actions (only the user can do these)

1. Export `final_report.md` → `Ermert_MIS401_Final_Report.pdf` (Pandoc, Word "Save As PDF," or markdown editor of choice).
2. Rename `final_slide_deck.pptx` → `Ermert_MIS401_Final_Deck.pptx` and visually skim once.
3. Time a rehearsal pass with `speaker_notes.md`. Trim parentheticals if over 13 minutes.
4. Record the presentation; save and copy the share link into the package.
5. Bundle and submit.
