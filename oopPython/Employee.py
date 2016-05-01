class Employee:
    'This is a simple class used to learn OOP concepts in Python'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Number of employess is: %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Neilson", 30000)
emp2 = Employee("Neylson", 15000)

emp1.displayCount()
emp1.displayEmployee()

emp2.displayCount()
emp2.displayEmployee()

emp1.age = 35

print(emp1.age)

print(hasattr(emp1, 'age'))
setattr(emp2, "age", 26)
print(emp2.age)
# delattr(emp1, 'age')
print(emp1.age)
print(getattr(emp2, 'name'))
print('--------------------')
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__base__)
print(Employee.__module__)