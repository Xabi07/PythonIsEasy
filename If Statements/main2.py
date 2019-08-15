"""
Author MyName
Date July 2019
Course Pyhton is Easy on Pirple
Assignment 3: If Statements
"""

def compare(val1,val2,val3):
    if int(val1) == int(val2) or int(val1) == int(val3) or int(val2) == int(val3):
        print(True)

    else:
        print(False)

compare(1,5,"5")

