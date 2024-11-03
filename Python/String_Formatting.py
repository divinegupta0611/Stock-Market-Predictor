price = 49
txt1 = "The price is {} dollars"
print(txt1.format(price))
txt2 = "The price is {:.2f} dollars"
print(txt2.format(price))
quantity = 3
itemNo = 569
txt3 = "I want {} pieces of {} for {:.2f} dollars"
print(txt3.format(quantity,itemNo,price))
name="John"
age=20
txt4="His name is {1}. {1} is {0} years old"
print(txt4.format(age,name))