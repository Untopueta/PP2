thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access to tuple is the same as access to list