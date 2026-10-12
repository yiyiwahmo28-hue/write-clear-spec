# Review guide

Use this guide when the task is to review a specification or decide whether its confirmed behavior is ready to hand off. It supplements the workflow in SKILL.md; it is not a requirement to inspect every possible risk.

## 1. Find decisions hidden in prose

Look for statements that permit several reasonable implementations. Common signals include undefined words such as "recent," "appropriate," "automatically," "valid," and "as needed." These words are not errors by themselves: inspect whether nearby rules define their meaning.

Ask what a reader would still have to choose. A notification requirement may be missing its recipient and trigger; a capacity requirement may be missing a unit or the behavior at the limit. Focus on choices that change observable behavior, rather than requesting details already delegated to implementation.

When a source says "A or B," check whether it defines when A applies and when B applies. Distinguish deliberate implementation freedom from an unresolved product outcome. If both outcomes are acceptable, record that acceptance explicitly instead of inventing a selection rule.

## 2. Trace each important path

Follow the actor and object through eligibility, action, intermediate states when relevant, final state, and feedback. Check that the next step has the information or resources it requires.

Select failure paths from the operation rather than a universal checklist. For example:

- an interrupted file import may need a partial-result policy;
- a repeated submission may need a duplicate-handling decision;
- a role change may affect access to previously created items;
- a scheduled action may need a time boundary and a retry decision.

These are questions to evaluate, not default product rules. Do not add persistence, retries, concurrency controls, or permission behavior unless the supplied requirement calls for them or the user confirms the decision.

## 3. Check consistency where the evidence reaches

Compare definitions that refer to the same business object. Check units, thresholds, allowed states, defaults, and examples. An acceptance scenario can repeat a rule, but must not silently change it.

Before calling two statements contradictory, check their actor, platform, phase, and conditions. A rule for a guest and a rule for an administrator may legitimately differ. Report conflicts with both source locations and the competing outcomes.

For revisions, follow the declared change through supplied sections and direct references. Report unavailable related documents as unreviewed dependencies. Do not expand a local rewrite into a repository-wide modification without authorization.

## 4. Check verification quality

For each critical behavior, identify how a person or test could distinguish success from failure. "A button is visible" may be sufficient for a visibility requirement, but does not verify the business action behind it.

Prefer observations that establish the requested outcome. A command returning successfully, a toast appearing, or a file being written proves only the corresponding event. It does not prove a later state was preserved or that the intended recipient received a result.

Keep specification review separate from execution. Review can show that a rule is testable; only execution evidence can support a claim that it currently works. If verification depends on an unspecified threshold or unresolved policy, record the missing decision.

## 5. Classify findings by consequence

- **Blocking decision:** plausible interpretations lead to materially different behavior, and the source does not choose among them.
- **Correctness conflict:** two applicable statements require incompatible outcomes.
- **Coverage gap:** an important stated behavior lacks a complete path or verification method.
- **Clarity improvement:** wording, placement, or repetition makes the requirement harder to use without changing its meaning.

Do not inflate stylistic differences into correctness findings. Respect existing technical contracts, document ownership, and deliberately delegated decisions.

## Finding format

Use the smallest useful format. A typical finding contains:

**Location:** source section or exact excerpt.

**Issue:** the missing decision or competing readings.

**Consequence:** what an implementer could do differently, or what acceptance cannot decide.

**Resolution:** a specific question or a proposed edit clearly labeled as a suggestion.

End with a scoped readiness statement. For example, the confirmed path is ready to implement while an interruption policy remains open. Do not label the whole specification ready if the open policy changes that path's implementation.
