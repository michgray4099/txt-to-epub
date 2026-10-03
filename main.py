"""TXT to EPUB — Wrap a UTF-8 text file into a minimal EPUB with a title and one chapter."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='txt_to_epub',
        description='Wrap a UTF-8 text file into a minimal EPUB with a title and one chapter.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('TXT to EPUB')
    print('A novel draft you can open in a reader.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
