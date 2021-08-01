from bs4 import BeautifulSoup
import requests
import re
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

MASTER_EXIT = "EXIT"


my_list = ["Blood E Surplus : How's Your Vision? No. 1",
"Nothing is Ever Really Black and White",
"Brain Set No. 1",
"Brain Set No. 2",
"Reevaluate Reevaluating",
"Reevaluate Your Craft",
"Darlin', Your Head's Not Right",
"Oh Shun View: I Had to Make him Leave",
"A Pansy-Ass Box Of Whoop-Ass",
"One Day, Baby, We'll Be Gold",
"A Parking Lot Made Up Of Makeup (Another Waste Of Space)"]

def show_directions():
    #print("Which title would you like to see next?")
    print("Type LIST to view available titles")
    print("Type EXIT to exit")
    #new_choice = input("Which title would you like to see? (copy/paste from list)  ")

new_choice = input("Which title would you like to see? (copy/paste from list)  ")  #choose from scraped list and repeat prompt
#while new_choice != "True":
#print(input("Which title would you like to see?  "))
#def new_choice_two = input("Which title would you like to see next?  ")
#while True:  

 
if new_choice == "Blood E Surplus : How's Your Vision? No. 1":
        print("https://megankociscak.com/#/blood-e-surplus/" )
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Nothing is Ever Really Black and White": 
        print("https://megankociscak.com/#/nothing-is-ever-really-black-and-white/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Brain Set No. 1": 
        print("https://megankociscak.com/#/brain-set-no-1/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Brain Set No. 2": 
        print("https://megankociscak.com/#/brain-set-no-2/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Reevaluate Reevaluating": 
        print("https://megankociscak.com/#/reevaluate-reevaluating/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Reevaluate Your Craft": 
        print("https://megankociscak.com/#/reevaluate-your-craft")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Darlin', Your Head's Not Right": 
        print("https://megankociscak.com/#/darlin-your-heads-not-right/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Oh Shun View: I Had to Make him Leave": 
        print("https://megankociscak.com/#/oh-shun-view/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "A Pansy-Ass Box Of Whoop-Ass": 
        print("https://megankociscak.com/#/a-pansy-ass-box-of-whoop-ass/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "One Day, Baby, We'll Be Gold": 
        print("https://megankociscak.com/#/one-day-baby-well-be-gold/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "A Parking Lot Made Up Of Makeup (Another Waste Of Space)": 
        print("https://megankociscak.com/#/a-parking-lot-made-up-of-makeup/")
        print(show_directions())
        new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "EXIT":
        sys.exit("Goodbye")
               
if new_choice == "LIST":
        print(my_list)       

else:
        print("Please choose from the list above  ")
    

new_choice = input("Which title would you like to see? (copy/paste from list)  ")