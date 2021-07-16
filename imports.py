from bs4 import BeautifulSoup
import requests
import re
import urllib
#import datetime
#import csv
#print(soup.prettify())
#print("What article would you like to see?")

URL = "https://www.megankociscak.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 

divs = soup.find_all('div', {'class': 'project-title'})
for div in divs:
    print(div.text)






#titles = [] #list to store titles

#store = soup.find('div class', attrs = {'class':'project-title'}) #find all storage

#for row in store.findAll('div', attrs = {'class':'project-title'}):
    #title = {}
    #titles.append(title)