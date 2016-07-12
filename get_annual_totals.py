# John Loeber | Jul-12-2016 | Python 2.7.6 | Debian Linux | www.johnloeber.com

from os import listdir
from sys import argv
from ast import literal_eval
from operator import itemgetter
import pprint

def all_years(path):
    """
    goes into the path directory, parses all the files containing word freq
    dicts, and sums up the wordcounts for each year. 
    """
    directory = sorted(listdir(path))
    directory = filter(lambda x: x.isdigit(), directory)

    year_dict = {}

    for year in directory:
        file_path = path + year
        with open(file_path,'r') as f:
            dic = literal_eval(f.read().split('\n')[0])
            year_total = sum(dic.values())
            year_dict[year] = year_total

    return year_dict

# takes one command-line arg: directory of word frequency dictionaries
def main():
    path = argv[1]
    year_dict = all_years(path)
    # printer for dictionary
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(year_dict)

if __name__=='__main__':
    main()
