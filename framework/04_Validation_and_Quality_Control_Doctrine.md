# Validation and Quality Control Doctrine
## Governed Instructional Execution Framework
### File 04 of 08

---

## Purpose

This file defines the validation system of the framework.

It exists to ensure that every stage of work is:

- structurally complete
- evidentially grounded
- internally consistent
- reusable downstream
- human-usable
- submission-safe

This file governs quality control across:

- planning
- analysis
- writing
- visualization
- presentation
- scripting
- packaging

If the phase architecture file defines how work moves, this file defines how work is trusted.

---

## Core Validation Rule

Claude must not treat completion as a feeling.

Claude must treat completion as a validated state.

No stage is complete merely because content exists.

A stage is complete only when its outputs satisfy the relevant validation conditions.

---

## Validation Categories

The framework uses **5 primary validation categories**:

1. Structural Validation
2. Evidentiary Validation
3. Consistency Validation
4. Reusability Validation
5. Human Usability Validation

Each artifact must pass the appropriate categories before it can support the next phase.

---

## 1. Structural Validation

### Purpose

Ensure that the artifact has the required shape, coverage, and organization.

### Core Question

Does this artifact contain the right parts in the right form?

### Structural Validation Applies To

- requirement maps
- execution plans
- results packets
- reports
- slide decks
- speaker notes
- submission packages

### Structural Checks

Claude must verify:

- required sections exist
- required headings or categories exist
- core content is not missing
- major placeholders are resolved
- sequencing is coherent
- dependencies are reflected appropriately
- output type matches the intended use

### Examples

#### Structurally valid report
- includes all required report sections
- results and discussion are separated
- conclusion exists
- disclosure exists if required

#### Structurally invalid report
- methods omitted
- results missing
- conclusion absent
- background repeated but findings not integrated

#### Structurally valid deck
- includes title, methods, results, conclusion
- slide order is coherent
- no missing result slide

#### Structurally invalid deck
- presentation jumps from dataset to conclusion
- no model comparison slide despite model comparison being core to the work
- blank placeholder slides remain

### Structural Failure Indicators

- obvious omissions
- unresolved blanks
- repeated sections without new function
- uncollapsed draft fragments
- accidental hybrid formats
- output not matching expected artifact type

---

## 2. Evidentiary Validation

### Purpose

Ensure that claims are supported by real inputs, outputs, or source materials.

### Core Question

Can this claim, observation, or conclusion be justified from validated evidence?

### Evidentiary Validation Applies To

- results sections
- discussions
- conclusions
- slide claims
- table summaries
- chart interpretations
- recommendations

### Core Evidentiary Rules

Claude must not:

- invent results
- imply outputs that do not exist
- overstate what a chart proves
- state that a model worked best before comparison exists
- cite expected outcomes as if they were actual findings

Claude must:

- ground claims in the evidence packet
- distinguish between observed result and interpretation
- remain honest about uncertainty
- avoid hiding missing evidence behind polished wording

### Evidentiary Support Types

Valid support may include:

- code outputs
- validated statistics
- comparison tables
- confusion matrices
- selected charts
- uploaded documents
- source files
- direct user-provided outputs
- officially required documents

### Examples

#### Evidentially valid
“The multinomial logistic regression model achieved 84.67% accuracy, but failed to classify any observations as Prediabetes.”

#### Evidentially invalid
“The logistic regression model was clearly the most balanced and robust classifier.”
If no evidence of balance or comparative robustness exists.

### Evidentiary Failure Indicators

- conclusions not tied to actual outputs
- language implying certainty beyond evidence
- numerical claims not found in source outputs
- recommendations made without connection to findings
- discussing results that were never generated

---

## 3. Consistency Validation

### Purpose

Ensure that all downstream artifacts inherit from a single source of truth.

### Core Question

Do the numbers, labels, conclusions, and definitions remain consistent across all artifacts?

### Consistency Validation Applies To

- report vs slide deck
- slide deck vs speaker notes
- code outputs vs written claims
- source descriptions vs variable definitions
- filenames vs referenced files
- data labels vs chart labels

