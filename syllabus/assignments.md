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
| A2 | Central tendency & graphs | 3 | HW2 Q2–4,8,9 · Lab3 Q1–3,11 · E1 Q14–17 | 14 | — |
| A3 | Spread & variability | 4 | HW2 Q5–7,10,11 · HW3 Q1–5 · Lab3 Q4–10 · E1 Q18–20,33–38 | 21 | — |
| A4 | Part 1 mixed review | 1–4 | surplus from A1–A3 | 12 | — |
| A5 | z-scores | 5 | HW3 Q6–10 · Lab4 Q1–6 · E1 Q21–26 | 17 | — |
| A6 | Standard normal distribution | 5 | HW4 Q1–3,6,8,9,11 · Lab4 Q7–10 · E1 Q27–32,39,40 | 19 | — |
| A7 | Probability | 6 | HW4 Q4,5,7,10 · Lab6 Q1,3–10 | 13 | — |
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
| 4    | 9/8–9/11    | T5 z-scores ×2                                     | A5, A6             | 2 |
| 5    | 9/15–9/18   | T6 probability · T7 sampling distributions         | A7, A8             | 2 |
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
