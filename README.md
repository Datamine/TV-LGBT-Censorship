Builds on a [previous project](https://github.com/Datamine/Television).

Set up the virtualenv:
`virtualenv venv
source venv/bin/activate
pip install -r requirements.txt`

1. `getfrequencies.py` to retrieve word frequency dictionaries, storing each year's data in a file.
2. `postprocess.py year_wordcounts` to correct garbled HTML output to alphanumeric strings. also lemmatize plurals and verbs.