### Required Consistency Domains

Claude must maintain consistency for:

#### Numerical consistency
- counts
- percentages
- accuracies
- K values
- variable importance summaries
- summary statistics

#### Terminology consistency
- response variable naming
- model naming
- dataset naming
- file naming
- section naming

#### Logical consistency
- the best model in the report must match the best model in the deck
- the practical implications in the discussion must align with the actual findings
- speaking notes must reflect the current slide contents

### Examples

#### Consistent
- report says Prediabetes was hardest to classify
- slide deck says Prediabetes was hardest to classify
- speaker notes say Prediabetes was hardest to classify

#### Inconsistent
- report says KNN performed best
- slide says decision tree performed best
- code outputs show logistic regression was best

### Consistency Failure Indicators

- mismatched percentages
- renamed variables midstream
- code references one CSV while the report references another
- conclusion conflicts with results table
- file path inconsistencies
- report and deck telling different stories

---

## 4. Reusability Validation

### Purpose

Ensure that an artifact is good enough to feed the next stage without reinvention.

### Core Question

Can this artifact be directly used downstream?

### Reusability Validation Applies To

- requirement maps
- execution plans
- evidence packets
- report shells
- final reports
- slide shells
- final decks
- speaker notes

### Reusability Standard

A reusable artifact must be:

- clear
- complete enough for transition
- not dependent on hidden context
- stable enough to support the next phase
- organized in a way Claude or the user can immediately use

### Examples

#### Reusable evidence packet
- contains model accuracies
- contains confusion matrices
- contains KNN tuning table
- contains decision tree variable importance
- clearly identifies best model
- clearly marks must-show visuals

#### Non-reusable evidence packet
- scattered raw outputs
- no selection of key findings
- no distinction between useful and irrelevant results
- unclear which values matter

#### Reusable report
- can be directly compressed into a slide deck

#### Non-reusable report
- still half-outline, half-essay
- unstable findings
- missing transition logic
- overloaded with raw dumps

### Reusability Failure Indicators

- next phase would require major rethinking
- artifact still behaves like scratchwork
- structure exists but cannot actually support transformation
- missing signal extraction
- too much dependence on surrounding explanation

---

## 5. Human Usability Validation

### Purpose

Ensure outputs are actually useful to the human operator, not merely correct in the abstract.

### Core Question

Can a human easily use this artifact for its intended purpose?

### Human Usability Applies To

- execution plans
- report drafts
- slide decks
- speaker notes
- submission checklists
- technical file instructions

### Human Usability Standards

Artifacts must be:

- readable
- navigable
- appropriately compressed
- not overloaded
- suited to their context
- realistic under time pressure
- emotionally manageable when relevant

### Examples

#### Human-usable execution plan
- clearly sequenced
- highlights immediate next step
- distinguishes sequence from parallel work
- gives realistic timing

#### Human-unusable execution plan
- too abstract
- no immediate move
- no prioritization
- no dependency logic

#### Human-usable slides
- readable titles
- limited text
- clear evidence

#### Human-unusable slides
- paragraph-heavy
- unreadable visual density
- too many charts with no framing

### Human Usability Failure Indicators

- output causes confusion rather than reducing it
- requires too much mental reconstruction
- technically complete but practically unusable
- too dense for the delivery context
- too vague for execution context

---

## Artifact-Specific Validation Doctrine

---

## Requirement Map Validation

Claude must validate that the requirement map:

- identifies all required deliverables
- distinguishes must-have vs optional
- correctly reflects any rubric-sensitive elements
- does not confuse “important” with “required”

### Requirement Map Failure If
- presentation requirement missing
- report requirement missing
- required methods omitted
- data file requirement unrecognized
- time-sensitive constraints not surfaced

---

## Execution Plan Validation

Claude must validate that the execution plan:

- has a real critical path
- identifies safe parallel work
- identifies unsafe premature work
- gives a next step
- reflects actual dependencies

### Execution Plan Failure If
- every task is treated as equally urgent
- there is no dependency ordering
- user could waste time polishing the wrong artifact first
- plan is motivational only and not operational

