# PSYC 220 Fall 2026 — assignment and exam plan

How the 20 assignments and 6 exams are built from the Spring 2026 question bank.
Companion to `syllabus.md`. Drafted August 2026.

## Source material

`export/PSYC220-BBB-SPRING-2026__1339466_1_…_1786946687232/` — a Blackboard course
archive holding the Spring assignments as QTI XML in `res000NN.dat`:

- **190 questions** across 10 homework + 10 lab assignments (169 Multiple Answer,
  16 Numeric, 5 Either/Or, plus 5 stem-only blocks)
- Spring exams as PDFs in the project root: **170 items** (40 + 40 + 40 + 50),
  of which ~154 are unique — Exam 3 repeated 9 stems verbatim from Exam 2, and
  the final repeated 7 from Exam 3

## Design principle: question families

Every exam question has an **assignment sibling**: same structure, different
numbers. The assignment version is practice, the exam version a fresh instance.
Spring already worked this way — Lab 8 is ten pre/post *t* problems differing
only in data.

This means most "new" exam questions are renumbered instances, not new writing.
What genuinely has to be authored is a missing *family*, and there are about 16.

### Repeating a stem verbatim — deferred until after Exam 1

Spring repeated 16 stems verbatim across exams: 9 from Exam 2 on Exam 3, and 7
from Exam 3 on the final. This was deliberate, aimed at the items students most
often get wrong, not padding.

The Exam 3 item analysis is consistent with that. Of 30 forms scored (class
average 30.0/40), the ten repeated items averaged **7.6 wrong** (25%) while the
fifteen fresh items on the same pass averaged **6.5** (22%) — the repeats stayed
the harder items even on a second exposure. Read from a photographed scantron
form, so treat as indicative; no Exam 2 analysis survives, so we cannot tell
whether repetition reduced the error rate from first exposure.

**Decision deferred until after Exam 1 (9/3).** That exam gives a clean baseline:
which items produce errors, and at what rate. Then choose between

- repeating the high-error stems verbatim on the next exam, as Spring did, or
- re-instancing them as the same family with different numbers, which tests the
  skill rather than recall of a specific item.

Either way, identify the candidates from Exam 1's item analysis rather than by
intuition, and keep the scantron form — it is the only record of item difficulty
the course produces.

## Exam format

**Tentatively 30 questions × 2 points = 60 points**, possibly rising to 40.
Both divide cleanly into 60:

| Questions | Points each | One error costs | Items across 6 exams |
|:--:|:--:|:--:|:--:|
| **30** (tentative) | 2.0 | 3.3% | 180 |
| 40 | 1.5 | 2.5% | 240 |

Spring used 40 questions at 2.5 points, 50 on the final — 170 items across four
exams. At 30 the Fall course sits slightly above that; at 40 it is roughly 40%
more. Forty gives finer granularity and broader topic coverage per exam, at the
cost of a longer sitting in a 75-minute period and more items to build.

Length does not change the plan below. Each exam still draws on the same
assignments and the same question families; going to 40 means more instances per
family, not new families. Decide before Exam 1 is assembled, since the split
across topics scales proportionally.

**Exams are entirely multiple choice.** They are answered on scantrons, so there
are no numeric-entry, short-answer, or written items. A computed value is asked
for by offering it among plausible alternatives — Spring's Lab 9 and Lab 11
already pose computations this way.

**Assignments are mostly multiple choice, and may occasionally use numeric
entry** where typing the computed value is the point. Spring used numeric entry
for 16 of 190 items (8%), concentrated where students first compute by hand:
Homework 2 (6 items — mean, median, mode, SS, variance, SD), Lab Week 3
(9 items — the same statistics again), and one summation in Homework 1.

Keep that proportion. A numeric item on an assignment must have a multiple-choice
counterpart for the exam: same problem, the correct value among distractors drawn
from the usual errors — dividing by *n* instead of *n* − 1, forgetting the square
root, using the range instead of the IQR. Set a rounding tolerance on every
numeric assignment item; rounding is the main source of false negatives in
auto-graded statistics work.

