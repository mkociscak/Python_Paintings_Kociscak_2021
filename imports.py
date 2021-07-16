from bs4 import BeautifulSoup
import requests
import re
import urllib



URL = "https://www.megankociscak.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 

divs = soup.find_all('div', {'class': 'project-title'})
for div in divs:
    print(div.text)


def show_directions():
    print("Which title would you like to see?")
    print("Type NONE to exit")


show_directions()
while True:
    new_choice = input("> ")
    #open new webpage and repeat prompt
    show_directions()
    if new_choice == "NONE":
        break




#titles = [] #list to store titles

#store = soup.find('div class', attrs = {'class':'project-title'}) #find all storage

#for row in store.findAll('div', attrs = {'class':'project-title'}):
    #title = {}
    #titles.append(title)