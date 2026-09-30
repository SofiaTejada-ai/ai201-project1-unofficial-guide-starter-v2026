# The Unofficial Guide

**Sofia Tejada** — corpus: `campus_life`

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.

---

# Unit 1

## What This Does

The Unofficial Guide answers questions about student life using the `campus_life` corpus — 88 short, real-world posts about dining halls, housing, courses, and administrative rules that aren't explained clearly anywhere official. It answers specific, factual questions with a right answer, like "when is the deadline to add a course?" or "how often can you change your meal plan tier?" — not open-ended opinions like "what's a good dorm?" Every answer is grounded in the retrieved documents and names its source, and the system refuses questions its corpus doesn't cover instead of guessing.

## Chunking Strategy

**Chunk size:** Whole document — no fixed character limit. Average ~317 characters, ranging 178–549.
**Overlap:** None — each document becomes exactly one chunk, so there's nothing to overlap.

The starter's 800-character fixed-size chunker never actually split anything in this corpus, since the longest document is only 549 characters — but that was incidental, not a decision. Once I read the documents, I could see why it didn't matter: campus_life posts already pack one complete thought into a single short document, often as one or two dense statements or a couple of related facts (like a dining hall's narrative plus its hours/cost). Splitting further would only cut a self-contained thought in half. So I replaced the chunker to treat each document as one chunk on purpose, rather than relying on a threshold no document happened to reach.

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt` — produced by: `chunker.py::split_documents`

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

**Chunk 2** — source: `course_biol_160.txt` — produced by: `chunker.py::split_documents`

BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

**Chunk 3** — source: `course_hist_118_workload.txt` — produced by: `chunker.py::split_documents`

Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt` — produced by: `chunker.py::split_documents`

Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

**Chunk 5** — source: `housing_innisfree_hall.txt` — produced by: `chunker.py::split_documents`

Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

**Question:** is the housing lottery random?

**Answer:** The housing lottery is not entirely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, with random tie-breaks used only for ties.

Source: admin_housing_lottery.txt

**My relevance cutoff:** 0.6 (the starter's default — kept as-is)

My five in-corpus questions had best distances of 0.234–0.347. My five out-of-scope questions had best distances of 0.825–0.934. That's a gap of about 0.478 with nothing in it, and 0.6 sits almost exactly in the middle of that gap — so I kept the default rather than moving it, since nothing in my data pointed anywhere else.

| Question | In corpus? | Best distance |
|---|---|---|
| When is the deadline to add a course? | Yes | 0.311 |
| For BIOL 160 Cell Biology, is the assessment curved? | Yes | 0.279 |
| How often can you change your meal plan tier, and how much time do you have? | Yes | 0.243 |
| For ECON 101, how many tests are there and are they all multiple choice? | Yes | 0.347 |
| When do study abroad applications open? | Yes | 0.234 |
| What is the capital of Mongolia? | No | 0.825 |
| How do I change the oil in a diesel engine? | No | 0.934 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.844 |
| How do I write a for loop in Rust? | No | 0.896 |

## How I Used AI

**1.** I hit a `TypeError: Number of requested results 0, cannot be negative, or zero` error when I ran `ask`. I asked Claude what it meant, and it explained the mechanism: my `index` run had gotten interrupted partway, leaving an empty vector store on disk, so the query asked for zero results. I deleted `chroma_db/` and re-ran `index` to completion, which fixed it.

**2.** For Milestone 3, I decided on my own chunking strategy — one document equals one chunk, since I'd read that campus_life posts already pack one complete thought each — but asked Claude to write the actual `split_documents` function for me. It matched what I described; I didn't need to change anything, since the decision (not splitting) was simple enough that there wasn't much room for it to guess wrong.

---

# Unit 2

# Unit 2

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk length matches a complete thought | 267–367 chars (avg) | 317 (one-time measurement — see Milestone 3) | — | — | MET |
| 5. Source attribution accuracy | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Full run log: `results/run_2026-09-23_1542.md`, produced by `run_eval.py::main`.
`scorer.py` doesn't exist yet, so these counts are my own judgment from reading
every answer — not automated.

**Real output** (one example per question, run 1 — full transcript of all 15 runs is in the committed results file):

### Criterion 1 & 5 — "When is the deadline to add a course?"

- Best distance: 0.3111 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160_workload.txt, course_cs_340.txt

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All three runs came back 5/5, not just the minimum 4/5 the target needed, and since retrieval is deterministic, the same sources came back every run, so it wasn't a lucky pass. |
| 2 | Every answer names a source | MET | All 15 answers (5 questions × 3 runs) named at least one source file explicitly, in every run. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5 refused in one deterministic pass, consistent with the huge 0.478-wide distance gap I measured back in Milestone 4. |
| 4 | Chunk length matches a complete thought | MET | The chunker's own summary line reports an average of exactly 317 characters, dead center of my 267–367 target range. |
| 5 | Source attribution accuracy | MET | Every named source actually contained the answer when I checked the underlying document myself, including the two-source citations on the BIOL 160 question; both files independently say "not curved." |

**A note on why everything passed so cleanly:** I designed my five test questions to be easy on purpose. I wanted to see how well Gemini 3.5 Flash-Lite performs at a baseline level before pushing it further, so I deliberately picked topics where the answer sits explicitly in one chunk (and since my chunking strategy is one document per chunk, that meant picking documents whose entire content is the answer, start to end, with nothing else mixed in). Retrieval and generation had very little room to fail with material shaped like that. A harder question set, one that needs two chunks combined, or asks something only implied rather than stated outright, would be a much more interesting test of where this system actually breaks.

## Diagnoses

I didn't miss any of my five criteria, on any of the three runs. That's not to say my system is automatically excellent, it could very well mean my criteria and test questions were set too easy. I designed my five test questions deliberately on the nose as base testing. Each one's answer sits explicitly in a single chunk (and since my chunking strategy is one document per chunk, that meant picking documents whose entire content is the answer), so retrieval and generation had very little room to fail.

On two of my five questions ("is BIOL 160 curved?" and "how many tests does ECON 101 have?"), the model cited two source files instead of one. I checked both cases by hand, and both citations are genuinely correct, `course_biol_160.txt` and `course_econ_101.txt` each independently restate the same fact their matching exams document states. So this isn't a retrieval failure (both documents are legitimately relevant) and it isn't a hallucination (nothing cited is wrong), it's that my corpus has redundant information, the general course overview and the course specific exams doc both happen to say the same thing. My criterion 5 as written ("the source named matches the document that contains the answer") is lenient enough to count this as a pass, since every source named is correct.

If I were tightening a criterion, I'd tighten criterion 5 so that "For at least 4 of my 5 test questions, exactly one source is named, and it's the single most relevant document." Under that stricter version, this run would have missed 2 of 5, since two questions named an extra, redundant source. That's the honest weak spot my current criteria are too loose to catch.

## The Improvement

**What I changed:**

Replaced my Milestone 3 chunker (one document = one chunk) with paragraph splitting: `chunker.py::split_documents` now splits each document on blank lines, so a document with a title and two paragraphs becomes three separate chunks instead of one.

**Why I picked it:**

I wanted to test Gemini at a more basic level rather than assume my perfect Unit 1 score meant the system was excellent. My chunker kept every document whole, which meant every chunk was already small and topically clean, so I wanted to see whether the clean result was really about the pipeline or just about how easy the chunks were.

### Run Log — After (paragraph-splitting)

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk length matches a complete thought | 267 to 367 chars (avg) | 101 (one time measurement, see below) | | | MISSED |
| 5. Source attribution accuracy | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |

Full run log: `results/run_2026-09-27_2139_after.md`, produced by `run_eval.py::main`.

**Chunking summary (produced by `chunker.py::split_documents`, printed by `python app.py index`):** 271 chunks, 101 characters average, shortest 10, longest 373. Compare to before: 88 chunks, 317 average, shortest 178, longest 549.

**Real output, the one question that changed behavior:**

### For ECON 101, how many tests are there and are they all multiple choice? — run 1

- Best distance: 0.4424 (passed the gate)
- Sources retrieved: course_biol_160_exams.txt, course_cs_210_exams.txt, course_econ_101.txt, course_econ_101_exams.txt, course_econ_101_workload.txt
I do not have enough information to answer how many tests there are for ECON 101 or whether they are all multiple choice (Source: course_econ_101_exams.txt, course_econ_101.txt, course_econ_101_workload.txt).


### For ECON 101, how many tests are there and are they all multiple choice? — run 2
I do not have enough information to answer this question from the provided documents.


**Retrieval check that shows why (`python app.py retrieve`, same question):**
distance source preview
1 0.4424 course_econ_101_exams.txt ECON 101 Introduction to Economics — assessment...
2 0.5226 course_econ_101.txt ECON 101 Introduction to Economics...
3 0.5324 course_econ_101_workload.txt Workload for ECON 101 Introduction to Economics...
4 0.5601 course_biol_160_exams.txt Four unit tests and a cumulative final. Not curved....
5 0.5732 course_cs_210_exams.txt Do the labs even though they're only 10% — the exams...


The top 3 results are all title only fragments ("ECON 101 Introduction to Economics", "ECON 101 Introduction to Economics — assessment", "Workload for ECON 101 Introduction to Economics"). Paragraph splitting cut each document's title onto its own line before the first blank line, which turned it into its own tiny chunk. That title fragment matches the question's course name keywords just as well as the real content does, without carrying any of the actual fact, so it crowded the answer bearing paragraph out of the top 5 entirely.

**Did it help?**

No. It made things measurably worse. Criterion 2 (every answer names a source) went from a clean 5/5 on all three runs to missing on two of three runs, and criterion 4 (chunk length) went from a dead center 317 characters to 101, far outside my target range. The mechanism, confirmed with `python app.py retrieve`, is that several of my documents start with a short title line before their first blank line, and splitting on paragraphs turned each title into its own tiny, generic chunk. For the ECON 101 question, those title fragments ranked ahead of the actual answer bearing paragraph in retrieval, so the model correctly refused to answer rather than guess, since it genuinely was not shown the fact. Criteria 1 and 5 still held, but only at the exact minimum (4 of 5) instead of comfortably (5 of 5), so the system got measurably more fragile even where it did not outright fail.

### Fixing the bug and re-testing (response to feedback)

After finding the title-fragment problem above, I fixed `chunker.py::split_documents` to merge a short first paragraph (under 60 characters, almost always a title) into the paragraph that follows it, instead of leaving it as its own chunk. I checked the chunk distribution *before* running the full eval this time: 183 chunks, 151 characters average, shortest 36, longest 397 — no more 10-character fragments.

I also built `scorer.py`, a `judge(question, expects, answer, results) -> bool` function that checks three things automatically: the answer isn't a refusal, it contains the `expects` phrase from `questions.py`, and it names at least one of the retrieved source files. `run_eval.py` picks this up automatically and fills in real pass/fail instead of leaving the Run columns for me to judge by eye.

**Run Log — Before, re-confirmed with `scorer.py`** (`results/run_2026-09-30_1458_before-scored.md`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Run Log — After, fixed chunker, scored with `scorer.py`** (`results/run_2026-09-30_1452_after-scored.md`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk length matches a complete thought | 267–367 chars (avg) | 151 (one-time measurement) | | | MISSED |
| 5. Source attribution accuracy | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Real output, ECON 101 (previously the one that broke) — now passing:**
For ECON 101, there are three tests (two midterms and a final), and they are all multiple choice (Sources: course_econ_101.txt and course_econ_101_exams.txt).


- Best distance: 0.4727 (passed the gate, up from 0.3467 before, but still comfortably under 0.6)

**Did it help, after the fix?** Partially. Fixing the title-fragment bug genuinely resolved the ECON 101 failure; criteria 1, 2, 3 and 5 now score identically before and after, confirmed automatically rather than by my own read-through. But criterion 4 is still missed: even with the fix, paragraph-splitting produces a 151-character average, well under my 267–367 target, because most paragraphs in this corpus are just shorter than a whole document. The improvement is no longer actively harmful, but it still doesn't meet the one criterion it was always going to struggle with, chunk size, and it didn't improve anything an easy question set could detect.
2. Update ## What's Still Broken to this
## What's Still Broken

**Criterion 4 (chunk length)** is still missed, even after fixing the title-fragment bug. Paragraph-splitting fundamentally produces smaller chunks than my 267–367 target, since most paragraphs in this corpus are shorter than a whole document. The real fix would be reverting to my Milestone 3 chunker (one document = one chunk), which measured 317, dead center of the target, or raising a merge threshold so short paragraphs combine with neighbors more aggressively. I didn't do either, since this unit's rule was one change, one fix, not a second redesign on top of the first.

Everything else (criteria 1, 2, 3, 5) is now MET and confirmed by an automated scorer rather than my own reading, which was the main gap a reviewer pointed out in my first submission.
3. Add a third How I Used AI moment
**4.** After getting feedback that my scoring was entirely manual and my chunker shipped without validating its own output, I asked Claude to help me build `scorer.py`. It proposed checking for a refusal, the `expects` phrase, and a cited filename, then I decided the specific logic should be all three required together, not any one alone. I also had it walk me through checking the chunk-length distribution with `python app.py index` before running the full eval again, which is a validate-first habit I hadn't been using.


## What's Still Broken
Criterion 4 (chunk length) is still broken. Paragraph splitting produces a lot of very short title-only fragments (shortest chunk is 10 characters), which drags the average down to 101, far under my 267–367 target. The real fix is either merging a title fragment into the paragraph that follows it instead of keeping it as its own chunk, or reverting to my Milestone 3 chunker (one document = one chunk), which actually measured better on every criterion. I didn't do either in this unit, since the rule was one change only, and reverting would just be undoing the change rather than measuring it.

Criterion 2 (every answer names a source) is still broken. When the model has to refuse because the real chunk wasn't retrieved, it sometimes drops the source citation entirely, since the grounding instruction only tells it to name a source when it answers, not what to do when it can't. The fix would be tightening GROUNDING_INSTRUCTION to say something like "even when you don't have enough information, name which documents you did check." I didn't make this change because it wasn't the one improvement I picked for this unit, and the rule was to measure one change at a time, not stack a second fix on top of the first without knowing which one caused what.

## What I'd Do Differently

Two things. First, I'd tighten criterion 5 to require exactly one source named, not "at least one correct one", the redundant two-source citations in Unit 1 were a real gap my original wording let through. Second, I'd write harder test questions from the start rather than five easy, on-the-nose ones. My Unit 1 questions were so easy that every criterion passed cleanly before I changed anything, which told me nothing about where my system actually breaks. It was only after deliberately breaking my own chunking that I found a real, honest failure. A test that can't fail isn't testing anything.

Addition to "How I Used AI" 

In Unit 2, my ECON 101 question started failing after I switched to paragraph-splitting, but the "Sources retrieved" list still showed the right files, which confused me. I asked Claude why a source could be listed but the answer still come back wrong, and it suggested re-running python app.py retrieve on that exact question to see the actual chunk previews instead of just the filenames. That surfaced the real mechanism: the top 3 results were all title-only fragments, not the paragraph with the actual fact. I hadn't thought to check chunk-level detail instead of file-level detail until that was pointed out.