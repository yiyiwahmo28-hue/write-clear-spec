# Demo: from a rough request to a consistent revision

[English README](../README.md) · [中文首页](../README.zh-CN.md)

This 24-second animation uses shortened excerpts from an actual assistant conversation applying version 0.1.0 of [SKILL.md](../SKILL.md). The user inputs are an original, scripted fictional example. The English animation translates the Chinese conversation. Visual layout and timing are editorial: this is not a screen recording or a measure of response speed.

下面保留三轮输入与助手原始回答。动图对文字做了节选、重排及英文翻译；报名产品没有实际运行，验收场景仍是待验证的预期结果。这个案例展示一次执行，不代表效果评测。

## Watch or read

- **Animation / 动图：** [English](assets/demo-en.gif) · [简体中文](assets/demo-zh-CN.gif)
- **Still image / 静态版：** [English](assets/demo-en.png) · [简体中文](assets/demo-zh-CN.png)
- **Key outcome / 关键结果：** when cancellation is extended to the start of the event, the original sign-up deadline still applies. 报名截止后、活动开始前，可以取消有效报名，但不能重新报名。

## Original conversation / 原始完整对话

Executed on 2026-10-12 by an AI assistant that read the skill instructions. All three assistant responses below are preserved without editing. Each user input was supplied only after the preceding response had completed.

### 1. Find the missing decisions / 找出关键决定

**User / 用户**

使用 $write-clear-spec 整理这条需求：支持取消报名，取消后返还名额。先指出影响实现的关键问题，暂时不要替我决定规则。

**Assistant applying the skill / 助手按 Skill 执行**

已明确的方向是支持取消报名，并返还名额。还需确认三个会影响实现的问题：

1. 谁可以取消哪些报名？是否有截止时间或报名状态限制？
2. 取消后何时返还多少名额？取消者能否再次报名？
3. 重复取消或取消失败时，报名状态和名额应如何处理？

这些决定确认前，我先不补充功能规则或验收结果。

### 2. Write rules and acceptance / 整理规则与验收

**User / 用户**

仅本人可取消自己的有效报名，报名截止前允许取消，截止时刻及以后不允许。每条报名占一个名额，成功后立刻返还一个名额。允许重新报名，但必须仍在报名期且有剩余名额。重复取消不得重复返还名额；取消失败保持原状态和名额。成功后显示“已取消”，失败后显示“取消失败，请重试”。请整理成简短规则和验收场景，不要新增产品设定。

**Assistant applying the skill / 助手按 Skill 执行**

规则

- 仅本人可以取消自己的有效报名。
- 报名截止前允许取消；截止时刻及以后不允许。
- 每条报名占一个名额。取消成功后，原报名不再有效，立即返还一个名额，并显示“已取消”。
- 取消后允许重新报名，但必须仍在报名期且有剩余名额。
- 重复取消不得再次返还名额。
- 取消失败时，报名状态与名额保持不变，并显示“取消失败，请重试”。

验收场景

1. 正常取消：本人有一条有效报名，尚未到截止时间，剩余名额为0。取消成功后，报名不再有效，剩余名额立即变为1，显示“已取消”。
2. 权限与截止边界：他人尝试取消这条报名，或本人在截止时刻及以后尝试取消，均不允许；有效报名和剩余名额保持不变，显示“取消失败，请重试”。
3. 重复取消：报名已取消，剩余名额为1。再次取消该报名后，剩余名额仍为1，不重复返还。
4. 取消失败：本人在截止前取消有效报名，但操作失败。报名仍有效，剩余名额不变，显示“取消失败，请重试”。
5. 重新报名：本人已取消报名，仍在报名期，剩余名额为1。重新报名成功后，新报名占一个名额，剩余名额变为0；若已不在报名期或没有剩余名额，则不允许重新报名。

未确认：重复取消时应显示哪种提示，原文未规定；这里只确定不得重复返还名额。

以上是依据确认内容整理的规则与待执行验收场景，未运行产品验证。

### 3. Revise consistently / 检查改稿影响

**User / 用户**

现在改一条规则：取消期限延长到活动开始前，活动开始时刻及以后不允许取消。本例报名截止早于活动开始。重新报名仍必须在原报名期内，不延长报名期限。其他规则不变。请更新受影响的规则和验收场景，删掉被替换的旧取消期限，保留无关规则。

**Assistant applying the skill / 助手按 Skill 执行**

更新后的规则

本例报名截止早于活动开始，原报名期限保持不变。

- 仅本人可以取消自己的有效报名。
- 活动开始前允许取消；活动开始时刻及以后不允许。
- 每条报名占一个名额。取消成功后，原报名不再有效，立即返还一个名额，并显示“已取消”。
- 取消后允许重新报名，但必须仍在原报名期且有剩余名额；取消期限延长不延长报名期限。
- 重复取消不得再次返还名额。
- 取消失败时，报名状态与名额保持不变，并显示“取消失败，请重试”。

更新后的验收场景

1. 正常取消：本人有一条有效报名，报名截止已过，但活动尚未开始，剩余名额为0。取消成功后，报名不再有效，剩余名额立即变为1，显示“已取消”。此时不能重新报名，因为原报名期已结束。
2. 权限与取消期限边界：他人尝试取消这条报名，或本人在活动开始时刻及以后尝试取消，均不允许；有效报名和剩余名额保持不变，显示“取消失败，请重试”。
3. 重复取消：报名已取消，剩余名额为1。再次取消该报名后，剩余名额仍为1，不重复返还。
4. 取消失败：本人在活动开始前取消有效报名，但操作失败。报名仍有效，剩余名额不变，显示“取消失败，请重试”。
5. 重新报名：本人已取消报名，仍在原报名期，剩余名额为1。重新报名成功后，新报名占一个名额，剩余名额变为0；若已不在原报名期或没有剩余名额，则不允许重新报名。

修改说明：取消期限与场景1、2、4已同步更新；重新报名沿用原报名期，其余规则保留。

未确认：重复取消时应显示哪种提示，原文未规定；这里只确定不得重复返还名额。

以上是更新后的需求与待执行验收场景，未运行产品验证。

## Reproduce the example / 自己试一次

Follow the [quickstart](../README.md#quickstart), then send the three user inputs above in sequence. You can also supply the complete skill folder to your assistant and ask it to apply `SKILL.md`. Model responses may vary; compare the decisions, preserved rules, and acceptance scenarios, rather than exact wording.

按[快速开始](../README.zh-CN.md#快速开始)准备 Skill 后，逐轮发送上面的用户输入。也可以向助手提供完整 Skill 文件夹，让它读取 `SKILL.md`。每轮等助手回应后再继续，观察它是否保留重新报名期限，并明确重复取消提示仍未决定。

## Rebuild the animation / 重新生成素材

The editable text and timings are in [storyboard.json](demo/storyboard.json); [render.py](demo/render.py) produces the GIFs and still images. Asset generation optionally requires Python, Pillow, and a font with Chinese and Latin characters. These are not dependencies for using the skill.

```sh
python -m pip install Pillow
python docs/demo/render.py --font font.ttc --bold-font bold-font.ttc
```

The original text remains the evidence for the demo; an animation is a presentation of that text, not evidence that an application passed its tests.
