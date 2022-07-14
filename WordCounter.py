import re

def countInString(searchFor, searchIn):
    return len(re.findall(searchFor, searchIn))

def countInList(searchFor, searchIn):
    count = 0
    for entry in searchIn:
        if entry == searchFor:
            count+=1
    return count 

    