x = lambda a : a + 10
print(x(5))#15

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))#22
mytripler = myfunc(3)
print(mytripler(11))#33