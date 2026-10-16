# Buy or Bye

一个站在消费者一边的理性购物 Skill：先判断这次购买是否应该发生，再讨论买什么。

它适用于“这个值得买吗”“双十一要不要冲”“我已经有类似的了还需要买吗”等问题，并给出明确结果：买、等待、先验证、继续使用或维修、借用或租赁、买二手、不买。

## 核心原则

> 在确认值得购买之前，不推荐任何商品。

- 不以返佣、广告、热度或平台星级排序；
- 把“不买”和低成本替代视为成功结果；
- 区分用户事实、外部事实、历史结果、推断和未知项；
- 默认最多追问三个真正可能改变结论的问题；
- 给出明确结论、下一步行动，以及什么条件会改变答案。

## 安装到 Codex

将本目录放到个人 Skills 目录：

```bash
cp -R buy-or-bye ~/.codex/skills/buy-or-bye
```

重新打开一个 Codex 任务后，可以直接说：

```text
使用 $buy-or-bye 帮我判断：AirPods Pro 3 现在降价了，但我已经有能用的 AirPods Pro 2，要不要换？
```

Skill 也允许自动触发，例如直接询问“这个商品值得买吗”。

## 文件结构

```text
buy-or-bye/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── decision-framework.md
    ├── output-contract.md
    └── calibration-cases.md
```

## 与普通购物助手的区别

普通购物助手通常从“买哪一个”开始；Buy or Bye 从“是否应该购买”开始。只有购买门槛通过后，它才会进行具体选品。

## 许可证

MIT
