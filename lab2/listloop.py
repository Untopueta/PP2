thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)#print all elements one by one

for i in range(len(thislist)):
    print(thislist[i])#all items by their index

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1#all items by their index 

[print(x) for x in thislist]#short hand for loop that will print all items