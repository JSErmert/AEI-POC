# 00_Project_Evidence_Digest
## Runtime Output and Evidence Intake Layer
### Optional Pre-Framework File

---

## Purpose

This file gives Claude a compact evidence-first snapshot of the project before it enters the main framework files.

It exists to provide immediate access to:

- the actual script used
- the actual dataset used
- whether execution completed fully or partially
- the outputs already produced
- the most important findings already observed
- warnings, errors, or anomalies
- what evidence still needs to be generated

This file reduces startup ambiguity and reduces dependence on code execution.

It is a live evidence digest.

It is not a doctrine file.

It is not a replacement for the framework.

It is the project’s runtime evidence layer.

---

## Recommended File Name

`00_Project_Evidence_Digest.md`

---

## Usage Rule

Claude should read this file before `01_Governed_Instructional_Execution_Framework.md` when it is available.

Its purpose is to anchor Claude in the real state of the project’s evidence before the broader framework activates.

---

## Project Identity

- **Project name:** Diabetes Risk Prediction by Patient Health Indicators
- **Project type:** academic analytics project
- **Primary question / objective:** compare multiple classification methods for predicting diabetes status using patient health indicators
- **Primary dataset used:** `diabetes_012_health_indicators_BRFSS2015_PRO.csv`
- **Primary script used:** final R modeling script using multinomial logistic regression, KNN, and decision tree
- **Primary response variable:** `Diabetes_012`
- **Response classes:** `0 = No Diabetes`, `1 = Prediabetes`, `2 = Diabetes`

---

## Runtime Assets Used

- **Requirements file used:** MIS 401 project requirements digest / requirements PDF if available
- **CSV file used in intended final R workflow:** `diabetes_012_health_indicators_BRFSS2015_PRO.csv`
- **Known alternate data file currently present in some bundles:** `diabetes_012_health_indicators_BRFSS2015_PRO.xlsx`
- **Important data-file note:** the R script expects a CSV unless revised to read Excel
- **R script filename:** full final diabetes modeling script must be provided separately
- **Saved runtime output currently available:** `outputs/model_runtime_output.md`
- **Runtime output status:** partial, not complete
- **Prior artifacts available or expected:** project proposal and pre-meeting / Step 2 exploratory analysis document

---

## Execution Status

- **Execution status:** partially completed
- **What completed successfully:** dataset inspection, train/test split, multinomial logistic regression, logistic regression confusion matrix, logistic regression accuracy, initial KNN run for k = 5
- **What did not complete in the captured output:** full KNN tuning table, best K selection, decision tree model, decision tree variable importance, final model comparison table, saved output confirmation
- **Current evidence state:** useful but incomplete
- **Evidence readiness:** not yet final-report-ready until remaining model outputs are generated or captured

---

## Key Outputs Generated

The following outputs have already been observed from earlier R execution.

### Dataset Inspection

- dataset loaded successfully from the intended PRO file during the successful run
- dimensions observed: `253,680` rows and `22` variables
- variables include:
  - `Diabetes_012`
  - `HighBP`
  - `HighChol`
  - `CholCheck`
  - `BMI`
  - `Smoker`
  - `Stroke`
  - `HeartDiseaseorAttack`
  - `PhysActivity`
  - `Fruits`
  - `Veggies`
  - `HvyAlcoholConsump`
  - `AnyHealthcare`
  - `NoDocbcCost`
  - `GenHlth`
  - `MentHlth`
  - `PhysHlth`
  - `DiffWalk`
  - `Sex`
  - `Age`
  - `Education`
  - `Income`

### Dataset Summary

The dataset contains health, lifestyle, and demographic predictors related to diabetes status.

Important observed summary values include:

- `BMI` mean: approximately `28.38`
- `GenHlth` mean: approximately `2.511`
- `MentHlth` mean: approximately `3.185`
- `PhysHlth` mean: approximately `4.242`
- `Age` mean: approximately `8.032`
- `Education` mean: approximately `5.05`
- `Income` mean: approximately `6.054`

### Train/Test Split

The split used:

- training proportion: `70%`
- testing proportion: `30%`
- random seed: `401`
- training rows: `177,576`
- testing rows: `76,104`

### Class Proportions

Training set class proportions:

- `NoDiabetes`: `0.84214083`
- `Prediabetes`: `0.01811619`
- `Diabetes`: `0.13974298`

