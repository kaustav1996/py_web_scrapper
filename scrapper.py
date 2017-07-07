import urlparse
import urllib
from bs4 import BeautifulSoup
mainsite="http://www.thelearningpoint.net"
url="http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school"
urls =[url] #stack of urls to scrape
schools=list()
names=list()
while len(urls)>0:
	htmltext=urllib.urlopen(urls[0]).read()
	soup= BeautifulSoup(htmltext,"lxml")
	urls.pop(0)
	for tag in soup.find('div',{'class': 'sites-search-results-wrapper'}).findAll('a',href= True):
		tag['href'] = mainsite+tag['href']
		schools.append(tag['href'])

print("\n".join(schools))
while len(schools)>0:
	htmltext=urllib.urlopen(schools[0]).read()
	soup= BeautifulSoup(htmltext,"lxml")
	schools.pop(0)
	ele=soup.find('span',{'id': 'sites-page-title'})
	names.append(ele.text.partition(":")[0])
	ele=soup.find('td',{'class': 'sites-layout-tile sites-tile-name-content-1'}).find('b')
	print ele
	
