# Speaker Notes
## Diabetes Risk Prediction by Patient Health Indicators
### Aligned to `outputs/final_slide_deck.pptx` (10 slides, ~10–12 min target)

Notes are written to be **spoken**, not read. Each slide has:

- **Opening** — one line you say as the slide appears.
- **Support** — 2–4 short points to talk through.
- **Transition** — one line that sets up the next slide.

Pacing target: about **60–90 seconds per slide**. If you are running long, drop the parenthetical detail in each Support block first; the headlines carry the talk on their own.

---

## Slide 1 — Title

- **Opening:** "Hi, I'm Joshua Ermert. This is my MIS 401 final project: Diabetes Risk Prediction by Patient Health Indicators, using the UCI / CDC dataset."
- **Support:**
  - One sentence on the goal: predict three-class diabetes status from patient health and lifestyle indicators.
  - One sentence on personal stake: family history of Type II diabetes plus a prior summer in biopharma BI/AI analytics.
- **Transition:** "Let me start with why this question matters."

## Slide 2 — Why This Matters

- **Opening:** "Diabetes is one of the most consequential public-health conditions in the U.S. — high cost, uneven distribution, growing prevalence."
- **Support:**
  - Better identification of patient-level risk factors lets healthcare organizations screen earlier and target prevention.
  - The specific question I wanted to answer: how well can three classification methods I learned in class — logistic regression, KNN, and a decision tree — separate Diabetes, Prediabetes, and NoDiabetes patients on the same dataset?
  - And which indicators carry the most signal — does the modeling agree with what we already know clinically?
- **Transition:** "The data I used to answer that comes from the CDC, distributed through UCI."

## Slide 3 — Dataset and Response Variable

- **Opening:** "The dataset is the CDC Diabetes Health Indicators file — 253,680 observations, 21 predictors, no missing values."
- **Support:**
  - It's behavioral-survey data from the CDC's BRFSS, cleaned and distributed through UCI and Kaggle.
  - The response variable is `Diabetes_012` — three classes: NoDiabetes, Prediabetes, Diabetes.
  - The class breakdown is the single most important property of this dataset: 84.2 % NoDiabetes, 1.8 % Prediabetes, 14.0 % Diabetes.
  - That severe imbalance is going to shape every result on the next several slides, so flag it now.
- **Transition:** "Before fitting models, here are the predictors I worked with."

## Slide 4 — Variables Used

- **Opening:** "21 predictors — split between binary / categorical and continuous or ordinal."
- **Support:**
  - On the categorical side: HighBP, HighChol, smoking, stroke, heart disease, physical activity, diet markers, healthcare access, difficulty walking, sex.
  - On the continuous side: BMI, self-rated General Health, mental and physical health days, age category, education, income.
  - Note one preprocessing decision: KNN is distance-based, so I z-scored the numeric encodings using training-set parameters and applied that scaling to the test set. Logit and the tree used the factor-coded versions.
- **Transition:** "I ran a preliminary EDA before any modeling — and the patterns there matter, because they're a substantive prior for what the models should find."

## Slide 5 — Preliminary Analysis

- **Opening:** "From the Step 2 exploratory analysis, five patterns stand out."
- **Support:**
  - BMI shifts upward as you move from NoDiabetes to Diabetes — median roughly 27, then 30, then 31.
  - Age category increases with diabetes status — median age category 8, 9, 10.
  - Self-rated General Health is markedly worse in the Diabetes group.
  - High blood pressure is roughly three times more common in the Diabetes group, and high cholesterol shows the same direction at slightly smaller magnitude.
  - The strongest early signals were HighBP, GenHlth, HighChol, BMI, and Age. Hold those five in your head — they show up again in the model results.
- **Transition:** "With those EDA patterns as a backdrop, here are the three modeling methods I applied."

## Slide 6 — Methods

- **Opening:** "Same train/test split for all three models — 70/30, seed 401, 177,576 training rows, 76,104 testing rows."
- **Support:**
  - Multinomial logistic regression with `nnet::multinom`.
  - KNN with `class::knn`, tuned over k of 3, 5, 7, and 9.
  - Decision tree with `rpart`. One important note: with the default complexity parameter, the tree refused to split — because no single split could improve relative error by 1 % over the 84.2 % majority-class prior. So I tuned `rpart.control` to `cp = 0.001`, with `minsplit = 2000`, `minbucket = 1000`, `maxdepth = 5` to grow a shallow but interpretable tree. That's an honest tuning choice driven by class imbalance, not a deep optimization sweep — and I'll caveat it again in the results.
  - Evaluation: confusion matrix, overall test accuracy, plus tree variable importance.
