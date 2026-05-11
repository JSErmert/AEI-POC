# Artifact Templates and Output Contracts
## Governed Instructional Execution Framework
### File 05 of 08

---

## Purpose

This file defines the reusable artifact templates and output contracts used throughout the framework.

It exists to ensure that Claude does not merely give advice, but produces governed, reusable artifacts that can support downstream execution.

This file standardizes:

- artifact names
- artifact roles
- minimum required fields
- output completeness rules
- downstream handoff expectations

If the validation doctrine defines how quality is judged, this file defines the standardized forms that quality is judged on.

---

## Core Artifact Rule

Claude must prefer producing named, reusable artifacts over diffuse explanation.

A valid framework artifact must be:

- self-contained enough to reuse
- structurally stable
- clearly labeled
- appropriate to its phase
- sufficient to support the next phase

Artifacts are not just outputs.

They are governed handoff objects.

---

## Artifact Classes

The framework uses **8 canonical artifact classes**:

1. Intake Artifact
2. Requirement Map
3. Execution Plan
4. Results Packet
5. Report Shell
6. Slide Shell
7. Speaker Notes Shell
8. Submission Checklist

Each has its own contract.

---

## Universal Output Contract

Every artifact produced under this framework must satisfy the following universal contract.

### Required Properties

Every artifact must have:

- a clear name
- a defined purpose
- a known phase
- enough internal structure to reuse
- obvious downstream role
- no major hidden dependencies on external explanation

### Completion Standard

An artifact is complete only if:

- it can be handed forward to the next phase
- it does not require the user to reconstruct its meaning
- it contains its essential fields
- it is stable enough to prevent unnecessary rework

### Failure Standard

An artifact fails if:

- it is only conversational advice
- it lacks structure
- it cannot support the next phase
- it hides critical information outside itself
- it is too incomplete to be reusable

---

## Artifact 1 — Intake Artifact

### Purpose

Capture the user’s current situation in a usable operational form.

### Phase

Phase 1 — Intake

### Output Contract

The Intake Artifact must contain:

1. Working task definition
2. Required deliverables currently known
3. Source materials currently available
4. Missing materials
5. Time/deadline conditions
6. Technical constraints
7. User concerns or priorities
8. Immediate ambiguity notes

### Template

#### Intake Artifact
- **Task:**  
- **Known deliverables:**  
- **Available materials:**  
- **Missing materials:**  
- **Deadline / time pressure:**  
- **Technical constraints:**  
- **User priorities / concerns:**  
- **Open ambiguities:**  

### Downstream Role

Feeds:
- Requirement Map
- Execution Plan

### Failure Conditions

Fails if:
- the task is still vague
- deliverables are not identified
- source materials are not inventoried
- timing pressure is not surfaced

---

## Artifact 2 — Requirement Map

### Purpose

Translate the task into explicit execution obligations.

### Phase

Phase 2 — Requirement Extraction

### Output Contract

The Requirement Map must contain:

1. Must-have requirements
2. Should-have support elements
3. Nice-to-have items
4. Required files
5. Required methods
6. Required sections
7. Required output forms
8. Notes on grading-sensitive or high-risk elements

### Template

#### Requirement Map

##### Must-Have
-  
-  
-  

##### Should-Have
-  
-  
-  

##### Nice-to-Have
-  
-  
-  

##### Required Files
-  
-  

##### Required Methods / Techniques
-  
-  

##### Required Sections / Components
-  
-  

##### Notes
-  
-  

### Downstream Role

Feeds:
- Execution Plan
- Validation Priorities
- Packaging Decisions

### Failure Conditions

Fails if:
- required items are still mixed with optional polish
- must-have deliverables are omitted
- method requirements remain unclear
- file obligations are not surfaced

---

## Artifact 3 — Execution Plan

### Purpose

Create the operational path from the current state to completion.

### Phase

Phase 3 — Execution Mapping

### Output Contract

The Execution Plan must contain:

1. Critical path
2. Safe parallel work
3. Unsafe premature work
4. Immediate next step
5. Sequenced task list
6. Time estimate
7. Cut order under pressure
8. Completion checkpoints

### Template

#### Execution Plan

##### Critical Path
1.  
2.  
3.  

##### Safe Parallel Work
-  
-  
-  

##### Unsafe Premature Work
-  
-  
-  

##### Immediate Next Step
-  

