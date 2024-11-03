i=1
while i<6:
    print(i,end=" ")
    i+=1

print("\n")
j=1
while j<6:
    if j==3: break
    print(j,end=" ")
    j+=1

print("\n")
k=0
while k<6:
    k+=1
    if k==3:
        continue
    print(k,end=" ")

print("\n")
l=1
while l<6:
    print(l,end=" ")
    l+=1
else: print("\nl is no longer greater than 6")