# Slide Deck Design Brief
## Diabetes Risk Prediction by Patient Health Indicators

**Use:** paste this entire file into Claude.ai (or Artifacts, Gamma, Canva, Slidev, etc.) with a prompt like *"Design a polished 10-slide presentation from this brief. Use a clean modern healthcare-analytics aesthetic. Output as an HTML slide artifact (or .pptx outline)."*

All numerical claims are taken from the validated R run (`runtime_output_full.md`). Do not change the numbers.

---

## Project metadata

- **Title:** Diabetes Risk Prediction by Patient Health Indicators
- **Subtitle:** UCI x CDC  |  MIS 401: Business Intelligence & Analytics
- **Author:** Joshua Ermert
- **Instructor:** Dr. Xialu Liu
- **Date:** 7 May 2026
- **Length target:** 10–12 minutes (10 slides)
- **Audience:** academic + healthcare-analytics literate

## Visual language (designer notes)

- **Mood:** clean, modern, healthcare-analytics. Not playful. Not corporate-sterile.
- **Palette suggestion:** deep navy (#0B2A4A) for headers, warm rust accent (#C1441E) for emphasis, neutral gray (#555555) for body text on white. Charts in teal / amber / muted red.
- **Typography:** sans-serif throughout (Inter / Source Sans / system-ui). Title 36–40 pt, body 18–22 pt, captions 12–14 pt.
- **Layout rule:** one idea per slide, generous whitespace, no walls of text.
- **Accent rule:** only one rust accent per slide (the headline number or single key insight).
- **Footer on every content slide:** project title  ·  J. Ermert  ·  MIS 401  ·  slide N of 10.
- **Embedded image:** `outputs/decision_tree_plot.png` for slide 8.

---

## Slide 1 — Title

- **Headline:** Diabetes Risk Prediction by Patient Health Indicators
- **Sub-headline:** UCI x CDC · MIS 401: Business Intelligence & Analytics
- **Author block:** Joshua Ermert · Dr. Xialu Liu · 7 May 2026
- **Visual:** clean type-led title slide. Optional subtle background motif (low-opacity grid, electrocardiogram line, or abstract shape). Reserve the rust accent for the underline of the title.

## Slide 2 — Why This Matters

- Diabetes is a leading U.S. public-health condition: high cost, uneven distribution.
- Identifying which patient indicators predict diabetes supports earlier screening and more targeted prevention.
- Question: how well can three classification methods separate Diabetes / Prediabetes / NoDiabetes — and which indicators carry the signal?
- Personal motivation: Type II diabetes has affected the author's family; prior biopharma BI/AI analytics work reinforced the practical value.
- **Visual:** an icon trio (heart / chart / target) or a single large statistic call-out (e.g., "1 in 10 U.S. adults has diabetes" — only if you have a verified citation; if not, drop it). Don't fabricate stats.

## Slide 3 — Dataset and Response Variable

- Source: CDC Diabetes Health Indicators (UCI ML Repository, BRFSS-derived).
- 253,680 observations · 21 predictors + Diabetes_012 · no missing values.
- Response: `Diabetes_012` with three classes
  - 0 = NoDiabetes — 213,703 (84.24 %)
  - 1 = Prediabetes — 4,631 (1.83 %)
  - 2 = Diabetes — 35,346 (13.93 %)
- **Headline insight (rust-accent):** severe class imbalance is the single most important property of the dataset.
- **Visual:** 3-segment horizontal stacked bar showing the 84.24 / 1.83 / 13.93 split, with the tiny Prediabetes slice highlighted in rust.

## Slide 4 — Variables Used

- **Two-column layout.**
- **Categorical / binary:** HighBP · HighChol · CholCheck · Smoker · Stroke · HeartDiseaseorAttack · PhysActivity · Fruits · Veggies · HvyAlcoholConsump · AnyHealthcare · NoDocbcCost · DiffWalk · Sex.
- **Continuous / ordinal:** BMI · GenHlth (1 excellent – 5 poor) · MentHlth (days/30) · PhysHlth (days/30) · Age (1 youngest – 13 oldest) · Education · Income.
- **Footnote:** categorical predictors converted to factors for logit + tree; KNN used numeric encoding with z-score scaling (training-set parameters applied to the test set).

## Slide 5 — Preliminary Analysis (EDA Highlights)

- BMI shifts upward with diabetes status (median ~27 → 30 → 31).
- Age category increases with diabetes status (median 8 → 9 → 10).
- Self-rated General Health is markedly worse in the Diabetes group.
- HighBP is roughly 3× more common in the Diabetes group than in NoDiabetes.
- HighChol shows the same direction at slightly smaller magnitude.
- PhysActivity is somewhat lower; Sex effect present but weaker than the four above.
- **Strongest early signals (rust-accent):** HighBP · GenHlth · HighChol · BMI · Age.
- **Visual:** small horizontal bar chart of effect direction by predictor, OR a 2×2 mini-grid of the EDA boxplots from the Step 2 writeup if you have them as PNGs.

## Slide 6 — Methods

- Same 70/30 train/test split with `set.seed(401)` for all three models. Train n = 177,576 · Test n = 76,104.
- **Multinomial logistic regression** — `nnet::multinom` on factor-coded predictors.
- **KNN** — `class::knn` on z-scored numeric predictors; tuned over k ∈ {3, 5, 7, 9}.
- **Decision Tree** — `rpart` with `method = "class"`. Default `cp = 0.01` refused to split. Tuned to `cp = 0.001, minsplit = 2000, minbucket = 1000, maxdepth = 5` to grow a usable shallow tree (an honest tuning choice driven by class imbalance, not a deep optimization sweep).
- Evaluation: confusion matrix + overall test accuracy; tree variable importance.
- **Visual:** three method icons in a row (logit → KNN → tree) with a small badge under each showing the package name.

## Slide 7 — Model Comparison

- **Headline table (centered, large type):**

  | Rank | Model | Test Accuracy |
  |:--:|---|---:|
  | 1 | Decision Tree (cp = 0.001, depth = 5) | **0.8475** |
  | 2 | Multinomial Logistic Regression | 0.8467 |
  | 3 | KNN (best K = 9) | 0.8382 |
  | 4 | KNN (k = 5) | 0.8301 |

- **Rust-accent callout:** all four variants land within ~2 points of each other — and within ~0.5 points of the 84.2 % majority-class baseline.
- **Body line (smaller):** Accuracy alone is misleading on this dataset; per-class evidence follows.
- **Visual:** horizontal bar chart of accuracy with a dashed vertical line at the 0.8424 baseline so the closeness is immediate.

## Slide 8 — Decision Tree Structure (full-bleed image)

- **Image:** `outputs/decision_tree_plot.png` (already generated, 1400 × 900 px, ready to embed full-bleed).
- **Caption (small, centered, italic):** One Diabetes-predicting leaf: HighBP=1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol=1 ∧ BMI ≥ 35  →  n = 3,961, ~60 % Diabetes.
- **No bullets on this slide.** Let the tree do the talking.

## Slide 9 — Variable Importance and Key Insights

- Decision-tree variable importance (top 6): **HighBP > GenHlth > HighChol > DiffWalk > Age > PhysHlth > BMI**.
- This lines up directly with EDA findings (BMI, Age, GenHlth, HighBP, HighChol) and with the established Type II diabetes risk-factor literature.
- All models predict NoDiabetes for ~98 % of test rows.
- Only KNN k = 5 ever predicts Prediabetes (88 times, 2 correct).
- Diabetes-class sensitivity: Tree 9 % · Logit 17 % · KNN k = 5 22 %.
- **Rust-accent callout:** the Decision Tree wins on accuracy by trading sensitivity for precision; logit is the most balanced single deployable model.
- **Visual:** horizontal bar chart of the 7–11 importance values (already in `runtime_output_full.md` and the report).

## Slide 10 — Practical Value and Conclusion

- Even at modest sensitivity, the tree is operationally useful in two ways:
  - **Rule-out branch:** 101,437 patients with HighBP = 0 → only 6 % Diabetes rate → safe to deprioritize from intensive screening.
  - **High-risk leaf:** 3,961 patients (BMI ≥ 35 + HighChol + GenHlth poor + HighBP = 1) → ~60 % Diabetes rate → ~5× the population base rate; tractable population for targeted intervention.
- **Honest framing:** accuracy ≈ baseline; class imbalance dominates results.
- Clearest improvement path is methodological — class weights, oversampling, or a cost-sensitive threshold — not a different algorithm.
- **AI disclosure (small footer-style):** generative AI organized + polished structure; data, methods, and analytical decisions are the author's, supported by validated R outputs.

---

## Hard rules for the design pass (pass these along to the design tool / Claude.ai)

1. **Numbers are frozen.** Do not change accuracy values, counts, percentages, or splits. They come from a real R run and the report cites them.
2. **No invented statistics.** Every figure on every slide already appears in this brief. If a designer wants to add one, it must be footnoted to a verified source.
3. **Tree image is canonical.** Use `outputs/decision_tree_plot.png` as-is on slide 8. Do not redraw the tree.
4. **One idea per slide.** If a slide gets crowded, simplify rather than shrink the type.
5. **Citations:** UCI link (https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators) and Kaggle link (https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) belong on slide 3 in small footer type.
6. **Recording target:** 10–12 minutes total → ~60–90 seconds per slide. Keep slide density compatible with that pace.
7. **Output format:** export to `.pptx` for submission. If you design as HTML/Artifacts, also export a PowerPoint version (PowerPoint is the rubric requirement).

---

## Suggested Claude.ai prompt (paste this with the brief)

> Design a polished 10-slide healthcare-analytics presentation from the brief below. Use a clean modern aesthetic with deep-navy headers, a single rust accent for emphasis, and generous whitespace. Render as an HTML slide artifact I can present from. Do not change any numbers. Use the decision-tree image at the path noted on slide 8. Keep one idea per slide and respect the 10–12 minute pacing target.

Then paste the brief above.
