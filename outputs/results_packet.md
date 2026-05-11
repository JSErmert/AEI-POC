# Results Packet
## Diabetes Risk Prediction by Patient Health Indicators
### Artifact 4 — Evidence Generation / Validation
### Generated 2026-05-07

---

## Provenance

- **Script:** `code/diabetes_modeling_script.R`
- **Data:** `data/diabetes_012_health_indicators_BRFSS2015_PRO.csv` (253,680 obs × 22 vars)
- **Random seed:** `set.seed(401)`
- **Train / test split:** 70 / 30 → 177,576 train / 76,104 test
- **Runtime log:** `outputs/runtime_output_full.md`
- **Output CSVs:** `model_comparison_results.csv`, `logit_confusion_matrix.csv`, `knn_confusion_matrix.csv`, `knn_k_tuning_results.csv`, `tree_confusion_matrix.csv`
- **Tree plot:** `outputs/decision_tree_plot.png`

All figures below are produced from the actual completed run; nothing in this packet is invented or estimated.

---

## Core Outputs

- Multinomial logistic regression confusion matrix and accuracy
- KNN initial model (k = 5) confusion matrix and accuracy
- KNN tuning table over k ∈ {3, 5, 7, 9} with best-K identified
- Decision tree CP table, fitted tree (depth ≤ 5), confusion matrix, accuracy, variable importance
- Decision tree plot (PNG)
- Final model comparison table (CSV) ranking all four model variants

---

## Key Numerical Findings

### Class proportions (training set)

| Class | Proportion |
|---|---:|
| NoDiabetes | 0.8421 |
| Prediabetes | 0.0181 |
| Diabetes | 0.1397 |

Test set proportions are within 0.001 of the training set, confirming a balanced split.

### Final model comparison (sorted by test accuracy)

| Rank | Model | Test Accuracy |
|:--:|---|---:|
| 1 | Decision Tree (cp=0.001, maxdepth=5) | **0.8475** |
| 2 | Multinomial Logistic Regression | 0.8467 |
| 3 | KNN (best K = 9) | 0.8382 |
| 4 | KNN (k = 5) | 0.8301 |

### Decision tree confusion matrix (test, n = 76,104)

|              | Actual NoDiabetes | Actual Prediabetes | Actual Diabetes |
|---|---:|---:|---:|
| Pred NoDiabetes | 63,541 | 1,358 | 9,572 |
| Pred Prediabetes | 0 | 0 | 0 |
| Pred Diabetes | 618 | 56 | 959 |

- Correct predictions: 63,541 + 0 + 959 = 64,500 → accuracy 0.8475 ✓
- Sensitivity for Diabetes class: 959 / (9,572 + 56 + 959) = **9.07 %**
- Sensitivity for Prediabetes class: **0 %**
- Specificity for NoDiabetes: 64,159 / 64,816 = 99.0 %

### Logistic regression confusion matrix (test, n = 76,104)

|              | Actual NoDiabetes | Actual Prediabetes | Actual Diabetes |
|---|---:|---:|---:|
| Pred NoDiabetes | 62,617 | 1,291 | 8,713 |
| Pred Prediabetes | 0 | 0 | 0 |
| Pred Diabetes | 1,542 | 123 | 1,818 |

- Sensitivity for Diabetes class: 1,818 / 10,531 = **17.27 %**
- Sensitivity for Prediabetes class: **0 %**

### KNN tuning over k

| K | Test Accuracy |
|---:|---:|
| 3 | 0.8160 |
| 5 | 0.8303 |
| 7 | 0.8354 |
| **9** | **0.8382** |

Accuracy increases monotonically with k across the swept range; best K = 9.

### KNN (k = 5) confusion matrix (test, n = 76,104)

|              | Actual NoDiabetes | Actual Prediabetes | Actual Diabetes |
|---|---:|---:|---:|
| Pred NoDiabetes | 60,860 | 1,201 | 8,183 |
| Pred Prediabetes | 50 | 2 | 36 |
| Pred Diabetes | 3,249 | 211 | 2,312 |

KNN (k=5) is the only model that ever predicts Prediabetes (88 such predictions, 2 correct).

### Decision tree variable importance (rpart)

| Rank | Variable | Importance |
|:--:|---|---:|
| 1 | HighBP | 3,230.6 |
| 2 | GenHlth | 1,950.6 |
| 3 | HighChol | 786.7 |
| 4 | DiffWalk | 694.5 |
| 5 | Age | 621.7 |
| 6 | PhysHlth | 485.5 |
| 7 | BMI | 446.9 |
| 8 | HeartDiseaseorAttack | 354.3 |
| 9 | MentHlth | 139.8 |
| 10 | Income | 77.8 |
| 11 | Education | 32.8 |