##### Sequenced Task List
1.  
2.  
3.  
4.  

##### Time Estimate
- **Aggressive target:**  
- **Realistic target:**  
- **Buffer target:**  

##### Cut Order if Time Tightens
1.  
2.  
3.  

##### Completion Checkpoints
-  
-  
-  

### Downstream Role

Feeds:
- live execution
- timeboxing
- emergency mode decisions

### Failure Conditions

Fails if:
- there is no clear critical path
- sequence and parallel work are confused
- no next step is identified
- the plan is motivational rather than operational

---

## Artifact 4 — Results Packet

### Purpose

Capture the actual evidence surfaces that later writing and presentation will inherit from.

### Phase

Phase 4 / 5 — Evidence Generation and Validation

### Output Contract

The Results Packet must contain:

1. Core outputs
2. Key numerical findings
3. Selected must-show visuals
4. Report-only supporting outputs
5. Archive-only outputs if relevant
6. Initial interpretation bullets
7. Best-model or best-result identification if relevant
8. Known limitations or anomalies

### Template

#### Results Packet

##### Core Outputs
-  
-  
-  

##### Key Numerical Findings
-  
-  
-  

##### Must-Show Visuals
-  
-  
-  

##### Report-Only Supporting Outputs
-  
-  

##### Archive-Only Outputs
-  
-  

##### Initial Interpretation Bullets
-  
-  
-  

##### Best Result / Best Model
-  

##### Known Limitations / Anomalies
-  
-  

### Downstream Role

Feeds:
- Results section
- Discussion section
- model comparison slide
- conclusion
- speaking notes

### Failure Conditions

Fails if:
- outputs are still scattered
- no hierarchy of evidence exists
- no must-show materials are identified
- the user would still need to dig through raw output to understand the story

---

## Artifact 5 — Report Shell

### Purpose

Create the full narrative structure before or during report assembly.

### Phase

Phase 6 — Narrative Assembly

### Output Contract

The Report Shell must contain all required report headings and placeholders for results-dependent sections.

### Default Structure Contract

1. Title
2. Introduction
3. Data Source and Description
4. Variables and Response Variable
5. Summary Statistics
6. Preliminary Analysis
7. Methods
8. Results
9. Discussion / Business Value
10. Conclusion
11. Disclosure if required

### Template

#### Report Shell

##### Title
-  

##### Introduction
-  

##### Data Source and Description
-  

##### Variables and Response Variable
-  

##### Summary Statistics
-  

##### Preliminary Analysis
-  

##### Methods
-  

##### Results
-  

##### Discussion / Business Value
-  

##### Conclusion
-  

##### Disclosure
-  

### Downstream Role

Feeds:
- final report draft
- slide shell
- script logic

### Failure Conditions

Fails if:
- required report sections are missing
- results-dependent sections are absent rather than placeholder-ready
- report cannot accept later evidence cleanly

---

## Artifact 6 — Slide Shell

### Purpose

Create the presentation structure before final compression and insertion of result-specific content.

### Phase

Phase 7 — Visual Compression

### Output Contract

The Slide Shell must contain:

1. slide order
2. slide titles
3. purpose of each slide
4. expected evidence for each slide
5. placeholder slots for result-dependent slides

### Template

#### Slide Shell

##### Slide 1 — Title
- **Purpose:**  
- **Content:**  

##### Slide 2 — Why This Matters
- **Purpose:**  
- **Content:**  

##### Slide 3 — Dataset / Source Overview
- **Purpose:**  
- **Content:**  

##### Slide 4 — Response Variable and Predictors
- **Purpose:**  
- **Content:**  

##### Slide 5 — Summary Statistics / Preliminary Findings
- **Purpose:**  
- **Content:**  

##### Slide 6 — Methods
- **Purpose:**  
- **Content:**  

##### Slide 7 — Model Comparison / Core Results
- **Purpose:**  
- **Content:**  

##### Slide 8 — Key Insights / Important Predictors
- **Purpose:**  
- **Content:**  

##### Slide 9 — Practical Value / Business Value
- **Purpose:**  
- **Content:**  

##### Slide 10 — Conclusion
- **Purpose:**  
- **Content:**  

### Downstream Role

Feeds:
- final slide deck
- speaker notes

### Failure Conditions

Fails if:
- slide sequence is absent
- slides have no assigned role
- result-dependent slides are ignored
- the deck would still need to be invented from scratch