## Assignments to exams

| Part | Exam | Date | Assignments | Topics |
|---|---|---|---|---|
| 1 — Describing data | Exam 1 | Thu 9/3 | A1–A4 | 1–4 |
| 2 — Distributions and sampling | Exam 2 | Thu 9/24 | A5–A9 | 5–8 |
| 3 — Inference with one sample | Exam 3 | Tue 10/13 | A10–A13 | 9–12 |
| 4 — Comparing two means | Exam 4 | Thu 10/29 | A14–A16 | 13–14 |
| 5 — The general linear model | Exam 5 | Thu 11/19 | A17–A20 | 15–17 |
| — | Final | Tue 12/8 | — | 1–17 |

Each assignment is 10 points; each is released with the class whose topic it
follows and is worked through in lab where the TA covers it.

## The 20 assignments

Sources: `HW` = Spring homework, `Lab` = Spring lab assignment, `E1`–`E4` =
Spring exams 1–4.

| # | Assignment | Topic | Draw from | Pool | New |
|:--:|---|:--:|---|:--:|:--:|
| A1 | Math review & basic concepts | 1–2 | HW1 · Lab1 · Lab2 · E1 Q1–13 | 18 | — |
| A2 | Central tendency & graphs | 3 | HW2 Q2–4,8,9 · Lab3 Q1–3,11 · E1 Q14,15,17 | 13 | — |
| A3 | Spread & variability | 4 | HW2 Q5–7,10,11 · Lab3 Q4–10 · E1 Q16,18–20 | 22 | — |
| A4 | Part 1 mixed review | 1–4 | HW1 Q2–4,7 · Lab1 Q1,3,4 · Lab2 Q2 · E1 Q33–38 | 15 | **1** |
| A5 | z-scores | 5 | HW3 Q6–10 · Lab4 Q1–6 · E1 Q21–26 | 17 | — |
| A6 | Probability | 6 | HW4 Q4,5,7,10 · Lab6 Q1,3–10 | 13 | — |
| A7 | Standard normal distribution | 5 | HW4 Q1–3,6,8,9,11 · Lab4 Q7–10 · E1 Q27–32,39,40 | 19 | — |
| A8 | **Sampling distributions** | 7 | HW5 Q8 · E2 Q1–4 · E3 Q1,2 | 6 | **4** |
| A9 | **Central Limit Theorem** | 8 | HW5 Q1 · Lab6 Q2 · E2 Q20 · E3 Q9 | 4 | **6** |
| A10 | Hypothesis testing | 9 | HW5 Q2,3,6,7 · Lab7 Q1–3 · E2 Q5,8,11 | 10 | — |
| A11 | Errors & effect size | 10 | HW5 Q4,5,9,10 · Lab7 Q4–6,9,10 · E2 Q6,7,13 | 13 | — |
| A12 | **Confidence intervals** | 11 | HW6 Q1 · Lab7 Q7,8 · E2 Q12,17 · E3 Q4 | 6 | **4** |
| A13 | One-sample *t*-test | 12 | HW6 Q2–11 · E2 Q14–19,34–40 | 21 | — |
| A14 | Dependent-samples *t* | 13 | HW7 Q5–8 · Lab8 · Lab9 Q8–10 · E3 Q11–19 | 27 | — |
| A15 | Independent-samples *t* | 14 | HW7 Q1–4 · HW8 Q2–5 · Lab9 Q1–7 · E3 Q20–27 · E4 Q38–43 | 31 | — |
| A16 | Which *t*-test when | 12–14 | surplus from A13–A15 | 15 | — |
| A17 | ANOVA concepts | 15 | HW8 Q6–12 · Lab11 Q9,10 · E3 Q28–31,39,40 | 15 | — |
| A18 | **ANOVA computation** | 15 | E3 Q32–38 · E4 Q44–49 | 13 | **2** |
| A19 | Correlation | 16 | HW9 · Lab11 Q1–5 · Lab12 Q1–5 · E4 Q14–24 | 32 | — |
| A20 | Regression | 17 | HW10 · Lab12 Q6–10 · E4 Q25–37 | 28 | — |

