from bs4 import BeautifulSoup
import json
import urllib
from urllib import urlopen
import re
import operator

def search(question):
        query = urllib.urlencode({'q': question})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.urlopen(url)
        search_results = search_response.read()
        results = json.loads(search_results)
        data = results['responseData']
        hits = data['results']
        pages = []
        for h in hits: pages.append(h['url'])
        #print pages
        text = read_urls(pages)
        ret = ""
        for t in text:
                ret += t
        return ret

def whosearch(question):
        text = search(question)
        names = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+", text)
        nameDict = makeDictWithCount(names)
        it = iter(nameDict)
        listOfResults = []
        for x in range(0,min(5,len(nameDict)-1)):
                listOfResults.append(it.next())
        return listOfResults
        

def whensearch(question):
        text = search(question)
        dates = re.findall("[A-Z][a-z]+\s[0-9]+", text)
        dates = [x for x in dates if check(x)]
        dateDict = makeDictWithCount(dates)
        it = iter(makeDictWithCount(dates))
        listOfResults = []
        for x in range(0,min(5,len(dateDict)-1)):
                listOfResults.append(it.next())
        return listOfResults
        #return max(makeDictWithCount(dates).iteritems(), key=operator.itemgetter(1))[0]


#Checks that a date has a valid month
def check(x):
        month = x.split(' ', 1)[0]
        if month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or month == "September" or month == "October" or month == "November" or month == "December":
                return True
        else:
                return False

def makeDictWithCount(x):
        countDict = {}
        for element in x:
                if element in countDict:
                        countDict[element] = countDict[element] + 1
                else:
                        countDict[element] = 1
        sorted_countDict = sorted(countDict.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_countDict

def read_urls(urls):
	html_text = []
	for url in urls:
		u = urlopen(url)
		html_text.append(u.read())
		u.close()
	text = []
	for page in html_text:
		text.append(BeautifulSoup(page).get_text().replace("\n"," "))
	return text
