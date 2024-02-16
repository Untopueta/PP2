#list containing only the fruits with the letter "a" in the name
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#

newlist = [x for x in fruits if "a" in x]#the same code as for the last question but shorter
print(newlist)

newlist = [x for x in fruits if x != "apple"]#items that are not "apple"
print(newlist)

newlist = [x for x in fruits]#all items from fuits list
print(newlist)

newlist = [x for x in range(10) if x < 5]#accept only numbers lower than 5, can be used without "if x<5"
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]#set the values in the new list to upper case(big numbers)
print(newlist)

newlist = ['hello' for x in fruits]#replace all values by hello
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]#Return "orange" instead of "banana"
print(newlist)