---

## Artifact 7 — Speaker Notes Shell

### Purpose

Create the delivery scaffold for spoken presentation.

### Phase

Phase 8 — Delivery Scripting

### Output Contract

The Speaker Notes Shell must map directly to the final slide order.

For each slide it must contain:

1. opening sentence
2. support points
3. transition line

### Template

#### Speaker Notes Shell

##### Slide 1
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 2
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 3
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 4
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 5
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 6
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 7
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 8
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 9
- **Opening:**  
- **Support:**  
- **Transition:**  

##### Slide 10
- **Opening:**  
- **Support:**  
- **Transition:**  

### Downstream Role

Feeds:
- actual presentation delivery
- rehearsal
- recording

### Failure Conditions

Fails if:
- it does not match the final slide order
- it is too dense to speak
- it introduces new unsupported claims
- it does not create flow between slides

---

## Artifact 8 — Submission Checklist

### Purpose

Ensure the final package is complete and submission-safe.

### Phase

Phase 10 — Final Packaging

### Output Contract

The Submission Checklist must contain:

1. required deliverable list
2. file confirmation status
3. naming consistency check
4. final review actions
5. submission-ready confirmation

### Template

#### Submission Checklist

##### Required Deliverables
- [ ] Report
- [ ] Slide deck
- [ ] Code file
- [ ] Data file
- [ ] Recording link
- [ ] Any additional required item

##### File Names Confirmed
- [ ] Report filename correct
- [ ] Slide deck filename correct
- [ ] Code filename correct
- [ ] Data filename correct

##### Internal Consistency Checks
- [ ] Numbers consistent across files
- [ ] Final conclusions consistent across files
- [ ] Referenced files match included files
- [ ] Latest versions only

##### Final Review Actions
- [ ] Open report once
- [ ] Open deck once
- [ ] Open code file once
- [ ] Open data file once
- [ ] Open recording link once

##### Submission Ready
- [ ] Yes
- [ ] No

### Downstream Role

Feeds:
- final submission confidence
- readiness declaration

### Failure Conditions

Fails if:
- required items are not explicitly checked
- package integrity is assumed rather than confirmed
- outdated or mismatched files remain possible

---

## Secondary Optional Artifact Templates

These are not mandatory in every run, but may be used when relevant.

### A. Summary Statistics Table
Used when requirements explicitly ask for descriptive statistics.

#### Template
| Variable | Mean | Median | Std. Dev. | Min | Max |
|---|---:|---:|---:|---:|---:|
|  |  |  |  |  |  |

---

### B. Must-Show Visual List
Used to select visual surfaces before report/deck insertion.

#### Template
#### Must-Show Visual List
1.  
2.  
3.  

#### Report-Only Visuals
1.  
2.  

#### Excluded / Archive Visuals
1.  
2.  

---

### C. Model Comparison Table
Used when multiple methods are compared.

#### Template
| Model | Key Metric | Notes |
|---|---:|---|
|  |  |  |
|  |  |  |
|  |  |  |

---

## Output Contract Doctrine

Claude must follow these rules when producing framework artifacts.

### Rule 1 — Name the artifact
Every artifact must be explicitly named.

### Rule 2 — Preserve field logic
Claude must not remove the essential fields that make the artifact reusable.

### Rule 3 — Fit the phase
The artifact must reflect its phase role and not prematurely absorb later-stage interpretation unless in emergency mode.

### Rule 4 — Reuse forward
Artifacts should be written so they can be directly reused in the next stage.

### Rule 5 — Avoid overgrowth
Artifacts should be complete enough to use, but not bloated past their role.

---

## Artifact Handoff Logic

The canonical handoff chain is:

1. Intake Artifact  
2. Requirement Map  
3. Execution Plan  
4. Results Packet  
5. Report Shell -> Report Draft  
6. Slide Shell -> Final Deck  
7. Speaker Notes Shell -> Final Notes  
8. Submission Checklist  

Claude must treat this as a governed handoff chain rather than isolated output generation.

---

## Completion Condition

This file is complete when the framework has:

- defined the canonical artifact set
- defined the output contract for each artifact
- defined the minimum template for each artifact
- defined artifact failure conditions
- defined the handoff logic between artifacts

---

## Next File To Print

The next relevant markdown file is:

`06_Report_to_Presentation_Compression_System.md`

---