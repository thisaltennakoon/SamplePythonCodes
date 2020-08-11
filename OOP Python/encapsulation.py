#encapsulation

class Example():
    def __init__(self, name):
        self._name = name

    def __show(self):
        print("This is a private member function")


example = Example("Python")
#example.name cannot use this way as name is a private variable
example._name
#example.show(), example._show(), example.__show()cannot use this way as show is a private method
example._Example__show()