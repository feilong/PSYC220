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

**And one notation, consistently.** Lowercase the statistical symbols: `p-value`
(not `P-value`), **`Cohen's d`** (not `Cohen's D`), `z-score`, `t-test`,
`t-distribution`. `H0`/`H1` with the digit zero, not `Ho`. `Type I`/`Type II` in
roman numerals.

### HA for the alternative hypothesis, with H1 noted occasionally

Settled 10/3. **Write `H0` and `HA`.** Occasionally — at the first use in a deck,
and once in any assignment that leans on the symbol — note that **`H1` means the
same thing**, either as `HA (H1)` or as "the alternative hypothesis (HA, also
written H1)".

The gloss is not decoration, and it runs in this direction for a reason: the
course taught `H1` first. L11 introduced hypothesis testing on 9/29 using `H1`
six times, and A10 went out with `H1`. Students already hold that symbol, so
`HA` needs to be introduced as the same idea rather than silently substituted.

Why `HA`:

| | |
|---|---|
| The textbook | writes `H_A` **68 times against `H_1` once**, and the syllabus sends students to Ch. 7 for this topic |
| Most decks already | `HA` is the primary symbol in every Spring deck not yet rebuilt — four of them |
| Reads as what it is | `A` for alternative, rather than a subscript that differs from `H0` by one glyph |

**Converted 10/3:** `build_a10_a11.py` (stem now glosses, options use `HA`;
answer sequence `ACBDCADBAB` byte-identical before and after) and
`build_mock3.py` (4 symbols, not yet administered). `Exam_3` never names the
alternative symbolically, so it needed no change. A12 and A13 use `H0` only.

**Still carrying `H1` as the primary symbol:** `Lecture_11_Hypothesis_testing`
(×6, taught 9/29), `Lecture_12_Statistical_errors_effect_size` (×3) and
`Lecture_14_One_sample_t_test` (×1). The last two already write `H1 (HA)` in
places — those glosses now read backwards and want flipping to `HA (H1)`.

`style_check.py` flags a bare `H1`, `H_1` or `$H_1$`, and allows both gloss
forms, which it strips before testing. `H0` is untouched.

**One mu, and it is the Greek one.** Use **U+03BC GREEK SMALL LETTER MU (μ)**,
never **U+00B5 MICRO SIGN (µ)**. They are near-identical on screen and were mixed
throughout every deck — Lecture 12 alone carried 16 micro signs against 3 mu.
Two different codepoints means Find fails, copy-paste is inconsistent, and a
screen reader may read one of them as "micro".

Fix it **character by character**, never by rewriting `object text`:

    set character N of object text of itm to μ

Rewriting the whole text flattens every subscript in the same box. The
character form leaves surrounding runs alone — verified on Lecture 14, where all
15 subscript spans survived. `slides/` has the script; the AppleScript literals
are `«data utxt00B5»` and `«data utxt03BC»`, big-endian, which is easy to get
backwards and fails silently with zero replacements.

**Do not sweep the assignment or exam builders.** Their uploads are pure ASCII
on purpose — Greek letters go out as the words "mu" and "sigma" — and the
`_ASCII` table in `build_a12_a13.py` deliberately carries *both* spellings as
keys so either one gets normalized. A blanket micro→mu replace collapses them
into a duplicate key and silently disables micro-sign handling, which is the
exact failure the table exists to prevent. It broke the A13 build on 10/3.

**Greek letters are spelled as letters.** Write `α` and `β`, not the words
"alpha" and "beta". These are plain Unicode and need no formatting, so they
*are* scriptable.

**Subscripts: `₀` yes, capital `A` no.** Unicode has a subscript zero (`H₀`,
U+2080) that renders correctly in HelveticaNeue and matches the look of a real
Keynote subscript closely enough. It has **no capital subscript A** — only a
lowercase `ₐ`, which is wrong for this course and sits visibly lower and
smaller than `₀`. So `H₀` can be written by script; `H_A` has to be formatted by
hand, every time.

**The weekly slide's right column is a `shape`, not a `text item`** — Lecture 13
is the reference: same `y` and height as the left body placeholder, at
`x = 638, y = 205, w = 540, h = 488`. A text item carries a different paragraph
style and centers its text; a shape takes the theme's **Body** style and
left-aligns.

**Telling the three apart.** `class` is not enough — a *placeholder* also
reports `class = shape`. Membership in the `shapes` collection is the
discriminator, and `text items` is no help at all because it returns everything
containing text:

| Box | `class` | in `shapes`? |
|---------------------------|-------------|:------------:|
| Title / body placeholder  | `shape`     | no           |
| Shape (what we want)      | `shape`     | **yes**      |
| Text box                  | `text item` | no           |

**Converting one to the other is not scriptable.** Every route is closed, tested
10/3 against Lecture 14:

| Attempt | Result |
|---------------------------------------|--------------------------------------------|
| `make new shape`, then strip the fill | `background fill type` reads but will not set |
| `duplicate` a Body-styled shape       | "Shapes can not be copied"                  |
| set the paragraph style to Body       | not in the dictionary                       |
| set alignment directly                | refused                                     |

A scripted shape therefore arrives as a **blue filled box with centered text**,
which is worse than the text box it would replace. Only `color of object text`
is settable, and that fixes just the white text.

