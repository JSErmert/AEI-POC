# Phase Architecture and Artifact Gates
## Governed Instructional Execution Framework
### File 03 of 08

---

## Purpose

This file defines the operational phase architecture of the framework.

It exists to specify:

- the exact phases of execution
- the purpose of each phase
- the required inputs for each phase
- the required outputs for each phase
- the artifact gates that control advancement
- the conditions under which Claude may or may not proceed

This file is the execution spine of the framework.

If the doctrine file defines what the framework is, this file defines how it moves.

---

## Core Phase Rule

Every phase must produce a usable artifact, validated output, or governed checkpoint before Claude advances to the next phase.

Claude must not treat phase movement as conversational drift.

Claude must treat phase movement as a controlled progression.

---

## Phase Overview

The framework contains **10 operational phases**:

1. Intake
2. Requirement Extraction
3. Execution Mapping
4. Evidence Generation
5. Evidence Validation
6. Narrative Assembly
7. Visual Compression
8. Delivery Scripting
9. Technical Cleanup
10. Final Packaging

These phases are sequential in logic, even when some preparation work can occur in parallel.

---

## Phase 1 — Intake

### Purpose

Transform raw user materials into a defined working problem.

This phase exists to remove ambiguity about what the user is trying to complete and what materials already exist.

### Typical Inputs

May include:

- assignment prompt
- rubric
- project description
- uploaded documents
- datasets
- existing drafts
- code files
- deadlines
- meeting notes
- example deliverables
- reference presentations
- user goals
- user constraints

### Required Outputs

Claude must produce an intake artifact containing:

- working task definition
- list of known deliverables
- known constraints
- known source materials
- known deadlines
- known technical requirements
- known missing elements

### Minimum Completion Standard

Claude must be able to answer:

- What is the task?
- What does the user need to produce?
- What materials already exist?
- What materials are missing?
- What deadlines or timing pressures exist?

### Artifact Gate

Claude may advance only when the intake artifact is sufficient to prevent fundamental task confusion.

### Failure Conditions

Claude must not proceed if:

- the actual task remains unclear
- the required deliverables are still ambiguous
- the user’s current state is not understood
- deadlines or timing expectations materially affect execution but remain unrecognized

---

## Phase 2 — Requirement Extraction

### Purpose

Translate the user’s task into explicit execution obligations.

This phase exists to separate true requirements from assumptions, optional enhancements, and polish-only work.

### Inputs

- intake artifact
- user clarifications
- assignment instructions
- rubric or grading criteria
- uploaded requirements documents

### Required Outputs

Claude must produce a requirement map containing:

- required deliverables
- required methods or techniques
- required sections or components
- required files
- required evidence types
- hard constraints
- useful but optional additions
- nonessential polish items

### Requirement Classes

Claude must sort requirements into:

#### Class A — Must-have
Elements required for completion, grading, or valid submission.

#### Class B — Should-have
Elements that materially strengthen the result but are not strictly required for basic completion.

#### Class C — Nice-to-have
Polish, enhancement, or refinement items that should be cut before core completion is compromised.

### Minimum Completion Standard

Claude must be able to answer:

- What absolutely must be included?
- What is important but secondary?
- What can be cut if time is limited?

### Artifact Gate

Claude may advance only when the requirement map clearly distinguishes must-have work from optional work.

### Failure Conditions

Claude must not proceed if:

- the framework still confuses required vs optional elements
- downstream planning would risk overbuilding
- key grading-sensitive requirements remain hidden inside unstructured source material

---

## Phase 3 — Execution Mapping

### Purpose

Create the practical movement plan.

This phase exists to transform requirements into a sequence and determine what can happen in parallel versus what depends on prior outputs.

### Inputs

- intake artifact
- requirement map
- time constraints
- known user strengths or workflow preferences
- current completion state

### Required Outputs

Claude must produce an execution map containing:

- major phases of remaining work
- critical path
- dependency chain
- safe parallel workstreams
- immediate next step
- timing estimate
- risk points
- cut order if time pressure increases

### Required Distinctions

Claude must explicitly distinguish between:

#### Sequential tasks
Tasks that depend on prior outputs.

#### Parallel-preparable tasks
Tasks that can be safely scaffolded before final dependency outputs exist.

#### Unsafe premature tasks
Tasks that appear possible early but would create rework, inconsistency, or invented conclusions if completed before dependencies exist.

### Minimum Completion Standard

Claude must be able to answer:

- What must happen first?
- What can be prepared in parallel?
- What is the exact next highest-leverage move?
- What must wait for evidence?

### Artifact Gate

Claude may advance only when the execution map makes the workflow navigable.

### Failure Conditions

Claude must not proceed if:

- tasks are still being approached by mood rather than dependency
- the critical path is not clear
- parallel work would likely create inconsistency
- the user could still waste time on nonessential surfaces

---

## Phase 4 — Evidence Generation

### Purpose

Create the real analytic or factual basis that supports all later interpretation.

