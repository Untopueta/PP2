thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})#or thisdict["year"] = 2020
print(thisdict)

thisdict.pop("model")#or del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)

#Print all key names in the dictionary, one by one:
for x in thisdict:#or: for x in thisdict.keys(): print(x)
    print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:#or: for x in thisdict.values(): print(x)
    print(thisdict[x])

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():#Loop through both keys and values
    print(x, y)

#copies
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

#a big dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])#Tobias

