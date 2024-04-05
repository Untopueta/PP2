items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('items.txt','w')
for the in items:
	file.write(the+"\n")
file.close()
