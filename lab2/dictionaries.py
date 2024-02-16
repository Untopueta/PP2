thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])#Ford

#3.7 ordered 3.6 unordered

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020#Duplicate values will overwrite existing values
}
print(thisdict)
print(len(thisdict))#3

#From Python's perspective, dictionaries are defined as objects with the data type 'dict'

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)