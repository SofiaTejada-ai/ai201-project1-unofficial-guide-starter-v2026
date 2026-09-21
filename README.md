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

<!-- Not yet — this is next unit's work. -->

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

## The Improvement

**What I changed:**

**Why I picked it:**

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

## What's Still Broken

## What I'd Do Differently