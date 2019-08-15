"""
Author MyName
Date July 2019
Course Pyhton is Easy on Pirple
Assignment 4: Lists
"""

myUniqueList = []

leftOverList = []
def populateList(value):
    if value in myUniqueList:
        popLeftOvers(value)
        print(False)

    elif value not in myUniqueList:
        myUniqueList.append(value)
        print(True)

def popLeftOvers(value):
    leftOverList.append(value)


print(myUniqueList)
populateList(1)
print(myUniqueList)
populateList(2)
print(myUniqueList)
print("Left Over List:",leftOverList)
populateList(2)
print(myUniqueList)
print("Left Over List:",leftOverList)
populateList(2)
print(myUniqueList)
print("Left Over List:",leftOverList)
populateList(3)
print(myUniqueList)