Variables not appearing in the importance list (e.g., CholCheck, Smoker, Stroke, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, Sex) had insufficient surrogate-split contribution to register.

### Decision tree split structure (depth-5 tree, eight terminal nodes)

| Path | Terminal class | n | Diabetes prob. |
|---|---|---:|---:|
| HighBP = 0 | NoDiabetes | 101,437 | 0.06 |
| HighBP = 1 ∧ GenHlth < 4 | NoDiabetes | 55,854 | 0.19 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI < 28 | NoDiabetes | 7,056 | 0.28 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 0 | NoDiabetes | 4,086 | 0.36 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 1 ∧ BMI < 35 | NoDiabetes | 5,182 | 0.46 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 1 ∧ BMI ≥ 35 | **Diabetes** | 3,961 | **0.60** |

Only one terminal node ever predicts Diabetes; no terminal node ever predicts Prediabetes.

---

## Must-Show Visuals

1. **Decision tree plot** — `outputs/decision_tree_plot.png` (color-coded, fallen-leaves layout, includes class proportions and node coverage)
2. **Model comparison bar/table** — built from `model_comparison_results.csv`
3. **KNN k-tuning curve** — built from `knn_k_tuning_results.csv` (K vs accuracy)

## Report-Only Supporting Outputs

- Class proportions table (train and test)
- All three confusion matrices side-by-side
- Variable importance table

## Archive-Only Outputs

- Full multinom coefficient and standard-error tables (already in runtime log; too large for the report body)
- Full rpart `summary(tree_model)` output (in runtime log)

---

## Initial Interpretation Bullets

- All four model variants land between 83 % and 85 % accuracy, very close to the **NoDiabetes base rate of 84.2 %** in the test set. Accuracy alone overstates how well any of these models perform on the minority classes.
- The Decision Tree narrowly tops the comparison (0.8475), but it does so by predicting the majority class on **98 % of test rows** (74,471 of 76,104) and only flagging Diabetes when a strict five-condition gate is met (HighBP = 1 AND GenHlth ≥ 4 AND BMI ≥ 28 AND HighChol = 1 AND BMI ≥ 35). This is high-precision, low-sensitivity behavior.
- Logistic regression catches **almost twice as many true Diabetes cases as the Decision Tree** (1,818 vs 959 true positives), at the cost of slightly more false positives. Whether this is preferable depends on screening goals.
- **No model ever predicts Prediabetes** at the level of practical use. KNN (k = 5) makes 88 such predictions, of which only 2 are correct. Prediabetes (1.8 % of observations) is too rare for unweighted classifiers trained at the default decision threshold.
- The decision tree's variable importance gives a clean clinical narrative: blood-pressure status → general-health self-rating → cholesterol status → BMI together carry almost all of the signal. This aligns with established diabetes risk factors and the project's preliminary EDA findings.
- Demographic and lifestyle predictors (Smoker, Fruits, Veggies, PhysActivity, HvyAlcoholConsump, Sex) did not enter the tree, suggesting their effects in this dataset are weaker or already captured through correlated health-status variables.

---

## Best Result / Best Model

- **Best by raw test accuracy:** Decision Tree (0.8475).
- **Best for Diabetes-class detection:** Multinomial Logistic Regression (17.3 % sensitivity vs 9.1 % for the tree, 22.0 % for KNN k=5 — but KNN k=5 has the lowest overall accuracy).
- **Honest framing for the report:** the three methods are within ~2 percentage points of each other and within ~0.5 points of the majority-class baseline. The Decision Tree is named the best **headline** model, with the explicit caveat that its advantage is small and class-imbalance-driven.

---

## Known Limitations / Anomalies

1. **Severe class imbalance.** Diabetes_012 distribution is 84.2 % / 1.8 % / 14.0 %. With default thresholds, no model usefully predicts the Prediabetes class.
2. **Default rpart did not split.** With cp = 0.01, no single split improved relative error by 1 % over the majority-class prior. We tuned `rpart.control(cp = 0.001, minsplit = 2000, minbucket = 1000, maxdepth = 5)` to grow a usable shallow tree. The tuning is conservative — depth was capped to keep the tree interpretable. Documented honestly in the report; we are not claiming an unconstrained optimal tree.
3. **Accuracy is a misleading headline metric here** because the majority-class prior is 84.2 %. The report and slides must caveat this and present per-class sensitivity / confusion-matrix evidence so the reader is not misled by the headline number.
4. **KNN with k = 5 is the only model that predicts Prediabetes**, and it does so almost entirely incorrectly (2 / 88). This is interesting for the discussion but not a recommended deployment choice.
5. **`rpart.plot` palette validator rejects its own internal default for single-node trees.** Documented in the script; the plot call is wrapped in `tryCatch` with an explicit `box.palette = "RdYlGn"` so plot failures cannot interrupt evidence generation again.
