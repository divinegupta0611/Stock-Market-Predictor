# Dictionaries are ordered, mutable and do not allow duplicates
# Duplicate values overwrite existing values
thisDict = {
    "brand":"Ford",
    "electric":"False",
    "year":1964,
    "colors":["red","black","white"]
}

print(thisDict)

# length of a dictionary
print(len(thisDict))
print(type(thisDict))

# creating dictionary using dict constructor
thisDict2 = dict(name="Divine",age=20,country="India")
print(thisDict2)

# Access Dictionary items
print(thisDict["year"])
print(thisDict.get("brand"))

print(thisDict.keys()) # will return all the keys
print(thisDict.values()) # will return all the values of the keys

print(thisDict.items()) # a tuple of key values will be returned in a list

if "brand" in thisDict:
    print("Present!!")
else:
    print("Not Present!!")

# Change Dictionary items
thisDict["year"] = 2018
print(thisDict["year"])

# Add Dictionary items
thisDict.update({"country":"India"})
print(thisDict)

# Remove Dictionary item
thisDict.pop("country")
print(thisDict)
thisDict.popitem() # will remove the last inserted item
print(thisDict)
del thisDict["electric"]
print(thisDict)

# Loop Dictionary
for x in thisDict:
    print(x,end=" ")
print("\n")
for x in thisDict:
    print(thisDict[x],end=" ") 
print("\n")
for x in thisDict.values():
    print(x,end=" ")
print("\n")
for x in thisDict.keys():
    print(x,end=" ")
print("\n")
for x,y in thisDict.items():
    print(x,y,end=" ")
print("\n")

# Copy Dictionary
# dict2 = dict1 -> any changes made in dict2 will reflect in dict1
thisDict2 = thisDict.copy()
print(thisDict2)
thisDict3 = dict(thisDict)
print(thisDict3)

# Nested Dictionaries
child1 = {
    "name":"Emil",
    "year":2004
}
child2 = {
    "name":"Tobias",
    "year":2005
}
myFamily = {
    "child1":child1,
    "child2":child2
}
print(myFamily["child1"]["name"])