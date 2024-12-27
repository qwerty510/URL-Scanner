import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = str(sys.argv[1])
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

listLayerOne = []
listLayerTwo = []
listLayerThree = []
listLayerFour = []
listLayerFive = []

for link in soup.find_all('a'):
	listLayerOne.append(link.get('href'))

for x in listLayerOne:
	try:
		if "http" in x:
			try:
				url = x
				print(url)
				page = urlopen(url)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerTwo.append(link.get('href'))
			except:
				pass
		else:
			try:
				newurl = url + x
				print(newurl)
				page = urlopen(newurl)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerTwo.append(link.get('href'))
			except:
				pass
	except:
		pass

for x in listLayerTwo:
	try:
		if "http" in x:
			try:
				url = x
				print(url)
				page = urlopen(url)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerThree.append(link.get('href'))
			except:
				pass
		else:
			try:
				newurl = url + x
				print(newurl)
				page = urlopen(newurl)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerThree.append(link.get('href'))
			except:
				pass
	except:
		pass

for x in listLayerThree:
	try:
		if "http" in x:
			try:
				url = x
				print(url)
				page = urlopen(url)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerFour.append(link.get('href'))
			except:
				pass
		else:
			try:
				newurl = url + x
				print(newurl)
				page = urlopen(newurl)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerFour.append(link.get('href'))
			except:
				pass
	except:
		pass

for x in listLayerFour:
	try:
		if "http" in x:
			try:
				url = x
				print(url)
				page = urlopen(url)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerFive.append(link.get('href'))
			except:
				pass
		else:
			try:
				newurl = url + x
				print(newurl)
				page = urlopen(newurl)
				html = page.read().decode("utf-8")
				soup = BeautifulSoup(html, "html.parser")
				listLayerFive.append(link.get('href'))
			except:
				pass
	except:
		pass

processedOne = list(set(listLayerOne))
processedTwo = list(set(listLayerTwo))
processedThree = list(set(listLayerThree))
processedFour = list(set(listLayerFour))
processedFive = list(set(listLayerFive))

unprocessedMasterList = processedOne + processedTwo + processedThree + processedFour + processedFive
processedMasterList = list(set(unprocessedMasterList))
print(processedMasterList) 