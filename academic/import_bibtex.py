import calendar
import os
import re
from datetime import date as calendar_date
from datetime import datetime
from pathlib import Path

import bibtexparser
from bibtexparser import Library
from bibtexparser.model import Entry, Field
from bibtexparser.middlewares import LatexDecodingMiddleware

from academic.generate_markdown import GenerateMarkdown
from academic.publication_type import PUB_TYPES_BIBTEX_TO_CSL


def import_bibtex(
    bibtex,
    slugs,
    pub_dir=os.path.join("content", "publication"),
    featured=False,
    overwrite=False,
    normalize=False,
    compact=False,
    dry_run=False,
):
    """Import publications from BibTeX file"""
    from academic.cli import log
    from academic.utils import AcademicError

    # Check BibTeX file exists.
    if not Path(bibtex).is_file():
        err = "Please check the path to your BibTeX file and re-run"
        log.error(err)
        raise AcademicError(err)

    # The default v2 stack resolves strings and removes enclosing braces.
    # Decode LaTeX accents to Unicode, matching the former customization.
    library = bibtexparser.parse_file(str(bibtex), append_middleware=[LatexDecodingMiddleware()])
    if library.failed_blocks:
        details = "; ".join(
            f"line {block.start_line}: {block.error}"
            for block in library.failed_blocks
        )
        err = f"Could not parse BibTeX: {details}"
        log.error(err)
        raise AcademicError(err)

    for bib_entry in library.entries:
        # Keep the existing Markdown helpers' dictionary interface.
        entry = {field.key.lower(): field.value for field in bib_entry.fields}
        entry["ID"] = bib_entry.key
        entry["ENTRYTYPE"] = bib_entry.entry_type.lower()
        parse_bibtex_entry(
            entry,
            slugs,
            pub_dir=pub_dir,
            featured=featured,
            overwrite=overwrite,
            normalize=normalize,
            compact=compact,
            dry_run=dry_run,
        )


def parse_bibtex_entry(
    entry,
    slugs,
    pub_dir=os.path.join("content", "publication"),
    featured=False,
    overwrite=False,
    normalize=False,
    compact=False,
    dry_run=False,
):
    """Parse a bibtex entry and generate corresponding publication bundle"""
    from academic.cli import log

    log.info(f"Parsing entry {entry['ID']}")

    # Validate before creating or overwriting any files.
    publication_date = parse_publication_date(entry)

    authors = None
    if "author" in entry:
        authors = entry["author"]
    elif "editor" in entry:
        authors = entry["editor"]

    authors = clean_bibtex_authors([i.strip() for i in authors.replace("\n", " ").split(" and ")])

    title = clean_bibtex_str(entry["title"])

    bundle_name = f"{publication_date.year:04d}{publication_date.month:02d}-{authors[0].split()[-1].lower()}-{slugify('-'.join(title.split()[:2]))}"

    bundle_path = os.path.join(pub_dir, bundle_name)
    markdown_path = os.path.join(bundle_path, "index.md")
    cite_path = os.path.join(bundle_path, "cite.bib")
    date = datetime.utcnow()
    timestamp = date.isoformat("T") + "Z"  # RFC 3339 timestamp.

    # Do not overwrite publication bundle if it already exists.
    if not overwrite and os.path.isdir(bundle_path):
        log.warning(f"Skipping creation of {bundle_path} as it already exists. " f"To overwrite, add the `--overwrite` argument.")
        return

    # Create bundle dir.
    log.info(f"Creating folder {bundle_path}")
    if not dry_run:
        Path(bundle_path).mkdir(parents=True, exist_ok=True)

    # Save citation file.
    log.info(f"Saving citation to {cite_path}")
    if not dry_run:
        citation = Entry(
            entry_type=entry["ENTRYTYPE"],
            key=entry["ID"],
            fields=[
                Field(key=key, value=value)
                for key, value in entry.items()
                if key not in {"ID", "ENTRYTYPE"}
            ],
        )
        citation_library = Library()
        citation_library.add(citation)
        with open(cite_path, "w", encoding="utf-8") as f:
            f.write(bibtexparser.write_string(citation_library))

    # Prepare YAML front matter for Markdown file.
    if not dry_run:
        from importlib import resources as import_resources

        # Load the Markdown template from within the `templates` folder of the `academic` package
        template = import_resources.read_text(__package__ + ".templates", "publication.md")

        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(template)

    page = GenerateMarkdown(Path(bundle_path), dry_run=dry_run, compact=compact)
    page.load(Path("index.md"))

    page.yaml["title"] = title

    if "subtitle" in entry:
        page.yaml["subtitle"] = clean_bibtex_str(entry["subtitle"])

    page.yaml["date"] = publication_date.isoformat()
    page.yaml["publishDate"] = timestamp

    if authors is not None and len(authors) > 0:
        page.yaml["authors"] = update_author_with_slugs(authors, slugs)

    # Convert Bibtex publication type to the universal CSL standard, defaulting to `manuscript`
    default_csl_type = "manuscript"
    pub_type = PUB_TYPES_BIBTEX_TO_CSL.get(entry["ENTRYTYPE"], default_csl_type)
    page.yaml["publication_types"] = [pub_type]

    if "abstract" in entry:
        page.yaml["abstract"] = clean_bibtex_str(entry["abstract"])
    else:
        page.yaml["abstract"] = ""

    page.yaml["featured"] = featured

    # HugoBlox structured publication metadata (plain text, not Markdown italics).
    publication = {}
    fields = {
        "name": ("booktitle", "journaltitle", "journal"),
        "short_name": ("shortjournal", "journalshort"),
        "volume": ("volume",),
        "issue": ("issue", "number"),
        "pages": ("pages",),
        "publisher": ("publisher",),
    }
    for target, sources in fields.items():
        for source in sources:
            if entry.get(source, "").strip():
                publication[target] = clean_bibtex_str(entry[source])
                break
    page.yaml["publication"] = publication

    if "keywords" in entry:
        page.yaml["tags"] = clean_bibtex_tags(entry["keywords"], normalize)

    if "doi" in entry:
        page.yaml["hugoblox"] = {"ids": {"doi": clean_bibtex_str(entry["doi"]).strip()}}

    links = []
    if all(f in entry for f in ["archiveprefix", "eprint"]) and entry["archiveprefix"].lower() == "arxiv":
        links += [{"name": "arXiv", "url": "https://arxiv.org/abs/" + clean_bibtex_str(entry["eprint"])}]

    if "url" in entry:
        sane_url = clean_bibtex_str(entry["url"])

        if sane_url[-4:].lower() == ".pdf":
            page.yaml["url_pdf"] = sane_url
        else:
            links += [{"name": "URL", "url": sane_url}]

    if links:
        page.yaml["links"] = links

    # Save Markdown file.
    try:
        log.info(f"Saving Markdown to '{markdown_path}'")
        if not dry_run:
            page.dump()
    except IOError:
        log.error("Could not save file.")
    return page


