import json
x = '{"name":"John","age":20,"country":"India"}' # a json data
y = json.loads(x) # converting json data to python dictionary
print(y["name"])

dict1 = {
    "name":"John",
    "age":20,
    "city":"New York"
} # a python dictionary
a = json.dumps(dict1) # converts python dictionary to json format
print(a)
