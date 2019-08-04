"""
Author MyName
Date July 2019
Course Pyhton is Easy on Pirple
Assignment 2: Functions
"""

import datetime #date


title = "Enter Sandman"
band = "Metallica"
duration = datetime.time(0,5,30)
releasedate = datetime.date(1991, 6,15)
genre = "Metal"
album = "Metallica"
price = 10.5
durationInSeconds = 330
country = "USA"
members = 4
leadvocals = "James Hetfield"
drummer = "Lars Ulrich"
leadGuitar = "Guitar Man"


print("Title: ", title)
print("Band: " , band)
print("Country of Origin: ", country)
print("Song Duration: " , duration)
print("Release Date: " , releasedate)
print("Genre: " , genre)
print("Album: " , album)
print("Album Cost: $",price)
print("Song duration in seconds: ", durationInSeconds)
print("No of Members in Band: ", members)
print("Lead Vocals: ", leadvocals)
print("Lead Guitar: ", leadGuitar)
print("Drummer: " ,drummer)

def theAlbum():
    output = album
    return output

name = theAlbum()
print(name)

def theCost():
    output = price
    return output

price = theCost()
print(price)

def theGenre():
    output = genre
    return output

type = theGenre()
print(type)

def aBoolean():
    if price <= 10.6:
        return True
    elif price >= 10.6:
        return False
print(aBoolean())