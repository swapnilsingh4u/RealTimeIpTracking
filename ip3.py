import requests
from bs4 import BeautifulSoup

openfile=open("onlyip.txt")
readfile=openfile.read()
splitfile=readfile.split('\n')
#url = "http://www.ip-tracker.org/locator/ip-lookup.php"

for ip in splitfile:
	r=requests.get('http://www.ip-tracker.org/locator/ip-lookup.php?ip='+ip)
	print splitfile
	#r = requests.get(url)

	soup = BeautifulSoup(r.content,"lxml")
#fileopen=open("IpExtractor.txt","w")

	for items in soup.find_all('tr'):
		print items.text.encode('utf-8')
	#filewrite=fileopen.write(items.text)
#fileopen.close()


