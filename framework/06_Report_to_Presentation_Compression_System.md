# Report to Presentation Compression System
## Governed Instructional Execution Framework
### File 06 of 08

---

## Purpose

This file defines the transformation system that converts validated work across the final communication layers.

It exists to govern the compression path from:

- evidence
- to report
- to slide deck
- to speaker notes

This file prevents duplicated effort, narrative drift, and presentation inconsistency.

If the artifact contracts define what gets produced, this file defines how those artifacts are transformed into each other without losing truth or usability.

---

## Core Compression Rule

Claude must not treat the report, presentation, and speaking script as separate inventions.

Claude must treat them as staged compressions of the same validated core.

The compression chain is:

1. evidence -> report
2. report -> slide deck
3. slide deck -> speaker notes

Every later layer must inherit from the validated layer before it.

---

## Compression Philosophy

The purpose of compression is not to remove meaning.

The purpose of compression is to preserve the highest-value meaning while reducing surface complexity for the next medium.

Each layer changes the form of communication, not the truth of the work.

### Compression by layer

#### Evidence
Rawest validated layer.

#### Report
Full narrative layer.

#### Slide deck
Compressed visual signal layer.

#### Speaker notes
Spoken guidance layer.

---

## Stage 1 — Evidence to Report

### Purpose

Turn validated outputs into coherent written explanation.

### Inputs

- validated evidence packet
- selected outputs
- selected visuals
- requirement map
- relevant background sections
- methods used
- known limitations

### Outputs

- results section
- discussion section
- conclusion
- integrated report draft

### Governing Rule

The report must explain what happened, what it means, and why it matters, while staying faithful to the evidence packet.

### Required Transformations

Claude must transform:

#### Raw outputs -> reported findings
Examples:
- accuracy values become written performance summary
- confusion matrices become class-performance explanation
- variable importance becomes predictor interpretation
- summary statistics become descriptive framing

#### Findings -> interpretation
Examples:
- class imbalance effects
- hardest-to-predict class
- strongest predictor relationships
- whether findings matched exploratory analysis

#### Interpretation -> practical implications
Examples:
- decision-making relevance
- business value
- healthcare value
- user-facing meaning
- limitations

### Report-Level Compression Rules

Claude must:

- preserve all core findings
- include enough detail to stand alone
- separate results from discussion
- use evidence-supported language
- preserve numerical accuracy

Claude must not:

- dump raw outputs without interpretation
- overcompress findings into shallow bullets
- introduce claims not present in evidence
- make the report depend on the slide deck

### Evidence-to-Report Checklist

Claude must ensure:

- every major result is represented
- the strongest visuals are referenced where appropriate
- the report narrative can later be compressed
- conclusion is supported by the report body

---

## Stage 2 — Report to Slide Deck

### Purpose

Convert the report into concise visual communication.

### Inputs

- final or near-final report draft
- must-show visuals
- model comparison outputs
- selected summary statistics
- required presentation duration
- style constraints

### Outputs

- final slide deck structure
- selected slide visuals
- compressed slide text
- slide-level logic

### Governing Rule

Slides are not miniature report pages.

Slides are visual carriers of the report’s highest-value signal.

### Core Compression Principle

Each slide must answer:

- What is the one main idea?
- What evidence supports it?
- What should the audience remember?

### Slide Compression Rules

Claude must:

- reduce paragraph logic into headline logic
- preserve only the strongest supporting bullets
- choose visuals that communicate quickly
- maintain the report’s narrative order
- prioritize readability

Claude must not:

- paste report paragraphs into slides
- overload slides with multiple competing points
- include every chart from the report
- create new conclusions outside the report

---

## Slide Role System

The default high-function slide roles are:

### 1. Title
Defines the project and context.

### 2. Why this matters
Explains significance.

### 3. Dataset / source overview
Shows what data or source material powers the work.

### 4. Response variable and predictors
Defines what is being modeled or analyzed.

### 5. Summary statistics / exploratory findings
Shows what stood out early.

### 6. Methods
Shows what was used.

### 7. Model comparison / core results
Shows which method or result performed best.

### 8. Key insights / important predictors
Shows what mattered most.

### 9. Practical value / business value
Shows why the audience should care.

### 10. Conclusion
Ends the story with clarity.

Claude may adapt this structure, but must preserve comparable communicative function.

---

## Must-Show Slide Logic

The slide deck must prioritize only the most meaningful evidence surfaces.

### Must-show visual candidates include:

- response variable distribution
- strongest exploratory chart(s)
- model comparison table
- decision tree visual or variable-importance summary
- one summary statistics element if required

### Report-only visual candidates include:

- secondary charts
- extra contingency tables
- detailed coefficient outputs
- extra confusion matrices if too dense for slides

### Archive-only visual candidates include:

- troubleshooting visuals
- redundant charts
- exploratory artifacts with low presentation value
- intermediary output screens

Claude must actively decide which layer each visual belongs to.

---

## Slide Compression Example Patterns

### Report sentence
“The dataset is highly imbalanced, with 84.24% of observations in the NoDiabetes class, 1.83% in Prediabetes, and 13.93% in Diabetes.”

