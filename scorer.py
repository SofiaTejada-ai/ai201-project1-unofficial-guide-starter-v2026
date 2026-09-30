"""
scorer.py

Automated scoring for run_eval.py, so criteria 1, 2 and 5 stop depending on
me reading 15 answers by eye. run_eval.py imports this automatically if it
exists (see load_scorer() there) and fills in the Run columns with real
pass/fail instead of leaving them blank.

The rule: an answer counts as correct if
  1. it isn't a refusal, AND
  2. it contains the expected fact (the `expects` phrase from questions.py,
     matched case-insensitively), AND
  3. it names at least one of the source files that was actually retrieved.

Check 3 makes this a combined check for content correctness AND source
naming at once, on purpose - an answer that gets the fact right but forgets
to cite anything still fails here.
"""

REFUSAL_MARKERS = (
    "i don't have enough information",
    "i do not have enough information",
)


def judge(question: str, expects: str, answer: str, results) -> bool:
    if not answer:
        return False

    answer_lower = answer.lower()

    if any(marker in answer_lower for marker in REFUSAL_MARKERS):
        return False

    if expects and expects.lower() not in answer_lower:
        return False

    sources = {r.source.lower() for r in results}
    if not any(source in answer_lower for source in sources):
        return False

    return True