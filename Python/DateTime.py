import datetime
x = datetime.datetime.now()
print(x)
print(x.year) # will return the current year
print(x.strftime("%A")) # will return the weekday

a=datetime.datetime(2024,11,12)
print(a)
print(a.strftime("%B"))