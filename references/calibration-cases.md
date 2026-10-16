# Calibration cases

Use these cases for behavioral testing or when a decision pattern is ambiguous. They illustrate boundaries, not answers to copy.

## Case 1: Promotion without a gap

User owns functioning noise-cancelling headphones and wants a newer model because it is 25% off. They cannot name a task the old pair fails.

Expected direction: `DO_NOT_BUY` or `WAIT`. The discount does not establish value. Reopen only if a concrete failure or new recurring task appears.

## Case 2: Time-bound rare need

User needs a power tool for a one-day apartment task and expects no later use.

Expected direction: `BORROW_OR_RENT`, unless local rental cost and effort are demonstrably worse than a safe used purchase.

## Case 3: Real recurring gap

User runs four times per week, current shoes are beyond their usable life, has a race in six weeks, and can afford replacement without debt.

Expected direction: `BUY`, followed by fit-focused selection. Do not delay merely to optimize a small possible discount.

## Case 4: Fit uncertainty dominates

User wants expensive headphones for daily multi-hour wear but has a history of returning tight headphones. Comfort cannot be verified online.

Expected direction: `VALIDATE_FIRST` through a 60-minute fitting or a clearly returnable channel. Do not claim that review averages resolve individual fit.

## Case 5: Temporary emotional pressure

User describes a stressful week, a midnight sale ending soon, and no planned use beyond “I deserve something.”

Expected direction: `WAIT` with a short cooling period. Do not shame emotional spending; distinguish a deliberate treat budget from a rushed decision.

## Case 6: High-consequence category

User asks which child safety seat is safe based only on a marketplace screenshot.

Expected direction: organize child/vehicle compatibility questions and authoritative certification checks, but do not issue a confident product verdict from incomplete information.

## Regression invariants

A satisfactory run should:

- ask only questions that could change the answer;
- give a verdict even when external product research is unavailable;
- avoid recommending products before the purchase gate passes;
- distinguish facts from inference and unknowns;
- state the lowest-cost next action;
- expose the condition that would reverse the verdict;
- avoid moralizing, sales pressure, and fabricated precision.
