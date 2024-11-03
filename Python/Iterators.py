myTuple = ("apple","banana","cherry")
myIt = iter(myTuple)
print(next(myIt))
print(next(myIt))
print(next(myIt))

class MyClass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<20:
            x=self.a
            self.a+=1
            return x
        else: raise StopIteration # To stop the iteration from going on forever
myClass = MyClass()
myIter = iter(myClass)
for x in range(25):
    print(next(myIter))