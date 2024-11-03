import Export_Module
import Export_Module_2 as mx # using mx as alias
from Export_Module import person1 # importing only person1 from Export_Module
import platform
Export_Module.greeting("Divine")
print(Export_Module.person1["name"])
print(Export_Module.person1["age"])
mx.printHello()
x=platform.system()
print(x)
print(dir(platform)) # dir function is used to list all the functions of the module
print(person1["name"])