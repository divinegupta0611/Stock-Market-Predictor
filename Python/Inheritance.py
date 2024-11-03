class Person:
    def __init__(self,firstName,age):
        self.firstName=firstName
        self.age=age
    def printName(self):
        print("My name is: "+self.firstName+" and my age is: ",self.age)

x = Person("John",36)
x.printName()

class Student(Person):
    def __init__(self,firstName,age,year): # This will overwrite the Parent's class constructor function
        Person.__init__(self,firstName,age)
        # super().__init__(self,firstName,age)
        self.year=year

obj = Student("Mike",32,1992)
obj.printName()
print(obj.year)