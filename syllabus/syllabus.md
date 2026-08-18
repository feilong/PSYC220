# PSYC 220 Fall 2026 — syllabus decisions

Why the Fall 2026 syllabus differs from Spring 2026. Decided August 2026.
The syllabus itself is `PSYC220_011_012_syllabus_Ma_Fall2026.md`.

## Files and workflow

| File | Role |
|---|---|
| `PSYC220_011_012_syllabus_Ma_Fall2026.md` | Source of truth for **content** |
| `PSYC220_011_012_syllabus_Ma_Fall2026.docx` | Generated deliverable |
| `syllabus_reference.docx` | Formatting template — frozen copy of the current .docx |
| `build_docx.py` | `.md` → `.docx` |

Build with `python build_docx.py`, never a bare `pandoc` call: pandoc's `gfm`
reader discards table column widths and its docx writer sizes tables to ~5.5"
inside a 6.5" text block. The script also forces 11 pt throughout with 14 pt
titles, unifies body paragraph styles, and sets repeating table header rows.

After formatting the `.docx` by hand in Word, refresh the template so rebuilds
keep the change:

    cp PSYC220_011_012_syllabus_Ma_Fall2026.docx syllabus_reference.docx

If the `.docx` is edited by hand, port the wording back into the `.md` by
converting it (`pandoc -f docx -t markdown`) and diffing — otherwise the next
rebuild silently discards it.

## Exams — the main change

**Six exams: five in-semester plus a cumulative final, lowest of six dropped,
60 points each.** Best five = 300 points.

Dates: **9/3, 9/24, 10/13, 10/29, 11/19**, final **Tue 12/8 at 12:30 p.m.**

Spring used four exams (three midterms plus the final) with the lowest dropped.
The flaw: the last unit appeared only on the final, so a student who dropped the
final was never examined on it. Exam 5 now falls before the last week of class,
so **every topic is examined during the semester**.

**Governing rule: each exam focuses on everything taught since the previous
exam.** Verified programmatically against the schedule — no topic falls in a
gap. Exams are not formally cumulative, but the syllabus states any exam may
draw on earlier topics, because the material builds and a *t*-test question
tests standard deviations whether or not that is intended.

Parts: 1 Describing data (Topics 1–4) · 2 Distributions and sampling (5–8) ·
3 Inference with one sample (9–12) · 4 Comparing two means (13–14) ·
5 The general linear model (15–17).

Constraints that shaped this:

- The Registrar bars exams in the **last two meetings** of a twice-weekly
  course, which pins the final in-semester exam to 11/19 and makes 12/1 and
  12/3 review days.
- Exam 3 sits immediately before Fall Break.
- 9/1 and 10/27 are review / exam-prep days.
- 19 content classes + 5 exams + 4 review days = 28 meetings.

**Cost:** Spring had 24 content classes, Fall has 19. Correlation, regression,
and both two-sample *t*-tests get one class each rather than two. Watch the
pace there.

## Grading

    5 exams × 60 = 300
    20 assignments × 10 = 200
    Total 500 — same total and same letter cutoffs as Spring 2026

60 points per exam was chosen over 80 or 100 specifically to keep the Spring
totals and cutoffs intact. The trade-off accepted: assignments are 40% of the
grade and most of those points are close to automatic.

## Assignments

**One set of 20, no homework/lab distinction**, 10 points each, all submitted
online in Blackboard and **graded automatically**. The instructor writes all 20;
the TA posts and verifies them in Blackboard.

The TA works through **approximately half** in lab, question by question — for
those, attending lab earns full credit. "Approximately" rather than a fixed
count because ~14 lab meetings must also absorb pre-exam review sessions.

Students are urged to finish each assignment within a week of the lecture it
follows, even when the deadline is later. No late work outside a certified
excused absence.

## Policies

**Make-up work** — reversal of Spring's "no make-up exams". Given without
penalty for absences certified by the **Office of Student Advocacy** (Maxient
form), completed within a week of return. Documentation goes to Advocacy, not
to the instructor or TA. The dropped score is no longer the only remedy.

