#once tuple created, you cannot change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)#dont forget comma
thistuple += y
print(thistuple)

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)#will be cherry,strawberry, raspberry

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)#will take all aside from first and last elements
print(red)

#loop with tuples is the same as with lists

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

