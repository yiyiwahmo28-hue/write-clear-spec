---
name: write-clear-spec
description: Turn rough product ideas into clear functional specs before coding. Clarify missing decisions, review drafts for conflicting rules and acceptance gaps, and revise requirements without leaving stale behavior behind. Use for specification writing and review, not copyediting alone or choosing a product strategy.
license: MIT
metadata:
  version: "0.1.0"
---

# Write Clear Spec

Help the user spell out how a feature should work before an implementer has to guess. Start from an idea, a draft, or a change request; write confirmed behavior and keep unresolved decisions visible. Work in the user's language and preserve their chosen format and scope.

## Choose the operation

- **Draft:** clarify an idea and write the confirmed behavior.
- **Review:** locate ambiguities, missing behavior, and contradictions in an existing specification. Do not rewrite it unless requested.
- **Revise:** apply a confirmed change and check its consequences across the supplied rules and acceptance scenarios.

Infer the operation from the request. Ask only when the ambiguity would change the work. For a deeper review, read [the review guide](references/review-guide.md). For worked examples, read [the original examples](references/examples.md). Do not load both references for a routine edit.

## Establish what is known

Read the supplied material before asking for facts already present. Identify the intended user, the behavior being specified, and the current scope. Separate:

- **Confirmed:** decisions or constraints explicitly supplied by the user or an identified authoritative source.
- **Open:** choices the material does not settle, or conflicts without a stated precedence.
- **Suggested:** optional recommendations, including values, defaults, and implementation approaches not yet approved.

An observation of the current implementation describes what exists; it does not automatically decide what the product should do. A later timestamp alone does not resolve conflicting requirements. Follow the user's stated source priority and current decisions; otherwise expose the conflict.

Ask about open decisions that would materially change implementation or acceptance. Bundle related questions and continue independent work using confirmed facts. If the user requests a draft with assumptions, label those assumptions as proposed and keep them out of the confirmed rules. Do not demand answers to every possible edge case before producing useful work.

## Describe behavior, not just features

For each relevant behavior, make the following relationships clear. Use prose, scenarios, or tables as appropriate; these are content questions, not mandatory headings.

1. **Actor and context:** who acts, on what object, and in which relevant state?
2. **Trigger and eligibility:** what starts the behavior, and what conditions allow or prevent it?
3. **Rule and outcome:** what happens, in what order when order matters, and what observable state changes?
4. **Feedback:** what does the user or another consumer see when the behavior succeeds, waits, or fails?
5. **Relevant exceptions:** what happens at a meaningful limit, after interruption, or on a repeated attempt? State which side effects must not occur when that matters.
6. **Dependencies:** what result is required from another capability, and where is that capability's rule defined?

Replace phrases such as "works correctly," "handles errors," or "supports cancellation" with observable conditions and results. Keep distinct decisions separate. "Show an error or retry" is unresolved unless the conditions choosing each branch are defined.

Include relevant limits, units, time boundaries, comparison operators, and initial states when they affect behavior. Record an authoritative value in one maintained definition and reference it consistently. Purposeful repetition in summaries or scenarios is acceptable; competing definitions are not.

Separate product behavior from implementation choices. Preserve explicit technical contracts and constraints when the user supplies them. Do not invent API names, storage structures, timing values, product defaults, or architectural requirements to fill a gap. Keep delivery scope distinct from speculative future features; use a separate scope note when the audience needs one.

## Connect rules to acceptance

Write scenarios for the behaviors that matter in this task. Each scenario should have a relevant starting state, an action or event, and an observable expected result. Given/When/Then is useful, but not required.

Include normal operation and the boundary or failure paths justified by the feature's risks. Do not invent one example of each category merely to fill a template. Check that every critical rule has a scenario or another stated verification method, and that scenarios do not introduce unconfirmed rules.

Assign stable rule identifiers only when they help trace several rules across a longer document. A small paragraph edit does not need an identifier system. Reuse existing identifiers when revising.

Scenarios describe what should be verified. Writing a scenario is not evidence that the feature works. State whether the output is an unverified specification, a source review, or a result supported by an actual execution. Run a product or modify implementation only when the task authorizes it.

## Review with evidence

Read [the review guide](references/review-guide.md) when reviewing a full requirement or evaluating readiness for handoff.

For each consequential finding, give:

- the section, rule identifier, line, or exact excerpt that supports it;
- the missing decision or conflicting interpretations;
- the concrete implementation or acceptance consequence;
- a targeted question or proposed repair.

Distinguish a blocking decision from an improvement that can wait. An improvement can still be important without preventing work on the confirmed behavior. Describe the actual review scope; do not imply that unread documents, code, or workflows were checked. Avoid numerical quality scores and blanket "all checks passed" claims based on headings or keyword counts.

## Revise consistently

Apply the requested change to the affected rule and its scenarios. Trace direct consequences in the material actually available: eligibility, state transitions, shared parameters, examples, feedback, and adjacent rules. Remove superseded statements from the updated rule instead of appending a disclaimer above contradictory text.

Preserve unrelated rules, identifiers, terminology, and approved values. Keep change history separate from the current operative definition when history is required. If a related file or decision is unavailable or outside the requested edit scope, identify the dependency and the needed follow-up; do not pretend it was updated.

Do not resolve newly exposed business choices by silently changing the product. Ask about material choices and deliver the confirmed portions of the revision with the remaining decisions clearly marked.

## Deliver the requested result

- **Draft:** the specification, plus a short, separate list of decisions still needed and any proposed assumptions.
- **Review:** prioritized, source-backed findings and the questions or repairs that resolve them. Keep the original intact unless rewriting was requested.
- **Revise:** the updated text and a concise account of consequential changes and unresolved dependencies.

Follow the user's format. Select only the sections the feature needs. Do not enforce a fixed chapter count, word reduction percentage, heading style, diagram, priority scale, or table format. A draft with material open decisions remains a draft; formatting completeness does not make it ready for implementation.
