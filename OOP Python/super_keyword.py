class Parent():

    def __init__(self):
        print("Parent class")

    def parentfunc(self):
        print("parentfunc")

    def commonfunc(self):
        print("commonfunc in parent class")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child class")

    def childfunc(self):
        print("childfunc")

    def commonfunc(self):
        print("commonfunc in child class")

child = Child()
child.commonfunc()

#Method resolution order

class Parent1():

    def __init__(self):
        print("Parent1 class")

    def parentfunc(self):
        print("parentfunc")

    def commonfunc(self):
        print("commonfunc in parent class")

class Parent2():

    def __init__(self):
        print("Parent2 class")

    def parentfunc(self):
        print("parentfunc")

    def commonfunc(self):
        print("commonfunc in parent class")

class Child1(Parent1,Parent2):

    def __init__(self):
        super().__init__()# here it will call constructor of Parent1 because it is the leftmost thing
        print("Child class")

    def childfunc(self):
        print("childfunc")

    def commonfunc(self):
        print("commonfunc in child class")

child1 = Child1()