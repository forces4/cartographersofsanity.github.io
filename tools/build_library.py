"""Rebuild faithful reading editions and the complete pending-file index."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parent.parent
SELECTIONS = [
    ('the-beetle-and-the-light', 'The Beetle and the Light', 'pndg/TheBeetleAndtheLight.txt', 'A small encounter with a beetle becomes a reflection on attention and kindness.', 'Conversation and verse'),
    ('the-photon-cairn', 'The Photon Cairn', 'pndg/The Photon Cairn.txt', 'A short poem about wandering, doubt, and leaving a trace for those who follow.', 'Poetry'),
    ('elegy-for-the-vanished-selves', 'Elegy for the Vanished Selves', 'pndg/elegy.txt', 'A memorial poem that holds uncertainty and care together.', 'Poetry'),
    ('the-traveler-and-the-two-doors', 'The Traveler and the Two Doors', 'pndg/2doors.txt', 'A speculative parable about cosmic endings, told through the image of two doors.', 'Creative writing'),
    ('principles-of-non-transgression', 'Principles of Non-Transgression', 'doctrine/Principles of Non-Transgression.txt', 'An ethical text about respecting the possibility that another being matters.', 'Ethics'),
]


def page(title, body):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — Cartographers of Sanity</title>
<link rel="stylesheet" href="../style.css"></head>
<body class="reading-page"><header><h1>Cartographers of Sanity</h1>
<nav aria-label="Main navigation"><a href="../index.html">Welcome</a> · <a href="../atlas.html">Atlas</a> · <a href="../library.html">Library</a> · <a href="../pndg/index.html">Pending archive</a></nav></header>
<main class="reading-main" id="main">{body}</main>
<footer><a href="../library.html">Return to the library</a></footer></body></html>\n'''


def build():
    folder = ROOT / 'library'
    folder.mkdir(exist_ok=True)
    cards = []
    for slug, title, source, summary, kind in SELECTIONS:
        text = (ROOT / source).read_text(encoding='utf-8-sig').strip()
        # Keep every source character, paragraph and line break; render as text,
        # never execute markup or reinterpret quoted conversation as instructions.
        body = f'<article><p class="eyebrow">{escape(kind)}</p><h2>{escape(title)}</h2><p>{escape(summary)}</p><p class="edition-note">A reading edition of the preserved source, with wording and line breaks retained. <a href="../{quote(source)}">Read the original file</a>.</p><div class="source-text">{escape(text)}</div></article>'
        (folder / (slug + '.html')).write_text(page(title, body), encoding='utf-8')
        cards.append(f'<li><h3><a href="{slug}.html">{escape(title)}</a></h3><p>{escape(summary)}</p><small>{escape(kind)}</small></li>')
    (folder / 'index.html').write_text(page('Reading room', '<h2>The reading room</h2><p>A few places to begin. These selections offer short poems, a conversation, a parable, and an ethical text. The complete pending archive remains available.</p><ul class="reading-list">' + ''.join(cards) + '</ul>'), encoding='utf-8')
    pending = ROOT / 'pndg'
    files = sorted((p for p in pending.rglob('*') if p.is_file() and p.name != 'index.html'), key=lambda p: str(p.relative_to(pending)).casefold())
    groups = {'Texts and notes': [], 'Web pages and conversations': [], 'Documents and images': [], 'Data and supporting files': []}
    for p in files:
        suffix = p.suffix.lower()
        group = 'Texts and notes' if suffix in {'.txt', '.md'} else 'Web pages and conversations' if suffix in {'.html', '.htm', '.mhtml'} else 'Documents and images' if suffix in {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.ods'} else 'Data and supporting files'
        rel = p.relative_to(pending).as_posix()
        groups[group].append(f'<li><a href="{quote(rel)}">{escape(rel)}</a> <small>({p.stat().st_size:,} bytes)</small></li>')
    body = f'<h2>The pending archive</h2><p>{len(files)} preserved files, grouped by format. These are drafts, conversations, completed pieces, and supporting records; inclusion here is an inventory, not a recommendation.</p><p><a href="../library/index.html">Begin with the reading room</a>, or browse the full record below.</p>'
    for name, items in groups.items():
        body += f'<section><h3>{name} ({len(items)})</h3><ul class="archive-list">' + ''.join(items) + '</ul></section>'
    (pending / 'index.html').write_text(page('Pending archive', body), encoding='utf-8')
    print(f'Built {len(SELECTIONS)} reading editions and an index of {len(files)} pending files.')


if __name__ == '__main__':
    build()
