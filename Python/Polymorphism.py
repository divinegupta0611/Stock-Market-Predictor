# Class Polymorphism
# Multiple classes can have same method
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def move(self):
        print("Drive!!")

class Boat:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def move(self):
        print("Fly!!")
    
car1 = Car("Audi","X005",1998)
boat1 = Boat("Ibiza","Touring20",2010)
plane1 = Plane("Boeing","747",2015)
for x in(car1,boat1,plane1):
    print(x.brand,end=" ")
    print(x.model,end=" ")
    print(x.year,end=" ")
    x.move()



# Inheritance Class Polymorphism
# Child class can have same method name as in parent class and it will be overridden
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!!")

class Car1(Vehicle):
    pass

class Boat1(Vehicle):
    def move(self):
        print("Sail!!")

class Plane1(Vehicle):
    def move(self):
        print("Fly!!")


car2 = Car1("Ford","Mustang")
boat2 = Boat1("Ibiza","X005")
plane2 = Plane1("Boeing","747")

for x in (car2,boat2,plane2):
    x.move()