Testing set class proportions:

- `NoDiabetes`: `0.84304373`
- `Prediabetes`: `0.01857984`
- `Diabetes`: `0.13837643`

Important interpretation:

- the response variable is strongly imbalanced
- `Prediabetes` is a very small minority class
- overall accuracy must be interpreted carefully because the majority class dominates the dataset

---

## Model Results Summary

### Multinomial Logistic Regression

- **Model status:** completed
- **Accuracy:** `0.8467`
- **Confusion matrix available:** yes
- **Important issue:** the model predicted no observations as `Prediabetes`
- **Interpretation status:** usable but must be framed carefully because high accuracy is partly influenced by class imbalance

#### Logistic Regression Confusion Matrix

| Predicted | Actual NoDiabetes | Actual Prediabetes | Actual Diabetes |
|---|---:|---:|---:|
| NoDiabetes | 62,617 | 1,291 | 8,713 |
| Prediabetes | 0 | 0 | 0 |
| Diabetes | 1,542 | 123 | 1,818 |

#### Logistic Regression Interpretation Notes

- Logistic regression achieved high overall accuracy.
- The model performed best at identifying the dominant `NoDiabetes` class.
- The model failed to classify any cases as `Prediabetes`.
- This supports the important project insight that class imbalance affects model usefulness.
- Accuracy alone is not enough to evaluate quality for this dataset.

---

### K-Nearest Neighbors

- **Model status:** partially completed
- **Initial K used:** `5`
- **Initial k = 5 run status:** completed in the observed output sequence
- **Full tuning status:** incomplete in captured runtime output
- **Best K known:** not finalized
- **KNN confusion matrix available:** partially, only if captured after the k = 5 run
- **KNN tuning table available:** not finalized
- **Important issue:** earlier paste/run sequence was interrupted around KNN tuning and later code merged incorrectly

#### KNN Evidence Needed

Claude should still obtain or validate:

- KNN confusion matrix for k = 5
- KNN accuracy for k = 5
- KNN accuracy table for k values such as `3`, `5`, `7`, `9`
- best K
- best KNN accuracy

---

### Decision Tree

- **Model status:** not finalized in captured runtime output
- **Decision tree confusion matrix available:** not yet finalized
- **Decision tree accuracy available:** not yet finalized
- **Variable importance available:** not yet finalized
- **Decision tree plot available:** not yet finalized
- **Important issue:** the decision tree block appears after the interrupted KNN section and needs a clean rerun

#### Decision Tree Evidence Needed

Claude should still obtain or validate:

- decision tree model summary
- decision tree plot
- decision tree confusion matrix
- decision tree accuracy
- decision tree variable importance

---

### Final Model Comparison

- **Comparison table available:** not finalized
- **Best model currently identified:** not responsibly finalized
- **Current best completed model:** logistic regression is the only fully completed model in the observed output
- **Important note:** final model ranking must wait until KNN and decision tree outputs are complete

#### Final Comparison Evidence Needed

Claude should still obtain or validate:

- final accuracy table for all three models
- best model by accuracy
- limitations of accuracy due to class imbalance
- class-level performance commentary
- model comparison interpretation

---

## Important Tables / Visuals Available

The following evidence surfaces are available or expected from prior work.

### Available From Exploratory Work

- response variable distribution
- class proportions
- histograms for selected numeric / ordinal variables:
  - `BMI`
  - `Age`
  - `MentHlth`
  - `PhysHlth`
- frequency tables for categorical predictors:
  - `HighBP`
  - `HighChol`
  - `PhysActivity`
  - `Sex`
- bar charts for selected categorical predictors
- boxplots by diabetes status:
  - `BMI ~ Diabetes_012`
  - `Age ~ Diabetes_012`
  - `GenHlth ~ Diabetes_012`
  - `MentHlth ~ Diabetes_012`
- contingency tables against diabetes status:
  - `HighBP`
  - `HighChol`
  - `PhysActivity`
  - `Sex`

### Available From Modeling Work

- logistic regression summary
- logistic regression confusion matrix
- logistic regression accuracy

### Still Needed From Modeling Work

- KNN confusion matrix
- KNN accuracy
- KNN tuning table
- decision tree confusion matrix
- decision tree accuracy
- decision tree variable importance
- final model comparison table
- saved output tables if required

---

## Errors / Warnings Encountered

The following runtime or file issues have been observed.

