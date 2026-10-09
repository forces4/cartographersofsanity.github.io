"""Validate maintained pages without treating historical exports as new content."""
from pathlib import Path
from urllib.parse import unquote, urlsplit

import pytest
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
PUBLIC_PAGES = sorted([*ROOT.glob('*.html'), *ROOT.glob('doctrine/*.html'), *ROOT.glob('library/*.html'), ROOT / 'pndg/index.html'])


@pytest.mark.parametrize('page', PUBLIC_PAGES, ids=lambda p: str(p.relative_to(ROOT)))
def test_public_links_and_assets(page):
    soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
    for tag in soup.find_all(['a', 'img', 'script', 'link']):
        url = tag.get('href') or tag.get('src')
        if not url:
            continue
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        assert '\\' not in parsed.path, f'{page}: Windows path {url}'
        path = unquote(parsed.path)
        target = ROOT / path.lstrip('/') if path.startswith('/') else page.parent / path
        assert target.exists(), f'{page}: missing target {url}'
        if parsed.fragment and target.suffix == '.html':
            linked = BeautifulSoup(target.read_text(encoding='utf-8'), 'html.parser')
            fragment = unquote(parsed.fragment)
            assert linked.find(id=fragment) or linked.find('a', attrs={'name': fragment}), f'{page}: missing fragment {url}'


def test_reading_editions_preserve_sources():
    import importlib.util
    spec = importlib.util.spec_from_file_location('build_library', ROOT / 'tools/build_library.py')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    for slug, _, source, _, _ in builder.SELECTIONS:
        assert slug == slug.lower() and ' ' not in slug
        soup = BeautifulSoup((ROOT / f'library/{slug}.html').read_text(), 'html.parser')
        assert soup.select_one('.source-text').get_text() == (ROOT / source).read_text(encoding='utf-8-sig').strip()


def test_pending_index_covers_every_file():
    pending = ROOT / 'pndg'
    soup = BeautifulSoup((pending / 'index.html').read_text(), 'html.parser')
    indexed = {unquote(a['href']) for a in soup.select('.archive-list a')}
    actual = {p.relative_to(pending).as_posix() for p in pending.rglob('*') if p.is_file() and p.name != 'index.html'}
    assert indexed == actual
