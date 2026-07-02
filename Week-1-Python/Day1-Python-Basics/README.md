Day 1 - Python Basics

1. Python Syntax

Python syntax is simple and easy to read.
Python uses indentation instead of curly braces.

Example
print("Hello World")

2. Variables

Variables are used to store data values.

Example
name = "Anushka"
age = 21
print(name)
print(age)

3. Datatypes

Datatypes means the type of data stored in variables.

Common Datatypes

 int
 float
 str
 bool
 list
 tuple
 dictionary

4. Control Flow

Control flow statements are used to make decisions in programs.

Example

age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

5. Loops

Loops are used to execute code repeatedly

For Loop Example

for i in range(5):
    print(i)

While Loop Example

count = 1
while count <= 5:
    print(count)
    count += 1

6. Functions

Functions are reusable blocks of code used to perform specific tasks.

def add(a, b):
    return a + b

print(add(10, 20))

7. Recursive Function

A recursive function is a function that calls itself

Example - Factorial
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

8. *args

*args allows a function to accept multiple arguments
Example

def total(*numbers):
    print(numbers)

print(total(1, 2, 3, 4))

9. **kwargs

**kwargs allows a function to accept multiple keyword arguments
Example

def details(**data):
    print(data)

details(name="Anushka", age=21)

 Programs Practiced

* Calculator Program
* Fibonacci Series
* Prime Number
* Reverse String
* Count Vowels

Today, I learned the fundamentals of Python programming including syntax, variables, datatypes, loops, functions, recursion, and basic string operations. These concepts helped me understand the basic structure and working of Python programs.
