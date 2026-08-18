#!/usr/bin/env python3
"""Build the Fall 2026 syllabus .docx from the .md, with real table column widths.

Pandoc sizes docx tables to a fraction of the text column that never quite
reaches the margins, so tables land ~5.5" wide inside a 6.5" text block and look
ragged. This runs pandoc, then rewrites each table's grid to span the full text
width using the proportions in COLUMN_PCT.

Usage:  python build_docx.py
"""
import re
import subprocess
import zipfile
from xml.etree import ElementTree as ET

MD = 'PSYC220_011_012_syllabus_Ma_Fall2026.md'
DOCX = 'PSYC220_011_012_syllabus_Ma_Fall2026.docx'
REFERENCE = 'PSYC220_003_004_syllabus_Ma_Spring2026.docx'

# Column widths as percentages of the text width, per table, in document order.
COLUMN_PCT = [
    [22, 32, 46],          # Exam dates at a glance: Exam | Date | Covers
    [9, 13, 62, 16],       # Class by class: Class | Date | Topic | Reading
]

WNS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W = '{%s}' % WNS
ET.register_namespace('w', WNS)
ET.register_namespace('w14', 'http://schemas.microsoft.com/office/word/2010/wordml')


def _sub_or_get(parent, tag, index=0):
    el = parent.find(W + tag)
    if el is None:
        el = ET.Element(W + tag)
        parent.insert(index, el)
    return el


TITLE_STYLES = ('Title', 'TitleChar', 'Subtitle', 'SubtitleChar')


def normalize_styles(xml_bytes, pt=11, title_pt=14):
    """One size everywhere except the document title; headings differ by weight."""
    half = str(pt * 2)
    title_half = str(title_pt * 2)
    doc = xml_bytes.decode('utf-8')
    open_tag = re.search(r'<w:styles\b[^>]*>', doc).group(0)
    for prefix, uri in re.findall(r'xmlns:([A-Za-z0-9_]+)="([^"]+)"', open_tag):
        try:
            ET.register_namespace(prefix, uri)
        except ValueError:
            pass
    root = ET.fromstring(doc)

    # document-wide default
    dd = root.find(W + 'docDefaults')
    if dd is not None:
        rprd = dd.find(W + 'rPrDefault')
        if rprd is not None:
            rpr = _sub_or_get(rprd, 'rPr')
            for tag in ('sz', 'szCs'):
                _sub_or_get(rpr, tag).set(W + 'val', half)

    for st in root.findall(W + 'style'):
        sid = st.get(W + 'styleId') or ''
        rpr = st.find(W + 'rPr')
        if rpr is None and (sid.startswith(('Heading', 'Title', 'Subtitle')) or True):
            rpr = ET.SubElement(st, W + 'rPr')
        size = title_half if sid in TITLE_STYLES else half
        for tag in ('sz', 'szCs'):
            _sub_or_get(rpr, tag).set(W + 'val', size)
        # headings: bold instead of bigger; deeper levels also italic
        if sid.startswith(('Heading', 'Title', 'Subtitle')):
            _sub_or_get(rpr, 'b')
            _sub_or_get(rpr, 'bCs')
            m = re.search(r'Heading(\d)', sid)
            if m and int(m.group(1)) >= 3:
                _sub_or_get(rpr, 'i')
                _sub_or_get(rpr, 'iCs')
        # never let a style shrink or grow text
        for bad in list(rpr.findall(W + 'caps')) + list(rpr.findall(W + 'smallCaps')):
            rpr.remove(bad)
        # drop indents inherited from the reference document, which made
        # BodyText sit 119 twips right of FirstParagraph/Normal
        if sid in ('BodyText', 'FirstParagraph', 'Compact', 'Normal'):
            ppr = st.find(W + 'pPr')
            if ppr is not None:
                for ind in ppr.findall(W + 'ind'):
                    ppr.remove(ind)

    # pandoc only emits styles it uses, so Title may not exist; create it.
    if not any((st.get(W + 'styleId') or '') == 'Title' for st in root.findall(W + 'style')):
        st = ET.SubElement(root, W + 'style')
        st.set(W + 'type', 'paragraph')
        st.set(W + 'styleId', 'Title')
        ET.SubElement(st, W + 'name').set(W + 'val', 'Title')
        ET.SubElement(st, W + 'basedOn').set(W + 'val', 'Heading1')
        ET.SubElement(st, W + 'next').set(W + 'val', 'Normal')
        ET.SubElement(st, W + 'qFormat')
        rpr = ET.SubElement(st, W + 'rPr')
        ET.SubElement(rpr, W + 'b')
        ET.SubElement(rpr, W + 'bCs')
        for tag in ('sz', 'szCs'):
            ET.SubElement(rpr, W + tag).set(W + 'val', title_half)

    out = ET.tostring(root, encoding='unicode')
    out = re.sub(r'^<w:styles\b[^>]*>', open_tag, out, count=1)
    ET.fromstring(out)
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + out).encode('utf-8')


def promote_titles(root):
    """The two opening H1s are the document title; give them Word's Title style
    (14 pt) rather than Heading 1."""
    n = 0
    for pstyle in root.iter(W + 'pStyle'):
        if pstyle.get(W + 'val') == 'Heading1':
            pstyle.set(W + 'val', 'Title')
            n += 1
    return n


