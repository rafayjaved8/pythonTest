class Employee:
    "Just a test class"
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def numberOfEmployees(self):
        print 'Total employees are: ',Employee.empCount

    def empDetails(self):
        print 'Name of employee: ',self.name
        print 'Salary of employee: ',self.salary

emp1 = Employee('Ali',20000)
emp1.numberOfEmployees()
emp2 = Employee('Ahmad',40000)
emp1.numberOfEmployees()

emp1.empDetails()
emp2.empDetails()

setattr(emp1, 'age', 8) # Set attribute 'age' at 8
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
delattr(emp1, 'age')    # Delete attribute 'age'


print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
