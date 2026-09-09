apk add --update --no-cache python3 py3-pip

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install bibtexparser ruamel.yaml pyYAML

# python -m academic.cli import publications.bib data/zh/authors content/zh/publications/ --compact --verbose --overwrite