# Write Clear Spec

**Clear specs before AI writes code.**

Turn rough ideas into clear requirements for your coding agent. Ask the missing questions, catch conflicting rules, and define what counts as done. Keep related requirements aligned as plans change.

For product managers, designers, and builders who know what they want to make but need help spelling out how it should work. Start with an idea, a draft, or a change request. The skill identifies decisions that affect implementation and turns confirmed answers into functional requirements. Open decisions stay visible.

## 中文说明

**在 AI 写代码之前，先把需求写清楚。**

帮用 AI 做产品的人，把零散想法写成功能需求：问清关键问题、找出遗漏和矛盾，说明怎样才算完成。改需求时一并检查相关规则，未确认的决定单独标出。

适合产品经理、策划和用 AI 做产品的人：知道想做什么，但还没有把功能怎样工作说完整。把一个想法交给开发之前、评审已有需求时、修改规则之后，都可以使用。

- **写清楚：**从“支持上传文件”这样的想法出发，问清格式、结果和失败处理，再写成具体需求。
- **审一遍：**在评审前找出开发仍然需要猜的地方，指出原文位置和需要决定的问题。
- **改完整：**改一条规则时，同步相关内容与验收场景，检查新旧说法是否冲突。

它不会替产品负责人决定未确认的功能，也不会把目录齐全或测试场景写完等同于功能已经通过验证。

## Use

Keep the complete `write-clear-spec` folder together, including `references/` and `agents/`. Place it in a skill directory supported by your assistant. Where named skill invocation is supported, invoke `$write-clear-spec`; otherwise ask the assistant to read `SKILL.md` and apply it to the supplied requirement.

This is an original, MIT-licensed Agent Skill. It requires no external service or executable dependency of its own; the host assistant supplies the model and any authorized file access. The two reference files are loaded only when the task needs them. `agents/openai.yaml` supplies optional interface metadata; the main instructions remain usable without that file.

Example prompts:

```text
Use $write-clear-spec to review this requirement. List decisions that could
change implementation, with their source locations. Do not rewrite it yet.
```

```text
使用 $write-clear-spec 把这个功能想法整理成需求。先列出已有事实，
只追问会影响实现的关键问题；其他已确认部分继续写。
```

```text
使用 $write-clear-spec 更新这份需求：只更改我指定的规则，
同步相关验收场景，并指出缺少资料而无法核对的关联内容。
```

## What the skill adds

The core is behavior clarification and evidence-backed review: actor, trigger, eligibility, outcome, feedback, relevant exceptions, and verification. It separates confirmed decisions from open questions and optional suggestions. It also traces the consequences of revisions in the supplied material.

There is no prescribed chapter count, diagram, typography, priority scale, or compression target. Team-specific conventions can be provided with the task. Explicit technical contracts remain part of the requirement when relevant.

See [SKILL.md](SKILL.md) for the workflow, [review guide](references/review-guide.md) for a deeper review, and [original examples](references/examples.md) for fictional cases.

## Scope and provenance

All instructions and examples in this package were independently written for this skill. Examples are fictional; no real project names, internal links, source excerpts, business configurations, or machine-specific paths are included.

This release supports specification work. It does not choose a product strategy or independently prove an implementation works. Use actual execution evidence to establish implementation results. Reduced rework or improved implementation accuracy has not been measured as a general performance claim.

## Contributing

Useful contributions are small, fictional before/after cases that show a consequential ambiguity, a conflicting rule, or a revision dependency. State the confirmed input, the open decisions, and what the proposed guidance changes. Keep examples independent of employer materials, customer data, and internal systems.

## License

[MIT](LICENSE). Version 0.1.0.
