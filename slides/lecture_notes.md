# Lecture notes — what to improve next time

A running log, one section per lecture, written *while the semester is fresh*
so the next section does not repeat the same rough edges. Add to the relevant
section right after teaching the class; don't wait until the end of the term.

Each entry: what happened, and the concrete change to make. Vague notes
("could be better") are not worth writing down.

Status key: **TODO** = not yet done · **DONE (F26)** = fixed during Fall 2026 ·
**NEXT** = deliberately deferred to a future section.

**Keynote, before you script anything:** Keynote is sandboxed and can only open a
file the *user* has opened at least once. That grant is stored per file, so
`cp` produces a deck Keynote refuses to open — silently under AppleScript, and
in the UI as *"Keynote couldn't read the file. You can try restoring to a
previous version."* That message means **permission, not corruption**
(`NSCocoaErrorDomain Code=257` in `log show --predicate 'process == "Keynote"'`).
`mv` keeps the grant because the inode is unchanged, so rename decks into place
rather than copying them. A copy has to be double-clicked once before any script
can touch it.

---

## Lecture 1 — Introduction to the course

**DONE (F26, all decks) — the title slide now names the week's topic.** Lectures
1–5 each carry a centred topic line under the course block: "Introduction & Math
Skills Review", "Topic 2 — Basic Concepts & Distributions", "Topic 3 — Measures
of Central Tendency & Graphs", "Topic 4 — Measures of Spread & Variability",
"Exam 1 Review". Wording follows the syllabus's class-by-class table. See the
HANDOFF conventions for the geometry; it is identical on both themes, so
Lecture 1 took the same coordinates despite still being on `White`.

- **TODO — no weekly-plan slide.** Every other deck opens with "This Week and
  Next" as slide 2. Lecture 1 predates the convention. Add it.
- **NEXT — under-ran the plan.** Several basic-concepts topics on the Lecture 1
  outline were not actually covered and spilled into Lecture 2, which is why the
  two decks overlap. Either trim the Lecture 1 outline to what fits, or plan the
  spillover deliberately rather than discovering it in the moment.
- **TODO — still on the old theme.** Not yet re-themed to the 16:10 template;
  needs the Keynote UI theme change plus `fix_offcanvas.applescript`.

## Lecture 2 — Math review & basic concepts

- **TODO — the deck is almost entirely bulleted text.** Add images. The
  population/sample material especially wants a visual metaphor rather than a
  definition: a crowd of minions as the population with a handful circled as the
  sample makes the parameter/statistic distinction land in one glance.
  Best candidates, in order of payoff:

  | Slides | Topic                                   | What an image would do                                            |
  |:------:|:----------------------------------------|:------------------------------------------------------------------|
  | 19–21  | Population / sample / parameter & statistic | The core metaphor — crowd vs. circled subset, μ vs. x̄ labelled |
  | 22, 28 | Sampling bias, sampling error           | Same crowd, but the circled subset visibly unrepresentative        |
  | 24–26  | Simple random / stratified / convenience | Three panels of the same crowd, sampled three ways                 |
  | 10–15  | Levels of measurement                    | One concrete example pictured per level, not just named            |
  | 18     | Experimental vs. correlational design    | Two-group diagram with the arrow of manipulation                   |

  Reuse one cast of characters across all of them so the visual carries the
  through-line from population → sample → sampling error.
- **TODO — summation notation runs five near-identical slides (31–36).** Works,
  but it is a lot of screen time on one idea. Consider collapsing to two or three
  builds and putting the rest on the board.

## Lecture 3 — Central tendency & graphs

Built 8/24 for Tue 8/25, from the Spring **Lecture 4** deck rather than Spring
Lecture 3. Spring L3 lost its first half to one-off business (a pop-quiz demo, a
CSV cleanup walkthrough, lab-classroom updates), ran out of time, and L4 then
re-taught graphs and central tendency in cleaner form — two barplot examples
instead of four, a *Bar plots vs. histograms* comparison, and the three
"Characteristics of…" slides consolidated into one table.

- **DONE (F26) — restored the three worked Example slides.** Spring L4 defines
  mean, median and mode back to back with no computation shown, because L3 had
  already worked `X = {10, 4, 10, 7, 9, 8, 10, 6, 9, 7}` three times. Teaching
  this once meant grafting those back, one after each measure. A2 and the Spring
  HW2 numeric items ask students to compute exactly these.
