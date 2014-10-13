from bs4 import BeautifulSoup
import json
import urllib
from urllib import urlopen
import re

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
        #FIND MOST COMMON NAME
        

def whensearch(question):
        text = search(question)
        dates = re.findall("[A-Z][a-z]+\s[0-9]+", text)
        dates = [x for x in dates if check(x)]


#Checks that a date has a valid month
def check(x):
        month = x.split(' ', 1)[0]
        if month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or month == "September" or month == "October" or month == "November" or month == "December":
                return true
        else:
                return false


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

if __name__ == "__main__":
	whosearch("Who plays Spiderman?")

