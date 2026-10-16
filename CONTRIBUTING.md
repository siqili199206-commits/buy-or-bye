# Contributing

Contributions are welcome when they improve a recognizable purchase-decision workflow without turning the skill into a generic product recommender.

## Submit a decision case

Use the `Share a decision case` issue form. Remove names, addresses, order numbers, phone numbers, payment details, and account identifiers.

A useful case contains:

- the real task behind the purchase;
- recent behavior rather than aspiration alone;
- owned substitutes;
- budget or timing pressure when relevant;
- the unknown most likely to change the verdict;
- the expected direction, if one exists.

## Propose a change

1. Add or update a prompt in `evals/prompts.csv` that demonstrates the problem.
2. Make the narrowest instruction or reference change that fixes it.
3. Run `python3 scripts/validate_repo.py`.
4. Explain the observed failure and why the change corrects it.

Avoid rules that merely force a preferred phrase or heading. Tests should focus on observable behavior: whether the skill asks a decision-changing question, avoids premature product recommendations, distinguishes facts from inference, and produces an actionable verdict.
