thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")#add "watermelon" as third item 
print(thislist)

thislist.append("orange")#add item at the end of the list
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)#combine thislist with tropical
print(thislist)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)#not only list + list
print(thislist)