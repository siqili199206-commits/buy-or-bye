# Buy or Bye

English · [简体中文](README.md)

[![Release](https://img.shields.io/github/v/release/siqili199206-commits/buy-or-bye)](https://github.com/siqili199206-commits/buy-or-bye/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A consumer-first Agent Skill that **decides whether a purchase should happen before recommending what to buy.**

![Running-shoe purchase verdict](assets/running-shoes-decision-card.png)

## Why it is different

Most shopping assistants start with “Which one should I buy?” Buy or Bye starts one step earlier: “Should this purchase happen at all?”

> No product recommendation until the purchase itself passes the purchase gate.

Its first-class outcomes are `BUY`, `WAIT`, `VALIDATE_FIRST`, `REUSE_OR_REPAIR`, `BORROW_OR_RENT`, `BUY_USED`, and `DO_NOT_BUY`.

## Example: replace running shoes for half-marathon training?

The user runs four times per week, has a half marathon in six weeks, and reports visible outsole wear and declining cushioning in the current pair. Replacing the shoes does not create budget pressure.

```text
BUY

Real gap: the current pair no longer reliably supports regular training.
Likely use: four runs per week and a concrete race deadline.
Key unknown: fit, stability, and long-run comfort in the new pair.
Next action: try the shoe in person or buy through a channel with clear returns,
then validate it on a short run before committing to long-distance use.
```

Only after this gate passes does the skill move into specific product selection.

## Install in Codex

```bash
git clone --depth 1 \
  https://github.com/siqili199206-commits/buy-or-bye.git \
  ~/.codex/skills/buy-or-bye
```

Update an existing installation:

```bash
git -C ~/.codex/skills/buy-or-bye pull --ff-only
```

Start a new Codex task and invoke it explicitly:

```text
Use $buy-or-bye to decide whether I should replace my running shoes. I run four times a week, have a half marathon in six weeks, and the current outsole is visibly worn.
```

The skill also supports implicit activation for questions such as “Is this product worth buying?” Explicit invocation is recommended for the first test.

## How it works

1. Identify the real task behind the purchase.
2. Ask one decision-changing question at a time, normally no more than three.
3. Verify volatile product facts only when they could change the verdict.
4. Separate supporting signals, opposing signals, and unknowns.
5. Give a verdict, one next action, and the condition that would reverse the answer.
6. Recommend specific products only after the purchase gate passes.

It does not rank by affiliate revenue, sponsorship, popularity, or marketplace star averages. It also avoids a misleading universal score.

## Compatibility

| Platform | Status |
|---|---|
| Codex Desktop | Tested |
| Codex CLI | Structurally compatible; broader testing pending |
| ChatGPT / Codex Plugin | Not packaged or submitted yet |
| Other Agent Skills clients | Uses an open `SKILL.md` structure; not individually verified |

## Validate

```bash
python3 scripts/validate_repo.py
```

The prompt set covers direct and indirect activation, follow-ups, negative controls, and high-consequence boundaries.

## Contributing

Submit an anonymized shopping dilemma through the [decision-case issue template](https://github.com/siqili199206-commits/buy-or-bye/issues/new?template=decision-case.yml). Remove order numbers, addresses, phone numbers, and other personal information. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Safety boundary

For medical devices, treatment claims, child safety, protective equipment, and other high-consequence purchases, the skill organizes needs and verifiable facts but does not replace qualified professional or authoritative guidance.

## License

[MIT](LICENSE)