def unify_body_styles(root):
    """pandoc tags the first paragraph after a heading 'FirstParagraph' and the
    rest 'BodyText'; use one style so they cannot drift apart."""
    n = 0
    for pstyle in root.iter(W + 'pStyle'):
        if pstyle.get(W + 'val') == 'FirstParagraph':
            pstyle.set(W + 'val', 'BodyText')
            n += 1
    return n


def strip_direct_sizes(root):
    """Remove run-level size overrides so the styles govern."""
    n = 0
    for rpr in root.iter(W + 'rPr'):
        for tag in ('sz', 'szCs'):
            for el in rpr.findall(W + tag):
                rpr.remove(el)
                n += 1
    return n


def text_width(root):
    """Usable width in twips = page width - left/right margins."""
    sect = root.iter(W + 'sectPr').__next__()
    pg = sect.find(W + 'pgSz')
    mar = sect.find(W + 'pgMar')
    return (int(pg.get(W + 'w'))
            - int(mar.get(W + 'left'))
            - int(mar.get(W + 'right')))


def split_width(total, pcts):
    """Integer twip widths summing exactly to total."""
    cols = [round(total * p / 100) for p in pcts]
    cols[-1] += total - sum(cols)
    return cols


def repeat_header_row(tbl):
    """Mark the first row as a header so it repeats on every page a table spans
    (a digital-accessibility requirement for USC syllabi)."""
    tr = tbl.find(W + 'tr')
    if tr is None:
        return False
    trPr = tr.find(W + 'trPr')
    if trPr is None:
        trPr = ET.Element(W + 'trPr')
        tr.insert(0, trPr)
    if trPr.find(W + 'tblHeader') is None:
        ET.SubElement(trPr, W + 'tblHeader')
        return True
    return False


def set_table_widths(tbl, cols):
    grid = tbl.find(W + 'tblGrid')
    for gc, w in zip(grid.findall(W + 'gridCol'), cols):
        gc.set(W + 'w', str(w))
    for tr in tbl.findall(W + 'tr'):
        for tc, w in zip(tr.findall(W + 'tc'), cols):
            tcPr = tc.find(W + 'tcPr')
            if tcPr is None:
                tcPr = ET.SubElement(tc, W + 'tcPr')
            tcW = tcPr.find(W + 'tcW')
            if tcW is None:
                tcW = ET.SubElement(tcPr, W + 'tcW')
            tcW.set(W + 'w', str(w))
            tcW.set(W + 'type', 'dxa')


def main():
    subprocess.run(
        ['pandoc', '-f', 'markdown+autolink_bare_uris', '-t', 'docx',
         '--reference-doc', REFERENCE, MD, '-o', DOCX],
        check=True)

    zin = zipfile.ZipFile(DOCX)
    parts = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    doc = parts['word/document.xml'].decode('utf-8')

    # Register every prefix pandoc declared on <w:document> BEFORE parsing.
    # ElementTree otherwise invents ns0/ns1 prefixes for unregistered
    # namespaces and declares them on the root -- which the root-tag restore
    # below would then delete, leaving unbound prefixes that Word refuses to
    # open (e.g. r:id on every hyperlink becoming ns1:id).
    open_tag = re.search(r'<w:document\b[^>]*>', doc).group(0)
    for prefix, uri in re.findall(r'xmlns:([A-Za-z0-9_]+)="([^"]+)"', open_tag):
        try:
            ET.register_namespace(prefix, uri)
        except ValueError:
            pass

    root = ET.fromstring(doc)
    total = text_width(root)

    titles = promote_titles(root)
    unified = unify_body_styles(root)
    dropped = strip_direct_sizes(root)
    parts['word/styles.xml'] = normalize_styles(parts['word/styles.xml'])

    tables = list(root.iter(W + 'tbl'))
    if len(tables) != len(COLUMN_PCT):
        raise SystemExit(f'{len(tables)} tables found but {len(COLUMN_PCT)} '
                         'width specs given — update COLUMN_PCT.')

    for tbl, pcts in zip(tables, COLUMN_PCT):
        ncol = len(tbl.find(W + 'tblGrid').findall(W + 'gridCol'))
        if ncol != len(pcts):
            raise SystemExit(f'table has {ncol} columns, spec has {len(pcts)}')
        set_table_widths(tbl, split_width(total, pcts))
        repeat_header_row(tbl)

    out = ET.tostring(root, encoding='unicode')
    out = re.sub(r'^<w:document\b[^>]*>', open_tag, out, count=1)

    # Gate: refuse to write a document.xml Word cannot parse.
    ET.fromstring(out)
    declared = set(re.findall(r'xmlns:([A-Za-z0-9_]+)=', open_tag))
    used = set(re.findall(r'</?([A-Za-z0-9_]+):', out))
    unbound = used - declared - {'xml'}
    if unbound:
        raise SystemExit(f'unbound namespace prefixes would break Word: {sorted(unbound)}')
    parts['word/document.xml'] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + out
    ).encode('utf-8')

    with zipfile.ZipFile(DOCX, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zout.writestr(info, parts[info.filename])

    print(f'{DOCX}: text width {total} twips ({total/1440:.2f}")')
    print(f'  typography: 11 pt throughout; {dropped} size overrides removed, '
          f'{unified} FirstParagraph -> BodyText, {titles} Heading1 -> Title (14 pt)')
    for i, pcts in enumerate(COLUMN_PCT, 1):
        cols = split_width(total, pcts)
        print(f'  table {i}: {cols} = {sum(cols)} twips '
              f'({sum(cols)/1440:.2f}")  {pcts}%')


if __name__ == '__main__':
    main()
