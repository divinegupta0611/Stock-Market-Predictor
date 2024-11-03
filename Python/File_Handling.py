import os
f=open("demoFile.txt","r") # Will open the file in read mode
#print(f.read()) # will read the content of the file
#print(f.read(5)) # will read only the first five characters of the file
#print(f.readline()) # will read the file line by line
for x in f: # will read all the lines(content of the file)
    print(x)
f.close() # will close the file

f1 = open("demoFile2.txt","a")
f1.write("One more line") # will append the data to the file

"""
   r -> read
   w -> write
   x -> create
   a -> append
   t -> text
   b -> binary
"""

#f2 = open("demoFile3.txt","a")
if os.path.exists("demoFile3.txt"):
    os.remove("demoFile3.txt") # removes the file
else:
    print("File does't exists")