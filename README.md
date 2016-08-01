Builds on a [previous project](https://github.com/Datamine/Television).

Set up the virtualenv:
`virtualenv venv
source venv/bin/activate
pip install -r requirements.txt`

1. `getfrequencies.py` to retrieve word frequency dictionaries, storing each year's data in a file.
2. `postprocess.py year_wordcounts` to correct garbled HTML output to alphanumeric strings. also lemmatize plurals and verbs.
3. `ipython notebook` (needs jupyter installed and able to handle jupyter 3 notebooks) to launch the analysis script.

## Update August-1-2016:

My findings didn't support the hypothesis, so there may not be anything interesting here. It's good to have set up the dataset
and the data gathering machinery. I'm going to shelve this project and wait until I think of something else to investigate.
(Maybe prevalence of dialogue related to drugs? Other gradually changing social norms? Attitudes to marriage?)

## TODO: semantic analysis on episodes mentioning marriage etc.
