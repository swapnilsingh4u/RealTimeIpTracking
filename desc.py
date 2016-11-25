
from clint.textui import colored

opencountry=open("country.txt")
readcountry=opencountry.read()
splitcountry=readcountry.split("\n")

openip=open("onlyip.txt")
readip=openip.read()
splitip=readip.split("\n")

opencity=open("city.txt")
readcity=opencity.read()
splitcity=readcity.split('\n')

#openregion=open("region.txt")
#readregion=openregion.read()
#splitregion=readregion.split('\n')

openprocess=open("process.txt")
readprocess=openprocess.read()
splitprocess=readprocess.split('\n')




i=0
while i<len(splitip):
	try:
		print "CONNECTED PROCESS:"+colored.red(splitprocess[i])+">>>>"+"CONNECTED IP:>>> "+colored.green(splitip[i])+":::REGION:"+colored.yellow(splitcity[i])+":::COUNTRY:"+colored.green(splitcountry[i])
	except IndexError:
		pass
	i+=1

