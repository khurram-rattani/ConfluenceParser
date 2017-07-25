#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import re
import datetime
import time

def getURLChildren(p_InitialURL, p_URL):
	p_UrlArray = []
	htmlData = urllib2.urlopen(p_URL)
	htmlParser = BeautifulSoup(htmlData, 'html.parser')
	for link in htmlParser.find_all(id="page-children"):
		htmlData = link
    if htmlData is None:
			print "[WARN] - getURLChildren : Found a null value, Ignoring"
		else:
			p_UrlArray.append(htmlData)
      
	htmlString = p_UrlArray
  
	htmlParser = BeautifulSoup(str(htmlString), 'html.parser')
	p_UrlArray2 = []
   
	for link in htmlParser.find_all('a'):
		p_UrlArray2.append(p_InitialURL + link.get('href'))
		print "[INFO] - getURLChildren : Appending " + p_InitialURL + link.get('href') + " to index"
		
	return p_UrlArray2
	
def appendArray(p_siteArray, p_URLArray):
	for item in p_URLArray:
		if item not in p_siteArray:
			p_siteArray.append(item)
			print "[INFO] - appendArray : Adding: " + item
		else:
			print "[WARN] - appendArray : Duplicate String Found! " + item
		
	return p_siteArray
	
def printArray(p_Array)
	print "[INFO] - printArray : #############################################"
	print "[INFO] - printArray :                                              "
	print "[INFO] - printArray :        Printing existing Array               "
	print "[INFO] - printArray :                                              "
	print "[INFO] - printArray : #############################################"
	print "[INFO] - printArray :                                              "
	print "[INFO] - printArray : Array Length: " + str(len(p_Array))
	for key in p_Array:
		for value in key:
			print key[value]
			
			
def checkIfURLExists(p_URL):
	try:
		response = urllib2.urlopen(p_URL)
		code = response.getCode()
		return code
	
	except urllib2.HTTPError as e:
		return e.code
	
	except:
		return -1
		
def getURLInformation(p_URL):
	p_UrlArray=[]
	htmlData = urllib2.urlopen(p_URL)
	htmlParser = BeautifulSoup(htmlData, 'html.parser')
	for link in htmlParser.find_all('a'):
		htmlData = link.get('href')
		
		if htmlData is None:
			print "[WARN] - getURLInformation : Found null value, Ignoring"
		elif htmlData.startswith("https://confluence"):
			p_UrlArray.append(link.get('href'))
			print "[INFO] - getURLInformation : Adding " + htmlData + " to array"
			
	return p_UrlArray
	
def getURLTitle(p_URL):
	htmlData = urllib2.urlopen(p_URL)
	htmlParser = BeautifulSoup(htmlData, 'html.parser')
	
	return htmlParser.title
	
#######MAIN#######
siteArray = [] # Stores all child pages given from URL Seed
InitialURL = "https://confluence.company.com # Used for full url paths given in siteArray
UrlChildArray = [] #Stores error 404 URLS based on the given URL Seed
UrlDictionary = {} #Stores Dictionary of URL Key and error 404 lists
UrlDictionaryArray = []
URL="https://confluence.company.com/confluence/display/SPACE_NAME/Site+Index"  #Seed Site

siteArray.append(URL)
urlCount = 0

for i in siteArray:
	UrlArray = getURLChildren(InitialURL, i)
	appendArray(siteArray, UrlArray)
	
print ""
print ""
print "[INFO] - Main : All pages in confluence have been stored in array"
print ""
print ""

### siteArray should contain all pages available in confluence space

for i in siteArray:
	urlCount += 1
	print "[INFO] - Main : ##################################################################"
	print "[INFO] - Main :                                                                   "
	print "[INFO] - Main : Working on URL " + str(urlCount) + " out of " + str(len(siteArray))
	print "[INFO] - Main :                                                                   "
	print "[INFO] - Main : ##################################################################"
	print "[INFO] - Main :                                                                   "
	print "[INFO] - Main :                                                                   "
	UrlArray = getURLInformation(i) #Get URLS from seed page
	
	for p in UrlArray:
		errorCode = checkIfURLExists(p)
		if errorCode == 0:
			print "[INFO] - checkIfURLExists : Error Code : 0 - " + p
		elif errorCode == 404:
			print "[WARN] - checkIfURLExists : Error Code: 404 : Adding URL to Error List Array - " + p
			UrlChildArray.append(p)
		else:
			print "[WARN] - checkIfURLExists : Error Code: " + errorCode + " : Adding URL to Error List Array - " + p
			UrlChildArray.append(p)
	
	print "[INFO] - Main : "
	print "[INFO] - Main : "
	if len(UrlChildArray) > 0:
		UrlDictionary[i] = UrlChildArray
		UrlDirectionaryArray.append(UrlDictionary)
		
	UrlChildArray = []
	
printArray(UrlDictionaryArray)
