class Student():
    school = 'Royal College' # this is a class level variable or static variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1 #all the variables inside the constructor are instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod#decorators
    def get_school_name(cls):#class method
        return cls.school

    @staticmethod#decorators
    def info():#static method. Can be use when there is nothing to do with class like taking the nth fibbonacci number
        print('static method in Student class')

s1 = Student(1,2,3)
s2 = Student(4,5,6)

print(s1.avg())
print(Student.get_school_name())
Student.info()