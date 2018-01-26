class Parent:
    parentAttrib = 0
    def __init__(self):
        print 'Calling parent constructor'

    def parentMethod(self):
        print 'Calling parent method'

    def setAttrib(self,var):
        Parent.parentAttrib = var

    def getAttrib(self):
        print ('Parent attrib is: ',Parent.parentAttrib)

class Child(Parent):
    def __init__(self):
        print 'Calling child constructor'

    def childMethod(self):
        print 'Calling child method'

c = Child()
c.childMethod()
c.parentMethod()
c.getAttrib()
c.setAttrib(200)
c.getAttrib()