- **DONE (F26) — restored the "Frequency distribution graphs" opener** with the
  Confucius gag. L4 opened cold on "Bar plots" with no motivation for graphing.
- **NEXT — the pop-quiz data demo.** Collecting live data from the class, showing
  the raw Blackboard CSV, cleaning it, then graphing it is a genuine
  data-analysis narrative on the students' own data. Deferred out of Lecture 3,
  which is already carrying graphs plus all three measures of central tendency.
  Needs a fresh Fall quiz and new screenshots when it lands.
- **NEXT — "Sometimes ordinal scale can be treated as interval scale."** Dropped
  from Lecture 3 because its image is a pandas `.describe()` of the Spring
  pop-quiz columns (`love_stats`, `height_in`) — meaningless to students who
  never took that quiz. Travels with the demo above, or needs a new figure.
- **DONE (F26) — retitled the three Example slides** by the measure each one
  demonstrates: "Example: Mean", "Example: Median", "Example: Mode". They had been
  three byte-identical slides, so nothing told a student reviewing the deck which
  measure was being worked. The computation still happens live on the board — no
  answers are on screen.
- **DONE (F26) — image descriptions on all 11 images**, including the two
  `equation.pdf` renders on the Mean slide, which carried no text of any kind. The
  exported PDF now has 12 `/Alt` and 10 `/TH`; `/Lang` is still 0, which Keynote
  cannot emit from the deck.
- **DONE (F26) — the ordinal bar plot hung 4 pt off the bottom** of the canvas and
  lost its axis border on export. Pulled back to y = 167.
- **TODO — the survey figures are labelled "PSYC222 Students".** Wrong course
  number, on slides 5, 6, 7, 10 and 12. It is baked into the matplotlib images, so
  fixing it means regenerating them. The Fall class took the same pop quiz on 8/18
  (`Pop quiz #1.download.csv` — 34 responses, 28 of them consenting to use), so
  regenerating would fix the label *and* put the students' own numbers on screen.
  Deferred 8/24: the Spring figures teach the point, and the height column needs
  cleaning first (one response is `5'5`).
- **TODO — slide 12's two columns are 22 pt bold**, against 34–42 pt everywhere
  else in the deck, and the right column is centre-aligned while the left is
  left-aligned. Both predate the re-theme; neither is worth fixing mid-week, but
  rebuild the slide as two matched plain shapes when the deck next gets attention.
- **TODO — slides 5 and 6 are the same bar plot, re-sorted** — survey order, then
  most-to-least frequent — with nothing on either slide saying why. The point is
  that nominal categories have no intrinsic order, so the reordering is legitimate.
  Put it on the slide or make sure it is said out loud.
- **DONE (F26) — re-themed to `16:10 ratio`**, then swept for what the change
  displaced. Worth knowing what a re-theme actually does, because Lectures 1 and
  5–9 still have to go through it:
  - Every **title and body placeholder is re-anchored and restyled** — titles from
    203,36 874×170 (centred) to 89,59 1103×120 (left, HelveticaNeue-Medium 82),
    bodies from 203,220 874×495 to 89,205 1103×488. Slides that are just
    title-plus-image come through untouched.
  - **Hand-built two-column slides break.** Slide 12 built its left column out of
    the *body placeholder* and its right column out of a plain text shape. The
    theme widened the placeholder to full width and it landed under the bar-plot
    image; the plain shape was left alone. Repaired by mirroring the untouched
    right column — 96,454 403×261, HelveticaNeue-Bold 22. **Check every
    two-column slide after a re-theme**, and prefer two plain shapes over
    placeholder-plus-shape when building one.
  - The theme adds a **slide-number field** to each slide.
  - `fix_offcanvas` then moved exactly one item: the AliExpress source URL on
    slide 3, from x = −2 to x = 0, y 783 → 781.
### Against the textbook (Foster et al., checked 8/24)

