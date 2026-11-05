#!/usr/bin/env python
"""House style for every student-facing item: American spelling, one notation.

Shared by the assignment builders and `exams/examlib.py` so the two trees can
never drift apart. Import it with the repo root on sys.path:

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
    from style_check import check_style

    check_style(all_text_fragments, label='A14')

Why this exists: CLAUDE.md has required American spelling since the start, and
nothing enforced it. Shipped items carry "centred" (A9), "behavioural" and
"favours" (Mock Exam 2), "centre" and "standardised" (Exam 2) -- most of them
authored *by* the agent that was told to write American English. Notation drifted
too: "Cohen's D" with a capital D in A11 against "Cohen's d" everywhere else, and
p-value spelled both ways across A10. A reviewer does not catch this reliably;
a regex does.

Run it over anything student-facing -- stems, options, and alt text alike.
"""
import re

# British -> American. Only unambiguous pairs: "analysis" and "practice" (noun)
# are identical in both and must NOT be flagged, so the verb forms are matched
# explicitly rather than by prefix.
BRITISH = [
    (r'\bbehaviour', 'behavior'),
    (r'\bcolour', 'color'),
    (r'\bcentr(e|ed|es|ing)\b', 'center / centered'),
    (r'\blabell(ed|ing)\b', 'labeled / labeling'),
    (r'\banalys(e|ed|ing)\b', 'analyze / analyzed / analyzing'),
    (r'\b(summaris|recognis|organis|normalis|standardis|randomis|generalis|'
     r'categoris|emphasis|minimis|maximis|hypothesis)(e|ed|es|ing)\b', '-ize'),
    (r'\bgrey\b', 'gray'),
    (r'\bfavour', 'favor'),
    (r'\bneighbour', 'neighbor'),
    (r'\bpractis(e|ed|ing)\b', 'practice / practiced / practicing'),
    (r'\bmodelling\b', 'modeling'),
    (r'\b(travell|cancell|totall|signall)(ed|ing)\b', 'single l'),
    (r'\bdefence\b', 'defense'),
    (r'\bsceptic', 'skeptic'),
    (r'\bjudgement\b', 'judgment'),
    (r'\bprogramme\b', 'program'),
    (r'\bmetre\b', 'meter'),
    (r'\bfulfil\b', 'fulfill'),
    (r'\blicence\b', 'license'),
]

# Notation. These are case-sensitive on purpose: the complaint was "Cohen's D".
NOTATION = [
    (r"Cohen'?s\s+D\b", "Cohen's d -- lowercase italic d"),
    # Lab 7 Q6 wrote the effect size as a capital D in its options as well as
    # its stem, which the phrase pattern above does not see. In this course a
    # capital D against a decimal is always Cohen's d.
    (r'\bD\s*=\s*\d*\.\d', "d = 0.2 -- lowercase d for Cohen's d"),
    (r'\bZ-?scores?\b', 'z-score -- lowercase z'),
    (r'\bT-tests?\b', 't-test -- lowercase t'),
    (r'\bT-distribution', 't-distribution -- lowercase t'),
    # Settled 11/4: N is a population's size (Σ(X − μ)² / N). The total of a
    # multi-group sample is lowercase n, with n₁, n₂, … for the groups, so the
    # ANOVA df read n − k and n − 1. The textbook writes N for that total.
    (r'\bN\s*[−-]\s*(k|1|2)\b', 'n − k / n − 1 -- lowercase n for a total sample size; N is a population size'),
    (r'\bP-?values?\b', 'p-value -- lowercase p; reword if it starts a sentence'),
    (r'\bHo\b', 'H0 -- the digit zero, not the letter o'),
    # The alternative hypothesis is HA in this course, matching the textbook
    # (which writes H_A 68 times against H_1 once). "HA (H1)" and "HA, also
    # written H1" are allowed as glosses and stripped before this runs -- see
    # GLOSS below. A bare H1 is not.
    (r'\bH_?\{?1\}?\b', 'HA -- the alternative hypothesis is HA here; '
     'write "HA (H1)" only to note that H1 means the same thing'),
    (r'\bType\s+[12]\b', 'Type I / Type II -- roman numerals'),
    (r'\bstandard error of mean\b', 'standard error of the mean'),
]


