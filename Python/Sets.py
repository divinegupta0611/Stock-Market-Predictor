# A set is unordered, immutable, un-indexed and duplicates are not allowed
mySet = {"apple","banana","cherry","orange"}
print(mySet)

# length of a set
print(len(mySet))

# creating set using constructor
mySet2 = set((1,2,3,4))
print(mySet2)

# Access Set elements
for x in mySet:
    print(x,end=" ")
print("\n")
print("banana" in mySet)

# Add set items
# Once the set is created we cannot change items but we can add items
mySet.add("guava")
print(mySet)
tropical = {"papaya","mango"}
mySet.update(tropical)
print(mySet)
myList = ["kiwi","avocado"]
mySet.update(myList)
print(mySet)

# Remove Set items
# To remove a set item we use remove() or discard() methods
# in remove() method if the item is not present it will raise an error but discard() method will not raise an error
# pop() method will remove random element and will return the removed element
mySet.remove("cherry")
print(mySet)
mySet.discard("papaya")
print(mySet)
print(mySet.pop())

mySet2 = {1,2,3,4,5}
print(mySet2)
mySet2.clear()
print(mySet2)
del mySet2

# looping through a set
for x in mySet:
    print(x,end=" ")
print("\n")

# Join Sets
x1 = {"apple","microsoft","google"}
x2 = {"nvidia","dell","hp","microsoft"}
print(x1.union(x2))
print(x1.intersection(x2))
x1.intersection_update(x2)
print(x1)
print(x1.symmetric_difference(x2))
x1.symmetric_difference_update(x2)
print(x1)

# In sets True and 1 are considered as same