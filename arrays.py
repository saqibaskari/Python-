stationarybox = ['pen', 'pencil', 'ballpoint', 'eraser']
#print(stationarybox[3])
strangelist = [4,10.2,"Cherry", ["an other list",1]]
#print(strangelist[3])


mylist = []
mylist.append(1)
mylist.append(2)
mylist.insert(1,12)
mylist.insert(0,14)
mylist.remove(1)
#print(mylist.index(2))
#print(mylist)


profession = {}

profession["Jenny"] = "Business Owner"

#print(profession["Jenny"])

list = ['a','b','c']
list2 = ['c', 'b', 'a']

#print(list)
#print(list2)

mylist = [4,2,3,4,5]
#print(4 in mylist)
#print(5 in mylist)

a = 'This is a Test'
#print(a.capitalize())
#print(a.upper())
#print(a.lower())

import numpy as np

myNotes = np.array([0, 5, 10, 15, 20])

from math import e
#print(e)

myDict = {'George': 4, 'Jean': 2, 'Paul': 10, 'Andrew': 18, 'Jacob': 8}

myDict['Steve'] = 12

toRemove = ['George', 'Paul', 'Jacob']
for elt in toRemove:
    myDict.pop(elt)

print(myDict.values())