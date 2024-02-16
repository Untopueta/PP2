thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()#Sort the list alphabetically or numerically; all capital letters being sorted before lower case letters
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)#Sort the list descending
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)#Sort the list based on how close the number is to 50
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#alphabetically despite upper or lower letter is
print(thislist)

