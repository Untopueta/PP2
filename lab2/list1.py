thislist = ["apple", "banana", "cherry"]

print(len(thislist)) #the number of elements
print(thislist[1]) #List indexed from 0 to n and you can summon them by their index
print(thislist[-1])#means the the first element from the end
print(thislist[0:2])#means summon all elements from 0 to 2 except 2 itself
print(thislist[:2])#all elements from the first to the n except n itself
print(thislist[1:])#all elements from n to the end exept n itself
print(thislist[-2:-1])#elements from -2 to -1 except -1 

if "apple" in thislist: #find element in the list
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"#replace second item 
print(thislist)
thislist[0:2] = ["blackcurrant", "watermelon"]#replace first and second item
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]#replace second item with 2 new elements
print(thislist)
thislist[0:2] = ["watermelon"]#replace first and second value with 1 element
print(thislist)