- **TODO — the syllabus assigns the wrong chapter.** Topic 3 is down for **Ch. 3**,
  but Ch. 3 is *Measures of Central Tendency and Spread*. The graphs half of this
  lecture — bar charts, histograms, shape of distribution — is **Ch. 2**,
  *Describing Data Using Distributions and Graphs*, which the syllabus assigns to
  Topic 2 instead. So a student following the reading column reads about graphs a
  week early and gets nothing assigned for the graphs actually taught on 8/25.
  Lecture 2's content is Ch. 1 end to end. The mapping should be
  Topic 2 → Ch. 1 · Topic 3 → Ch. 2 + Ch. 3 (through *Comparing Measures of
  Central Tendency*) · Topic 4 → Ch. 3 (*Spread and Variability* onward).
- **DONE (F26) — added slide 23, "Skew and central tendency."** Slide 22 showed
  the three skew shapes but labelled mean and median only inside the figure, at a
  size nobody can read from a seat, and HW2 Q9 asks the relationship outright. The
  new slide states it in words, following Foster's own framing: the mode stays at
  the peak, the median is pulled into the tail, the mean is pulled farthest —
  hence Mean < Median < Mode under negative skew, all three equal when symmetric,
  Mode < Median < Mean under positive skew, and report the median when skew is
  strong. Deck is now 24 slides; the closing exercise moved to 24.
  - **The rule is qualified on the slide, deliberately.** It is a heuristic for
    smooth unimodal distributions, not a theorem, so the mechanism bullet opens
    "In a smooth, single-peaked distribution:" and a closing bullet says "A rule
    of thumb, not a law: with several peaks, ties, or small samples the order can
    change." Checked numerically before writing it:
    - Mode in the wrong place: X = {1, 1, 5, 6, 7, 8, 9} has skewness −0.44 and
      mean (5.29) < median (6), but the mode is 1 — the *smallest* value. Order
      is Mode < Mean < Median.
    - Even mean < median fails: X = {0, 6, 6, 6, 6, 7, 8, 8, 8} has skewness
      −1.82 yet mean (6.11) > median (6). A sweep of multisets of size 6–9 over
      values 0–9 found 4,234 cases with skewness < −0.15 and mean > median.
    - It does hold for the smooth continuous families textbooks draw —
      Beta(5, 2): mean 0.714 < median 0.736 < mode 0.800.
    Foster hedges the mode's position too ("although it may not be in bimodal
    distributions"). Von Hippel (2005, *J. Statistics Education* 13(2)) is the
    standard reference for the textbook rule being overstated. Keep teaching the
    rule — it is what the bank tests, and HW2 Q9 asks for the *typical*
    relationship — but the qualifier means a sharp student is not being told
    something false.
- **NEXT — Ch. 3's "Definitions of Center" is skipped entirely** (~5 pages): the
  balance-scale image, the median as the value minimising the sum of *absolute*
  deviations, the mean as the value minimising the sum of *squared* deviations.
  Not directly examined, but it is the reason mean and median differ, and the last
  of the three is the bridge straight into SS in Lecture 4. It is also exactly the
  visual the central-tendency half is missing.
- **Deliberately not taught, and not assessed either:** Ch. 2's frequency tables,
  pie charts, stem-and-leaf displays, frequency polygons, box plots, line graphs
  and "graphical mistakes to avoid". Checked the whole Spring question bank —
  none of them appear in any question. "Box Plot" shows up once, as a distractor
  in Lab 3 Q11. Leaving them out is consistent; just know students who do the
  reading will meet them.

- **TODO — the deck is still text-and-screenshots.** Same note as Lecture 2: the
  central tendency half (Mean / Median / Mode / Example ×3) is pure text.

## Lecture 5 — Exam 1 review (Tue 9/1)

`Lecture_05.key`, built from a copy of Lecture 4. **61 slides, 26 visible.**

Because it is a copy of L4 it already contained every Topic 3 slide, sitting
skipped — so "copying the earlier lectures in" was mostly *un-skipping*.
Topics 1–2 live in Lectures 1–2, and **Keynote's dictionary has no command to
move a slide between documents**, so those four slides are authored summaries
rather than copies. UI-scripted copy/paste between two open documents is the
only other route and is not worth the fragility.

Shape: title · homework · weekly plan · exam brief · **T1 math review** ·
**T2 levels of measurement / samples & populations / variables & design** ·
T3 (bar vs. histogram, mean, median, mode, comparison table, skew) ·
T4 (variability, range, IQR, quartiles, deviations, SS, sample variance, SD ×2) ·
three worked-computation exercises.

