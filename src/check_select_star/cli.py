"""Creating CLI to wrap around custom pre-commit check."""

import argparse
from typing import Sequence

from .check_select_star import check_select_star


def main(argv: Sequence[str] | None = None) -> int:
    """Doc string."""
    parser = argparse.ArgumentParser(prog='check_select_star')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )

    args = parser.parse_args(argv)
    results = [check_select_star(filename) for filename in args.filenames]
    return int(any(results))

