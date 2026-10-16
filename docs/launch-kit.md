# Buy or Bye launch kit

Replace `<REPO_URL>` with `https://github.com/siqili199206-commits/buy-or-bye` when a platform does not render Markdown links.

## 小红书

### 标题

我做了一个先判断“该不该买”的 AI

### 正文

大多数 AI 购物助手一上来就在回答“买哪一双”。

我做的这个会先问：这次购买本身应该发生吗？

我拿“六周后跑半马，要不要换跑鞋”试了一次。它只问了三个真正影响结论的问题：

1. 过去三个月实际跑步频率是多少？
2. 现在的鞋具体哪里不能满足训练？
3. 换鞋会不会造成明显预算压力？

答案是：每周跑四次、旧鞋鞋底明显磨损、预算可以承受。

最后判决是 BUY，但它没有马上推商品，而是先提醒：新鞋的尺码、稳定性和长距离脚感仍然未知，应该试穿，并先完成一次短距离验证。

它也可能劝你等待、维修旧物、租借、买二手，或者直接不买。

我把它做成了一个开源 Agent Skill：Buy or Bye。

GitHub：<REPO_URL>

如果你有一件正在纠结的东西，可以把“商品、为什么想买、已有替代品”留在评论区。

## 即刻

没有资源先做 App，所以我把 Aura 的 Decision Core 拆成了一个开源 Skill。

它只有一条硬规则：没有先证明这次购买值得发生，就不允许进入具体选品。

第一次公开案例换成了跑鞋：每周跑四次、六周后半马、旧鞋已经明显磨损。结论是可以买，但先验证脚感，再选具体型号。

这不是“反消费”，而是把买、等、维修、租借、二手和不买放回同一张决策桌上。

代码和方法都开源了：<REPO_URL>

现在想征集第一批匿名案例。留下一件你正在纠结的东西，我会用它跑一遍完整判断。

## X / Twitter

Most AI shopping assistants start with: “Which one should I buy?”

Buy or Bye starts one step earlier: “Should this purchase happen at all?”

The launch case is a runner training four times a week for a half marathon in six weeks, with visibly worn shoes. Verdict: BUY — but validate fit and short-run comfort before selecting a model.

First-class outcomes also include Wait, Repair, Rent, Buy Used, and Don’t Buy.

Open source: <REPO_URL>

## Reddit / Show HN

Title: Buy or Bye — an open-source agent skill that decides whether a purchase should happen

I built Buy or Bye because most AI shopping assistants assume the transaction should happen and optimize only for product selection.

This skill places a purchase gate before recommendations. It asks at most one decision-changing question at a time, distinguishes verified facts from inference and unknowns, and returns one of seven actionable verdicts.

The launch example is intentionally ordinary: replacing running shoes before a half marathon. The user runs four times a week, the current outsole is worn, and the race is six weeks away. The purchase passes, but model selection is deferred until fit and short-run comfort can be validated.

The repository includes the skill, decision framework, output contract, calibration cases, and a positive/negative evaluation prompt set.

Repository: <REPO_URL>
