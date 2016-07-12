# John Loeber | 07-JUL-2016 | Python 2.7.6 | Debian Linux | www.johnloeber.com

from bs4 import BeautifulSoup
from collections import Counter
import os
import urllib2

def parselink(url):
    """
    url: link to a season of a television show. finds the list of episodes therein,
    parses it, and returns a dictionary of word frequencies.
    """
    allwords = {}
    global stopwords
    # this is very inefficient/hacky, but works quickly enough.
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html,"html5lib")
    cells = soup.findAll("td", class_="description")
    for cell in cells:
        for match in cell.findAll('a'):
            match.unwrap()
        for match in cell.findAll('p'):
            match.unwrap()

        # split the cell up into individual lines
        lines = str(cell).lower().split('\n')
        for snip in lines:
            # remove formatting. catching a few edge cases. there's a bit of
            # heterogeneity in cell formatting (it's wikipedia, after all).
            if "united states</td>" in snip or "<small>" in snip:
                continue
            elif "<b>" in snip and ":" in snip:
                continue
            else:
                # this text processing is faster than bs4's unwrap, etc.
                if  "<td class=" in snip:
                    snip = snip[snip.index(">")+1:]
                while "<span" in snip:
                    newsnip = snip[:snip.index("<span")] + \
                              snip[snip.index("</span>")+7:]
                    # in certain badly-formatted cases, the above doesn't work.
                    if len(newsnip)>=len(snip):
                        # this happens extremely rarely.
                        break
                    else:
                        snip = newsnip
                while "<sup" in snip:
                    newsnip = snip[:snip.index("<sup")] + \
                              snip[snip.index("</sup>")+6:]
                    if len(newsnip)>=len(snip):
                        # this happens extremely rarely.
                        break
                    else:
                        snip = newsnip

                snip = snip.replace("</td>","")
                snip = snip.replace("<i>","")
                snip = snip.replace("</i>","")
                snip = snip.replace("<br/>","")
                snip = snip.replace("</br>","")
                snip = snip.replace("<hr/>","")
                snip = snip.replace("</b>","")
                snip = snip.replace("<b>","")
                snip = snip.replace("<ul>","")
                snip = snip.replace("</ul>","")
                snip = snip.replace("<li>","")
                snip = snip.replace("</li>","")
                if "<" in snip or ">" in snip:
                    continue

                # remove punctuation
                snip = snip.translate(None, ',.!?\'"()\n;$:[]{}')
                # remove hyphenation. this is a controversial decision.
                snip = snip.replace("-", " ")

                #split up the line into individual words
                snip = snip.split(" ")
                for y in snip:
                    if y=='' or y in stopwords:
                        continue
                    if y in allwords:
                        allwords[y] += 1
                    else:
                        allwords[y] = 1

    # remove nonwords or garbled words
    for word in allwords.keys():
        if '\\' in word or '<' in word or '>' in word or '/' in word:
            del allwords[word]
    return allwords

def getwords(url):
    """
    takes a url: wikipedia category for tv seasons of a given year.
    page contains links, each to a page of episode summaries for that season of a tv show.
    then calls parselink, which for each page collects all the episode summaries 
    on that page, and then constructs a word frequency count.
    returns the total word frequency count for that year, as a Counter() object.
    """
    allwords = Counter({})
    collectedlinks = []
    r = urllib2.urlopen(url).read()
    soup = BeautifulSoup(r,"html5lib")
    # get links to each show's season
    shows = soup.find("div", id="mw-pages")
    seasons = shows.findAll('a')
    for link in seasons:
        x = str(link.get('href'))
        # I am under the impression that the "season" marker is always lowercase
        if 'season' in x:
            # remember: each link is to a season of a tv show.
            collectedlinks.append("http://en.wikipedia.org"+x)
    # get word frequencies for each season
    for season in collectedlinks:
        season_counter = Counter(parselink(season))
        allwords += season_counter
    return allwords
    
def main():
    # open and retrieve the list of stopwords.
    global stopwords
    with open("stopwords-final","r") as h:
        stripped = [x.strip() for x in h.readlines()]
        stopwords = filter(lambda y: y!='', stripped)
    
    # start by getting the category linking to all television seasons by year.
    category = "http://en.wikipedia.org/wiki/Category:Television_seasons_by_year"
    r = urllib2.urlopen(category).read()
    soup = BeautifulSoup(r,"html5lib")
    divs = soup.findAll("div", class_="CategoryTreeSection")

    # create a list of urls, each linking to a category containing all television
    # show seasons in a given year
    urls = []
    for div in divs:
        urls.append("http://en.wikipedia.org" + div.find('a').get('href'))
    
    # as of 07-JUL-2016, there are two category types: by year and by country.
    # "by country" is a recent addition. we filter down to the ones by year only.
    # any year-category will have a year in the url string at indices 38:42.
    urls = filter(lambda x: x[38:42].isdigit(), urls)

    # delete the most recent year since it is most likely incomplete
    del urls[-1]    
    
    # create a folder where each year is represented by a word frequency count file
    directory_name = "year_wordcounts"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # process each year / url
    for index, url in enumerate(urls):
        year = str(index + 1950)        
        # print the year to indicate progress
        print year
        with open(directory_name + "/" + year, "w") as f:
            worddict = dict(getwords(url))
            # write two things to the file: a dictionary representing a word
            f.write(str(worddict)+'\n'+str(sum(worddict.values())))

if __name__=='__main__':
    main()
