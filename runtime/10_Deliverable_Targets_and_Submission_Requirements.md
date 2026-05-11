# 10_Deliverable_Targets_and_Submission_Requirements
## Based on `project_guideline.pdf`
### Claude Runtime Requirements Digest

---

## Purpose

This file preserves the project requirements in markdown form based on `project_guideline.pdf` so Claude can reliably use them during execution even if direct PDF access is unavailable.

It exists to define:

- what the project requires
- what intermediate checkpoints matter
- what final deliverables must be produced
- what the presentation/report/code/data expectations are
- what should be treated as must-have versus support material

This file is a requirements digest derived from the project guideline source.

---

## Source Authority

- **Primary source:** `project_guideline.pdf`

If the original PDF is available, it should remain the highest-authority requirements source.

If the original PDF is unavailable, this markdown file should be treated as the operative requirements reference for Claude execution.

---

## Project Type

This is a multi-stage analytics project that requires:

- a project proposal
- a checkpoint / meeting stage with preliminary analysis
- at least three methods learned in class
- a final report
- a final presentation
- supporting technical files
- a final submission package

---

## Core Method Requirement

The project must use **at least three methods learned in class**.

For this project, the chosen methods are:

1. multinomial logistic regression
2. K-nearest neighbors (KNN)
3. decision tree

These should be treated as the minimum required analytical methods for the final execution path.

---

## Step 1 Requirement — Proposal

A project proposal is required.

The proposal should establish the planned project direction and include the project’s basic framing, such as:

- title
- data source
- response variable
- methods
- variables
- why the project matters
- AI disclosure if required by the course

The proposal acts as the first formal project-definition artifact.

---

## Step 2 Requirement — Preliminary Analysis / Meeting

A checkpoint meeting or Zoom discussion is required for the second stage of the project.

This stage requires evidence that the project has moved beyond proposal framing into actual preliminary analysis.

### Step 2 should include

#### Variable understanding
- response variable
- predictor variables
- variable types

#### Exploratory analysis
Examples include:
- histograms for continuous variables
- frequency tables / bar charts for categorical variables
- analysis of relationships between the response variable and selected predictors

#### Method planning
The project should identify at least three methods that will be used in the final analysis.

This stage is intended to demonstrate readiness for full model execution and final report/presentation development.

---

## Final Presentation Requirement

A final presentation is required.

### Presentation length
- approximately **10 to 12 minutes**

### Presentation should include
- background and interpretation of the data
- summary statistics
- why the analysis matters
- variables that are important or useful
- analysis / model results
- practical interpretation of the findings

The presentation should communicate the project clearly enough for an audience to understand:

- the problem
- the data
- the methods
- the results
- the main takeaway

---

## Final Report Requirement

A final report is required.

### Report should show
- all major project work
- what models or methods were considered
- the model-building or analysis process
- the results
- interpretation of the results

### Recommended report structure
1. title
2. introduction
3. data source and description
4. variables and response variable
5. summary statistics
6. preliminary analysis
7. methods
8. results
9. discussion / practical value
10. conclusion
11. AI disclosure if required

The report is the master narrative artifact that should later feed the slide deck.

---

## Final Code Requirement

The final submission must include the **R code** used in the project.

### Code expectation
The code should be sufficiently clear and complete so that others can understand and reasonably replicate the analysis.

That means the submitted code should ideally be:

- complete
- readable
- consistently named
- aligned with the actual submitted data file(s)
- free of obvious broken fragments

---

## Final Data File Requirement

The final submission must include the **data file** used for the project.

### Data expectation
This is typically a **CSV file**.

For this project, the submitted data file should be the actual diabetes dataset used in the analysis.

---

## Final Recording Requirement

The final submission must include a **recording link** for the presentation.

This means the project requires both:

- the presentation file itself
- a recorded spoken delivery of that presentation

---

## Final Submission Package

The final submission package must include:

1. **PowerPoint / presentation file**
2. **recording link**
3. **R code**
4. **data file**
5. **report**

These are the core final deliverables Claude should protect throughout execution.

---

## Summary Statistics Requirement

The presentation expectations include **basic summary statistics**.

To satisfy this safely, the project should include at least a small descriptive statistics component for key variables.

Examples may include:
- mean
- median
- variance
- standard deviation
- minimum / maximum where useful

For this project, likely key variables include:
- BMI
- Age
- MentHlth
- PhysHlth

These may appear in:
- the report
- the presentation
- or both

---

## Practical Completion Standard

For this project to count as operationally complete, the following should exist.

### Analytical layer
- all three required methods represented
- model comparison logic exists
- results are evidence-based

### Writing layer
- report completed
- Results section completed
- Discussion section completed
- Conclusion completed

### Presentation layer
- slide deck completed
- results slide(s) included
- conclusion slide included
- speaking support prepared if needed

### Technical layer
- final R script included
- final CSV included
- filenames consistent

### Submission layer
- presentation file
- recording link
- R code
- data file
- report

---

## Requirement Hierarchy

### Must-Have
- at least three methods used
- proposal completed
- Step 2 preliminary analysis completed
- final report
- final presentation
- final recording link
- final R code
- final data file

### Should-Have
- summary statistics section
- clear interpretation of model performance
- discussion of important predictors
- consistent visuals supporting the findings

### Nice-to-Have
- additional visual polish
- appendix materials
- extra tables beyond what is required
- enhanced styling beyond baseline clarity

---

## Claude Execution Notes

Claude should treat the following as requirement-critical:

- method count
- final deliverable package
- report existence
- presentation existence
- recording link existence
- R code inclusion
- data file inclusion
- summary statistics presence
- results interpretation

Claude should not let optional polish displace these.

---

## Completion Condition

This file is complete when Claude can use it to determine:

- what the project requires
- what stages matter
- what final deliverables are mandatory
- what analytical expectations exist
- what must be protected under deadline pressure

---