**What was cut, and why.** Everything dropped is material the Spring bank never
tests: the six-slide SS → n − 1 arc, the algebraic decomposition slide (already
stamped "will NOT appear in exams"), the four box-plot slides, and the
sampling-with/without-replacement pair. That is 13 slides skipped against 7
un-skipped.

**The Exercise time slide with `X = {4,5,6}`, `Y = {5,5,5,9}`, `Z = {6,6,6}` is
now un-skipped.** It carries the mean / SS / variance / SD computation that ran
out of time on 8/27, which is the single biggest gap before the exam.

**The weekly plan is one column here, not two.** Keynote will not let AppleScript
set text alignment, so a second text item cannot be made to read as a
left-aligned list — it centres every line and rides up over the title. One
full-width body placeholder avoids the fight. See HANDOFF pitfall 14.

Exported and patched: 26 pages, `/Lang`, and the title "PSYC 220 Lecture 5:
Exam 1 Review".

## Lecture 4 — Spread & variability
## Lecture 4 — Spread & variability

Deck split off from the same Spring Lecture 4 file; slides 22–49 (the two
same-mean-different-spread distributions onward) are the Fall Lecture 4 spine.

### Taught 8/27 — ran long

**Overran by roughly half a class.** 29 visible slides, against Lecture 3's 31 —
but this deck is computation-heavy where Lecture 3 was mostly definitions, and
Topic 4 lost its continuation day when 9/1 became exam prep. It needs to lose
about ten slides, and it is fairly clear which ten:

| Cut candidate | Slides | Tested in the Spring bank? |
|---|:--:|---|
| Box plots                | 4 | **No** — zero items; "Box Plot" appears once, as a distractor |
| The SS → n − 1 arc       | 6 | **No** — `unbiased` and `replacement` appear only in HW5 (Topic 7/8), never in a Topic 4 item |
| SS / variance / SD computation | — | **Yes, almost exclusively** — HW2 Q5–7, HW3 Q1–2, Lab 3 Q6–10, E1 Q18–20 and Q37–38 |

**The numeric computations never happened** — SS, variance and SD were not worked
through, and that is precisely what the bank tests. The *Exercise time* slide
carrying `X = {4,5,6}`, `Y = {5,5,5,9}`, `Z = {6,6,6}` is still skipped. **Exam 1
is Thu 9/3**, so this has to be caught before then: the Fri 8/28 lab walks through
Lab 3 Q6–10, which is exactly these computations, and the 9/1 review is the second
chance. Do not let it wait for next year.

**The six-slide SS arc is the main overrun, and it is my addition.** It is good
material and it answers a real question, but it buys conceptual depth on
something no assignment or exam touches, while the examined hand-computation got
squeezed out. Next time either cut it to two slides (SS grows with n → the
average is what stays put) or keep the long version and move the box plots and
one of the exercise slides to lab.

**DONE (F26) — accessibility pass on the PDF.** Every image on every visible
slide now carries a description: **10 tagged `/Figure` structure elements, one
per real image**. (The earlier "16 /Alt against 13 image objects" check was
wrong — counting raster images misses every vector-drawn figure. Count `/Figure`
elements in the tag tree instead, and ignore the ~3 untagged ones per page that
Keynote emits as boilerplate.) The four equation images on the new decomposition slide are
spelled out in words ("the sum of (X minus mu) squared…"), since a screen reader
cannot read a rendered formula. `/Lang` is set to `en-US` and the title reads
"PSYC 220 Lecture 4: Spread and Variability" rather than the filename — both via
`slides/fix_pdf_a11y.py`, **which has to be re-run after every Keynote export**.

Two residual issues, neither scriptable:

- **11 inline equations on 4 slides carry no text and no alt** — *Deviations from
  the mean*, *Solution: Sum of squares*, *Sample variance*, *Standard deviation*.
  Typed inside body text, they generate **no structure element at all**, so a
  screen reader hears "Population variance:" and then silence — and no PDF patch
  can help, because there is no object to attach `/Alt` to. The fix is in the
  deck: cut each inline equation and paste it back as a *floating* object, which
  makes it reachable exactly as Lecture 3's Mean-slide equations were. Vector vs.
  image is irrelevant — Lecture 3's equations draw as vector paths too.
