# AEI-POC — Diabetes Risk Prediction by Patient Health Indicators

**MIS 401: Business Intelligence & Analytics — Final Project**
**Joshua Ermert** — San Diego State University, Weber Honors College — May 2026

---

## What This Is

A solo end-to-end business-analytics deliverable built under a **governed execution framework**: data → exploratory analysis → three classification models → comparison → final report → presentation deck → recorded talk. The substantive question is whether widely collected self-reported health and lifestyle indicators can usefully separate individuals with diabetes, prediabetes, and no diabetes — and which indicators carry the most signal for clinical screening prioritization.

This repository is the **first end-to-end validation** of a reusable execution-substrate pattern (the operator's "MUSCLE PT orchestration") applied to a new domain (academic business analytics on public health data). The project is referred to internally as **AEI-POC** — Adaptive Execution Intelligence, proof of concept — because its purpose was to prove that the substrate generalizes beyond the domain it was originally built in.

---

## Dataset

**CDC Diabetes Health Indicators** (BRFSS 2015 cleaned three-class version)

- UCI: https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators
- Kaggle: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

253,680 observations × 22 variables (21 predictors + response `Diabetes_012`). Public-domain CDC survey data. The raw CSV is excluded from this repo (~12MB) — download from the source above and place under `data/`.

---

## Methods

Three classification methods learned in course, applied to the same 70/30 train/test split (`set.seed(401)`):

1. **Multinomial logistic regression** — `nnet::multinom(Diabetes_012 ~ ., data = train_data)`
2. **K-nearest neighbors** — `class::knn` on z-score-scaled predictors, tuned across k ∈ {3, 5, 7, 9}
3. **Decision tree** — tuned and pruned

All three evaluated on the same held-out test set with confusion matrices, accuracy, macro-F1, and per-class precision/recall reported.

---

## Repository Layout

```
AEI-POC/
├── code/                                # Modeling + presentation generation code
│   ├── diabetes_modeling_script.R       # R: data prep, three models, confusion matrices, comparison
│   ├── diabetes_tree_only_emergency.R   # R: decision tree fallback path
│   ├── build_charts.py / build_charts_v2.py     # Python: chart generation for the deck
│   └── build_slides.py / build_slides_v2.py     # Python: slide-deck composition (python-pptx)
│
├── outputs/                             # Generated artifacts
│   ├── final_report.md                  # Markdown source of the final written report
│   ├── final_slide_deck_polished.pptx   # Polished PowerPoint deck
│   ├── speaker_notes.md                 # Recording-ready speaker notes
│   ├── chart_*.png                      # All generated charts
│   ├── model_comparison_results.csv     # Model accuracies side-by-side
│   ├── knn_confusion_matrix.csv         # KNN confusion matrix
│   ├── logit_confusion_matrix.csv       # Logistic regression confusion matrix
│   └── runtime_output_full.md           # Full R run log
│
├── Ermert_Joshua_MIS401_Project_Submission/   # Course-submitted deliverable package
│   ├── Ermert_MIS401_Final_Report.pdf
│   ├── presentation_slide_deck.pptx
│   └── diabetes_modeling_code.R
│
├── framework/                           # Governed execution framework (substrate)
│   ├── 00_Project_Evidence_Digest.md
│   ├── 01_Governed_Instructional_Execution_Framework.md
│   ├── 02_Framework_Manifest_and_Print_Order.md
│   ├── 03_Phase_Architecture_and_Artifact_Gates.md
│   ├── 04_Validation_and_Quality_Control_Doctrine.md
│   ├── 05_Artifact_Templates_and_Output_Contracts.md
│   ├── 06_Report_to_Presentation_Compression_System.md
│   ├── 07_Emergency_Execution_Mode_and_Timeboxed_Workflows.md
│   └── 08_Claude_Readiness_and_Activation_Protocol.md
│
├── enhancements/                        # Cross-portfolio enhancements imported into this run
├── runtime/                             # Runtime state + priority queue + behavior discipline
├── prior-artifacts/                     # Earlier proposal + pre-meeting writeup
└── data/                                # (gitignored — see Dataset section for source)
```

---

## Key Findings (full detail in `outputs/final_report.md`)

- **BMI, Age, GenHlth (self-rated general health), HighBP, HighChol** carry the strongest signal — consistent with established Type II diabetes risk-factor literature.
- **Class imbalance is the dominant property** of the dataset (84% NoDiabetes / 2% Prediabetes / 14% Diabetes) and shapes every model's interpretation.
- **Logistic regression and tuned decision tree** both reach the same upper-end accuracy as KNN at substantially lower computational cost; the tree is most interpretable for clinical screening prioritization.
- **Prediabetes is the hardest class** for all three models, recovering little signal beyond the marginal prior — a known limitation of survey-based screening for an intermediate clinical state.

---

## Reproducibility

```bash
# 1. Place the CSV under data/ (download from UCI link above)
# 2. R modeling
Rscript code/diabetes_modeling_script.R

# 3. Python deck generation
pip install matplotlib python-pptx pandas
python code/build_charts_v2.py
python code/build_slides_v2.py
```

Outputs land under `outputs/`.

---

## Engineering Discipline Applied

This project is a class deliverable in form, but the engineering substrate underneath is the same governed-execution pattern used in the operator's larger portfolio:

- **Phase architecture** with artifact gates (see `framework/03_Phase_Architecture_and_Artifact_Gates.md`)
- **Validation doctrine** — every generated chart and table is checked against the modeling code's runtime output before being included in the report (see `framework/04_Validation_and_Quality_Control_Doctrine.md`)
- **Compression chain** — report → slide deck → speaker notes as governed transformations, not freehand authoring (see `framework/06_Report_to_Presentation_Compression_System.md`)
- **Emergency execution mode** — timeboxed fallback workflows for when validation gates fail close to a deadline (see `framework/07_Emergency_Execution_Mode_and_Timeboxed_Workflows.md`)

The intent was to demonstrate that a discipline built for high-stakes engineering work transfers cleanly to an academic deliverable — and to validate the pattern before extending it to other domains.

---

## Author

Joshua Ermert — [linkedin.com/in/josh-ermert-79496b176](https://www.linkedin.com/in/josh-ermert-79496b176/)
