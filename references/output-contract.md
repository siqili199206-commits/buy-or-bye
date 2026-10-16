# Output contract

## Default decision card

Respond in the user's language. Keep the first screen concise.

```markdown
## Verdict: [BUY / WAIT / VALIDATE FIRST / REUSE OR REPAIR / BORROW OR RENT / BUY USED / DO NOT BUY]

**One-line judgment:** [direct conclusion tied to the user's real task]
**Confidence:** [high / medium / low] — [brief reason]

### What decides it
- **For:** [strongest positive signal]
- **Against:** [strongest negative signal]
- **Unknown:** [decision-changing unknown, or “none material”]

### Do this next
[one concrete action, deadline, or test]

**Reopen the decision if:** [specific condition that would change the verdict]
```

Add the following only when they materially help:

- `Promotion check`: normal price, current price, retrieval date, and whether waiting is justified.
- `Options`: at most three product or non-purchase directions after the purchase gate passes.
- `Evidence boundary`: what came from the user, external sources, prior outcomes, inference, and what remains unverified.
- `Aftercare`: at most three post-purchase checkpoints.

Do not expose private chain-of-thought. Provide concise decision factors, evidence, assumptions, and uncertainty instead.

## JSON contract

Use only when requested or when another system needs structured output.

```json
{
  "capability_level": "L1 | L2 | L3",
  "verdict": "buy | wait | validate_first | reuse_or_repair | borrow_or_rent | buy_used | do_not_buy",
  "headline": "Direct one-sentence judgment",
  "confidence": {
    "level": "high | medium | low",
    "reason": "Why the decision is or is not stable"
  },
  "positive_signals": [
    {
      "name": "Meaningful signal",
      "strength": "high | medium | low",
      "fact": "Decision-relevant fact",
      "basis": "user | verified_external | prior_outcome | inference"
    }
  ],
  "negative_signals": [],
  "unknowns": [
    {
      "fact": "Unknown fact",
      "how_to_verify": "Lowest-cost validation",
      "impact": "How it may change the verdict"
    }
  ],
  "excluded_options": [],
  "candidates": [],
  "next_action": {
    "action": "One concrete action",
    "when": "Date, duration, or triggering condition"
  },
  "what_changes_the_answer": [],
  "aftercare_plan": [],
  "sources": [
    {
      "title": "Source title",
      "url": "https://example.com",
      "retrieved_at": "YYYY-MM-DD",
      "supports": "Claim supported"
    }
  ]
}
```

Do not add empty precision. Arrays may be empty, and unknown values should remain explicit rather than guessed.
