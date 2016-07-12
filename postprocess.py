# John Loeber | Oct-28-2014 | Python 2.7.6 | Debian Linux | www.johnloeber.com

from sys import argv
from ast import literal_eval
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
import os

def is_alphanumeric(x):
    """
    returns true if all characters in string are alphanumeric [stricter than ascii], 
    false otherwise.
    """
    return all((96 < ord(c) < 123) or (64 < ord(c) < 91) or (47 < ord(c) < 58) for c in x)

def replace(x):
    """
    replaces html-garbled characters with the closest alphanumeric representation.
    """
    # NBSP
    x = x.replace('\xc2\xa0',' ')
    # SPECIAL PUNCTUATION
    x = x.replace('\xc2\xa1',' ')
    x = x.replace('\xc2\xa2',' ')
    x = x.replace('\xc2\xa3',' ')
    x = x.replace('\xc2\xa4',' ')
    x = x.replace('\xc2\xa5',' ')
    x = x.replace('\xc2\xa6',' ')
    x = x.replace('\xc2\xa7',' ')
    x = x.replace('\xc2\xa8',' ')
    x = x.replace('\xc2\xa9',' ')
    x = x.replace('\xc2\xaa',' ')
    x = x.replace('\xc2\xab',' ')
    x = x.replace('\xc2\xac',' ')
    x = x.replace('\xc2\xad',' ')
    x = x.replace('\xc2\xae',' ')
    x = x.replace('\xc2\xaf',' ')
    x = x.replace('\xc2\xb0',' ')
    x = x.replace('\xc2\xb1',' ')
    x = x.replace('\xc2\xb2',' ')
    x = x.replace('\xc2\xb3',' ')
    x = x.replace('\xc2\xb4',' ')
    x = x.replace('\xc2\xb5',' ')
    x = x.replace('\xc2\xb6',' ')
    x = x.replace('\xc2\xb7',' ')
    x = x.replace('\xc2\xb8',' ')
    x = x.replace('\xc2\xb9',' ')
    x = x.replace('\xc2\xb9',' ')
    x = x.replace('\xc2\xba',' ')
    x = x.replace('\xc2\xbb',' ')
    x = x.replace('\xc2\xbc',' ')
    x = x.replace('\xc2\xbd',' ')
    x = x.replace('\xc2\xbe',' ')
    x = x.replace('\xc2\xbf',' ')

    # ACTUAL CHARACTERS
    x = x.replace('\xc3\x80','a')
    x = x.replace('\xc3\x81','a')
    x = x.replace('\xc3\x82','a')
    x = x.replace('\xc3\x83','a')
    x = x.replace('\xc3\x84','a')
    x = x.replace('\xc3\x85','a')
    x = x.replace('\xc3\x86','ae')
    x = x.replace('\xc3\x87','c')
    x = x.replace('\xc3\x88','e')
    x = x.replace('\xc3\x89','e')
    x = x.replace('\xc3\x8a','e')
    x = x.replace('\xc3\x8b','e')
    x = x.replace('\xc3\x8c','i')
    x = x.replace('\xc3\x8d','i')
    x = x.replace('\xc3\x8e','i')
    x = x.replace('\xc3\x8f','i')
    x = x.replace('\xc3\x90','d')
    x = x.replace('\xc3\x91','n')
    x = x.replace('\xc3\x92','o')
    x = x.replace('\xc3\x93','o')
    x = x.replace('\xc3\x94','o')
    x = x.replace('\xc3\x95','o')
    x = x.replace('\xc3\x96','o')
    x = x.replace('\xc3\x97',' ')
    x = x.replace('\xc3\x98','o')
    x = x.replace('\xc3\x99','u')
    x = x.replace('\xc3\x9a','u')
    x = x.replace('\xc3\x9b','u')
    x = x.replace('\xc3\x9c','u')
    x = x.replace('\xc3\x9d','y')
    x = x.replace('\xc3\x9e','p')
    x = x.replace('\xc3\x9f','sz')

    x = x.replace('\xc3\xa0','a')
    x = x.replace('\xc3\xa1','a')
    x = x.replace('\xc3\xa2','a')
    x = x.replace('\xc3\xa3','a')
    x = x.replace('\xc3\xa4','a')
    x = x.replace('\xc3\xa5','a')
    x = x.replace('\xc3\xa6','ae')
    x = x.replace('\xc3\xa7','c')
    x = x.replace('\xc3\xa8','e')
    x = x.replace('\xc3\xa9','e')
    x = x.replace('\xc3\xaa','e')
    x = x.replace('\xc3\xab','e')
    x = x.replace('\xc3\xac','i')
    x = x.replace('\xc3\xad','i')
    x = x.replace('\xc3\xae','i')
    x = x.replace('\xc3\xaf','i')

    x = x.replace('\xc3\xb0','o')
    x = x.replace('\xc3\xb1','n')
    x = x.replace('\xc3\xb2','o')
    x = x.replace('\xc3\xb3','o')
    x = x.replace('\xc3\xb4','o')
    x = x.replace('\xc3\xb5','o')
    x = x.replace('\xc3\xb6','o')

    x = x.replace('\xc3\xb7',' ')
    x = x.replace('\xc3\xb8','o')
    x = x.replace('\xc3\xb9','u')
    x = x.replace('\xc3\xba','u')
    x = x.replace('\xc3\xbb','u')
    x = x.replace('\xc3\xbc','u')
    x = x.replace('\xc3\xbd','y')
    x = x.replace('\xc3\xbe','y')

    x = x.replace('\xc4\x80','a')
    x = x.replace('\xc4\x81','a')
    x = x.replace('\xc4\x82','a')
    x = x.replace('\xc4\x83','a')
    x = x.replace('\xc4\x84','a')
    x = x.replace('\xc4\x85','a')
    x = x.replace('\xc4\x86','c')
    x = x.replace('\xc4\x87','c')
    x = x.replace('\xc4\x88','c')
    x = x.replace('\xc4\x89','c')
    x = x.replace('\xc4\x8a','c')
    x = x.replace('\xc4\x8b','c')
    x = x.replace('\xc4\x8c','c')
    x = x.replace('\xc4\x8d','c')
    x = x.replace('\xc4\x8d','c')
    x = x.replace('\xc4\x8e','d')
    x = x.replace('\xc4\x8f','d')
    x = x.replace('\xc4\x90','d')
    x = x.replace('\xc4\x91','d')
    x = x.replace('\xc4\x92','e')
    x = x.replace('\xc4\x93','e')
    x = x.replace('\xc4\x94','e')
    x = x.replace('\xc4\x95','e')
    x = x.replace('\xc4\x96','e')
    x = x.replace('\xc4\x97','e')
    x = x.replace('\xc4\x98','e')
    x = x.replace('\xc4\x99','e')
    x = x.replace('\xc4\x9a','e')
    x = x.replace('\xc4\x9b','e')
    x = x.replace('\xc4\x9c','g')
    x = x.replace('\xc4\x9d','g')
    x = x.replace('\xc4\x9e','g')
    x = x.replace('\xc4\x9f','g')
    
    x = x.replace('\xc4\xa0','g')
    x = x.replace('\xc4\xa1','g')
    x = x.replace('\xc4\xa2','g')
    x = x.replace('\xc4\xa3','g')
    x = x.replace('\xc4\xa4','h')
    x = x.replace('\xc4\xa5','h')
    x = x.replace('\xc4\xa6','h')
    x = x.replace('\xc4\xa7','h')

    x = x.replace('\xc4\xa7','h')
    x = x.replace('\xc4\xa8','i')
    x = x.replace('\xc4\xa9','i')
    x = x.replace('\xc4\xaa','i')
    x = x.replace('\xc4\xab','i')
    x = x.replace('\xc4\xac','i')
    x = x.replace('\xc4\xad','i')
    x = x.replace('\xc4\xae','i')
    x = x.replace('\xc4\xaf','i')
    x = x.replace('\xc4\xb0','i')
    x = x.replace('\xc4\xb1','i')

    x = x.replace('\xc4\xb2','ij')  
    # got tired of doing this manually. now just going to insert replacement
    # codes for the most common cases and filter out the rest (< 50 occurrences total). 
    x = x.replace('\xe2\x80\x99s','')
    x = x.replace('\xc5\x8d','o')
    x = x.replace('\xc5\xab','u')

    x = x.replace('\xe2\x80\x80',' ')
    x = x.replace('\xe2\x80\x81',' ')
    x = x.replace('\xe2\x80\x82',' ')
    x = x.replace('\xe2\x80\x83',' ')
    x = x.replace('\xe2\x80\x84',' ')
    x = x.replace('\xe2\x80\x85',' ')
    x = x.replace('\xe2\x80\x86',' ')
    x = x.replace('\xe2\x80\x87',' ')
    x = x.replace('\xe2\x80\x88',' ')
    x = x.replace('\xe2\x80\x89',' ')
    x = x.replace('\xe2\x80\x8a',' ')
    x = x.replace('\xe2\x80\x8b',' ')
    x = x.replace('\xe2\x80\x8c',' ')
    x = x.replace('\xe2\x80\x8d',' ')
    x = x.replace('\xe2\x80\x8e',' ')
    x = x.replace('\xe2\x80\x8f',' ')

    x = x.replace('\xe2\x80\x90','-')
    x = x.replace('\xe2\x80\x91','-')
    x = x.replace('\xe2\x80\x92','-')
    x = x.replace('\xe2\x80\x93','-')
    x = x.replace('\xe2\x80\x94','-')
    x = x.replace('\xe2\x80\x95','-')

    x = x.replace('\xe2\x80\x96',' ')
    x = x.replace('\xe2\x80\x97',' ')
    x = x.replace('\xe2\x80\x98','')
    x = x.replace('\xe2\x80\x99','')
    x = x.replace('\xe2\x80\x9a','')
    x = x.replace('\xe2\x80\x9b','')
    x = x.replace('\xe2\x80\x9c','')
    x = x.replace('\xe2\x80\x9d','')
    x = x.replace('\xe2\x80\x9e','')
    x = x.replace('\xe2\x80\x9f','')
    x = x.replace('\xe2\x80\xa0','')
    x = x.replace('\xe2\x80\xa1','')
    x = x.replace('\xe2\x80\xa2','')
    x = x.replace('\xe2\x80\xa3','')
    x = x.replace('\xe2\x80\xa4',' ')
    x = x.replace('\xe2\x80\xa5',' ')
    x = x.replace('\xe2\x80\xa6',' ')
    x = x.replace('\xe2\x80\xa7',' ')
    x = x.replace('\xe2\x80\xa8',' ')
    x = x.replace('\xe2\x80\xa9',' ')
    
    return x

