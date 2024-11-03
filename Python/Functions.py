def printName(name):
    print("My name is: ",name)

printName("Divine")
printName("ABC")

# Return values
def Sum(a,b):
    return a+b

print("Sum of 2 and 5 is: ",Sum(2,5))

# Arbitrary arguments *args
def func1(*name): # here a tuple is passed in the parameters
    print("Youngest child is: "+name[2])

func1("Divine","Emil","Tobias")

# Keyword arguments
def Multiply(a,b,c):
    return a*b*c

print(Multiply(b=10,c=20,a=50))

# Arbitrary keyword arguments
def func2(**kids): # Here dictionary is passed in the parameters
    print("His last name is: "+kids["lname"])

func2(fname="Tobias",lname="Ref")

# Default parameter values
def func3(country="Norway"):
    print("My country is: "+country)

func3("India")
func3()

# pass statement -> a function can't be empty so we use pass statement
def func4():
    pass

# passing a list as an argument
def printList(list1):
    for x in list1:
        print(x,end=" ")

list1 = ["apple","banana","cherry"]
printList(list1)

print("\n")

def Rec_Sum(n):
    if n==0:
        return 0
    return n+Rec_Sum(n-1)

print(Rec_Sum(5))