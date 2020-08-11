#polymorphism means one thing can take many forms
#there are four methods to achive polymorphism in python (1)Duck typing (2)Operator Overloading
#(3)Method Overloading (4)Method Overriding
#method over-ridding

class Parent():
    def __init__(self):
        print("Parent class")
    def parentfunc(self):
        print("parentfunc")

    def commonfunc(self):
        print("commonfunc in parent class")

class Child(Parent):
    #if there is no constructor in the child, it will call the Parent class constructor by default
    def childfunc(self):
        print("childfunc")

    def commonfunc(self):
        print("commonfunc in child class")

child = Child()
child.commonfunc()

#(1)Duck typing
#if there is a bird and it behaves like a duck,walks like a duck,quacks like a duck,swims like a duck, then it should be a duck
#in this case if there a method called execute, we don't bother about the which class object it is
#in jave this is achived using an interface. first we create an interface called IDE and create class PyCharm,MyEditor implementing that interface

class PyCharm():
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor():
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop():
    def code(self,ide):
        ide.execute()

ide1 = PyCharm()
ide2 = MyEditor()

lap = Laptop()
lap.code(ide1)
print('\n')
lap.code(ide2)

#Operator overloading
#if we use +,-,*,/,<,> behind the sences interpreter calls inbuilt methods in the interger class or string class
# + __add__(self,other)
# - __sub__(self,other)
# * __mul__(self,other)
# / __div__(self,other)
# < __lt__(self,other)
# > __gt__(self,other)
#>= __ge__(self,other)

class Student():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return Student(self.m1+other.m1 , self.m2+other.m2)

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return str(self.m1)+' '+str(self.m2)

s1 = Student(58,69)
s2 = Student(70,65)

s3 = s1 + s2 # now two student objects can be added

if s1 > s2: # now two student objects can be compared
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a) # this will call __str__(self) function

print(s1)# now student objects can be printed
print(s2)

#Method overloading - there is no such thing in python
#class Student123():
#    def average(self,a,b):
#        return a+b
#    def average(self,a,b,c):
#        return a+b+c

# but we can achive this in indirect way
print('\nMethod overloading')
class Student_for_Method_overloading():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

student_for_method_overloading = Student_for_Method_overloading(12,21)
print(student_for_method_overloading.sum(1))
print(student_for_method_overloading.sum(1,2))
print(student_for_method_overloading.sum(1,2,3))
