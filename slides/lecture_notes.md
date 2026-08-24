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
- **TODO — the deck is still text-and-screenshots.** Same note as Lecture 2: the
  central tendency half (Mean / Median / Mode / Example ×3) is pure text.

## Lecture 4 — Spread & variability

Deck split off from the same Spring Lecture 4 file; slides 22–49 (the two
same-mean-different-spread distributions onward) are the Fall Lecture 4 spine.

- **TODO — not yet built.** Needs the admin and central-tendency half deleted,
  the Week 2 / Week 3 plan slide added, and a decision on whether the
  central-tendency exercise (`X = {3,4,5,6,7}`, `Y = {5,5,5,5,5}`) stays at the
  end of Lecture 3 as practice or moves here as the hook into variability. It is
  currently at the end of Lecture 3.
- **NEXT — seven skipped slides carry instructor keys** (one with raw LaTeX,
  `$\bar{x}$, rendered as literal text). If those are meant to be shown, the
  LaTeX needs rendering; if not, they are fine skipped.
