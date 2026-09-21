# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

My documents put the answer in one explicit sentence, so I expect this to be
an easy target, since there's no inference required. I'm keeping it at 4 of 5
rather than 5 of 5 anyway: one unlucky retrieval (two similar admin documents
landing close in distance) shouldn't fail the whole criterion when the system
is otherwise working as intended.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

Naming a source is a simple instruction-following task rather than something
requiring reasoning, so I expect the model to get it right every time. Gemini
3.5 Flash-Lite is a lighter model, which makes me a little less confident than
I'd be with a larger one, but since the grounding instruction tells it to name
a source on every answer, I don't expect it to drop that instruction even if
it occasionally struggles with harder judgment calls.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**

I expect the gate to have a harder time than criteria 1 and 2, since
embeddings can pick up on shared wording even when topics are genuinely
unrelated — a question about "a for loop in Rust" could still land closer to
a course-related chunk than I'd like, just from overlapping vocabulary. That's
why I'm not expecting a perfect 5 of 5: I want room for one edge case without
treating the whole gate as broken.

> **Milestone 4 update:** The gap turned out even cleaner than expected — my
> in-corpus questions maxed out at 0.347 and my out-of-scope questions
> started at 0.825, a 0.478-wide gap with nothing in it. I kept the default
> 0.6 cutoff since it already sits in the middle of that gap.

---

## 4. Chunk length matches a complete thought

After I build my own chunker, the average chunk length lands within 50
characters of my corpus's average document length (~317 characters) — i.e.
roughly 267 to 367 characters.

**Why this target:**

My campus_life documents already pack an answer into one to three sentences,
and the starter's own chunking summary already reports ~317 characters as the
average document length for this corpus. A chunk near that size already holds
one full post's worth of thought, so I want my chunker's average chunk length
to land in that same range rather than drifting much smaller (cutting a
thought in half) or much larger (merging unrelated posts together).

---

## 5. Source attribution accuracy

For at least 4 of my 5 test questions, the source named in the answer matches
the document that actually contains the answer.

**Why this target:**

The system retrieves up to five chunks per question (top-k=5), not just the
one with the answer, so there's a real chance Gemini 3.5 Flash-Lite cites a
source it merely retrieved rather than the one it actually drew the answer
from. I don't expect the answer content itself to be wrong — that's already
covered by criterion 1 — just that with several plausible-looking sources in
front of it, the model could mix up which one it names.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->