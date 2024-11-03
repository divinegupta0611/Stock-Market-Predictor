# tuple is ordered and immutable
tuple1 = ("apple","banana","cherry","mango","guava")
print(tuple1)
print(type(tuple1))

tuple2 = ("apple",)
print(type(tuple2))

# Access tuple
print(tuple1[1])
print(tuple1[-1])
print(tuple1[1:4])
print(tuple1[:4])
print(tuple1[4:])
print(tuple1[-4:])

if "apple" in tuple1:
    print("Present...")

# although tuples are immutable but we can convert it into list, make changes and then convert it into tuple
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
x = tuple(y)
print(x)

# add tuple to tuple
x1 = (1,2,3,4)
x2 = (5,6,7,8)
print(x1+x2)
print(x1*2)

# Looping through a tuple
for i in tuple1:
    print(i,end=" ")
print("\n")
for i in range(len(tuple1)):
    print(tuple1[i],end=" ")
print("\n")

# unpack tuples
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

(g,*y) = fruits
print(g)
print(y)