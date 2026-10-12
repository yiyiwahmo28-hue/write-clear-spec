<div align="center">

<img src="./docs/assets/logo.svg" width="120" height="120" alt="Write Clear Spec logo" />

<h1>Write Clear Spec</h1>

**Clear specs before AI writes code.**

An Agent Skill for turning rough ideas into clear requirements, finding missing decisions, and keeping changes consistent.

[![Skill version](https://img.shields.io/badge/skill-v0.1.0-1677FF?style=flat-square)](SKILL.md) [![MIT license](https://img.shields.io/badge/license-MIT-1677FF?style=flat-square)](LICENSE) [![Agent Skill](https://img.shields.io/badge/format-Agent_Skill-596579?style=flat-square)](SKILL.md)

[Quickstart](#quickstart) · [Example](#example) · [Feedback](https://github.com/yiyiwahmo28-hue/write-clear-spec/issues) · English · [简体中文](README.zh-CN.md)

</div>

---

For product managers, designers, and builders working with AI. Bring an idea, a draft, or a change request. The skill helps you decide what the feature should do and how to check it.

## Features

- **Draft with the right questions.** Find decisions that would change implementation, then write the confirmed behavior.
- **Review with evidence.** Point to the source of an ambiguity, conflicting rule, or missing acceptance condition.
- **Revise consistently.** Follow a change through related rules and scenarios in the supplied material.
- **Keep decisions visible.** Separate confirmed requirements, open questions, and optional suggestions. Use your language and document format.

## Quickstart

Install with the [Skills CLI](https://github.com/vercel-labs/skills), then select your assistant:

```sh
npx skills add yiyiwahmo28-hue/write-clear-spec --skill write-clear-spec
```

The installer uses Node.js and npm. The skill itself is a folder of instructions with no executable dependency or external service of its own. It uses your assistant's model and authorized file access.

In an assistant that supports named skill invocation, start with:

```text
Use $write-clear-spec to review this requirement.
Ask about decisions that change the behavior. Do not rewrite it yet.

[Paste your requirement here]
```

<details>
<summary>Manual setup and other prompts</summary>

Download this repository, name its folder `write-clear-spec`, and place it in a skill directory supported by your assistant. Keep `SKILL.md`, `references/`, and `agents/` together. To try it without named invocation, ask your assistant to read `SKILL.md` and apply it to your requirement, with the supporting files available.

**Draft an idea**

```text
Use $write-clear-spec to turn this idea into functional requirements.
Ask only about consequential missing decisions and continue with confirmed parts.
```

**Update a requirement**

```text
Use $write-clear-spec to apply this rule change.
Update the affected acceptance scenarios and flag dependencies you cannot check.
```

</details>

## Example

### “Let users cancel and return their place.”

*An original, fictional event-registration example. The answers below are decisions supplied by the fictional user.*

**The skill asks:**

- When is cancellation allowed?
- What happens if the same registration is canceled twice, or cancellation fails?
- Should a canceled registration still appear in the active list?

**The user confirms:** cancellation is allowed before the registration deadline. Success immediately returns one place and removes the registration from the active list. Admin exports include active registrations only. Repeated cancellation releases no additional place; failure changes neither the registration nor capacity.

**The resulting requirements make the consequences explicit:**

- Successful cancellation decreases the active count by one, frees one place, and excludes the registration from the active-registration export.
- Canceling that same registration again does not free another place.
- Failed cancellation preserves the registration's pre-operation status and remaining capacity.

<details>
<summary>Acceptance scenario and open decisions</summary>

Before the deadline, start with a full event and cancel one active registration. Exactly one place should become available. Repeat the cancellation: available places must not increase again. Check that the canceled registration is absent from the active count and export.

Behavior at the exact deadline and success/failure messages still need a decision. These are expected results to verify; no event application was executed for this example.

The fuller [registration-change example](references/examples.md#示例三需求更新时保留规则并找出关联遗漏) also covers re-registration, remaining capacity, and preserving existing rules.

</details>

## Documentation

- [Skill instructions](SKILL.md) — the draft, review, and revise workflow.
- [Review guide](references/review-guide.md) — evidence, consistency, and verification.
- [Worked examples (中文)](references/examples.md) — missing decisions, concrete requirements, and scoped changes.
- [中文说明](README.zh-CN.md) — the complete Chinese introduction.

## Contributing

Share a small, fictional before/after case in an [issue](https://github.com/yiyiwahmo28-hue/write-clear-spec/issues). Include the input, confirmed decisions, and what the skill missed. Improvements to questions, examples, and wording are welcome.

All instructions and examples were independently written for this skill. Keep contributions free of employer materials, customer data, and internal systems. This project supports specification work; implementation results require actual execution evidence.

## License

[MIT](LICENSE).
