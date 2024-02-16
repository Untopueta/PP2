a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:#if the previous conditions were not true, then try this condition
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b: print("a is greater than b")#one line statement

a = 2
b = 330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")#with 3 conditions

c = 1
if a > b and c > a:#we can use "or" as well
    print("Both conditions are True")

if not a > b:
    print("a is NOT greater than b")

#use pass to avoid error in empty if