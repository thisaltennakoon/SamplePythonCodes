#simple inheritance
print("simple inheritance")
class Parent1():
    def parent1func(self):
        print("parent1func")

class Child1(Parent1):
    def child1func(self):
        print("child1func")

child1=Child1()
child1.parent1func()
child1.child1func()

#multiple inheritance
print("\nmultiple inheritance")

class Parent2():
    def parent2func(self):
        print("parent2func")

class Parent3():
    def parent3func(self):
        print("parent3func")

class Child2(Parent2,Parent3):
    def child2func(self):
        print("child2func")

child2 = Child2()
child2.child2func()
child2.parent2func()
child2.parent3func()

#multi level inheritance

print("\nmulti level inheritance")

class Parent4():
    def parent4func(self):
        print("parent4func")

class Parent5(Parent4):
    def parent5func(self):
        print("parent5func")

class Child3(Parent5):
    def child3func(self):
        print("child3func")

child3 = Child3()
child3.child3func()
child3.parent4func()
child3.parent5func()

#polymorphism
