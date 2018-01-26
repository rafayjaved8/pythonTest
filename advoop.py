# Overiding methods

class Parent:
    def myMethod(self):
        print 'Parent method'

class Child(Parent):
    def myMethod(self):
        print 'Child method'

child = Child()
child.myMethod()

# Operator Overloading

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector (%d,%d)'%(self.x,self.y)

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

vec1 = Vector(2,3)
vec2 = Vector(2,3)
print vec1
print vec2
print vec1+vec2


# Data Hiding

class Count:
    __varCounter = 0
    var = 0

    def counter(self):
        self.__varCounter += 1
        self.var += 1
        print self.__varCounter

cnt = Count()
cnt.counter()
cnt.counter()
cnt.counter()
print cnt.var
