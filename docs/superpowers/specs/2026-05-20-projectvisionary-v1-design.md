# ProjectVisionary v1 — Design Spec

**Date:** 2026-05-20
**Status:** Approved (brainstorm complete); ready for implementation plan
**Repo:** built as an upgrade inside `AEI-POC`
**Taxonomy:** see `ProjectBrainer/memory/doctrine_aei_naming_taxonomy.md`

---

## 1. Purpose & Placement

**ProjectVisionary = Generative AEI, properly scoped** — it generates high-design **artifacts** (here: presentations) from real project material. It is the generative *surface* of the AEI stack and a constituent of the deferred ProjectGenesis (`ProjectGenesis = ProjectVisionary ∘ ProjectBrainer ∘ trinity`).

This spec covers **ProjectVisionary v1: a presentation generator**, built by upgrading AEI-POC's hardcoded one-off `code/build_slides.py` into a reusable, grounded, LLM-driven generator that produces decks matching the **Legacy Archive v5** design quality across all portfolio projects.

**Why AEI-POC is the home:** AEI-POC already owns slide generation (it produced the MIS401 diabetes deck via python-pptx). v1 generalizes that capability instead of starting a new repo.

### Non-goals (v1)
- No web UI (VisionAir-style wizard is v2; may eventually merge with VisionAir).
- No full-system generation (that is ProjectGenesis, deferred).
- No new "Project" name for portfolio mode or parallel synthesis — that is "ProjectVisionary, portfolio mode, quantum-orchestrated" (naming-discipline per taxonomy doctrine).

---

## 2. Decisions locked in brainstorm (2026-05-20)

| Dimension | Decision |
|---|---|
| Generation model | **LLM-generative** (Claude Opus) **+ guided pivotal questions before generation** — VisionAir's pattern applied to presentations |
| Grounding level | **C — operator answers + project's own docs + ProjectBrainer/Digital Brain memory** (anti-confabulation; carries honest maturity caveats) |
| Output unit | **Both modes, configurable** — `deep-dive` (one project, full deck) and `portfolio` (all projects → one combined master deck) |
| Design capture | **Clean template with master layouts + named placeholders**, built once from the Legacy aesthetic; generator does `add_slide(layout)` + fill placeholders |
| Interface | **Python CLI v1** (interactive prompts); web UI deferred to v2 |

**Quantum-orchestration note:** `portfolio` mode (run per-project generation across all 11–13 projects in parallel, then coherence-synthesize into one master deck) is the **first concrete quantum-orchestration instance** — a deliverable the operator could not produce solo at that quality.

---

## 3. Architecture — 5-stage pipeline

```
1. ELICIT      guided pivotal questions (per mode)              → answers
2. GROUND      read project docs + Digital Brain memory          → grounding bundle
3. GENERATE    Claude Opus (answers + grounding)                 → SlideContent JSON (schema-validated)
4. RENDER      python-pptx fills the clean template placeholders → .pptx
5. SYNTHESIZE  (portfolio mode) run 1–4 per project in parallel  → one master deck
```

Stages 1–4 are the deep-dive path. Stage 5 wraps 1–4 for portfolio mode.

---

## 4. Components

Each unit has one purpose, a defined interface, and is testable in isolation.

### 4.1 `template/projectvisionary.pptx` — the design system
A clean PowerPoint template built **once**, derived from the Legacy Archive v5 aesthetic. Contains slide-master **layouts** with **named placeholders**:
- `TITLE` (the big statement title), `KICKER` (the "NUMBER / CATEGORY" header), `STATEMENT` (the 2–3 line big-statement), `PILLAR_1..PILLAR_4` (the bottom category strip), `BODY` (paragraph), `IMAGE` (optional figure).
- Theme: the Legacy color/typography system.
- **Design lives here, not in code.** Changing the look = editing this file, not the generator.

### 4.2 `elicit.py` — guided-question engine
Asks the **pivotal questions** before generation. Per project (deep-dive) the candidate set:
1. One-line essence (what is this project, in a sentence)?
2. Who/what is it for?
3. The single most impressive **real** thing it does?
4. Honest maturity: shipped / prototype / visionary idea?
5. The 3–4 category pillars?
6. (deep-dive) per-section emphasis / the narrative arc.

Portfolio mode asks a smaller per-project set + a portfolio-level framing question (the "one pattern" through-line).
- **Interface:** `elicit(mode, project) -> Answers`
- **Depends on:** nothing (pure interactive I/O); answers may be pre-supplied via input file for non-interactive runs.

### 4.3 `ground.py` — grounding gatherer (level C)
Collects real material so generation is grounded, not invented:
- Project repo: README, ARCHITECTURE, key docs.
- ProjectBrainer/Digital Brain memory for that project (assessments, decisions, the "one pattern" framing).
- **Interface:** `gather(project) -> GroundingBundle`
- **Depends on:** filesystem read access to the project repo + `digital-brain/projects/<project>/`.

