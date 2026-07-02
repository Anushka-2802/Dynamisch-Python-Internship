#constructor is a special method in class used to create and initialize object in class
#constructor is unique function that get called automatically when object is created
#default constructor: It is does not accept any argument from object it has only one argument self 
class employee_data:
    def __init__(self):
        self.name="Anushka"
        self.empid=63
        self.age=21
        self.department="Developer"
        self.salary=20000

a=employee_data()
print("name:",a.name)
print("id:",a.empid)
print("Age:",a.age)
print("Department:",a.department)
print("Salary:",a.name)

#parameterized constructor: It accept any number of argument along with self from object
class person:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def show(self):
        print(f"Empolyee name: ",self.name)
        print(f"Employee Id: ",self.id)
        print(f"Employee age: ",self.age)
a=person("Anushka",21,63)
a.show()
