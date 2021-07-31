from bs4 import BeautifulSoup
import requests
#import re
import urllib
import sys
import pandas as pd
import csv

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

#my_list=[]
#my_list = [(div.text)]
#a = prop_dict  
#type(a[0])
#df = pd.DataFrame(a)
#df.to_csv(r'CSV_files/property_info.csv')



print()
print()

#MASTER_EXIT = "EXIT"
#MASTER_LIST = "LIST"


my_list = ["Blood E Surplus : How's Your Vision? No. 1",
"Nothing is Ever Really Black and White",
"Brain Set No. 1",
"Brain Set No. 2",
"Reevaluate Reevaluating",
"Reevaluate Your Craft"]

def show_directions():
    print("Which title would you like to see next?")
    print("Type LIST to view available titles")
    print("Type EXIT to exit")

new_choice = input("Which title would you like to see? (copy/paste from list)  ")  #choose from scraped list and repeat prompt
#while new_choice != "True":
    #print(input("Which title would you like to see?  "))
#def new_choice_two = input("Which title would you like to see next?  ")


#while True:   
if new_choice == "Blood E Surplus : How's Your Vision? No. 1":
        print("https://megankociscak.com/#/blood-e-surplus/" )
        print(show_directions())

elif new_choice == "Nothing is Ever Really Black and White": 
        print("https://megankociscak.com/#/nothing-is-ever-really-black-and-white/")
        print("Which title would you like to see next?  ")
        print("Type LIST to view available titles")
        print("Type EXIT to exit")

elif new_choice == "Brain Set No. 1": 
        print("https://megankociscak.com/#/brain-set-no-1/")
        print("Which title would you like to see next?  ")
        print("Type LIST to view available titles")
        print("Type EXIT to exit")

elif new_choice == "Brain Set No. 2": 
        print("https://megankociscak.com/#/brain-set-no-2/")
        print("Which title would you like to see next?  ")
        print("Type LIST to view available titles")
        print("Type EXIT to exit")

elif new_choice == "Reevaluate Reevaluating": 
        print("https://megankociscak.com/#/reevaluate-reevaluating/")
        print("Which title would you like to see next?  ")
        print("Type LIST to view available titles")
        print("Type EXIT to exit")

elif new_choice == "Reevaluate Your Craft": 
        print("https://megankociscak.com/#/reevaluate-your-craft")
        print("Which title would you like to see next?  ")
        print("Type LIST to view available titles")
        print("Type EXIT to exit")

elif new_choice == "EXIT":
        sys.exit("Goodbye") 
        
elif new_choice == "LIST":
        print(my_list)      
else:
        input("Please choose from the list above  ")
    