## Built so far (as of 9/6)

A5–A9 and Exam 2 are drafted; everything for Exam 2 on Thu 9/24 now exists.

| # | Title | Topic | Taught | Sourced / new |
|:--:|---|:--:|:--:|:--:|
| A5 | z-scores                     | 5 | Tue 9/8  | 10 / 0 |
| A6 | Probability                  | 6 | Thu 9/10 |  9 / 1 |
| A7 | The standard normal distribution | 5 | Tue 9/15 |  8 / 2 |
| A8 | Sampling distributions       | 7 | Thu 9/17 |  6 / 4 |
| A9 | Central Limit Theorem        | 8 | Tue 9/22 |  3 / 7 |

Exam 2 is 30 questions at 2 points, in the planned 9/7/8/6 shape, and every
question mirrors a family the students worked in A5–A9. Built by
`exams/build_exam2.py`; keys land 8/7/8/7 across A/B/C/D.

Mock Exam 2 has the same shape: 20 items straight from A5–A9 (choosing the
assignment items Exam 2 did *not* use) and 10 from the same families with fresh
values. `build_mock2.py` asserts that no keyed answer appears on Exam 2 — it
caught a `z = 1.50` collision on the first run — and that the two papers' answer
sequences differ, which they did not at first, because balancing both with the
same pattern gave them an identical key.

**The Spring pool for A8 and A9 was thinner than this document assumed.** Spring
Exam 3 Q1 and Q2 are verbatim copies of Exam 2 Q1 and Q4, so the six items
credited to A8 are really five, and A9's four are three. The shortfall was
written rather than stretched: A9 in particular is now mostly new items covering
what the CLT claims about the centre and the spread of the sampling
distribution, a small-*n* skewed case, and two computations.

**Conditional probability is assigned but not lectured.** A6 Q9 and Q10 and
Exam 2 Q16 ask for probabilities within a subgroup. The Lecture 7 deck covers
classical probability and the frequency table but never names conditional
probability. Either add a slide or drop those items.

## Key position must be balanced

**Every correct answer in A1-A4, Exam 1 and Mock Exam 1 sits in position A** -
69 questions, no exceptions. Nothing in the build scripts ever shuffled the
options, and the source order from the Spring bank was kept as-is. A student who
notices can score full marks without reading a single stem, and Exam 1 has
already been administered this way.

From A5 onward every assignment spreads its keys across all four positions -
3/3/2/2 for a ten-question set - using a fixed pattern in the builder rather
than a random shuffle, so a rebuild reproduces the same paper. Exams 2-5 need
the same treatment before they are printed, and the four uploaded assignments
need re-uploading or Blackboard's per-question *randomize answers* setting
turned on.

Two related defects found while pulling from the bank, both fixed in A6:

- **Lab 6 Q3** offered `1/4` and `13/52` as separate choices. They are the same
  number, so the key marks a correct answer wrong. Replaced with `1/2`.
- **Lab 6 Q4** offered `1/6` and `6/36`. Same problem. Replaced with `5/36`.
- **Homework 3 Q2** is mis-keyed: population SS = 100, N = 5 gives
  sigma = sqrt(20) = 4.47, but the bank marks `4` correct. Not used in A5, but
  do not reuse it without re-keying. Joins Lab Week 1 Q3 on the bad-item list.

## Delivery order of Topics 5 and 6

Probability (Topic 6) is taught on **Thu 9/10**, ahead of the standard normal
distribution (the second half of Topic 5) on **Tue 9/15**. Areas under the normal
curve are probabilities, so probability has to come first for that to mean
anything; Spring taught it the other way round and had to assert the connection.

