
firstfile = open('items.txt', 'r') 
secondfile = open('second.txt', 'w')

for line in firstfile:
    secondfile.write(line)

firstfile.close()
secondfile.close()
