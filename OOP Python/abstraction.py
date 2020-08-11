#abstraction
from abc import ABC


class Animal(ABC):
    def legCount(self):
        pass
    def intro(self):
        print("This is an animal")

class Dog(Animal):
    numberOfLegs = 4 #class level variable
    def __init__(self, name):
        self._name=name # instance level variable
    def getName(self):
        print(self._name)
    def setName(self,name):
        self._name=name
    def legCount(self):
        print(self.numberOfLegs)

class Ant(Animal):
    numberOfLegs = 6 #class level variable
    def __init__(self, name):
        self._name=name # instance level variable
    def getName(self):
        print(self._name)
    def setName(self,name):
        self._name=name
    def legCount(self):
        print(self.numberOfLegs)

dog = Dog("Dog1")
dog.getName()
dog.legCount()

dog = Dog("Dog2")
dog.getName()
dog.legCount()

ant = Ant("Ant name")
ant.getName()
ant.legCount()