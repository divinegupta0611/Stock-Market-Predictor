a=33
b=200

if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")

# Short hand if
if a>b: print("a is greater than b")

# Short hand if...else
print("B") if b>a else print("A")

a1=330
b1=330
print("A") if a1>b1 else print("=") if a1==b1 else print("B")

x=10
y=20
if x<20 and y>10:
    print("True!!")
if x<20 or y>10:
    print("True!!")
if not(x>20 and y<10):
    print("True!!")

if 20<40:
    pass
# pass is used when we don't have any statements