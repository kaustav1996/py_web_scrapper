import urlparse
import urllib
from bs4 import BeautifulSoup
mainsite="http://www.thelearningpoint.net"
url="http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school"
urls =[url,"http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=10","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=20","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=30","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=40","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=50","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=60","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=70","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=80","http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=90"] #stack of urls to scrape
schools=list()
names=list()
emails=list()
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
	
	ele=soup.find('span',{'id': 'sites-page-title'})
	nm=ele.text.partition(":")[0]
	if(nm==''):#if Name is not found no need to scrape for email
		print("Parsing Failed!! No Name Found at "+schools[0])
	elif nm.find("Schools")!=-1 or nm.find("Top")!=-1 :
		print("Parsing Failed!! No Name Found at " +schools[0])
	else:#if Name is found trying to scrape email
		names.append(nm)
		for ele in soup.find('td',{'class': 'sites-layout-tile sites-tile-name-content-1'}).findAll('b'):
			flag=0
			if ele.text.find("Email:")!=-1:
				em=ele.text[ele.text.find("Email:")+6:ele.text.find(",")]
				if em=='':
					em="No Email Found"#if "Email:" is present but no email is given
				emails.append(em)
				flag=1
				break
		if(flag==0):
			print("Parsing Failed!! No Email Found for "+nm) #if Email: is not present
			em="No Email Found"
			emails.append(em)
	schools.pop(0)
i=-1
while(i< len(names)):
	if(i==-1):
		print("""School No."""+","+"""School Name"""+"""Email""")
	else:
		print(('"{}"'+","+'"{}"'+","+'"{}"').format(str(i+1),names[i],emails[i]))
	i=i+1
