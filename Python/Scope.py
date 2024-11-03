txt1="Hello" # global variable
def printTxt():
    global a # a global variable declared inside a function
    a=200
    txt2 = "Hi" # local variable
    print(txt2)
printTxt()
print(txt1)
print(a)