# A gloss noting that H1 means the same as HA is deliberate; strip it so the
# bare-H1 rule above does not fire on it. Both shapes are allowed:
#   "HA (H1)"            and   "HA, also written H1"
GLOSS = re.compile(
    r'H_?\{?[Aa]\}?\s*\(\s*H_?\{?1\}?\s*\)'
    r'|H_?\{?[Aa]\}?\s*,?\s*(?:also\s+written|or)\s+H_?\{?1\}?',
    re.IGNORECASE)


# --- what a Blackboard tab-delimited upload actually cannot take ----------
#
# NOT "non-ASCII". That rule was an over-generalization and is now withdrawn:
# the original HANDOFF note was about *LaTeX* flattening -- HW1's summation
# extracted as "X1X2X3X4X565536(sum)i=15Xi2" -- and the Unicode summation sign
# in that very string came through intact. A1, A5, A7, A8 and A9 all shipped
# with Greek letters, a superscript two, plus-minus, an arrow and even a
# plane-1 math-italic sigma, and uploaded fine. Unicode is allowed; write
# H-nought as H₀ and sigma-squared as σ² if you want to.
#
# Two things genuinely break an upload:
_UPLOAD_FATAL = [
    (r'\t', 'a literal TAB — the upload format is tab-delimited, so this '
             'splits the row into the wrong fields'),
    (r'\n|\r', 'a newline — it ends the row early'),
]
# ...and one genuinely flattens, losing its structure rather than its characters:
_LATEX_IN_ITEM = [
    (r'\\[a-zA-Z]+', r'a LaTeX command (\frac, \sigma, ...) — assignment items '
                       'are plain text, not MathJax; use the Unicode character'),
    (r'\$[^$\n]{1,80}\$', 'LaTeX math delimiters — these flatten on upload; '
                           'write the symbols directly'),
    (r'[\^_]\{', 'TeX grouping (^{...} or _{...}) — use ² ₀ ₘ or plain text'),
    # An underscore between two alphanumerics is a LaTeX-ism: Blackboard's
    # upload has no markup pass, so `s_M` reaches the student as the literal
    # three characters s, underscore, M. A run of underscores on its own is a
    # fill-in-the-blank line (A10 Q2) and is left alone.
    (r'[A-Za-z0-9]_[A-Za-z0-9]',
     'an underscore subscript — it renders literally, not as a subscript. Use a '
     'Unicode subscript (sₘ, H₀, sₚ) or spell the quantity out'),
]


def check_upload_safe(texts, label=''):
    """Fail on what a tab-delimited Blackboard upload cannot carry.

    Unicode is fine. Call this from the assignment writer only: exams render
    through MathJax and are *expected* to contain LaTeX.
    """
    bad = []
    for t in texts:
        if not t:
            continue
        for pat, why in _UPLOAD_FATAL + _LATEX_IN_ITEM:
            for m in re.finditer(pat, t):
                bad.append(f'  {m.group(0)!r} -> {why}\n      in: {t[:70]}')
    if bad:
        raise AssertionError(
            f'{label}: {len(bad)} item(s) a Blackboard upload cannot carry:\n'
            + '\n'.join(bad))
    return True


def find_style_issues(texts):
    """Return [(found, guidance, context)] for every violation in `texts`."""
    out = []
    for t in texts:
        if not t:
            continue
        t = GLOSS.sub('HA', t)
        for pat, fix in BRITISH:
            for m in re.finditer(pat, t, re.IGNORECASE):
                out.append((m.group(0), fix, t[:72]))
        for pat, fix in NOTATION:
            for m in re.finditer(pat, t):
                out.append((m.group(0), fix, t[:72]))
    return out


def check_style(texts, label=''):
    """Fail the build on any American-spelling or notation violation."""
    bad = find_style_issues(texts)
    if bad:
        lines = [f'  {found!r} -> {fix}\n      in: {ctx}' for found, fix, ctx in bad]
        raise AssertionError(
            f'{label}: {len(bad)} house-style violation(s) '
            f'(CLAUDE.md: American spelling, one notation):\n' + '\n'.join(lines))
    return True
