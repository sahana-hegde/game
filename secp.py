import re
import urllib2
url=raw_input("enter url:")
p=urllib2.urlopen(url)
page=p.read()
img=re.compile('<img.*src="(.*\.jpg)"',re.IGNORECASE)
n=re.findall(img,page)
f=open("link.txt","w")
for i in n:
	f.write(url+i+"\n")
