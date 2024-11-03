# Lists can hold any data type

# creating lists
list1 = ["apple","banana","cherry","grapes","pineapple","kiwi","melon"];
list2 = list(("apple","banana","cherry"))

print(list1)
print(list2)

# length of a list
print(len(list1))

# Access list items
print(list1[1])
print(list1[-1])
print(list1[2:5])
print(list1[:5])
print(list1[5:])
print(list1[-4:-1])
print("apple" in list1)

# Change list items
list1[1] = "black current"
print(list1)

list1[2:4] = ["papaya","custard"]
print(list1)

list1.insert(4,"watermelon")
print(list1)

# add list items
list1.append("orange")
print(list1)

list1.insert(5,"guava")
print(list1)

num1 = [1,2,3]
num2 = [4,5,6]
num3 = (7,8,9)
num1.extend(num2)
print(num1)
num1.extend(num3) # any iterable can ebe added
print(num1)

# Remove list items
num1.remove(2)
print(num1)
num1.pop(2)
print(num1)
num1.pop() # will remove last element
print(num1)
del num2[0]
print(num2)
num2.clear()
print(num2)

# looping through a list
for i in num1:
    print(i,end=" ")

print("\n******")

for i in range(len(num1)):
    print(num1[i],end=" ") 

print("/n")

# printing using list comprehension
[print(x) for x in list2]

# List Comprehension
fruits = ["apple","banana","kiwi","guava","cherry"]
newFruits = [x for x in fruits if 'a' in x]
print(newFruits)

# Sort list
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.sort(key=str.lower)

def myFunc(n):
    return abs(n-50)

thisList = [100,50,23,25]
thisList.sort(key=myFunc)
print(thisList)

# Copy list
list2 = fruits.copy()
print(list2)

list3 = list(list2)
print(list3)

# We can't do list1=list2 it will pass a reference and any changes made in list2 will also reflect in list1