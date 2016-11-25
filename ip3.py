import requests
from bs4 import BeautifulSoup

openfile=open("onlyip.txt")
readfile=openfile.read()
splitfile=readfile.split('\n')


for ip in splitfile:
	r=requests.get('http://www.ip-tracker.org/locator/ip-lookup.php?ip='+ip)
	print splitfile
	

	soup = BeautifulSoup(r.content,"lxml")


	for items in soup.find_all('tr'):
		print items.text.encode('utf-8')
	



