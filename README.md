# Buy or Bye · 先别买

[English](README_EN.md) · 简体中文

[![Release](https://img.shields.io/github/v/release/siqili199206-commits/buy-or-bye)](https://github.com/siqili199206-commits/buy-or-bye/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一个站在消费者一边的理性购物 Agent Skill：**先判断这次购买是否应该发生，再讨论买什么。**

![跑鞋购买判决示例](assets/running-shoes-decision-card.png)

## 它和普通购物助手有什么不同？

普通购物助手通常从“买哪一个”开始；Buy or Bye 从“是否应该购买”开始。

> 在确认值得购买之前，不推荐任何商品。

它可能给出的结果包括：

- `BUY`：购买缺口真实，可以进入选品；
- `WAIT`：需求可能真实，但时机、价格或状态不合适；
- `VALIDATE_FIRST`：先用一次低成本测试解决关键未知项；
- `REUSE_OR_REPAIR`：继续使用或维修已有物品；
- `BORROW_OR_RENT`：需求真实但短暂、低频；
- `BUY_USED`：值得拥有，但没必要承担新品折旧；
- `DO_NOT_BUY`：没有足够的真实缺口，或闲置风险更高。

## 真实流程示例：半马训练要不要换跑鞋？

```text
用户：我六周后要跑半马，要不要买双新跑鞋？

Buy or Bye：过去三个月实际跑步频率是多少？
用户：每周四次。

Buy or Bye：现在的跑鞋具体哪里已经不能满足训练？
用户：鞋底磨损明显，缓震也衰减了。

Buy or Bye：换鞋会不会造成明显的预算压力？
用户：不会。
```

最终判决：

```text
BUY · 建议购买

真实缺口：已有跑鞋磨损，无法可靠覆盖接下来的规律训练。
使用概率：每周四次，并且六周后有明确比赛。
关键未知：新鞋的尺码、稳定性和长距离脚感。
下一步：线下试穿或选择退换条件清楚的渠道，先完成一次短距离验证。
```

购买门槛通过之后，它才会继续帮你挑选具体跑鞋。

## 安装到 Codex

直接克隆到个人 Skills 目录：

```bash
git clone --depth 1 \
  https://github.com/siqili199206-commits/buy-or-bye.git \
  ~/.codex/skills/buy-or-bye
```

如果该目录已经存在，可以在目录内更新：

```bash
git -C ~/.codex/skills/buy-or-bye pull --ff-only
```

重新打开一个 Codex 任务后显式调用：

```text
使用 $buy-or-bye 帮我判断：我六周后要跑半马，目前每周跑四次，现有跑鞋鞋底已经明显磨损，要不要换？
```

它也允许自动触发，例如直接询问“这个商品值得买吗”。首次测试建议显式写出 `$buy-or-bye`。

## 工作方式

1. 找出购买背后的真实任务，而不是默认用户一定要买；
2. 每次只问一个可能改变结论的问题，通常不超过三轮；
3. 需要时核实价格、规格、促销和退换条件；
4. 分开呈现支持信号、阻力信号和未知项；
5. 给出明确判决、下一步，以及改变答案的条件；
6. 只有购买门槛通过后才进入具体选品；
7. 购买后可建议退换期、首次关键使用和闲置检查节点。

它不以返佣、广告、销量、热度或平台平均星级排序，也不会把所有因素压缩成一个看似精确的万能总分。

## 兼容性

| 平台 | 状态 |
|---|---|
| Codex Desktop | 已测试 |
| Codex CLI | 结构兼容，待扩大测试 |
| ChatGPT / Codex Plugin | 尚未包装提交 |
| Claude Code 等 Agent Skills 客户端 | 使用开放 `SKILL.md` 结构，尚未逐项验证 |

## 项目结构

```text
buy-or-bye/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── running-shoes-decision-card.png
│   └── running-shoes-decision-card.svg
├── evals/
│   └── prompts.csv
├── references/
│   ├── decision-framework.md
│   ├── output-contract.md
│   └── calibration-cases.md
└── scripts/
    └── validate_repo.py
```

## 验证

```bash
python3 scripts/validate_repo.py
```

测试集包含显式触发、自然触发、连续追问、不应触发和高风险边界场景。

## 贡献真实案例

欢迎通过 [Decision case issue](https://github.com/siqili199206-commits/buy-or-bye/issues/new?template=decision-case.yml) 提交匿名购物纠结。请删除订单号、地址、电话号码等个人信息。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 边界

对于医疗器械、治疗承诺、儿童安全、防护装备等高后果购买，本 Skill 只帮助整理需求与可核实事实，不替代专业人士或权威机构判断。

## 许可证

[MIT](LICENSE)
