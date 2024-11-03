# A class is a blueprint for an object
# An object is an instance of a class

class MyClass1:
    x=5

p1 = MyClass1()
print(p1.x)

# __init__() function in python is a constructor. It is always invoked whenever an instance of a class is created
# __ str__() function controls what should be returned when an object is represented as a string
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "Object"
    def func1(self):
        print("Hello my name is: "+self.name)
    def func2(abc):
        print("My age is: ",abc.age)
obj1 = Person("John",36)
print(obj1.name)
print(obj1.age)
print(obj1)
obj1.func1()
obj1.func2()