### Data File Issues

- early attempts to read `diabetes_012_health_indicators_BRFSS2015.csv` failed when the file was accidentally represented as a folder or unavailable
- the final successful workflow used `diabetes_012_health_indicators_BRFSS2015_PRO.csv`
- some bundles may currently include only an `.xlsx` version instead of the required `.csv`
- if the R script uses `read.csv()`, the CSV must be present or the script must be changed to use an Excel-reading package

### R Execution Issues

- one earlier execution attempted to read the wrong CSV filename
- the KNN block was interrupted after `knn()`
- later code appears to have been pasted into the console before the previous block fully completed
- the KNN tuning loop was not completed in the captured output
- decision tree and final model comparison were not completed in the captured output

### Evidence Completeness Issues

- runtime output currently available should be treated as partial
- final report conclusions should not be based only on the partial output
- final best-model claim must wait until all three models are completed

---

## Missing Evidence Still Needed

Before the evidence layer is complete, the following must be generated or provided.

### Required Missing Evidence

- KNN confusion matrix
- KNN accuracy
- KNN tuning table
- best K
- best KNN accuracy
- decision tree confusion matrix
- decision tree accuracy
- decision tree variable importance
- final model comparison table
- saved output files if expected by the final script

### Required Missing Files

- final CSV file matching R script expectations:
  - `diabetes_012_health_indicators_BRFSS2015_PRO.csv`
- full final R script:
  - should be provided as a `.R` file
- complete runtime output after a clean full run:
  - can replace or supplement `outputs/model_runtime_output.md`

---

## Immediate Interpretation Notes

The following notes are evidence-backed or strongly supported by observed outputs.

- The dataset is highly imbalanced toward `NoDiabetes`.
- `Prediabetes` is a very small class, around 1.8% of the data.
- Logistic regression achieved high overall accuracy at `0.8467`.
- Logistic regression did not predict any observations as `Prediabetes`.
- This suggests that overall accuracy is not sufficient by itself for judging model usefulness.
- Class imbalance is likely a major driver of model behavior.
- The final model comparison cannot be responsibly completed until KNN and decision tree outputs are finalized.
- The final report should discuss both accuracy and class-level limitations.
- Prediabetes appears likely to be the hardest class to classify.

---

## Best Next Evidence Step

The exact next evidence step is:

1. provide the full final R script as a `.R` file
2. provide the CSV file expected by the script:
   - `diabetes_012_health_indicators_BRFSS2015_PRO.csv`
3. run the script cleanly from top to bottom
4. capture the complete runtime output
5. confirm that the following are produced:
   - KNN confusion matrix
   - KNN tuning table
   - decision tree confusion matrix
   - decision tree variable importance
   - final model comparison table
   - saved output CSV files if used
6. replace the partial runtime output with a complete run output file

---

## Current Evidence Readiness Status

### Evidence Layer Status

`PARTIAL`

### Can Claude write final Results section now?

`NO`

Claude can draft the structure, but should not finalize results until the missing model outputs are complete.

### Can Claude write background/source/variables/methods now?

`YES`

These can be built from the proposal, Step 2 document, requirements digest, and planned methods.

### Can Claude build final slides now?

`PARTIAL ONLY`

Claude can scaffold slides, but should not finalize model comparison or final insights slides until all model results are complete.

### Can Claude create speaker notes now?

`PARTIAL ONLY`

Claude can create notes for background, data, and methods slides, but should wait on final results-dependent notes.

---

## Runtime Priority Surface for This Project

- **Current phase:** Evidence Generation moving into Evidence Validation
- **Current blocker:** KNN, decision tree, and final model comparison outputs are incomplete
- **Top priority:** complete the full R model run cleanly
- **Why now:** final Results, Discussion, model comparison slides, and speaker notes depend on complete evidence
- **Exact next action:** provide and run the full R script with the correct CSV file, then capture complete output
- **Do not switch to yet:** final report conclusion, final result slides, recording, or final packaging
- **What this unlocks next:** results packet, Results section, Discussion section, model comparison slide, final report, final deck, speaker notes, and submission package

---

## Completion Condition

This file is complete when it gives Claude enough runtime evidence state to know:

- what data was used
- what script was used or must be provided
- what outputs already exist
- what outputs are still missing
- what issues were encountered
- what interpretation is already safe
- what conclusions must wait
- what the next evidence step is

---