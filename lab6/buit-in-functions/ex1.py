def multiplyList(myList):
	result = 1
	for x in myList:
		result = result * x
	return result

#ex
ar = [1, 2, 3]
br = [3, 2, 4]
print(multiplyList(ar))
print(multiplyList(br))