**Do it by copy-paste instead:** copy the right-hand column from Lecture 13 and
paste it in. The clipboard carries fill, paragraph style and alignment, which is
exactly what AppleScript will not. Then set `x = 638, y = 205, w = 540, h = 488`.
Script the *content* and the *geometry* first so the pasted box drops straight
in.

Two related traps: `make new shape with properties {object text:…}` is refused
outright, and selecting the old column by text length picks the *body
placeholder*, whose deletion raises "Can't set default body item of slide to
any" — select by class and width.

**The decks cannot be fixed by script.** `H0`/`H1` in the slides are *real*
Keynote subscripts (the H at 42 pt, the digit at 28 pt), and setting
`object text` rewrites the whole run at one size, flattening them. Every slide
change involving these symbols is a Format inspector job.

### p vs P — they are two different things

Settled 10/2 after auditing the decks. The casing depends on what the symbol
means, and both appear in this course:

| | Case | Examples in the decks |
|---|---|---|
| **Probability** of an event | capital **P** | `P(E)`, `P(A \| B)`, "P = 0: an impossible event", "an event where P ≤ .05" — L7 ×8, L8 ×1 |
| The **p-value** of a test | lowercase **p** | `p-value`, `p < .05`, `p > α` — L12 ×5 |

Capital P for probability is standard and correct; leave it. Lowercase p for
the p-value is APA 7, which is what these students will have to write, and it
is what every assignment already uses.

`style_check.py` enforces the word `p-value`. It deliberately does **not** flag
a bare `P < .05`, because that is indistinguishable by regex from the legitimate
probability usage in L7 and L8 — that one needs a human eye.

### This is enforced, not just requested

`style_check.py` at the repo root holds both lists and is wired into the two
funnels every item passes through:

* `assignments/build_a5_a6.write()` — checks the exact stems and options the
  student sees, for every assignment builder that calls it.
* `exams/examlib.check()` — same, via `style=True`, which is the default.

Either one refuses the build and names the word, the fix and the stem it is in.
It does **not** false-positive on `analysis`, `analyses`, `practice`,
`parameter` or `diameter`; only the unambiguous British verb forms are matched.

**Why it exists.** The American-spelling rule above was in force the whole time
and nothing checked it, so violations shipped — most of them written by the
agent that had just been told to use American English:

| Item | Carried | Outcome |
|---|---|---|
| A9 | `centred` | **fixed** 10/2 |
| A10 | `P-value` ×2 (against `p-value` elsewhere) | **fixed** 10/2 |
| A11 | `Cohen's D`, and `D = 0.8/0.5/0.2/0.4` in its options | **fixed** 10/2 |
| Exam 2 | `centred`, `favours`, `standardised` | grandfathered — administered 9/24 |
| Mock Exam 2 | `behavioural`, `favours` | grandfathered — already released |

**A1–A13 now all pass with the gate fully enforced; no assignment uses
`grandfathered=True`.** Only the two Week-6 papers keep `style=False`, each with
a comment naming its defect. **Neither flag is ever right for a new item.**

The A9/A10/A11 corrections changed wording only: all three answer-letter
sequences are byte-identical before and after, and the one keyed answer whose
text moved was `D = 0.2` → `d = 0.2`, the same value. **`assignments/as_released/`
holds a copy of all 13 assignments exactly as students received them**, taken
before the edits — never regenerate it, and never point a builder at it.

**These three need re-uploading to Blackboard** to take effect; the files on
disk are corrected but the live tests are not.

One more, not caught by the gate because it is instructor-facing rather than
item text: `examlib.write()` is called with the column header **"Practised in"**
by `build_exam2.py`. Use **"Practiced in"** from Exam 3 onward.

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

- **A bare `*` inside `$...$`.** `convert.py` runs its `*italic*` regex over the
  whole line, math included, so a *pair* of asterisks inside math is silently
  eaten. Exam 3 had `$z^{*}$ ... $z^{*}$` in one stem; the pair became `<em>`,
  the braces collapsed to `z^{}`, MathJax gave up, and the raw `\left(\sigma /
  \sqrt{n}\right)` printed on the page. Write `\ast`, never a bare `*`, inside
  math. `check_markup()` now refuses it. Note the failure needs *two*
  asterisks in one block, so a single `$t^{*}$` can survive by luck — which is
  why the rule is absolute rather than "watch out for it".

- **An escaped quote inside a raw string.** `r"a student writes: \"...\""`
  keeps the backslash, because Python drops it only in a normal string. Mock
  Exam 3 Q6 and Q17 printed `\"…\"` on the page until 10/6. Put a stem that
  quotes someone in single quotes, `r'a student writes: "..."'`.
  `check_markup()` now refuses `\"` and `\'` outside math.

Reading the `.md` is not enough to catch this class of bug — `\emph{not}` looks
deliberate in source. Render the PDF and look at the page, or extract its text:

```
~/miniconda3/envs/nb/bin/python -c "
import pymupdf, re, sys
t = '\n'.join(p.get_text() for p in pymupdf.open(sys.argv[1]))
print(sorted({m.group(0) for m in re.finditer(r'\\\\[a-zA-Z]+|\\\\[%&_#]', t)}) or 'clean')
" exams/Exam_2.pdf
```