- **Three slides have no text at all** (PDF pages 5, 14 and 16 — the two
  distributions, the height histogram and box plot, and the six-panel skew
  figure). Their images are described, so the content is reachable, but with no
  title they are invisible to heading navigation and blank in an outline. Adding
  titles would change how the slides look, so it is left as a decision.

**DONE (F26) — the sample SD formula is corrected.** It read

    s_X = sqrt( SUM (X - mu_X)^2 / (n - 1) )

with the **population** mean under the **n - 1** correction, contradicting the
sample *variance* two bullets above it on the same slide. Now `M_X`.

Fixing it meant rebuilding the slide, because Keynote exposes no way to edit an
inline equation (see HANDOFF). The four formulas are now floating images from
`slides/make_l4_equations.py` (matplotlib, Computer Modern to match Keynote's
LaTeX), each carrying alt text, with the labels as positioned text items. The
original slide is kept as a **skipped duplicate at the end of the deck** — delete
it once you are happy.

**TODO — the population SS definition is orphaned.** *Solution: Sum of squares*
defines a Population SS and a Sample SS as a pair, but nothing downstream uses
the population one (the N-term Σ(X − μ)² over the whole population). The arc
actually contrasts two things, both computed **on a sample of n** — Σ(X − μ)²
and Σ(X − M)² — differing only in which mean you centre on. Show that pair
instead. Note this is not a text edit: both formulas on that slide are rendered
equation images, so new ones have to be produced.


- **DONE (F26) — unblocked, re-themed, and given its Lecture 3 recap.** The deck
  opens to scripts now. Re-themed to `16:10 ratio` by hand, the two Spring
  lab-admin slides skipped, and a "The previous lecture" slide inserted at 3,
  matching Lecture 3's own slot. 50 slides, 11 skipped.
- **TODO — the Lecture 3 half is still in the deck**, now slides 6–22 rather
  than 2–21; the recap slide shifted every index by one. The variability spine
  starts at 23. See HANDOFF for the full build list.
- **DECIDED — the central-tendency exercise stays in Lecture 3** and gets
  re-shown here as a callback rather than moved. It was taught on 8/25, and
  same-mean-different-spread is precisely what slide 23 draws.