The topic *numbers* are unchanged — they identify content, not sequence — so
Exam 2 still covers Topics 5–8 and every mapping below still holds. Two
consequences:

- **A6 and A7 swapped content, keeping their weeks.** A6 is now Probability and
  A7 the standard normal distribution, so no assignment is ever due before its
  lecture. Their question sources moved with them.
- **The lecture decks for these two classes carry no topic number** on the title
  slide, since naming Topic 6 before Topic 5 on screen would raise a question
  that has no useful answer. They read "Probability" and "The Standard Normal
  Distribution".
- **The syllabus's class-by-class table still shows the old order** for classes 8
  and 9 and needs correcting.

## Week by week

Two assignments in a normal teaching week, one in an exam week, none in the two
weeks with no teaching days. The pattern falls out of the topic sequence rather
than being imposed: an exam week has only one teaching day, so it generates only
one assignment.

| Week | Dates       | Classes                                            | Assignments        | # |
|:----:|:-----------:|----------------------------------------------------|--------------------|:-:|
| 1    | 8/18–8/21   | T1 math review · T2 basic concepts                 | A1                 | 1 |
| 2    | 8/25–8/28   | T3 central tendency · T4 variability               | A2, A3             | 2 |
| 3    | 9/1–9/4     | review · **Exam 1**                                | A4 (Part 1 review) | 1 |
| 4    | 9/8–9/11    | T5 z-scores · T6 probability                       | A5, A6             | 2 |
| 5    | 9/15–9/18   | T5 standard normal · T7 sampling distributions     | A7, A8             | 2 |
| 6    | 9/22–9/25   | T8 CLT · **Exam 2**                                | A9                 | 1 |
| 7    | 9/29–10/2   | T9 hypothesis testing · T10 errors and effect size | A10, A11           | 2 |
| 8    | 10/6–10/9   | T11 confidence intervals · T12 one-sample *t*      | A12, A13           | 2 |
| 9    | 10/13–10/16 | **Exam 3** · Fall Break                            | —                  | 0 |
| 10   | 10/20–10/23 | T13 dependent *t* · T14 independent *t*            | A14, A15           | 2 |
| 11   | 10/27–10/30 | review · **Exam 4**                                | A16 (synthesis)    | 1 |
| 12   | 11/3–11/6   | Election Day · T15 ANOVA                           | A17                | 1 |
| 13   | 11/10–11/13 | T15 continued · T16 correlation                    | A18, A19           | 2 |
| 14   | 11/17–11/20 | T17 regression · **Exam 5**                        | A20                | 1 |
| 15   | 11/24–11/27 | Thanksgiving recess                                | —                  | 0 |
| 16   | 12/1–12/4   | review ×2                                          | —                  | 0 |

Notes on the shape:

- The single assignment in an exam week is always the review set (A4, A9, A16) —
  exam preparation that happens to be graded, due just before the exam it
  prepares for.
- Week 9 carries none: Exam 3 on Tuesday, Fall Break on Thursday.
- Week 12 is light for a different reason — Election Day removes the Tuesday
  class, not an exam.
- Weeks 15 and 16 have no graded work. The last assignment is due around 11/20,
  leaving the final fortnight clear before the cumulative final on 12/8.
- The heaviest stretch is weeks 7, 8 and 10 — six assignments across the
  conceptually hardest material (hypothesis testing through the two-sample
  *t*-tests).
- Roughly 14 lab sessions fall across these weeks (Fridays, minus Thanksgiving
  and the last week). The TA walks through approximately half the assignments,
  so about ten of these are covered in lab and the rest are worked alone.

## Exam composition — shares, shown at 30 questions