# script takes one command-line arg: path to directory containing year data    
path = argv[1]

files = os.listdir(path)
files.sort()
# all year-files have integer filenames
files = filter(lambda x: x.isdigit(), files)

# creates a directory for storing the postprocessed data
if not os.path.exists("processed_"+path):
    os.makedirs("processed_"+path)

# process each year's file, and create a corresponding postprocessed file
for year in files:
    lemmatizer = WordNetLemmatizer()
    year_path = path + year
    cc = Counter({})
    with open("processed_" + year_path, "w") as g:
        with open(year_path, 'r') as f:
            word_frequencies = literal_eval(f.read().split('\n')[0])
            # need a temp variable store
            not_alphanumeric = dict((x,y) for x,y in word_frequencies.items() if not is_alphanumeric(x))
 
            # convert all non-alphanumeric words to alphanumeric
            for word in not_alphanumeric:
                del word_frequencies[word]
                replaced = filter(lambda x: x!='', replace(word).split(" "))
                for fixed_word in replaced:
                    if fixed_word in word_frequencies:
                        word_frequencies[fixed_word] += not_alphanumeric[word]
                    else:
                        word_frequencies[fixed_word] = not_alphanumeric[word]

            # remove hyphens (again) and remove garbled words leftover from that
            for old_word in word_frequencies.keys():
                if not is_alphanumeric(old_word):
                    new_words = filter(lambda x: x!='', old_word.replace("-", " ").split(" "))
                    for new_word in new_words:                    
                        if is_alphanumeric(new_word):
                            if new_word in word_frequencies:
                                word_frequencies[new_word] += word_frequencies[old_word]
                            else:
                                word_frequencies[new_word] = word_frequencies[old_word]
                    del word_frequencies[old_word]

            # loop over the word_frequencies, lemmatize all the verbs and plurals
            for word in word_frequencies.keys():
                lemmatized = lemmatizer.lemmatize(word,"v")
                if lemmatized != word:
                    if lemmatized in word_frequencies:
                        word_frequencies[lemmatized] += word_frequencies[word]
                    else:
                        word_frequencies[lemmatized] = word_frequencies[word]
                    del word_frequencies[word]

        g.write(str(word_frequencies))
