# Website repair — October 9, 2026

This pass preserves the archive and improves its public entry points. No source texts were deleted or rewritten, and nothing has been published from this workspace.

## Delivered

- Five reading editions in `library/`, linked prominently from the existing library page. Original wording and line breaks are preserved, including conversation framing and rough edges; each edition links to its source.
- A reading-room index and a complete `pndg/index.html` inventory: 309 files, grouped by format, with encoded URLs that work with spaces and punctuation.
- Larger body text, more comfortable line spacing, keyboard focus indicators, wrapping for long links, and a narrow-screen navigation layout in the shared stylesheet.
- Repairs to Windows-style paths, relative links in the wrong directory, a missing image reference, and external addresses missing `https://`.
- Repairs to navigation in older library and memory indexes where the intended file exists.
- A URL-decoding fix for the existing link checker, plus checks for public-page assets, fragments, reading-edition fidelity, and complete pending-index coverage.

## Validation

`/workspace/.setup-venv/bin/pytest -q tests/test_public_pages.py`: 39 passed.

Full test run: 142 passed, 3 failed. The remaining failures are missing historical resources:

- `archive/GWI.html`: `file:///C:/Users/wheat/OneDrive/Desktop/cmhPub_57-1-1.pdf`
- `archive/Sanity.html`: `..\pndg\Collection.zip`
- `pndg/Fairies.html`: `file:///C:/Users/Me/Desktop/Unity/Unity.zip`

These targets are not present in the repository. Their links remain in the record. The historical checker stops at the first broken link in each file, so additional missing references may remain in these three documents.

External website availability and visual browser layout were not checked. The public checks validate local files and fragments, not third-party service health.

## Filename work remaining

Every new reading-page filename is lowercase with hyphens and no spaces. Legacy source filenames remain unchanged so existing bookmarks and links continue to work. Repository-wide renaming is still unfinished; it needs a compatibility map before migration, particularly for downloaded conversations and their asset folders. Conventional repository controls such as `CNAME` should retain the names their hosting tools require.

The 309-file index is a complete inventory, not a claim that all files have received editorial review. Five source texts were selected and read for this pass; broader curation remains.

## Rebuilding

Run `python tools/build_library.py` after adding pending files or changing a selected source. The script rebuilds the reading editions and pending index. Add further reviewed works to `SELECTIONS` in that script.
