from bs4 import BeautifulSoup
import requests
import urllib
import sys
import csv 
#above for BS #below for PDF
import fitz


print()

pdf = 'Art museum deaccessioning _ conflict between museum professionals, donor intent, the public, and living artists_.pdf'
doc = fitz.open(pdf)
print(doc.metadata)

page7 = doc.load_page(6)  #abstract is page 7 of pdf
page7text = page7.get_text("text")
print(page7text)

print("This graduate thesis in its entirety can be found at https://ir.library.louisville.edu/cgi/viewcontent.cgi?article=1768&context=etd.")
print()
print("Thanks for reading! To read more click the link above.")
print()
print('Type "LIST" to return to the list of my painting titles or type "EXIT" to exit the program.')

new_choice = input()

if new_choice == "EXIT":
    print()
    sys.exit("Goodbye")

if new_choice == "LIST":
    exec(open("start.py").read())
