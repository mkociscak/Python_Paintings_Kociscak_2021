from bs4 import BeautifulSoup
import requests
import urllib
import sys
import csv 
import cv2
import numpy 
from PyPDF2 import PdfFileReader


print()
print()
print("Below is a list of painting titles for abstract paintings I have made.")
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
print("Choose one title and copy/paste it here. This will give you a link to view the painting.")

def show_directions():
    print()
    print("Nice choice!")
    print("If you would like to see another painting paste the title in now (* must be lower on the list).")
    print()
    print('You can also type "TEXT" to view a writing sample (my graduate thesis) or type "EXIT" to exit the program.')

new_choice = input("Which title would you like to see? (copy/paste from list)  ")  #choose from scraped list and repeat prompt

if new_choice == "Blood E Surplus : How's Your Vision? No. 1":
    print()
    print("https://megankociscak.com/#/blood-e-surplus/" )
    print(show_directions())
    new_choice = input()

if new_choice == "Nothing is Ever Really Black and White": 
    print()
    print("https://megankociscak.com/#/nothing-is-ever-really-black-and-white/")
    print(show_directions())
    new_choice = input()

if new_choice == "Brain Set No. 1": 
    print()
    print("https://megankociscak.com/#/brain-set-no-1/")
    print(show_directions())
    new_choice = input()

if new_choice == "Brain Set No. 2": 
    print()
    print("https://megankociscak.com/#/brain-set-no-2/")
    print(show_directions())
    new_choice = input()

if new_choice == "Reevaluate Reevaluating": 
    print()
    print("https://megankociscak.com/#/reevaluate-reevaluating/")
    print(show_directions())
    new_choice = input()

if new_choice == "Reevaluate Your Craft": 
    print()
    print("https://megankociscak.com/#/reevaluate-your-craft")
    print(show_directions())
    new_choice = input()

if new_choice == "Darlin', Your Head's Not Right": 
    print()
    print("https://megankociscak.com/#/darlin-your-heads-not-right/")
    print(show_directions())
    new_choice = input()

if new_choice == "Oh Shun View: I Had to Make him Leave": 
    print()
    print("https://megankociscak.com/#/oh-shun-view/")
    print(show_directions())
    new_choice = input()

if new_choice == "A Pansy-Ass Box Of Whoop-Ass": 
    print()
    print("https://megankociscak.com/#/a-pansy-ass-box-of-whoop-ass/")
    print(show_directions())
    new_choice = input()

if new_choice == "One Day, Baby, We'll Be Gold": 
    print()
    print("https://megankociscak.com/#/one-day-baby-well-be-gold/")
    print(show_directions())
    new_choice = input()

if new_choice == "A Parking Lot Made Up Of Makeup (Another Waste Of Space)": 
    print()
    print("https://megankociscak.com/#/a-parking-lot-made-up-of-makeup/")
    print(show_directions())
    new_choice = input()

if new_choice == "Stop Signs Start Stuttering": 
    print()
    print("https://megankociscak.com/#/stop-signs-start-stuttering/")
    print(show_directions())
    new_choice = input()

if new_choice == "Can't Keep His Mind On Nothing Else": 
    print()
    print("https://megankociscak.com/#/cant-keep-his-mind-on-nothing-else/")
    print(show_directions())
    new_choice = input()

if new_choice == "Once Upon A Time Limit on Bullshit": 
    print()
    print("https://megankociscak.com/#/once-upon-a-time-limit-on-bullshit/")
    print(show_directions())
    new_choice = input()

if new_choice == "Amber Waves of Grain Belt": 
    print()
    print("https://megankociscak.com/#/amber-waves-of-grain-belt/")
    print(show_directions())
    new_choice = input()

if new_choice == "A Chili Pepper Xmas and a Tissue Made of Scars (X Marks the Christ)": 
    print()
    print("https://megankociscak.com/#/a-chili-pepper-xmas-and-a-tissue-made-of-scars/")
    print(show_directions())
    new_choice = input()

if new_choice == "Almost Better Than Finding A New Roll Of Toilet Paper (That Shit Was Good)": 
    print()
    print("https://megankociscak.com/#/almost-better-than-finding-a-new-roll-of-toilet-paper/")
    print(show_directions())
    new_choice = input()

if new_choice == "Seven Candy Corns & One Greedy Spider": 
    print()
    print("https://megankociscak.com/#/seven-candy-corns-one-greedy-spider/")
    print(show_directions())
    new_choice = input()

if new_choice == "Swing Vote For Swing Sets": 
    print()
    print("https://megankociscak.com/#/swing-vote-for-swing-sets/")
    print(show_directions())
    new_choice = input()

if new_choice == "Your Band-Aid is Different Than Mine": 
    print()
    print("https://megankociscak.com/#/your-bandaid-is-different-than-mine/")
    print(show_directions())
    new_choice = input()

if new_choice == "Duck, Duck, Fuck You": 
    print()
    print("https://megankociscak.com/#/duck-duck-fuck-you/")
    print(show_directions())
    new_choice = input()

if new_choice == "My Head Is Splitting at Your Seeems": 
    print()
    print("https://megankociscak.com/#/my-head-is-splitting-at-your-seeems/")
    print(show_directions())
    new_choice = input()

if new_choice == "Free Duh K N N Y C": 
    print()
    print("https://megankociscak.com/#/free-duh-k-n-n-y-c/")
    print(show_directions())
    new_choice = input()

if new_choice == "I Won't Let You Bury This": 
    print()
    print("https://megankociscak.com/#/i-wont-let-you-bury-this/")
    print(show_directions())
    new_choice = input()

if new_choice == "This Is Worse Than Its Seams": 
    print()
    print("https://megankociscak.com/#/this-is-worse-than-its-seams/")
    print(show_directions())
    new_choice = input()

if new_choice == "Battle of the Bulge-Like Forms": 
    print()
    print("https://megankociscak.com/#/battle-of-the-bulge-like-forms/")
    print(show_directions())
    new_choice = input()

if new_choice == "To Find in this Place, Hide in this Space": 
    print()
    print("https://megankociscak.com/#/to-find-in-this-place-hide-in-this-space/")
    print(show_directions())
    new_choice = input()

if new_choice == "Abstract Blood Spatter No. 1": 
    print()
    print("https://megankociscak.com/#/abstract-blood-spatter-no-1/")
    print(show_directions())
    new_choice = input()

if new_choice == "Isabetta's, Lichtenstein's and Louis' Blood": 
    print()
    print("https://megankociscak.com/#/isabettas-lichtensteins-and-louis-blood/")
    print(show_directions())
    new_choice = input()
    
if new_choice == "EXIT":
    print()
    sys.exit("Goodbye")

if new_choice == "TEXT":
    exec(open("thesisAbstract.py").read())

else:
    print()
    print('That was not a valid response. Please try again. You can also type "TEXT" to view a writing sample (my graduate thesis) or type "EXIT" to exit the program.')
    exec(open("start.py").read())
    
    