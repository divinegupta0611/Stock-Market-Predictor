a1 = "Hello 1"
a2 = 'Hello 2'
# Both are valid
print(a1)
print(a2)

# Multiline string
str1 = """This is a
          multiline string"""
print(str1)

# Strings are arrays
arr = "Hello World"
print(arr[0])

# looping through a string
for i in arr:
    print(i,end=" ")

print("\n")

# string length
print(len(arr))

txt = "Just chill in life"
print("Just" in txt)
if "Just" in txt:
    print("Present")

print("CHILL" not in txt)
if "CHILL" not in txt:
    print("Not Present!!!")

# String slicing
print(txt[1:5]) # 1 included but 5 excluded
print(txt[:5]) # from start to 5 excluded
print(txt[2:]) # from 2 to end
print(txt[-6:])

# Modifying string
txt2 = " Hello, World "
print(txt2)
print(txt2.upper())
print(txt2.lower())
print(txt2.strip())
print(txt2.replace("H","J"))
print(txt2.split(", "))

# String concatenation
txt3 = "Divine"
txt4 = "Gupta"
txt5 = txt3+txt4;
txt6 = txt3+" "+txt4
print(txt5)
print(txt6)

# Format strings
age = 20;
txt7 = "My age is {}"
print(txt7.format(age))

quantity = 20;
price = 100;
cost = quantity*price
msg = "I have ordered {1} burgers of worth {0} at a total cost of {2}";
print(msg.format(price,quantity,cost))
