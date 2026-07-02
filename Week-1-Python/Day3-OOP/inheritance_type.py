#Multiple inheritance: One child class inherits from more than one parent class.
class EmpSystem:
    def login(self):
        print("Employee logged into the system")

class SalarySystem:
    def salary(self):
        basic_salary = 50000
        bonus = 10000
        total = basic_salary + bonus
        print("Basic Salary:", basic_salary)
        print("Bonus:", bonus)
        print("Total Salary:", total)

class Employee(EmpSystem, SalarySystem):
    def employee_info(self):
        print("Employee Name: Anushka")

emp = Employee()
emp.employee_info()
emp.login()
emp.salary()

#multilevel inheritance: A class inherits from another child class form a chain.
class Person:
    def show_name(self,name):
        self.name=name
        print(f"Employee name is {self.name}")

class Employee(Person):
    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    def info(self,name):
        self.name=name
        print(f"Reporting Manager name is {self.name} ")

m = Manager()
m.show_name("Anushka")
m.work()
m.info("Gadkari Sir")

#hierarchical inheritance: Multiple child classes inherit from the same parent class.
class Company:
    def company_name(self):
        print("Company: Dynamisch")

class Developer(Company):
    def coding(self,name):
        self.name=name
        print(f"Developers Team Head: {self.name}")

class Tester(Company):
    def testing(self):
        print("Tesing Team working ")

d = Developer()
t = Tester()
d.company_name()
d.coding("Sahil kajare")
t.testing()

# Hybrid inheritance: Combination of two or more types of inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")

class TeachingAssist(Student, Teacher):
    def assist(self):
        print(self.name, "is assisting in lab")

ta = TeachingAssist("Anushka")
ta.show_name()
ta.study()
ta.teach()
ta.assist()