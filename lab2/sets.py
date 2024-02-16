thisset = {"apple", "banana", "cherry"}
print(thisset)#the set list is unordered, meaning: the items will appear in a random order

#Once a set is created, you cannot change its items, but you can remove items and add new items

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#dublicate will be ignored

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#True and 1 have the same value (same with false and 0)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)#will be True

