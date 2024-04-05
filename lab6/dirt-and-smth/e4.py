file = open("text.txt", "r")
n = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
	if i:
		n += 1

print("Number of lines ", n)
