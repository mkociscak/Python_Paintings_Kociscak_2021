from bs4 import BeautifulSoup
import requests
#import re
import urllib
import sys
#import pandas as pd
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
"A Parking Lot Made Up Of Makeup (Another Waste Of Space)",
"Stop Signs Start Stuttering",
"Can't Keep His Mind On Nothing Else",
"Once Upon A Time Limit on Bullshit",
"Amber Waves of Grain Belt",
"A Chili Pepper Xmas and a Tissue Made of Scars (X Marks the Christ)",
"Almost Better Than Finding A New Roll Of Toilet Paper (That Shit Was Good)",
"Seven Candy Corns & One Greedy Spider",
"Swing Vote For Swing Sets",
"Your Band-Aid is Different Than Mine",
"Duck, Duck, Fuck You",
"My Head Is Splitting at Your Seeems.",
"Free Duh K N N Y C",
"I Won't Let You Bury This",
"This Is Worse Than Its Seams",
"Battle of the Bulge-Like Forms",
"To Find in this Place, Hide in this Space",
"Abstract Blood Spatter No. 1",
"Isabetta's, Lichtenstein's and Louis' Blood",
]


def show_directions():
    #print("Which title would you like to see next?")
    print("Type LIST to view available titles")
    print("Type EXIT to exit")
    #new_choice = input("Which title would you like to see? (copy/paste from list)  ")

new_choice = input("Which title would you like to see? (copy/paste from list)  ")  #choose from scraped list and repeat prompt
#while new_choice != "True":
#print(input("Which title would you like to see?  "))
#def new_choice_two = input("Which title would you like to see next?  ")
#while new_choice -= true: 

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

if new_choice == "Stop Signs Start Stuttering": 
    print("https://megankociscak.com/#/stop-signs-start-stuttering/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Can't Keep His Mind On Nothing Else": 
    print("https://megankociscak.com/#/cant-keep-his-mind-on-nothing-else/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Once Upon A Time Limit on Bullshit": 
    print("https://megankociscak.com/#/once-upon-a-time-limit-on-bullshit/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Amber Waves of Grain Belt": 
    print("https://megankociscak.com/#/amber-waves-of-grain-belt/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "A Chili Pepper Xmas and a Tissue Made of Scars (X Marks the Christ)": 
    print("https://megankociscak.com/#/a-chili-pepper-xmas-and-a-tissue-made-of-scars/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Almost Better Than Finding A New Roll Of Toilet Paper (That Shit Was Good)": 
    print("https://megankociscak.com/#/almost-better-than-finding-a-new-roll-of-toilet-paper/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Seven Candy Corns & One Greedy Spider": 
    print("https://megankociscak.com/#/seven-candy-corns-one-greedy-spider/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Swing Vote For Swing Sets": 
    print("https://megankociscak.com/#/swing-vote-for-swing-sets/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Your Band-Aid is Different Than Mine": 
    print("https://megankociscak.com/#/your-bandaid-is-different-than-mine/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Duck, Duck, Fuck You": 
    print("https://megankociscak.com/#/duck-duck-fuck-you/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "My Head Is Splitting at Your Seeems.": 
    print("https://megankociscak.com/#/my-head-is-splitting-at-your-seeems/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Free Duh K N N Y C": 
    print("https://megankociscak.com/#/free-duh-k-n-n-y-c/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "I Won't Let You Bury This": 
    print("https://megankociscak.com/#/i-wont-let-you-bury-this/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "This Is Worse Than Its Seams": 
    print("https://megankociscak.com/#/this-is-worse-than-its-seams/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Battle of the Bulge-Like Forms": 
    print("https://megankociscak.com/#/battle-of-the-bulge-like-forms/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "To Find in this Place, Hide in this Space": 
    print("https://megankociscak.com/#/to-find-in-this-place-hide-in-this-space/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Abstract Blood Spatter No. 1": 
    print("https://megankociscak.com/#/abstract-blood-spatter-no-1/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")

if new_choice == "Isabetta's, Lichtenstein's and Louis' Blood": 
    print("https://megankociscak.com/#/isabettas-lichtensteins-and-louis-blood/")
    print(show_directions())
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")


if new_choice == "LIST":
    print(my_list) 
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")
    
if new_choice == "EXIT":
    sys.exit("Goodbye")

else:
    print("Please choose from the list above  ")
    new_choice = input("Which title would you like to see? (copy/paste from list)  ")