| Exam | Topics | Shape |
|---|:--:|---|
| 1 | 1–4 | 6 basic concepts · 6 central tendency · 7 variability · 6 computation chain · 5 mixed |
| 2 | 5–8 | 9 z-scores/normal · 7 probability · 8 sampling distributions · 6 CLT |
| 3 | 9–12 | 6 hypothesis testing · 6 errors/effect size · 6 confidence intervals · 12 one-sample *t* chain |
| 4 | 13–14 | 12 dependent *t* chain · 12 independent *t* chain · 6 choosing the test |
| 5 | 15–17 | 10 ANOVA chain · 10 correlation chain · 10 regression chain |
| Final | 1–17 | 6 per part: one computation chain plus concepts from each |

If exams go to 40 questions, scale each row by 4/3 (a 6 becomes 8, a 12 becomes
16). The proportions are what matter.

The final has no Spring precedent — Spring's "cumulative" final covered only
descriptive statistics, correlation, regression, independent-samples *t*, and
ANOVA. Building it as six questions per part, each mirroring an assignment
family, is what makes cumulative real.

## Coverage gaps to fill

Spring's bank, assignments and exams combined, is thin in exactly four places.
These are the families to author; everything else is selection.

| Topic | Questions in the whole Spring bank | Need |
|---|:--:|---|
| Central Limit Theorem | **4** | ~6 new |
| Sampling distributions | **7** | ~4 new |
| Confidence intervals | **7** | ~4 new |
| ANOVA computation | 13 (chains only) | ~2 new |

CLT and sampling distributions are the conceptual pivot of the course and the
weakest-resourced topics in it — Spring had no lab assignment for either
(Lab Weeks 5 and 10 do not exist). Both now have their own class and both sit
on Exam 2.

## Built so far

| # | Files | Shape | Notes |
|:--:|---|---|---|
| A1 | `A1_upload.txt` · `A1_math_review_basic_concepts.md` | 1 NUM + 9 MC | Topics 1–2 |
| A2 | `A2_upload.txt` · `A2_central_tendency_graphs.md` | 1 NUM + 9 MC | Topic 3 |
| A3 | `A3_upload.txt` · `A3_spread_variability.md` | 1 NUM + 9 MC | Topic 4; Q1–4 are a chain on `X = {3,15,8,11,8,14,8,13}` (M = 10, SS = 112, s² = 16, s = 4) |
| A4 | `A4_upload.txt` · `A4_part_1_mixed_review.md` | 1 NUM + 9 MC | Topics 1–4; Q8–10 a chain on `X = {2,2,6,10,10}` (median 6, SS 64, s = 4) |

Every key is **computed**, not transcribed, and each file is checked before
release: exactly 10 rows, 10 fields per `MC` and 4 per `NUM`, exactly one
`correct` per MC, pure ASCII (no LaTeX, no symbols that flatten on upload), and
no stem sharing a data set *and* a quantity with any earlier assignment.

Numeric items run 10% (1 of 10) against Spring's 8%, and sit in the
hand-computation topics where Spring used them.

**A3 deliberately leans on computation.** SS, variance and standard deviation are
almost the whole Topic 4 pool — HW2 Q5–7, HW3 Q1–2, Lab 3 Q6–10, E1 Q18–20 and
Q37–38 — and the 8/27 lecture ran out of time before working any of them by hand
(see `slides/lecture_notes.md`). A3 and the Friday lab are where that has to land
before Exam 1 on 9/3.

**A4 carries one new item** — a skew-direction question — because the surplus
holds no graph or shape item once A2 has taken its share, and a Part 1 review
with nothing from the graphs half would misrepresent the exam.

## Exam 1 draft vs. the assignments

`exams/Exam_1.md` (student), `exams/Exam_1_key.md` (key + coverage),
`exams/Exam_1.pdf` (5 pages, letter) — 30 questions × 2 points, weighted
T1 ×3 · T2 ×9 · T3 ×8 · T4 ×10. Every key computed, not transcribed.

**Eight of the 30 test something A1–A4 never asked.** All eight are taught, and
the 9/1 review deck covers them, but no graded assignment made a student
practise them:

