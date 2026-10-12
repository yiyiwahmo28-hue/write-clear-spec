<div align="center">

<img src="./docs/assets/logo.svg" width="120" height="120" alt="Write Clear Spec 标识" />

<h1>Write Clear Spec</h1>

**在 AI 写代码之前，先把需求写清楚。**

把零散想法写成功能需求，找出遗漏与矛盾，修改规则时检查前后是否一致。

[![Skill 版本](https://img.shields.io/badge/skill-v0.1.0-1677FF?style=flat-square)](SKILL.md) [![MIT 许可证](https://img.shields.io/badge/license-MIT-1677FF?style=flat-square)](LICENSE) [![Agent Skill](https://img.shields.io/badge/format-Agent_Skill-596579?style=flat-square)](SKILL.md)

[快速开始](#快速开始) · [看个例子](#看个例子) · [反馈问题](https://github.com/yiyiwahmo28-hue/write-clear-spec/issues) · [English](README.md) · 简体中文

</div>

---

适合产品经理、策划和用 AI 做产品的人。带来一个想法、一份草稿或一次改动，让 Skill 帮你写清功能怎样工作、怎样才算完成。

## 特性

- **写清楚：** 找出会影响实现的关键决定，再把已确认的行为写成需求。
- **审一遍：** 定位原文中的歧义、规则矛盾和验收缺口，说明还需要决定什么。
- **改完整：** 改一条规则时，一并检查给定材料中受影响的规则和验收场景。
- **保留决定权：** 区分已确认、待决定与可选建议，沿用你的语言和文档格式。

## 快速开始

通过 [Skills CLI](https://github.com/vercel-labs/skills) 安装，再选择你使用的助手：

```sh
npx skills add yiyiwahmo28-hue/write-clear-spec --skill write-clear-spec
```

安装命令需要 Node.js 和 npm。Skill 本身是一个指令文件夹，使用助手提供的模型和已授权文件访问能力，无需独立运行服务。

在支持按名称调用 Skill 的助手中，可以这样开始：

```text
使用 $write-clear-spec 检查这段需求。
先问清会影响功能行为的关键决定，暂时不要改写。

[在这里粘贴需求]
```

<details>
<summary>手动安装与其他用法</summary>

下载仓库，将文件夹命名为 `write-clear-spec`，放入你的助手支持的 Skill 目录。将 `SKILL.md`、`references/` 和 `agents/` 保持在一起。也可以在提供完整文件夹后，让助手读取 `SKILL.md`，按其中的方法处理需求。

**整理一个想法**

```text
使用 $write-clear-spec 把这个功能想法整理成需求。
只追问会影响实现的关键问题，已确认的部分继续写。
```

**修改已有需求**

```text
使用 $write-clear-spec 更新这份需求。
同步受影响的验收场景，并指出缺少资料而无法核对的关联内容。
```

</details>

## 看个例子

### “支持取消报名，取消后返还名额。”

*原创虚构案例。下面的规则由案例中的用户确认。*

**Skill 先问清楚：**

- 什么时候允许取消？
- 对同一条报名重复取消，或者取消失败时，名额和状态怎么处理？
- 取消之后，这条报名还在有效名单里吗？

**用户确认：** 报名截止前可以取消。成功后立即释放一个名额，并退出有效名单；管理员导出仅包含有效报名。重复取消不再释放名额，失败时状态和名额都不变。

**整理后的需求，把这些影响写出来：**

- 取消成功：有效人数减一，恢复一个名额，导出的有效名单不再包含这条报名。
- 对同一条已取消报名重复操作：名额不再增加。
- 取消失败：保持操作前的报名状态和剩余名额。

<details>
<summary>展开验收场景与待决定事项</summary>

在截止前，从满员状态取消一条有效报名，确认只恢复一个名额。再次取消同一条报名，确认名额不再增加。同时核对有效人数和导出名单。

恰好到截止时刻如何处理，以及成功／失败时的提示，仍需用户决定。这些是待验证的预期结果，本例没有执行活动产品。

完整的[报名规则改稿示例](references/examples.md#示例三需求更新时保留规则并找出关联遗漏)还展示了再次报名、剩余名额和原有规则的检查。

</details>

## 文档

- [Skill 指令](SKILL.md)：写需求、审需求、改需求的完整流程。
- [审查指南](references/review-guide.md)：检查证据、一致性与验收条件。
- [原创示例](references/examples.md)：需求缺口、具体规则和局部改稿。
- [English](README.md)：英文介绍。

## 参与贡献

欢迎在 [Issue](https://github.com/yiyiwahmo28-hue/write-clear-spec/issues) 中分享小型虚构案例：提供原始输入、已确认的决定，以及 Skill 遗漏的问题。也欢迎改进追问、示例和表述。

本项目的指令和示例均为原创。请使用独立构造的案例，避免放入雇主资料、客户数据和内部系统信息。Skill 支持需求整理；功能实现是否正确，需要实际执行验证。

## 许可证

[MIT](LICENSE)。
