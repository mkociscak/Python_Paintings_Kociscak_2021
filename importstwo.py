from bs4 import BeautifulSoup
import requests
import re
import urllib
import sys

print()
print()
print("Below is a list of painting titles. Choose one and copy/paste it into the prompt underneath.")
print()
print()

URL = "https://www.megankociscak.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 

divs = soup.find_all('div', {'class': 'project-title'})
for div in divs:
    print(div.text) 
    
print()
print()

MASTER_EXIT = "EXIT"

new_choice = input("Which title would you like to see?  ")  #choose from scraped list and repeat prompt
#while new_choice != "True":
    #print(input("Which title would you like to see?  "))
    
if new_choice == "Blood E Surplus : How's Your Vision? No. 1":
    print("https://megankociscak.com/#/blood-e-surplus/")
elif new_choice == "Nothing is Ever Really Black and White": 
    print("https://megankociscak.com/#/blood-e-surplus/")
elif new_choice == MASTER_EXIT:
    sys.exit("Goodbye")      
else:
    input("Please choose from the list above  ")
    
