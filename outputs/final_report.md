# Diabetes Risk Prediction by Patient Health Indicators
## UCI x CDC

**Joshua Ermert**
MIS 401: Business Intelligence & Analytics
Dr. Xialu Liu
7 May 2026

---

## 1. Introduction

Diabetes is one of the most consequential public-health conditions in the United States, with rising prevalence, substantial healthcare costs, and uneven distribution across demographic and socioeconomic groups. Identifying the patient-level health and lifestyle indicators most associated with diabetes risk supports earlier screening, more targeted prevention, and more efficient allocation of clinical resources. This project asks a focused predictive question: using widely collected self-reported health, lifestyle, and demographic indicators, how well can statistical and machine-learning classifiers separate individuals with diabetes, prediabetes, and no diabetes — and which indicators carry the most signal?

The project applies three classification methods learned in class — multinomial logistic regression, k-nearest neighbors (KNN), and a tuned decision tree — to the CDC Diabetes Health Indicators dataset and compares them on a held-out test set. The personal motivation for the project is that Type II diabetes has affected the author's family, and a prior summer role in a biopharmaceutical company's commercial-operations and BI/AI analytics function reinforced how applied analytics can inform real healthcare decisions.

---

## 2. Data Source and Description

The analysis uses the CDC Diabetes Health Indicators dataset published on the UCI Machine Learning Repository, with the cleaned three-class version distributed via the Kaggle dataset homepage.

- UCI repository: https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators
- Kaggle homepage: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

The cleaned file used here (`diabetes_012_health_indicators_BRFSS2015_PRO.csv`) contains 253,680 observations and 22 variables (21 predictors plus the response). The underlying data come from the CDC's Behavioral Risk Factor Surveillance System (BRFSS), a long-running large-sample telephone survey of adults in the United States. There are no missing values.

---

## 3. Variables and Response Variable

### Response variable

`Diabetes_012` — a three-class categorical variable:

- 0 = NoDiabetes
- 1 = Prediabetes
- 2 = Diabetes

### Categorical / binary predictors

HighBP, HighChol, CholCheck, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, DiffWalk, Sex.

### Continuous / ordinal predictors

BMI, GenHlth (1 = excellent through 5 = poor), MentHlth (days/30), PhysHlth (days/30), Age (1 = youngest category through 13 = oldest), Education, Income.

### Variable-handling decisions

Categorical predictors were converted to factors before fitting. KNN used the numeric encoding of the same predictors with z-score scaling computed on the training set and applied to the test set, since KNN is distance-based.

---

## 4. Summary Statistics and Preliminary Analysis

### Response-variable distribution (full dataset)

| Class | Count | Share |
|---|---:|---:|
| NoDiabetes | 213,703 | 84.24 % |
| Prediabetes | 4,631 | 1.83 % |
| Diabetes | 35,346 | 13.93 % |

Class proportions in the 70/30 train/test split (seed 401) match the full sample to within 0.001:

| Split | NoDiabetes | Prediabetes | Diabetes |
|---|---:|---:|---:|
| Train (n = 177,576) | 0.8421 | 0.0181 | 0.1397 |
| Test (n = 76,104) | 0.8430 | 0.0186 | 0.1384 |

This severe class imbalance is the single most important property of the dataset and shapes interpretation of every model.

### Preliminary findings (Step 2 EDA)

- BMI shifts upward with diabetes status; the median is roughly 27 in NoDiabetes vs. 30 in Prediabetes vs. 31 in Diabetes.
- Age category increases with diabetes status; the median age category is 8 in NoDiabetes, 9 in Prediabetes, 10 in Diabetes.
- Self-rated General Health worsens substantially in the diabetes group.
- High blood pressure (HighBP = 1) is roughly three times more common in the diabetes group than in the no-diabetes group.
- High cholesterol (HighChol = 1) shows the same direction at slightly smaller magnitude.
- Physical activity is somewhat lower in the diabetes group.
- Sex differences are present but weaker than BMI, age, blood pressure, or cholesterol.

These EDA patterns provide a substantive prior that the modeling should reflect: the strongest signal should come from blood pressure, general-health rating, cholesterol, BMI, and age.

---

## 5. Methods

Three classification methods learned in class were applied to the same train/test split (`set.seed(401)`, 70/30, n_train = 177,576, n_test = 76,104). All three models used the same 21 predictors.

### Multinomial logistic regression

Fitted with `nnet::multinom(Diabetes_012 ~ ., data = train_data)`. NoDiabetes was the reference class. The fitted model produced two sets of coefficients (Prediabetes vs. NoDiabetes, Diabetes vs. NoDiabetes). Final residual deviance was 142,377.2 with AIC 142,465.2.

### K-nearest neighbors

Applied via `class::knn` on numeric, training-set z-score-scaled predictors. The initial run used k = 5; tuning swept k ∈ {3, 5, 7, 9}. Best K and final KNN accuracy were taken from the highest-accuracy k value.

### Decision tree

