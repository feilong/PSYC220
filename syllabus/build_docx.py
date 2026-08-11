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
    root = ET.fromstring(doc)
    total = text_width(root)

    tables = list(root.iter(W + 'tbl'))
    if len(tables) != len(COLUMN_PCT):
        raise SystemExit(f'{len(tables)} tables found but {len(COLUMN_PCT)} '
                         'width specs given — update COLUMN_PCT.')

    for tbl, pcts in zip(tables, COLUMN_PCT):
        ncol = len(tbl.find(W + 'tblGrid').findall(W + 'gridCol'))
        if ncol != len(pcts):
            raise SystemExit(f'table has {ncol} columns, spec has {len(pcts)}')
        set_table_widths(tbl, split_width(total, pcts))

    out = ET.tostring(root, encoding='unicode')
    orig_open = re.search(r'<w:document\b[^>]*>', doc).group(0)
    out = re.sub(r'^<w:document\b[^>]*>', orig_open, out, count=1)
    parts['word/document.xml'] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + out
    ).encode('utf-8')

    with zipfile.ZipFile(DOCX, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zout.writestr(info, parts[info.filename])

    print(f'{DOCX}: text width {total} twips ({total/1440:.2f}")')
    for i, pcts in enumerate(COLUMN_PCT, 1):
        cols = split_width(total, pcts)
        print(f'  table {i}: {cols} = {sum(cols)} twips '
              f'({sum(cols)/1440:.2f}")  {pcts}%')


if __name__ == '__main__':
    main()
