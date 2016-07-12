Builds on a [previous project](https://github.com/Datamine/Television).

Set up the virtualenv:
`virtualenv venv
source venv/bin/activate
pip install -r requirements.txt`

First: `getfrequencies.py` to retrieve word frequency dictionaries, storing each year's data in a file.
Second: `postprocess.py year_wordcounts` to correct garbled HTML output to alphanumeric strings. also lemmatize plurals and verbs.
