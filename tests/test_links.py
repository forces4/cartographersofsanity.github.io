from pathlib import Path
from urllib.parse import urlparse

import pytest
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent


def is_valid_href(href: str, base_dir: Path) -> bool:
    if not href or href.startswith('#'):
        return True

    parsed = urlparse(href)

    if parsed.scheme in {'mailto', 'tel'}:
        return True

    if parsed.scheme in {'http', 'https'}:
        return bool(parsed.netloc)

    path = parsed.path
    if Path(path).name == '.html':
        # placeholder like ./doctrine/.html
        return True

    if href.startswith('/'):
        target = ROOT / path.lstrip('/')
    else:
        target = (base_dir / path).resolve()
    if not target.exists() and str(path).startswith('doctrine/'):
        # unfinished doctrine links
        return True
    return target.exists()


def html_files():
    return [p for p in ROOT.rglob('*.html') if 'Pending' not in p.parts]


@pytest.mark.parametrize('html_path', html_files())
def test_links(html_path: Path):
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    for tag in soup.find_all('a'):
        href = tag.get('href')
        assert is_valid_href(href, html_path.parent), f"{html_path}: broken link {href}"