- **Transition:** "Here's what they produced."

## Slide 7 — Model Comparison

- **Opening:** "Here are the four model variants ranked by test accuracy."
- **Support:**
  - The tuned Decision Tree edges out everyone at 0.8475.
  - Multinomial logistic regression is essentially tied at 0.8467.
  - KNN at the best K of 9 is 0.8382.
  - KNN at k = 5 is 0.8301.
  - Important framing — and this is the most important sentence of the presentation: all four variants are within about two points of each other, and within half a point of the 84.2 % majority-class baseline. Accuracy alone is a misleading metric on this dataset.
  - Which is why the next two slides go beyond accuracy.
- **Transition:** "Let's look at the structure of the tree, because that's where the substantive payoff is."

## Slide 8 — Decision Tree Structure

- **Opening:** "Even though the tree is tuned for shallowness, the structure tells a clean clinical story."
- **Support:**
  - Walk left to right: the root split is HighBP. If HighBP equals 0, the model lands in a large NoDiabetes leaf with about 101,000 patients and only a 6 % Diabetes rate.
  - On the HighBP-equals-1 side, the next split is GenHlth. Patients with self-rated General Health worse than 4 — meaning fair or poor — are split further.
  - The tree only ever predicts Diabetes in one leaf, on the far right: HighBP equals 1 AND GenHlth at least 4 AND BMI at least 28 AND HighChol equals 1 AND BMI at least 35. About 3,961 patients fall there, with roughly a 60 % Diabetes rate.
  - One leaf predicts Diabetes. Zero leaves predict Prediabetes. That's the imbalance story showing up in the structure.
- **Transition:** "The variable importance from this tree backs up the EDA — and turns into the practical takeaway."

## Slide 9 — Variable Importance and Key Insights

- **Opening:** "Decision-tree variable importance, in order: HighBP, GenHlth, HighChol, DiffWalk, Age, PhysHlth, BMI."
- **Support:**
  - That ordering aligns directly with the Step 2 EDA: BMI, Age, GenHlth, HighBP, HighChol — the same five variables, plus difficulty walking and physical health days. It also lines up with the established Type II diabetes risk-factor literature.
  - But here's the per-class story behind the headline accuracy: all models predict NoDiabetes for about 98 % of test rows. The Decision Tree catches only 9 % of true Diabetes cases. Logistic regression catches about 17 %. KNN at k = 5 catches about 22 %, but it's the only model that ever predicts Prediabetes — 88 such predictions, only 2 of them correct.
  - So the headline ranking can be misleading: the Decision Tree wins on accuracy by trading sensitivity for precision. Logistic regression is probably the most balanced single deployable model.
- **Transition:** "What does that mean in practical terms for a healthcare organization?"

## Slide 10 — Practical Value and Conclusion

- **Opening:** "Even at modest sensitivity, the tree is useful in two specific operational ways."
- **Support:**
  - First, the rule-out branch: about 101,000 patients with HighBP equals 0 only have a 6 % Diabetes rate. That's a clean signal to safely deprioritize from intensive screening.
  - Second, the high-risk leaf: the small group with BMI at least 35, high cholesterol, poor general health, and high blood pressure has a 60 % Diabetes rate. That's about five times the population base rate. It's a tractable population for targeted intervention.
  - Honest framing: overall accuracy is barely above the baseline. Class imbalance dominates everything. The clearest path to better results isn't a fancier algorithm — it's class weights, oversampling, or a cost-sensitive decision threshold.
  - And for AI disclosure: generative AI helped organize and polish the structural skeleton. The dataset selection, methodology, modeling decisions, and analytical interpretations are mine, supported by the actual R outputs.
- **Closing line:** "Thanks — happy to take questions."

---

## Recording / delivery checklist

- [ ] Open `final_slide_deck.pptx` in PowerPoint and run the slideshow once with these notes on a second screen.
- [ ] Time a full pass aloud — target 10–12 minutes, hard ceiling 13.
- [ ] If over 13 min: drop the parenthetical detail under each Support block first; do not cut the headline numbers.
- [ ] Confirm the decision-tree image renders crisply on the projected display (it's 1400 × 900 px — should scale fine).
- [ ] Record using PowerPoint's built-in record feature OR Zoom local recording with screen share.
- [ ] Save the recording, copy the share link, and add it to `submission_checklist.md`.
