# PSYC 220 (Fall 2026) — project rules

Instructions for any agent working in this folder. Start with `HANDOFF.md` for
how the decks, assignments and exams are built, and `syllabus/assignments.md`
for the assignment-to-exam plan.

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
a `PATTERN` constant; copy that approach.

**Why this is a rule.** Assignments 1–4, Exam 1 and Mock Exam 1 were built with
the correct answer in position A for all 69 questions, because the source order
from the Spring question bank was kept as-is and nothing ever shuffled it. A
student who notices scores full marks without reading a stem. Exam 1 had already
been administered before this was caught.

## Related item-quality checks

While you are in the bank, two failure modes have shown up more than once:

- **Two options that are the same number.** Lab 6 Q3 offered `1/4` and `13/52`;
  Lab 6 Q4 offered `1/6` and `6/36`. A correct answer gets marked wrong.
- **Mis-keyed items.** Homework 3 Q2 (population SD with SS = 100, N = 5) is
  keyed `4` when the answer is `4.47`; Lab Week 1 Q3 is keyed to the wrong list.
  Recompute every numeric key rather than trusting the bank.