### 4.4 `generate.py` — LLM content generation
Claude Opus takes `Answers + GroundingBundle` → `SlideContent` (JSON). In the operator's voice, grounded in the bundle, preserving honest maturity caveats.
- **Anti-confabulation:** system prompt instructs "only claim what the grounding supports; flag unverifiable claims rather than emit them." Output is **validated against the SlideContent schema** before it can proceed (reject/regenerate on malformed — mirrors VisionAir's Zod-validated `/api/blueprint`).
- **Prompt-injection discipline:** grounding material wrapped as delimited untrusted data (per the SECURITY.md §5 pattern already used in VisionAir + the commit-review hook).
- **Interface:** `generate(answers, grounding) -> SlideContent`
- **Depends on:** Anthropic SDK + `ANTHROPIC_API_KEY` (env, server-side).

### 4.5 `render.py` — template-fill renderer
Opens `template/projectvisionary.pptx`, for each slide in `SlideContent` does `add_slide(layout)` and fills the named placeholders. Outputs `.pptx`.
- **Interface:** `render(slide_content, out_path) -> Path`
- **Depends on:** python-pptx + the template file. **Knows nothing about the LLM** — pure content→pptx.

### 4.6 `synthesize.py` — portfolio mode
Runs stages 1–4 per project (parallel dispatch), collects N `SlideContent` results, and produces one coherent master deck (intro + one slide/section per project + the "one pattern" through-line). The coherence pass is the ACE-flavored synthesis.
- **Interface:** `synthesize(projects) -> SlideContent` (master)
- **Depends on:** `elicit`, `ground`, `generate`.

### 4.7 `cli.py` — orchestrator
`python -m projectvisionary --mode {deep-dive|portfolio} [--project <name>] [--answers <file>] [--out <path>]`. Wires the stages per mode.

---

## 5. The load-bearing interface — `SlideContent` schema

The clean boundary between generation and rendering. `generate.py` outputs it; `render.py` consumes it; validated in between.

```jsonc
{
  "deck_title": "string",
  "mode": "deep-dive | portfolio",
  "slides": [
    {
      "layout": "title | statement | pillars | body | image",   // maps to a template layout
      "kicker": "string",            // "NUMBER / CATEGORY" header
      "title": "string",             // big statement title
      "statement": "string",         // 2-3 line big statement (optional per layout)
      "pillars": ["string", ...],    // up to 4 (optional per layout)
      "body": "string",              // paragraph (optional per layout)
      "image_ref": "path | null",    // optional figure
      "grounding_trace": ["string"]  // which grounding facts back this slide's hard claims
    }
  ]
}
```

`grounding_trace` is the anti-confabulation hook: every slide carries the grounding facts its hard claims rest on; a validation pass can flag slides whose claims don't trace.

---

## 6. Error handling & disciplines

- **Schema validation gate:** malformed LLM output is rejected; regenerate once, then fail clearly. The renderer never receives invalid content.
- **Grounding-trace check:** slides with hard claims lacking a `grounding_trace` entry are flagged for operator review before render (anti-confabulation).
- **Missing API key:** fail clearly with a message (this is an operator tool, not an always-on service — no silent fallback needed, unlike VisionAir's graceful degradation).
- **Template missing/changed:** validate the template has the expected named layouts/placeholders at startup; fail with a clear message if not.
- **Secrets:** `ANTHROPIC_API_KEY` from env only; never in code or output. (gitleaks + the commit-review hook already guard the repo.)

---

## 7. Testing

- **Render golden test:** a fixed `SlideContent` → `.pptx` with the expected slide count, layouts, and filled placeholders.
- **Schema validation test:** malformed generation output is rejected.
- **Grounding-trace test:** a generated `SlideContent` whose claims lack grounding traces is flagged (anti-confabulation).
- **Acceptance test:** regenerate one real project's deck end-to-end at Legacy quality (candidate: a project with rich docs — e.g., HydrOS or AEI-POC itself), operator eyeball-verifies design fidelity.

---

## 8. Build order (for the implementation plan)

1. Build the clean template (`template/projectvisionary.pptx`) from the Legacy aesthetic — design system first.
2. `SlideContent` schema + validation.
3. `render.py` (template-fill) — testable against the schema with hand-written content, no LLM.
4. `generate.py` (LLM) — to the schema.
5. `ground.py` + `elicit.py`.
6. `cli.py` deep-dive mode end-to-end → acceptance test on one real project.
7. `synthesize.py` + portfolio mode (the quantum-orchestration deliverable).

Deep-dive (steps 1–6) is shippable on its own; portfolio mode (step 7) is the fast-follow that produces the master portfolio deck.

---

## 9. Relationship to the rest of the stack

- **VisionAir** is a sibling ProjectVisionary instance (consumer-tier: one idea → blueprint artifact). ProjectVisionary-the-presentation-generator is operator-tier (project material → deck). Same pattern, different surface; both could share the `SlideContent`-style validated-generation discipline.
- **ProjectGenesis** (deferred) composes this generative surface with ProjectBrainer + the trinity to generate working systems.
- **Portfolio mode** is the first concrete quantum-orchestration instance.
