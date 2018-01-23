class Employee:
    empCount = 0
    def _init_(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
