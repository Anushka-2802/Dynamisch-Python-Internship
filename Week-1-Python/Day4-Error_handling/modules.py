#module is a single file that contains functions,variables,class and reusable codes
#instead of writing same code again and again, store it in single file and reuse when needed
#Built-in modules
import math #math is built-in module
class Arithmetic:
    def arithmetic(self, a, b):
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Square Root of a:", math.sqrt(a))
        print("Power:", math.pow(a, 2))
obj = Arithmetic()
obj.arithmetic(10, 5)

# import more built-in module
import math
import random
import datetime
import os
import platform
# math module
print("Square Root of 64:", math.sqrt(64))
# random module
print("Random Number:", random.randint(1, 100))
# datetime module
#current_date = datetime.datetime.now()
print("Current Date and Time:", datetime.datetime.now())
# os module
print("Current Working Directory:", os.getcwd())
# platform module
print("Operating System:", platform.system())

#Userdefined module 
import Student_module
m1=30
m2=40
m3=80
total = Student_module.total_marks(m1, m2, m3)
per = Student_module.percentage(total)
status = Student_module.result(per)
print("Total Marks:", total)
print("Percentage:", per)
print("Result Status:", status)