def update_author_with_slugs(authors, slugs):
    """Update author names with slugs from the provided dictionary."""
    updated_authors = []
    for author in authors:
        # Check if the author name exists in the slugs dictionary
        if author.replace(" ","").lower() in slugs:
            updated_authors.append(author.replace(" ","").lower())
        else:
            updated_authors.append(author)  # Keep the original name if no slug is found
    return updated_authors

def slugify(s, lower=True):
    bad_symbols = (".", "_", ":")  # Symbols to replace with hyphen delimiter.
    delimiter = "-"
    good_symbols = (delimiter,)  # Symbols to keep.
    for r in bad_symbols:
        s = s.replace(r, delimiter)

    s = re.sub(r"(\D+)(\d+)", r"\1\-\2", s)  # Delimit non-number, number.
    s = re.sub(r"(\d+)(\D+)", r"\1\-\2", s)  # Delimit number, non-number.
    s = re.sub(r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))", r"\-\1", s)  # Delimit camelcase.
    s = "".join(c for c in s if c.isalnum() or c in good_symbols).strip()  # Strip non-alphanumeric and non-hyphen.
    s = re.sub("-{2,}", "-", s)  # Remove consecutive hyphens.

    if lower:
        s = s.lower()
    return s


def clean_bibtex_authors(author_str):
    """Convert author names to `firstname(s) lastname` format."""
    authors = []
    for s in author_str:
        s = s.strip()
        if len(s) < 1:
            continue

        if "," in s:
            split_names = s.split(",", 1)
            last_name = split_names[0].strip()
            first_names = [i.strip() for i in split_names[1].split()]
        else:
            split_names = s.split()
            last_name = split_names.pop()
            first_names = [i.replace(".", ". ").strip() for i in split_names]

        if last_name in ["jnr", "jr", "junior"]:
            last_name = first_names.pop()

        for item in first_names:
            if item in ["ben", "van", "der", "de", "la", "le"]:
                last_name = first_names.pop() + " " + last_name

        authors.append(" ".join(first_names) + " " + last_name)

    return authors


def clean_bibtex_str(s):
    """Clean BibTeX string and escape TOML special characters"""
    s = s.replace("\\", "")
    s = s.replace('"', '\\"')
    s = s.replace("{", "").replace("}", "")
    s = s.replace("\t", " ").replace("\n", " ").replace("\r", "")
    return s


def clean_bibtex_tags(s, normalize=False):
    """Clean BibTeX keywords and convert to TOML tags"""

    tags = clean_bibtex_str(s).split(",")
    tags = [tag.strip() for tag in tags]

    if normalize:
        tags = [tag.lower().capitalize() for tag in tags]

    return tags


def month2number(month):
    """Convert a numeric or English BibTeX month, rejecting invalid values."""
    value = str(month).strip()
    if value.isdigit():
        number = int(value)
    else:
        names = {name.lower(): i for i, name in enumerate(calendar.month_name) if name}
        names.update({name.lower(): i for i, name in enumerate(calendar.month_abbr) if name})
        number = names.get(value.lower().rstrip("."), 0)
    if not 1 <= number <= 12:
        raise ValueError(f"Invalid month: {month!r}")
    return f"{number:02d}"


def parse_publication_date(entry):
    """Normalize partial ISO dates or BibTeX year/month/day; never invent a year.

    An explicit date takes precedence. Missing month/day default to January/1.
    Unsupported ranges and invalid calendar dates are errors, not guesses.
    """
    from academic.utils import AcademicError

    raw = str(entry.get("date", "")).strip()
    try:
        if raw:
            match = re.fullmatch(r"(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?", raw)
            if not match:
                raise ValueError("expected YYYY, YYYY-MM, or YYYY-MM-DD")
            year, month, day = match.groups()
            month, day = month or "1", day or "1"
        else:
            year = str(entry.get("year", "")).strip()
            if not re.fullmatch(r"\d{4}", year):
                raise ValueError("a four-digit year is required")
            month = month2number(entry.get("month", "1"))
            day = str(entry.get("day", "1")).strip()
        return calendar_date(int(year), int(month), int(day))
    except (TypeError, ValueError) as exc:
        raise AcademicError(f"Invalid publication date for entry `{entry['ID']}`: {exc}. Fix its date/year/month/day fields.") from exc
