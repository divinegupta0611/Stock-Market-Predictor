a = "Hello"
try: # To test a block of code
    print(a+5)
except NameError: # Handles the error
    print("An error ocurred")
except:
    print("Something else went wrong")
else: # is executed when there is no error
    print("In else block")
finally: # will always be executed irrespective of the error
    print("finally is always executed")

try:
    x = int(input("Enter a number"))
    if x<0:
        raise Exception("Sorry, no numbers below zero") # raise keyword help to create custom exceptions
except:
    print("An error ocurred")
    