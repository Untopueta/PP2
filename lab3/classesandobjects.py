class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)#5

class Person:
  def __init__(self, name, age):#The __init__() function is called automatically every time the class is being used to create a new object
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)#John
print(p1.age)#36


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
p1.age = 40#modify
print(p1.age)
del p1.age
del p1
#we can use pass to avoid error
