#A formatter is a tool that automatically arranges Python code in a clean and standard format
#Black is an automatic Python code formatter
#It reformats code according to Python standard style
#without black formatter
class Student:
 def __init__(self,name,marks):
          self.name=name
          self.marks=marks

 def display(self):
               print("Student Name:",self.name)
               print("Student Marks:",self.marks)

student1=Student("Anushka",90)

student1.display()

#Install Black Formatter Extension
#Select Formatter: format Document with - Black Formatter
#right click inside file select format document
#After Formatter
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)


student1 = Student("Anushka", 90)

student1.display()