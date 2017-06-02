import urllib
import lxml.html
import subprocess

fo=open("bing.txt","wb")
fo.close()
get=raw_input("Enter the text  \n")
mark = ["https://www.bing.com/images/search?q="+get+"&first=01&count=28&qft=+filterui:color2-FGcls_GRAY&FORM=HDRSC2","https://www.bing.com/images/search?q="+get+"&first=30&count=28&qft=+filterui:color2-FGcls_GRAY&FORM=HDRSC2","https://www.bing.com/images/search?q="+get+"&first=60&count=28&qft=+filterui:color2-FGcls_GRAY&FORM=HDRSC2"]
i=0
for i in range(len(mark)):
	connection = urllib.urlopen(mark[i])
	fo = open("bing.txt", "a")
	dom =  lxml.html.fromstring(connection.read())
	for link in dom.xpath('//a/@href'): 
		if link.startswith("http") and link.endswith(".jpg"):
			print link
			fo.write(link)
			fo.write("\n")
	fo.close()
	def uniquelines(lineslist):
	    unique = {}
	    result = []
	    for item in lineslist:
	        if item.strip() in unique: continue
	        unique[item.strip()] = 1
	        result.append(item)
	    return result	

subprocess.call(['wget','-c','-i','bing.txt','--directory-prefix=Images/'+str(get)])
