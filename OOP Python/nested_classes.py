class Student():

    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()

    class Laptop():
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('thisal',1)
s1.show()