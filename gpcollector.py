class Point:
    def __init__ (self,x=0,y=0):
        self.x = x
        self.y = y

    def __del__ (self):
        className = self.__class__.__name__
        print className,' is deleted'

pnt1 = Point()
pnt2 = pnt1
pnt3 = pnt1
print id(pnt1),id(pnt2),id(pnt3)
del pnt1
del pnt2
del pnt3