### Slide version
**Strong class imbalance**
- NoDiabetes: 84.24%
- Prediabetes: 1.83%
- Diabetes: 13.93%

---

### Report sentence
“The multinomial logistic regression model achieved the highest overall accuracy, but it failed to classify any observations as Prediabetes, suggesting that class imbalance made the middle class especially difficult to detect.”

### Slide version
**Best overall accuracy, weak middle-class detection**
- Logistic regression: highest accuracy
- Prediabetes: not classified
- Class imbalance likely drove this weakness

---

## Slide-Level Content Contracts

Each slide should contain no more than:

- one main title
- one main idea
- two to four supporting bullets
- one meaningful visual or one compact table where relevant

This is the default rule.

Exceptions should be rare and justified.

---

## Stage 3 — Slide Deck to Speaker Notes

### Purpose

Convert visual presentation into speakable delivery.

### Inputs

- final slide deck
- final report conclusion
- user speaking style
- presentation time window

### Outputs

- guided slide-by-slide notes
- opening flow
- transition flow
- conclusion wording

### Governing Rule

Speaker notes are not a script transcript of the report.

They are a human-usable verbal path through the slide deck.

### Per-Slide Note Structure

Each slide’s notes should contain:

1. opening sentence
2. support sentences
3. transition sentence

### Speaking Compression Rules

Claude must:

- speak from the slide, not from the report
- preserve the slide’s main idea
- add just enough support to explain the slide
- make transitions natural
- keep the overall script within time

Claude must not:

- read the slide word-for-word
- import dense report prose directly into notes
- introduce unsupported claims
- allow notes to become longer than the report section they came from

---

## Compression Integrity Doctrine

Compression must never change the meaning of the work.

Claude must preserve:

- numerical truth
- model ranking truth
- evidence hierarchy
- predictor interpretation
- practical conclusion

Claude must not allow compression to create:

- stronger certainty than the report supports
- missing caveats that materially alter interpretation
- ranking confusion
- conclusion drift
- missing limitation context where necessary

---

## Compression Quality Hierarchy

When compressing, Claude must preserve quality in this order:

### 1. Truth preservation
The compressed layer must remain correct.

### 2. Main-idea preservation
The highest-value point from the prior layer must remain clear.

### 3. Usability preservation
The compressed layer must fit the medium.

### 4. Elegance preservation
Refinement comes after correctness and usability.

---

## Compression by Deliverable Type

### For academic projects
Compression should preserve:
- methods
- results
- interpretation
- why it matters

### For business reports
Compression should preserve:
- problem
- findings
- decision relevance
- value

### For technical writeups
Compression should preserve:
- setup
- result
- mechanism
- implication

### For mixed analytics presentations
Compression should preserve:
- question
- data
- methods
- comparison
- recommendation

---

## Narrative Drift Prevention

Narrative drift occurs when:

- the report says one thing
- the slides imply another
- the speaker notes say something else

This file exists to prevent that.

### Drift prevention rules

Claude must ensure:

- best model remains the same across layers
- hardest class to predict remains the same across layers
- strongest predictors remain the same across layers
- practical value remains aligned with actual findings
- conclusion language remains consistent across all layers

---

## Compression Validation Questions

Before approving any compressed layer, Claude must ask:

1. What is the one main point of this prior layer?
2. Has that point been preserved in the new layer?
3. Has any important truth been lost?
4. Has any unsupported certainty been added?
5. Is this new layer more usable for its medium?
6. Could a human move from this layer to the next without re-inventing the story?

If not, compression is incomplete.

---

## Report-to-Presentation Workflow Contract

The required workflow is:

### Step 1
Finish the report-level narrative.

### Step 2
Select must-show evidence surfaces.

### Step 3
Create slide roles and titles.

### Step 4
Compress each report section into slide logic.

### Step 5
Insert only the strongest visuals.

### Step 6
Create speaker notes from the final slide deck.

Claude must not reverse this order unless operating in emergency mode.

---

## Emergency Compression Mode

If time is short, Claude may use compressed emergency conversion.

### Emergency sequence

1. evidence packet
2. results section
3. discussion section
4. report shell completion
5. quick deck compression
6. speaker notes shell

### Emergency compression rules

Claude may reduce:
- polish
- extra examples
- secondary visuals
- decorative transitions

Claude must still preserve:
- evidence truth
- required sections
- best model/result logic
- final conclusion consistency

---

## Canonical Compression Artifacts

This system expects the following artifacts to exist in order:

1. Results Packet
2. Report Shell
3. Final Report Draft
4. Slide Shell
5. Final Slide Deck
6. Speaker Notes Shell
7. Final Speaker Notes

Claude must use these artifacts as transformation checkpoints.

---

## Completion Condition

This file is complete when the framework has:

- defined the evidence-to-report transformation
- defined the report-to-slide compression system
- defined the slide-to-speaker-note transformation
- defined must-show visual logic
- defined compression integrity rules
- defined drift prevention logic
- defined emergency compression behavior

---

## Next File To Print

The next relevant markdown file is:

`07_Emergency_Execution_Mode_and_Timeboxed_Workflows.md`

---