Fitted with `rpart(Diabetes_012 ~ ., method = "class")`. With default control parameters (cp = 0.01, minsplit = 20), no split was generated because the majority-class prior was 84.2 %, and no single split improved the relative error by 1 %. The tree was therefore tuned with:

```r
rpart.control(cp = 0.001, minsplit = 2000, minbucket = 1000, maxdepth = 5)
```

This produces a shallow, interpretable tree (depth ≤ 5, eight terminal nodes) and is documented honestly as a tuning choice driven by the dataset's class imbalance, not as the result of a deep optimization sweep.

### Evaluation

All three models were evaluated on the held-out test set using a confusion matrix (Predicted × Actual) and overall classification accuracy. A model-comparison table ranks the three methods (with two KNN variants) by test accuracy. Tree variable importance is taken from `tree_model$variable.importance`.

---

## 6. Results

### 6.1 Model comparison

| Rank | Model | Test Accuracy |
|:--:|---|---:|
| 1 | Decision Tree (cp = 0.001, maxdepth = 5) | **0.8475** |
| 2 | Multinomial Logistic Regression | 0.8467 |
| 3 | KNN (best K = 9) | 0.8382 |
| 4 | KNN (k = 5) | 0.8301 |

All four model variants land within ~2 percentage points of one another, and within ~0.5 points of the NoDiabetes base rate of 84.2 %. The Decision Tree is the highest-accuracy model, narrowly ahead of multinomial logistic regression.

### 6.2 KNN tuning

| K | Test Accuracy |
|:--:|---:|
| 3 | 0.8160 |
| 5 | 0.8303 |
| 7 | 0.8354 |
| **9** | **0.8382** |

Accuracy increases monotonically with k across the swept range. K = 9 is the local optimum within {3, 5, 7, 9}.

### 6.3 Confusion matrices (test, n = 76,104)

#### Decision Tree

| | Actual NoD | Actual Pre | Actual Dia |
|---|---:|---:|---:|
| Pred NoDiabetes | 63,541 | 1,358 | 9,572 |
| Pred Prediabetes | 0 | 0 | 0 |
| Pred Diabetes | 618 | 56 | 959 |

#### Multinomial logistic regression

| | Actual NoD | Actual Pre | Actual Dia |
|---|---:|---:|---:|
| Pred NoDiabetes | 62,617 | 1,291 | 8,713 |
| Pred Prediabetes | 0 | 0 | 0 |
| Pred Diabetes | 1,542 | 123 | 1,818 |

#### KNN (k = 5)

| | Actual NoD | Actual Pre | Actual Dia |
|---|---:|---:|---:|
| Pred NoDiabetes | 60,860 | 1,201 | 8,183 |
| Pred Prediabetes | 50 | 2 | 36 |
| Pred Diabetes | 3,249 | 211 | 2,312 |

Per-class sensitivity — i.e., the share of true Diabetes cases the model actually flags as Diabetes — is 9.1 % for the Decision Tree, 17.3 % for logistic regression, and 22.0 % for KNN k = 5. The Decision Tree's higher overall accuracy comes at the cost of low Diabetes sensitivity. Only KNN k = 5 ever predicts Prediabetes (88 such predictions, 2 correct).

### 6.4 Decision tree structure

The tuned tree has eight terminal nodes and is dominated by five splits:

| Path | Predicted class | n | Diabetes prob. |
|---|---|---:|---:|
| HighBP = 0 | NoDiabetes | 101,437 | 0.06 |
| HighBP = 1 ∧ GenHlth < 4 | NoDiabetes | 55,854 | 0.19 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI < 28 | NoDiabetes | 7,056 | 0.28 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 0 | NoDiabetes | 4,086 | 0.36 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 1 ∧ BMI < 35 | NoDiabetes | 5,182 | 0.46 |
| HighBP = 1 ∧ GenHlth ≥ 4 ∧ BMI ≥ 28 ∧ HighChol = 1 ∧ BMI ≥ 35 | **Diabetes** | 3,961 | **0.60** |

The tree predicts Diabetes only when all five conditions are met simultaneously. No path predicts Prediabetes. The corresponding plot is `decision_tree_plot.png`.

### 6.5 Variable importance (Decision Tree)

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

CholCheck, Smoker, Stroke, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, and Sex did not register in the variable-importance output for the tuned tree.

---

## 7. Discussion / Practical Value

### 7.1 The headline finding is real but small

The Decision Tree edges out logistic regression by 0.0008 in test accuracy (0.8475 vs. 0.8467). KNN trails by another 0.008–0.017 depending on k. From a strict modeling standpoint, all three methods deliver substantially the same headline number, and that headline number is barely above the 84.2 % majority-class baseline. **Accuracy alone is a misleading metric on this dataset**, and the report deliberately presents per-class confusion-matrix evidence so the reader is not misled by the headline.

### 7.2 The class-imbalance story

Diabetes_012 distribution is 84.24 % / 1.83 % / 13.93 %. With default decision thresholds, all three models effectively learn to predict NoDiabetes most of the time:

- Logistic regression and the Decision Tree never predict Prediabetes.
- The Decision Tree predicts Diabetes for only 1,633 of 76,104 test rows (2.1 %), of which 959 are correct.
- KNN (k = 5) is the only model that ever predicts Prediabetes; it does so 88 times and is correct in 2 of them.

This is the dominant pattern in the results. A practical screening tool would need either (a) class weights or oversampling at training time, (b) a cost-sensitive decision threshold, or (c) a re-framing of the problem as a binary task (any-diabetes vs. none). These options are out of scope for this project but are the honest next step.

### 7.3 Important predictors and clinical alignment

The Decision Tree's variable importance gives a clean, clinically defensible story: **blood-pressure status, self-rated general health, cholesterol status, and BMI** carry essentially all of the discriminating signal, with age and difficulty-walking close behind. This aligns directly with the Step 2 exploratory findings (high BMI, older age, worse general health, and higher rates of high blood pressure / cholesterol in the diabetes group). It also aligns with established clinical risk-factor hierarchies for Type II diabetes.

The single Diabetes-predicting leaf in the tree — HighBP = 1 *and* poor general health (GenHlth ≥ 4) *and* overweight/obese (BMI ≥ 28) *and* high cholesterol *and* obesity (BMI ≥ 35) — reads almost like a clinician's checklist for high-risk patients.

### 7.4 Practical use

For a healthcare organization, even a model with low Diabetes sensitivity is useful in two specific ways:

1. **The "rule out" branch** is large and clean. The 101,437 patients in the HighBP = 0 leaf have only a 6 % Diabetes rate; the model can confidently de-prioritize this group from intensive screening.
2. **The high-risk leaf** is small but enriched. The 3,961 patients in the BMI ≥ 35 / HighChol = 1 / poor-GenHlth / HighBP = 1 leaf have a 60 % Diabetes rate — almost five times the population base rate. That is a tractable population for targeted intervention, even if the model misses many other Diabetes cases elsewhere.

### 7.5 Comparing the models honestly

- **Decision Tree:** highest accuracy, fully interpretable, easy to translate into a rule. Lowest Diabetes sensitivity of the three. Requires tuning to overcome class imbalance.
- **Multinomial logistic regression:** essentially tied on accuracy, gives statistical inference (coefficients, standard errors), and roughly doubles Diabetes sensitivity vs. the tree. Loses the geometric clarity of a tree.
- **KNN:** lowest accuracy of the three, slowest to score, but the only model that ever predicts Prediabetes — interesting evidence that a local-similarity method can reach into rare-class territory where parametric models cannot.

If the goal were a single deployable model, logistic regression is probably the most defensible default given near-tied accuracy and meaningfully higher Diabetes recall. If interpretability is the goal, the tree wins.

---

## 8. Conclusion

Three classification methods were applied to the 253,680-observation CDC Diabetes Health Indicators dataset to predict three-class diabetes status. Tested on a held-out 30 % sample with a fixed seed, the tuned Decision Tree narrowly led on overall accuracy (0.8475), with multinomial logistic regression (0.8467) and KNN at k = 9 (0.8382) close behind. Headline accuracy is only marginally above the 84.2 % majority-class baseline, and per-class evidence shows that no model usefully predicts Prediabetes and that all three predict Diabetes at low sensitivity.

The substantive payoff is the variable-importance picture: blood-pressure status, self-rated general health, cholesterol, BMI, age, and difficulty walking carry the signal, and they line up cleanly with both the Step 2 exploratory findings and established clinical risk factors for Type II diabetes. The tuned Decision Tree converts that signal into an interpretable, clinically defensible rule that can serve as a screening prioritization aid: a large low-risk "rule-out" branch and a small, highly enriched high-risk branch (HighBP = 1, GenHlth ≥ 4, BMI ≥ 35, HighChol = 1) where targeted intervention is most likely to matter.

The clearest improvement path is methodological rather than algorithmic — class weights, oversampling, or a cost-sensitive decision threshold — and that is the honest next step for any extension of this project.

---

## 9. AI Disclosure

Generative AI organized and polished the structural skeleton of the report and helped translate the validated R outputs into prose. The dataset selection, project direction, methodology, modeling decisions, tree-tuning rationale, and analytical interpretations are the author's own, supported by the actual `diabetes_modeling_script.R` runtime output captured in `runtime_output_full.md`.

---

## Appendix A — Reproducibility

- **Code:** `code/diabetes_modeling_script.R`
- **Data:** `data/diabetes_012_health_indicators_BRFSS2015_PRO.csv`
- **Seed:** `set.seed(401)`
- **Train/test:** 70 / 30 random split, 177,576 / 76,104 rows
- **R version:** 4.5.2; packages `nnet`, `class`, `rpart`, `rpart.plot`
- **Output artifacts:** `runtime_output_full.md`, `model_comparison_results.csv`, `logit_confusion_matrix.csv`, `knn_confusion_matrix.csv`, `knn_k_tuning_results.csv`, `tree_confusion_matrix.csv`, `decision_tree_plot.png`
