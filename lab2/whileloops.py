i = 1
while i < 6:
    print(i)#1 2 3 4 5 each on new line
    i += 1

i = 1
while i < 6:
    print(i)
    if (i == 3):
        break#even if statement is true
    i += 1#will be 1 2 3


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Note that number 3 is missing in the result

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

