# PSYC 220 (Fall 2026) — project rules

Instructions for any agent working in this folder. Start with `HANDOFF.md` for
how the decks, assignments and exams are built, and `syllabus/assignments.md`
for the assignment-to-exam plan.

## Always use American spelling

This is a US course. Write **center, labeled, standardize, summarize, analyze,
behavior, color, practice** (noun and verb alike) — never centre, labelled,
standardize, summarize, analyze, behavior, color, practice.

It applies to everything: slide text, figure descriptions and alt text, exam and
assignment items, and the notes and documentation in this repo. Alt text counts —
a screen reader reads it aloud to the same students.

## Balance the answer key across all four positions

**Every multiple-choice set — assignment, mock, or exam — must spread its
correct answers roughly evenly across positions A, B, C and D.** For a
ten-question set that means 3/3/2/2; for thirty questions, 7/8/7/8 or similar.

Check it before shipping anything:

```
~/miniconda3/envs/nb/bin/python -c "
import sys, collections
d = collections.Counter()
for line in open(sys.argv[1]):
    p = line.rstrip('\n').split('\t')
    if p and p[0] == 'MC':
        opts = p[2:]
        d[next(i//2 for i in range(0, len(opts), 2)
               if opts[i+1].strip().lower() == 'correct')] += 1
print('A/B/C/D =', [d[i] for i in range(4)])
" assignments/AN_upload.txt
```

Use a **fixed pattern, not a random shuffle**, so that rebuilding a paper
reproduces it exactly. `assignments/build_a5_a6.py` has a `balance()` helper and
a `PATTERN` constant; `exams/examlib.py` has the same for exams, and
`examlib.check()` now refuses to write a paper where one position holds more
than 40% of the keys.

**A mock and its real exam must not share an answer sequence.** Both are 30
questions with the key written first, so the same pattern hands them an
identical key — memorising the mock would then pass the exam. Pass a different
`offset=` to `examlib.balance()`; `build_mock2.py` verifies its sequence against
`Exam_2_key.md` and fails if more than 40% of positions match.

## A mock must differ from its exam in the questions, not just the numbers

**Cover the same skills; ask different questions.** A mock that is the exam with
fresh numerals teaches students to pattern-match a template instead of doing the
statistics, and it turns the practice paper into a partial answer key.

Mock Exam 2 is the case that prompted this rule, and it shows the failure is not
plagiarism. It reuses **nothing** verbatim — every numeral differs. But mask the
numbers and the shapes line up: **7 of 30 items sit at ≥ 0.80 similarity to an
Exam 2 item, 16 at ≥ 0.60, and 5 of those land at the very same question
number.** Mean best-match similarity is 0.61. Four items are the same sentence
with different values, e.g. "A population has σ = 100 … standard error for
n = 25?" against "… σ = 18 … n = 9?".

**Exam 2 and Mock Exam 2 are grandfathered** — both were print-ready when this
was found, and Exam 2 must not be touched. The rule starts at Exam 3.

Check it before shipping a mock:

```python
import examlib
examlib.check_distinct(mock_questions, exam_questions)
```

It masks every number and math span, scores each mock item against its closest
exam item, and fails on either `TWIN_LIMIT` (no item ≥ 0.80) or `CLONE_SHARE`
(at most 20% ≥ 0.60). It is deliberately **not** wired into `examlib.check()`,
so that `build_mock2.py` keeps running; call it from `build_mock3.py` onward.

**Ways to differ that keep the skill intact** — swapping the cover story is the
weakest of these and rarely moves the score much:

| Technique | Exam asks | Mock asks |
|---|---|---|
| Reverse the task | given σ and n, find the standard error | given the standard error and σ, find n |
| Change what is asked | compute the value | choose the right formula, or interpret a value you are handed |
| Change the representation | bare numbers in prose | a small table, or a worked solution with an error to find |
| Go one step further | compute z | compute z, then say what it means about the sample |

**This does not conflict with the rehearsal rule above.** That rule is checked by
*skill tag*, not by wording — `check_rehearsed()` compares `EXAM_SKILLS` against
`MOCK_SKILLS` and `ASSIGNMENT_SKILLS`. A mock can therefore cover every exam
skill while asking about it differently, which is exactly the target: identical
skill coverage, low wording similarity.

**Why this is a rule.** Assignments 1–4, Exam 1 and Mock Exam 1 were built with
the correct answer in position A for all 69 questions, because the source order
from the Spring question bank was kept as-is and nothing ever shuffled it. A
student who notices scores full marks without reading a stem. Exam 1 had already
been administered before this was caught.

## Most exam questions should have been rehearsed

**Most questions on an exam should have something similar in the homework
assignments *or* in that exam's mock.** Either one is enough; it does not have
to be both. The rule runs one way only — homework and mocks may go further than
the exam, and often should. Adding a question to an assignment never obliges you
to add one to the exam.

An exam question that rehearses nothing is a **warning worth reading**, not a
defect. A handful is normal. Only a large share means the paper has drifted away
from what students were given to practice on, and that is worth failing the
build over.

Check by **skill, not by provenance label**. `exams/build_mock2.py` carries
`EXAM2_SKILLS`, `MOCK2_SKILLS` and `ASSIGNMENT_SKILLS` — one tag per question in
paper order for the two papers, plus the set A5–A9 covers — and
`check_rehearsed()` prints every unrehearsed question, failing only past
`UNREHEARSED_LIMIT` (20% of the paper). Copy that for Exams 3–5.

Labels hide what tags catch. Mock Exam 2's provenance labels all looked healthy
while six Exam 2 skills went unrehearsed *in the mock* — it spent two slots on
sampling with replacement, which Exam 2 never asks about. Under the OR rule
those six were fine, because the homework had already covered them; the tags are
what let you see the situation and judge it, rather than guess from `A8 Q9`.

## Related item-quality checks

While you are in the bank, two failure modes have shown up more than once:

- **Two options that are the same number.** Lab 6 Q3 offered `1/4` and `13/52`;
  Lab 6 Q4 offered `1/6` and `6/36`. A correct answer gets marked wrong.
- **Mis-keyed items.** Homework 3 Q2 (population SD with SS = 100, N = 5) is
  keyed `4` when the answer is `4.47`; Lab Week 1 Q3 is keyed to the wrong list.
  Recompute every numeric key rather than trusting the bank.
- **LaTeX outside `$...$`.** The exam pipeline is Markdown → HTML → Chrome print;
  MathJax only touches what sits between dollar signs, so a backslash command in
  plain prose is printed *exactly as typed*. Exam 2 and Mock Exam 2 were both
  print-ready with `\emph{not}` and `68\%` on the page. Write `*italic*` for
  emphasis and a bare `%` for percent, and keep backslashes inside `$...$`.
  `examlib.check()` now calls `check_markup()`, which fails the build on any
  `\command` or `\%` found outside math mode.

Reading the `.md` is not enough to catch this class of bug — `\emph{not}` looks
deliberate in source. Render the PDF and look at the page, or extract its text:

```
~/miniconda3/envs/nb/bin/python -c "
import pymupdf, re, sys
t = '\n'.join(p.get_text() for p in pymupdf.open(sys.argv[1]))
print(sorted({m.group(0) for m in re.finditer(r'\\\\[a-zA-Z]+|\\\\[%&_#]', t)}) or 'clean')
" exams/Exam_2.pdf
```
