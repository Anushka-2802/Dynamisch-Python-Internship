#dunder method is special method in python start and end with double underscore

#1.__init__() constructor
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Name of Student: {self.name}")
        print(f"ID of Student: {self.id}")
a=Student("Anushka",21)
a.show()

#2.__str__():Controls what prints when object is printed
class car:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Car name is {self.name}"
c=car("Swift")
print(c)

#3.__len__(): length of object used with len()
class student:
    def __init__(self,members):
        self.members=members
    def __len__(self):
        return len(self.members)
s=student(["Anushka","Divya","Prachi","Arfa","Esha","Abhilasha","Athrav"])
print("length of object is:",len(s))

#4 __add__(): + operator overloading
class number:
    def __init__(self,number):
        self.number=number
    def __add__(self,other):
        return self.number + other.number
n1=number(10)
n2=number(20)
print("Addition of two number is:",n1+n2)

#5 __eq__(): == Comparison
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks
s1 = Student(90)
s2 = Student(90)
print(s1 == s2) #print boolean result

#6 __it__(): less than
class Watch:
    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price
w1 = Watch(5000)
w2 = Watch(10000)
print(w1 < w2) # print boolean result

#7 __getitem__(): Indexing allows object indexing like lists
class List:
    def __init__(self,data):
        self.data=data
    def __getitem__(self,index):
        return self.data[index]
obj=List([12,13,20,45,34])
print(obj[3]) #print the third index element

#8 __call__(): call object like function 
class Employee:
    def __call__(self):
        print(f"{self.name} joined today")
    def show(self,name):
        self.name=name
        print(f"Name of employee is {self.name}")
emp = Employee()
emp.show("Anushka")
emp()

#9 __del__(): destructor called when object is destroyed
class car:
    '''def demo(self,name):
        self.name=name
        print(f"car name: {self.name}")
        '''
    def __del__(self):
        print("Object is destroyed")
c=car()
#c.demo("KIA")
del c

#there are many more dunder(special) methods :initialization, arithmetic, numeric, string, comparison etc