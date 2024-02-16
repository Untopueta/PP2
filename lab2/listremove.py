alist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist = ["apple", "banana", "cherry"]
alist.remove("banana")#more than one specified value, method removes the first occurance
print(alist)

thislist.pop(1)#remove by index
print(thislist)
thislist.pop()#remove last item
print(thislist)

del thislist[0]#remove first item
print(thislist)
del alist#remove list

alist.clear()#empties list
print(alist)