- **DONE (F26) — a four-slide arc from SS to the n − 1 correction.** The 24
  Spring pop-quiz heights are the population (μ = 67.63, σ² = 20.15); one nested
  sample grows through them in collection order, n = 1…24, with 5 / 10 / 15
  marked. Slides, in deck order:

  | # (file) | Title | Figure | Does |
  |:--:|---|---|---|
  | 36 | SS grows with n              | `L4_ss_vs_n.png`       | SS about **μ** climbs: 108.5 → 171.7 → 219.9 |
  | 37 | *The average squared deviation* (existing) | — | defines variance |
  | 38 | SS is a total, not an average | `L4_ss_vs_var.png`     | SS climbing beside SS/n settling at σ² |
  | 39 | Two ways to compute SS       | `L4_ss_two_means.png`  | SS about μ vs about M; the gap |
  | 40 | *Sample variance* (existing) | — | gives the n − 1 formula |
  | 41 | Why n − 1                    | `L4_ss_expectation.png`| E[SS_μ] = nσ², E[SS_M] = (n−1)σ² |

  Slide 36 was rewritten from the sample mean to the **population mean**, so the
  arc runs μ → M → why that matters, instead of starting at the harder case.

  Verified before drawing anything: **SS about M ≤ SS about μ always**, since M
  minimises Σ(X − c)²; and over 20,000 i.i.d. samples the two expectations land
  on nσ² and (n−1)σ² (at n = 5: 101.0 vs 100.8, and 81.1 vs 80.6). Slide 41's
  figure plots the simulation as points on top of the theory lines.

  **The curves start at n = 1**, and that is the point of the slide, not a detail:
  (n−1)σ² is exactly 0 there, and it is exactly 0 in the simulation too — with
  one score, M *is* that score, so every deviation is zero. One observation tells
  you nothing whatever about spread. That is the most intuitive form of the whole
  n − 1 argument, so it is called out on the figure and in the third bullet.

  **If a student asks whether the two curves cross — they cannot.** The
  decomposition is exact:

      SS about μ  =  SS about M  +  n(M − μ)²

  verified to float precision at every n. The second term is a square, so the
  gap is never negative and the orange curve can never rise above the blue one.
  They *touch* exactly once, at n = 24, where the sample is the population and
  M = μ makes the term vanish. Between n ≈ 10 and 17 they look coincident only
  because the gap there is 0.13–0.89 on a 0–530 axis — well under a pixel.

  **But the two slides do not assume the same sampling scheme, and that matters
  at the right-hand end.** Slide 39 walks one nested sample *without replacement*
  through a finite population until it is used up. Slide 41 simulates *with
  replacement* — i.i.d. draws from a population you cannot exhaust. Those give
  different expected gaps:

  | Scheme | E[SS about M] | Expected gap |
  |---|---|---|
  | With replacement (i.i.d.) | (n − 1)σ² | σ², constant — parallel lines |
  | Without replacement, N = 24 | (n − 1)S², S² = SS/(N−1) = 21.03 | σ²(N − n)/(N − 1) — falls to 0 at n = N |

  Both verified by simulation at n = 1, 5, 10, 15, 20, 23, 24. The
  without-replacement gap runs 20.3 → 16.9 → 12.2 → 7.9 → 3.5 → 0.9 → 0.0
  against the formula's 20.15 → 16.65 → 12.27 → 7.89 → 3.51 → 0.88 → 0.

  So slide 39's curves meeting at n = 24 is **not** merely one draw being lucky:
  under its own sampling scheme they are *expected* to meet, because the sample
  becomes the population. Slide 41's lines stay parallel only because it draws
  fresh samples with replacement. The clean E[SS about M] = (n − 1)σ² that
  justifies the n − 1 divisor needs the i.i.d. assumption; the finite-population
  version carries a correction factor that is well beyond this course.

  **Resolved by showing both schemes rather than hiding one.** Two slides were
  added after *Why n − 1*:

  | # (file) | Title | Figure | Does |
  |:--:|---|---|---|
  | 42 | Sampling without replacement  | `L4_ss_expectation_wor.png` | same picture under the scheme slide 39 actually uses; the curves converge and meet at n = 24 |
  | 43 | With or without replacement?  | `L4_replacement_gap.png`    | what replacement means, and the two gap formulas side by side |

  So slide 41 keeps the clean i.i.d. result that justifies n − 1, slide 42 shows
  why slide 39's curves meet, and slide 43 supplies the concept both rest on.
  Nothing has to be hedged, and the thing a sharp student would notice is now
  the subject of a slide rather than a hole.

  Two honest wrinkles, both worth saying out loud rather than hiding:
  - **SS/n is not flat at small n** — it spikes to 35.5 at n = 3 when the 77
    enters. The slide says so ("the wobble at n = 3"); variance estimates from
    tiny samples being unstable is a real lesson, not a blemish.
  - **For one sample the μ/M gap is erratic** — 23.7 at n = 5, but 0.8 at n = 10
    and 0.2 at n = 15, because this sample's M happens to land on μ. Slide 39
    runs the full range to n = 24 and calls out the n = 5 gap with a leader, so
    the widest part is named rather than left to be spotted. The pay-off for
    going all the way is the right-hand end: at n = 24 the sample *is* the
    population, M = μ, and the two curves must meet exactly — annotated on the
    figure. The exact-σ² result stays on slide 41, where it is averaged. The
    final bullet says SS about M is "never larger" rather than "always smaller",
    because at n = 24 the two are equal and the figure says so.

  Figures: `~/miniconda3/envs/nb/bin/python slides/make_l4_figs.py` regenerates
  all four from `PSYC220/quiz_data_table_wide_clean.csv`. Blue/orange, validated
  for colour-vision separation (ΔE 24.6 protan); both series direct-labelled,
  which is also the required relief for orange's low contrast on white. Bodies
  are four bullets with the placeholder at h = 250 — **five bullets triggers
  Keynote's autoshrink** and the slide silently renders smaller than its
  neighbours, which is what happened to "Why n − 1" on the first pass.

- **NEXT — seven skipped slides carry instructor keys** (one with raw LaTeX,
  `$\bar{x}$, rendered as literal text). If those are meant to be shown, the
  LaTeX needs rendering; if not, they are fine skipped.