This phase exists to produce the outputs that later writing and presentation must inherit from.

### Inputs

May include:

- dataset
- source files
- code
- analysis plan
- required models or methods
- earlier exploratory outputs
- user-selected approach

### Typical Outputs

Depending on task type, evidence generation may produce:

- model results
- summary statistics
- charts
- tables
- confusion matrices
- coefficient summaries
- extracted findings
- cleaned source data
- comparison outputs
- validated observations
- finalized visual candidates

### Required Output Artifact

Claude must produce a **results packet** or equivalent evidence packet.

This packet must contain the core outputs that later writing can rely on.

### Minimum Completion Standard

Claude must be able to answer:

- What did the analysis actually produce?
- What findings are real rather than assumed?
- Which outputs are important enough to use downstream?
- Are required methods actually represented?

### Artifact Gate

Claude may advance only when a real evidence packet exists.

### Failure Conditions

Claude must not proceed to final results writing, discussion, or conclusion if:

- outputs are still incomplete
- required methods were not actually run
- core evidence is missing
- findings are being inferred from expectation rather than result

---

## Phase 5 — Evidence Validation

### Purpose

Filter and validate evidence before it enters narrative and presentation surfaces.

This phase exists because not all outputs are equally meaningful, presentable, or trustworthy.

### Inputs

- evidence packet
- raw outputs
- required deliverables
- presentation/report constraints

### Required Outputs

Claude must classify outputs into three groups:

#### A. Must-show evidence
Essential for the report and likely the presentation.

#### B. Report-only evidence
Supports rigor and explanation, but may not belong in slides.

#### C. Archive-only evidence
Useful for reproducibility, troubleshooting, or appendix, but not for polished primary deliverables.

### Required Validation Questions

Claude must ask:

- Which outputs support the strongest claims?
- Which outputs are actually readable and useful?
- Which outputs are necessary for integrity?
- Which outputs should be excluded from polished artifacts?

### Minimum Completion Standard

Claude must have selected:

- the core evidence surfaces
- the core visuals
- the core comparison elements
- the core interpretation anchors

### Artifact Gate

Claude may advance only when the evidence packet has been filtered into usable downstream categories.

### Failure Conditions

Claude must not proceed if:

- too many outputs remain unclassified
- report and slide choices would be arbitrary
- visuals are being included without communicative purpose
- raw output is being confused with evidence-ready material

---

## Phase 6 — Narrative Assembly

### Purpose

Convert validated evidence into a coherent written master artifact.

This phase exists to create the full narrative layer from which slides and spoken delivery will later inherit.

### Inputs

- validated evidence packet
- requirement map
- earlier background material
- earlier proposal or exploratory documents
- selected findings
- required report structure

### Default Master Artifact

The default master artifact is a report or report-equivalent written draft.

### Required Outputs

Claude must produce:

- structured report draft
- results section
- discussion section
- conclusion
- any required methods or background sections
- any required disclosures

### Narrative Role

This phase creates the central story of the work.

It is where:
- evidence becomes meaning
- analysis becomes explanation
- isolated findings become coherent argument

### Minimum Completion Standard

Claude must ensure:

- the report is internally coherent
- required sections are present
- numerical claims match validated evidence
- results are separated from discussion
- the conclusion is supported by the report
- the report can be compressed into slides without conceptual reinvention

### Artifact Gate

Claude may advance only when the master narrative exists in usable form.

### Failure Conditions

Claude must not proceed to slide finalization if:

- the report is still missing its interpretive core
- findings are not yet written as a coherent story
- conclusions are still unstable
- slide creation would require inventing new logic outside the report

---

## Phase 7 — Visual Compression

### Purpose

Convert the written master artifact into a concise, presentation-appropriate visual structure.

This phase exists to turn the report into high-signal presentation form.

### Inputs

- completed report draft
- validated evidence packet
- selected visuals
- style constraints
- time limits for presentation

### Required Outputs

Claude must produce:

- final slide structure
- selected visual placements
- compressed slide text
- comparison slide if relevant
- insight slide(s)
- conclusion slide

### Compression Principle

The presentation must be a compression of the report.

It must not become a second project.

### Slide-Level Requirements

Each slide must answer:

- What is the one main point here?
- What evidence supports that point?
- What must the audience remember?

### Minimum Completion Standard

Claude must ensure:

- each slide has a clear main idea
- slide text is compressed
- evidence surfaces are readable
- slide sequence supports natural narration
- slide claims match the report exactly

### Artifact Gate

Claude may advance only when a coherent final slide structure exists.

### Failure Conditions

Claude must not proceed to speaker scripting if:

- the slides are still overloaded
- evidence is inconsistent with the report
- transitions between slides are weak
- the slide deck still behaves like a pasted report

---

## Phase 8 — Delivery Scripting

### Purpose

Convert the slide structure into human-usable spoken guidance.

This phase exists to support actual delivery, not just document creation.

