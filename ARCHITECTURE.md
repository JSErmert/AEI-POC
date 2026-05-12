# AEI-POC — Architecture

A short reference for how this analytics project is organised and how the pieces compose. For the substantive what / why, see [`README.md`](README.md).

---

## 1. What this is

A solo end-to-end business-analytics deliverable on the **CDC BRFSS 2015 Diabetes Health Indicators** dataset (253,680 × 22). Three classification methods are trained and compared on a fixed 70/30 split; the full deliverable chain (final report, slide deck, speaker notes, all charts) is generated through a governed compression pipeline so the spoken talk can be traced back to the same source data and modelling code.

---

## 2. Pipeline

```
data/   (raw CSV, gitignored)
  ↓
code/   (R analysis — multinomial logit, KNN with k-tuning, tuned decision tree)
  ↓
outputs/   (model artefacts, charts, audit logs)
  ↓
framework/   (Python deck-generation pipeline — python-pptx + matplotlib)
  ↓
bundle/   (final deliverable — report + slides + notes + charts, all programmatically generated)
```

Every transformation along this chain is **governed**: report → deck → notes are generated transformations of the same source artefacts, not freehand authoring. This preserves evidence lineage from the raw CDC survey data all the way through to the spoken talk.

---

## 3. Models

All three trained on the same fixed 70/30 split with `set.seed(401)`:

- **Multinomial logistic regression** — `nnet::multinom` baseline
- **K-Nearest Neighbours** — k-tuning across k ∈ {3, 5, 7, 9} on z-score-scaled predictors
- **Decision tree** — fitted, pruned via cost-complexity, evaluated on test set

Headline signal (consistent with established Type II diabetes literature):
**BMI, Age, GenHlth, HighBP, HighChol** are the strongest predictors across all three methods.

---

## 4. Repository layout

```
AEI-POC/
├── data/                                 # raw CSV (gitignored, see README for source)
├── code/                                 # R analysis scripts
├── framework/                            # Python deck-generation pipeline
├── bundle/                               # final deliverable artefacts
├── outputs/                              # model outputs, charts, audit logs
├── enhancements/                         # post-submission improvements
├── prior-artifacts/                      # superseded earlier versions, retained for lineage
├── runtime/                              # execution / runtime configuration
├── Ermert_Joshua_MIS401_Project_Submission/   # original submission package
├── README.md
├── ARCHITECTURE.md
├── SECURITY.md
└── LICENSE
```

---

## 5. Reproducibility

- **Seed** locked at `set.seed(401)` across all models
- **Split** fixed at 70/30, deterministic
- **Source data** is public-domain CDC BRFSS 2015 cleaned three-class version; URL in README
- **Deck generation** is fully programmatic — re-running produces identical artefacts from the same source

---

## 6. Further reading

- [`README.md`](README.md) — substantive overview, dataset, methods, signal
- [`SECURITY.md`](SECURITY.md) — responsible-disclosure policy
- [`LICENSE`](LICENSE) — MIT
