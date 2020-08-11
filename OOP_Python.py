class Person:#super class
  def __init__(self, fname, lname):#contructor
    self.firstname = fname
    self.lastname = lname

  def printname(self):#needless to declare 'self' as the parameter,any parameter can be given
    print(self.firstname, self.lastname)

class Student(Person):#inheritance 
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)#calling super class contructor
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
  
  def printname(self):#method overrinding
    print(self.lastname,self.firstname)
  
x = Student("Mike", "Olsen", 2019)
x.welcome()
x.printname()