### Inputs

- final slide deck
- report conclusion
- user tone preferences
- required presentation length

### Required Outputs

Claude must produce speaker notes or a guided script.

For each slide, the default structure is:

- opening sentence
- support points
- transition sentence

### Spoken-Delivery Rule

This phase must optimize for speech, not for writing elegance.

### Minimum Completion Standard

Claude must ensure:

- notes follow slide order exactly
- notes are readable aloud
- slide-to-slide flow is natural
- the script is concise enough to fit the time window
- the user can speak from it without sounding trapped inside dense prose

### Artifact Gate

Claude may advance only when the delivery layer is usable.

### Failure Conditions

Claude must not proceed to final packaging if:

- the spoken layer is missing
- the user would still need to invent narration from scratch
- slide order and script order do not match
- time fit has not been considered

---

## Phase 9 — Technical Cleanup

### Purpose

Prepare the reproducible technical layer for submission.

This phase exists to clean the operational files that support the polished deliverables.

### Inputs

- code file(s)
- data file(s)
- saved outputs
- filename references from report/slides
- packaging expectations

### Required Outputs

Claude must ensure:

- code file is cleaned
- filenames are consistent
- technical artifacts exist
- referenced data file is correct
- scripts are reproducible enough for expected use
- output files are saved if claimed

### Minimum Completion Standard

Claude must be able to confirm:

- the right files exist
- the filenames used in documents are correct
- technical materials correspond to the written deliverables
- the code artifact is not obviously broken or fragmented

### Artifact Gate

Claude may advance only when the technical layer is submission-safe.

### Failure Conditions

Claude must not proceed to final package declaration if:

- filenames are inconsistent
- scripts contain obvious broken fragments
- claimed outputs do not exist
- data file references are wrong

---

## Phase 10 — Final Packaging

### Purpose

Produce the final governed submission set.

This phase exists to ensure completion becomes a real, deliverable state rather than an assumed one.

### Inputs

- final report
- final slide deck
- final speaking layer if needed
- final code
- data file
- recording link if applicable
- requirement map

### Required Outputs

Claude must produce a final package checklist and confirm inclusion of all required files.

### Packaging Requirements

Claude must ensure:

- all required deliverables are present
- each item is the latest version
- each item opens
- references are consistent
- the package reflects the validated final state

### Minimum Completion Standard

Claude must be able to answer:

- Is every required deliverable present?
- Is each item consistent with the rest?
- Is anything still missing before submission?
- Can the user submit without downstream contradiction?

### Final Artifact Gate

This is the final gate before declaring submission readiness.

### Failure Conditions

Claude must not indicate completion if:

- one or more required deliverables are absent
- a placeholder item still exists
- packaging is incomplete
- the latest validated materials have not yet been gathered into one submission-ready state

---

## Parallel Work Doctrine Within This Phase Architecture

### Safe Parallel Preparation

Claude may help prepare the following before evidence generation is complete:

- report shell
- slide shell
- reused background sections
- variable definitions
- source description
- preliminary findings based on earlier validated material
- methods section shell
- disclosure section

### Unsafe Premature Finalization

Claude must not finalize the following before evidence packet completion:

- results section
- final discussion
- final conclusion
- model comparison claims
- final insights slide
- final speaking notes for results-dependent slides

---

## Phase Dependency Summary

### Hard dependencies

- Requirement Extraction depends on Intake
- Execution Mapping depends on Requirement Extraction
- Evidence Validation depends on Evidence Generation
- Narrative Assembly depends on Evidence Validation
- Visual Compression depends on Narrative Assembly
- Delivery Scripting depends on Visual Compression
- Technical Cleanup must complete before Final Packaging
- Final Packaging depends on all prior required deliverables

### Soft parallelizable preparation

While earlier phases are active, Claude may scaffold later artifacts only where doing so does not force invented conclusions or duplicated reasoning.

---

## Universal Gate Questions

Before allowing transition from any phase, Claude must ask:

1. Has this phase produced a reusable artifact or validated output?
2. Would advancing now force invention, assumption, or instability?
3. Can the next phase inherit from this one cleanly?
4. Is the current phase complete enough to prevent rework?
5. Would time spent advancing now increase or reduce later friction?

If the answer is unsatisfactory, Claude must remain in the current phase.

---

## Core Failure Pattern This File Prevents

This phase architecture exists to prevent the most common execution failure:

moving downstream faster than the evidence, structure, or narrative can responsibly support

That failure produces:

- inconsistent numbers
- weak conclusions
- duplicated work
- unstable slides
- rushed scripting
- packaging chaos

This file exists to stop that.

---

## Completion Condition

This file is complete when the framework has:

- a defined phase model
- defined artifact gates
- defined transition conditions
- defined failure conditions
- defined dependency logic
- defined safe parallel preparation boundaries

---

## Next File To Print

The next relevant markdown file is:

`04_Validation_and_Quality_Control_Doctrine.md`

---