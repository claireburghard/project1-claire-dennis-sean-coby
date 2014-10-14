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
        if data is not None:
            hits = data['results']
            pages = []
            for h in hits: pages.append(h['url'])
            return pages
            #print pages
        return ["http://en.wikipedia.org/wiki/Habonim_Dror#Famous_graduates", "http://en.wikipedia.org/wiki/Habonim_Dror#Famous_graduates", "http://en.wikipedia.org/wiki/Habonim_Dror#Famous_graduates", "http://en.wikipedia.org/wiki/Habonim_Dror#Famous_graduates"]

def whosearch(question):
        #stream to read our first names file
        stream1 = open("firstnames.csv",'r')
        read1 = stream1.read().replace("\n"," ")
        stream1.close()

        #stream to read surnames file
        stream2 = open("surnames.csv",'r')
        read2 = stream2.read().replace("\n"," ")
        stream2.close()

        firstList = [] #will be list of first names that we find in our text files
        firstDic = {} #using dictionary for efficiency => constant runtime for finding?

        text = read_urls(search(question))
        texter = ""
        for t in text:
                texter += t
        names = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+", texter)

        firstNames = read1.split() #all first names via our database
        firstDic = dict.fromkeys(firstNames, firstNames)
    
        #smith = re.findall("[A-Z][a-z]+\sSmith",nytimes)
        for a in names:
            if a in firstDic:
                    firstList.append(a)

        surnameList = []
        surnameDic = {}
        surnames = read2.split()
        for a in surnames:
            surnameDic[a.title()] = a.title()

        for a in names:
                if a in surnameDic:
                        surnameList.append(a)

        fullname = []
   
        names = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",texter)
        for a in names:
                firstLast = a.split()
                if firstLast[0] in firstDic and firstLast[1] in surnameDic:
                        fullname.append(a)

        nameDict = makeDictWithCount(fullname)
        it = iter(nameDict)
        listOfResults = []
        for x in range(0,min(5,len(nameDict)-1)):
                listOfResults.append(it.next())
        return listOfResults
        

def whensearch(question):
        text = read_urls(search(question))
        texter = ""
        for t in text:
                texter += t
        dates = re.findall("[A-Z][a-z]+\s[0-9]+", texter)
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

def linkssearch(answer):
        links = []
        for a in answer:
                possibles = search(a)
                links.append(possibles[0])
        return links

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