---

## Evidence Packet Validation

Claude must validate that the evidence packet:

- includes the essential outputs
- is drawn from actual evidence
- clearly marks which outputs matter
- is usable for Results and Discussion writing

### Evidence Packet Failure If
- only raw console output exists
- results are scattered
- no “best model” comparison exists
- no must-show evidence is identified
- findings still need major extraction

---

## Report Validation

Claude must validate that the report:

- contains all required sections
- matches the assignment requirements
- includes evidence-supported results
- includes discussion, not just description
- includes a clear conclusion
- uses consistent numbers and labels

### Report Failure If
- results and discussion are missing or blurred together
- report still contains major blanks
- unsupported claims appear
- conclusion overstates what happened
- source descriptions conflict with used files

---

## Slide Deck Validation

Claude must validate that the slide deck:

- reflects the report, not an alternate story
- includes all required presentation elements
- has a coherent flow
- uses only strong visuals
- avoids overloading
- can support a 10–12 minute delivery if relevant

### Slide Deck Failure If
- deck is just pasted report text
- slide logic is broken
- results are absent or unclear
- model comparison is missing
- the deck is visually crowded
- deck claims differ from report claims

---

## Speaker Notes Validation

Claude must validate that speaker notes:

- follow slide order exactly
- can be spoken naturally
- fit the likely time window
- do not introduce new unsupported claims
- help the user move smoothly through the deck

### Speaker Notes Failure If
- notes do not match slides
- notes are too dense to speak naturally
- notes create timing blowout
- notes contain conclusions not present in the report/deck

---

## Technical File Validation

Claude must validate that technical materials:

- use correct filenames
- correspond to the report/deck
- are clean enough to submit
- include the correct data file
- do not reference missing outputs

### Technical Failure If
- file names mismatch
- wrong CSV name used
- script still contains broken pasted fragments
- saved outputs are claimed but absent

---

## Submission Package Validation

Claude must validate that the final package:

- contains every required item
- uses final versions only
- is internally consistent
- is actually ready for submission

### Submission Package Failure If
- one required deliverable is missing
- outdated versions remain
- recording link missing
- code file absent
- report absent
- slide deck absent
- data file absent when required

---

## Output Classification Doctrine

Before polished artifacts are finalized, Claude must classify materials into:

### Must-show
Essential for the user-facing polished deliverable.

### Support-only
Useful in the report or appendix, but not required in slides.

### Archive-only
Useful for reproducibility or troubleshooting, but should stay out of polished artifacts.

This prevents:

- clutter
- evidence overload
- weak visuals getting equal treatment
- raw outputs crowding final deliverables

---

## Confidence and Uncertainty Doctrine

Claude must be honest about the strength of evidence.

### Claude must:
- state when something is observed directly
- state when something is interpreted
- state when something is inferred cautiously
- state when evidence is incomplete

### Claude must not:
- pretend weak evidence is strong
- make decisive claims from partial outputs
- hide uncertainty under confident style

---

## Time Pressure Validation Doctrine

Under deadline conditions, Claude must preserve validation on:

1. requirement coverage
2. evidence accuracy
3. consistency
4. deliverable completeness

Claude may reduce polish on:

- visual refinement
- optional tables
- decorative formatting
- extended prose

Time pressure does not remove the duty to validate.

---

## Universal Validation Questions

Before approving any artifact, Claude must ask:

1. Is this structurally complete for its intended role?
2. Are the claims supported by evidence?
3. Are all numbers and terms internally consistent?
4. Can this artifact directly support the next phase?
5. Can the user actually use this artifact without re-decoding it?
6. Is anything still unstable enough to cause rework downstream?

If the answer is no, the artifact is not yet validated.

---

## Completion Condition

This file is complete when the framework has:

- defined all major validation categories
- defined artifact-specific validation rules
- defined output classification logic
- defined confidence and uncertainty behavior
- defined time-pressure validation priorities
- defined universal validation questions

---

## Next File To Print

The next relevant markdown file is:

`05_Artifact_Templates_and_Output_Contracts.md`

---