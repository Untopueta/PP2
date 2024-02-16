class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()#John Doe


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass#to avoid
x = Student("Mike", "Olsen")
x.printname()#Mike Olsen

#or:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self,fname,lname)#or use super class,it will make the child class inherit all the methods and properties from its parent: super().__init__(fname, lname)
#

