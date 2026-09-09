#!/usr/bin/env python3

import argparse
import importlib.metadata
import logging
import sys
from pathlib import Path
import yaml
from argparse import RawTextHelpFormatter

from academic.import_bibtex import import_bibtex
from academic.utils import AcademicError

# Initialise logger.
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.WARNING,
    datefmt="%I:%M:%S%p",
)
log = logging.getLogger(__name__)


def main():
    # Strip command name (currently `academic`) and feed arguments to the parser
    try:
        parse_args(sys.argv[1:])
    except AcademicError as exc:
        log.error("%s", exc)
        raise SystemExit(1) from exc


def parse_args(args):
    """Parse command-line arguments"""

    # Initialise command parser.
    parser = argparse.ArgumentParser(description=f"Academic CLI", formatter_class=RawTextHelpFormatter)
    subparsers = parser.add_subparsers(help="Sub-commands", dest="command")

    # Sub-parser for import command.
    parser_a = subparsers.add_parser("import", help="Import content into your website or book")
    parser_a.add_argument("input", type=str, help="File path to your BibTeX or Jupyter Notebook file(s)")
    parser_a.add_argument("authors_dir", type=str, help="Directory containing author information")
    parser_a.add_argument("output", type=str, help="Output path (e.g. `content/publication/`)")
    parser_a.add_argument("--featured", action="store_true", help="Flag publications as featured")
    parser_a.add_argument("--overwrite", action="store_true", help="Overwrite existing files in output path")
    parser_a.add_argument("--compact", action="store_true", help="Generate minimal markdown")
    parser_a.add_argument(
        "--normalize",
        action="store_true",
        help="Normalize each BibTeX keyword to lowercase with uppercase first letter",
    )
    parser_a.add_argument("-v", "--verbose", action="store_true", required=False, help="Verbose mode")
    parser_a.add_argument(
        "-dr",
        "--dry-run",
        action="store_true",
        required=False,
        help="Perform a dry run (e.g. for testing purposes)",
    )

    known_args, unknown = parser.parse_known_args(args)



    # If no arguments, show help.
    if len(args) == 0:
        parser.print_help()
        parser.exit()
    else:
        slugs = []
        if known_args.authors_dir:
            
            for yaml_file in Path(known_args.authors_dir).rglob("*"):
                if yaml_file.suffix.lower() not in {".yaml", ".yml"}:
                    continue

                with yaml_file.open("r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

                if isinstance(data, dict) and "slug" in data:
                    slugs.append(data["slug"])

        # The command has been recognised, proceed to parse it.
        if known_args.command:
            if known_args.verbose:
                # Set logging level to debug if verbose mode activated.
                logging.getLogger().setLevel(logging.INFO)
            if known_args.input.lower().endswith(".bib"):
                # Run command to import bibtex.
                import_bibtex(
                    known_args.input,
                    slugs=slugs,
                    pub_dir=known_args.output,
                    featured=known_args.featured,
                    overwrite=known_args.overwrite,
                    normalize=known_args.normalize,
                    compact=known_args.compact,
                    dry_run=known_args.dry_run,
                )


if __name__ == "__main__":
    main()
