# A lambda function is a small anonymous function
# It can have any number of arguments but will only have one expression
x = lambda a:a+10
print(x(5))

# Power of lambda can be shown when its use inside the function
def Multiply(n):
    return lambda a: a*n

myDoubler = Multiply(2)
print(myDoubler(11))