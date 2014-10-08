from bs4 import BeautifulSoup
from urllib import urlopen

def read_urls(urls):
	html_text = []
	for url in urls:
		u = urlopen(url)
		html_text.append(u.read())
		u.close()
	text = []
	for page in html_text:
		text.append(BeautifulSoup(page).get_text())
	return text

if __name__ == "__main__":
	urls = ["http://4c.alfaromeo.com/", "http://www.caranddriver.com/alfa-romeo/4c", "http://en.wikipedia.org/wiki/Alfa_Romeo_4C", "http://www.topgear.com/uk/tags/Alfa-Romeo-4C"]
	print read_urls(urls)