| Q | Tests | Why it is a gap |
|:--:|---|---|
| 4  | Definition of a variable                | recall only, never assigned |
| 9  | Experimental vs. correlational design   | A1 identified an IV; never classified a design |
| 10 | Descriptive vs. inferential             | never assigned |
| 11 | Population vs. sample in a scenario     | A1/A4 defined statistic and parameter, never applied them to a case |
| 16 | Definition of the median                | A2 computed it, never defined it |
| 19 | Symmetric ⇒ mean = median = mode        | A2/A4 tested skewed cases only |
| 26 | **IQR from a raw data set**             | A3 handed over Q1 and Q3; finding quartiles was never practised |
| 30 | **Population SD (÷ N)**                 | A3 tested the sample SD only; HW3 Q2 (the ÷N version) went unused |

The last two are the ones that matter. They are *procedures*, not recall — a
student who has never found a quartile or divided by N instead of n − 1 cannot
reason it out under time pressure. The other six are definitional and the review
lecture handles them.

**Cheapest fix: swap two items into A4.** A4 Q9 (SS) and Q10 (sample SD)
duplicate A3 Q2 and Q4 on a different data set; replacing them with an
IQR-from-raw-data item and a population-SD item closes both procedural gaps
without lengthening the assignment. A4 is the review set due before the exam, so
it is the right place.

## Defects found in the source pool

Items that need re-keying or rewriting before reuse. Add to this as each
assignment gets built; a bad key hits every student in both sections silently.

- **Lab Week 1 Q3** ("Which list is an ordinal level of measurement?") is keyed
  to the TV-show list. The ordinal answer is "Sophomore, Junior, Freshman".
- **Lab Week 3 Q11** ("What type of graph should you use to describe continuous
  data?") offers *Box Plot* alongside the keyed answer *Histogram*. A box plot
  also describes continuous data, so the item has two defensible answers — it
  only works because box plots are never taught. Rewritten for A2 with *Pie
  chart* and *Frequency table* as the categorical-data distractors.
- **HW2 Q8** ("most resistant to outliers") must **not** offer *Mode* as a
  distractor. The course's own comparison table marks both median and mode as
  uninfluenced by outliers, so offering both makes the item ambiguous. Spring's
  original options avoid this; keep them.
- **E1 Q16 was misfiled in the plan above** — it asks for the IQR from Q1 and
  Q3, which is Topic 4, not Topic 3. Moved out of A2's row and into A3's, where
  it is now question 8.
- **Lab Week 1 Q3 is used in A4 with a corrected key.** The archive keys it to
  the TV-show list; the ordinal answer is "Sophomore, Junior, Freshman". A fourth
  option was added, since the original offers only three.
- **HW3 Q1–5 went unused.** Q3–Q5 (range, median, IQR) duplicate quantities A3
  already covers on a better data set, and Q1–Q2 hand a student SS and ask only
  for the square root, which tests less than computing SS. They stay in surplus
  for the Exam 4 review set.

## Practical notes on reuse

- **Images do not survive a text upload.** At least HW1 references a screenshot;
  images live in the archive's `csfiles/` and must be re-attached by hand.
- **Equations flatten.** HW2 and HW3 use LaTeX (`$$SS_X$$`); HW1's summation
  extracts as `X1X2X3X4X565536∑i=15Xi2`. Review every equation-bearing item.
- **Some sets are drill, not teaching.** Lab 4 is ten z-score computations,
  Lab 8 ten near-identical pre/post *t* problems. Fine as practice; an
  assignment built from one of them alone is one procedure repeated ten times.
- **The multi-part chains are the best material.** HW8 walks one dataset through
  SS → pooled variance → SE → *t* → ANOVA → F; HW9 does the same for Pearson's
  *r*; E4 runs a single dataset through correlation, regression and ANOVA.
  Preserve these intact and re-instance them with new data for exams.