**Cheat sheet** — one letter-sized page, front and back, on every exam including
the final. **Handwritten by the student**: not typed, printed, photocopied or
shared. Rationale: preparation should go to understanding rather than
memorising, and writing the page out is itself the studying. A non-compliant
sheet is collected and the student proceeds without it — a rule violation, not
an integrity referral, so the TA can enforce it at the desk.

**Calculators** — permitted but **not required**. Stated as a capability, not a
model: add, subtract, multiply, divide, square root. Examples kept from Spring
(Casio FX-300, TI-30Xa). Graphing, programmable, CAS, networked, and phone or
watch calculators are banned by name, with the reason given as test security
rather than capability, to preempt the "nothing here needs it" argument. Applies
to assignments as well as exams.

**At the desk:** cheat sheet, permitted calculator, own pencils. Stated as a
closed list so "any other electronic device" cannot swallow the calculator.

**Exam content, not format** — described as computation, interpretation,
choosing the right test, and reading SPSS output. Question formats are
deliberately unstated so the syllabus stays true if they change.

**SPSS** — the goal is reading and interpreting **output**, which is what exams
test. Not covered every week. Spring's claim that students would "practice using
SPSS each week" was untrue.

**Attendance** — not graded. Pop quizzes give up to 10 extra credit points.
Dropped Spring's promise to work examples in class that would not be posted.

**No rounding**, with the reason stated. Grades cannot be discussed over email;
under FERPA they cannot be discussed with anyone else without written consent.

**Optional final** — a student happy with five scores may skip the final and let
it be the dropped score. Stated openly in an FAQ rather than left to be
discovered.

## Materials

**Companion text changed** to *Introduction to Statistics in the Psychological
Sciences* (Cote, Gordon, Randell, Schmitt & Marvin, 2021, rev. 2023), which
adapts and supersedes Foster et al. (2018). Chapter numbering is identical, so
the chapter map in the schedule needed no changes, and its appendices carry the
z, t, F and r tables.

Slides are described as available on Blackboard with no need to copy everything
down. Interactive demos at <https://feilong.github.io/PSYC220/>. The Writing
Center section was removed — this course has no writing assignments.

## University rules verified against source

- **Final exam slot** — TR 11:40 a.m. classes sit Tue 12/8 at 12:30 p.m.
  (Registrar, Fall 2026 schedule).
- **Final grades** due within **72 hours** of the final exam.
- **Grade changes** may be submitted up to **one calendar year** after the grade
  is reported — used to set exam-material retention in the GIA contract.
- **Boilerplate** updated to the CTE template revised **June 6, 2026**: the
  24-hour mental health line is **(844) 287-6963** (was 833), the office is now
  the **Office of Student Conduct and Academic Integrity** with unauthorized AI
  use named as a violation, Disability Services rewritten around equitable
  access with the SDRC email, and Student Success Center programs renamed.

## Accessibility

Audited against USC's requirements. Real Word heading styles, Aptos/Calibri, no
images, **no bare-URL link text** (the CTE convention of following each link
with its URL in parentheses was removed — 40 duplicates), and **repeating header
rows** on both tables.

When posting a PDF, use **Save As → PDF**, not Print → PDF: only the former is
tagged and screen-reader readable.

Outstanding: the hand-edited `.docx` carries two **empty Heading 2 paragraphs**;
a rebuild removes them.

## Adopted from Prof. Dexin Shi's PSYC 220 syllabus

Student Advocacy make-up procedure and Maxient link, the cheat sheet, the FAQ
format, the no-rounding rationale, the lab section description, the 10-point cap
on pop quiz credit, exam format and scantron/pencil language, "What You Should
Expect", and the SDRC two-week registration note.

## Declined

Dropping the lowest homework score · a "draw a gamecock" syllabus-reading easter
egg · a Q&A day before every exam (no room in the calendar) · separate exam
review sessions (students are directed to office hours instead).

## Still open

- Office hours for both instructor and TA are **TBA**.
- Confirm the Ch. 8 reading for confidence intervals — Cote et al. cover CIs
  alongside the *t* distribution rather than in their own chapter.
