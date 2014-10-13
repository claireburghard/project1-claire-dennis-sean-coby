from bs4 import BeautifulSoup
import json
import urllib
from urllib import urlopen


def whosearch(question):
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
        print text
        #NOW WE NEED THE OP TO FIND THE MOST COMMON NAME OR WHATEVER

def whensearch(question):
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
        print text
        #NOW WE NEED THE OP TO FIND THE MOST COMMON DATE OR WHATEVER

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

