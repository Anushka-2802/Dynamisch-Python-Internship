#Functions 
def sum(a,b):
    return a+b
print("Sum of numbers: ",sum(5,10))

# Parameter Passed using Argument Keyword
def student(name,age,branch):
    print("Name: ",name)
    print("Age: ",age)
    print("Branch: ",branch)
student("Anushka",28,"CSE")

#Arbitrary Arguments *args
def total(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
print(total(1,2,3,4))
print(total(4,5,6))        

#Arbitrary Keyword Arguments **kwargs
def details(**data):
    print(data)
details(Name="Anushka",Emp_id=28,payment=20000,)

#Recursive Function
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print("Factorial",factorial(12))

#Reverse the String
def reverse_string(text):
    reverse_text=text[::-1]
    return reverse_text
text=str(input("Enter Name: "))
print("Reversed String is: ",reverse_string(text))