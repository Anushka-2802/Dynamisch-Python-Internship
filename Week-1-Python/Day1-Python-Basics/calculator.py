#Take input from User
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
#Take choice From User
print("1:Addition")
print("2:Subtraction")
print("3:Division")
print("4:Multiplication")

choice= int(input("Enter choice: "))
if choice==1:
    print("Addition of",num1,"+",num2,"is",num1+num2)
elif choice==2:
    print("Substraction of",num1,"-",num2,"is",num1-num2)
elif choice==3:
    if num2!=0:
        print("Substraction of",num1,"/",num2,"is",num1/num2)
    else:
        print("Division by Zero Error")
elif choice==4:
    print("Multiplication of",num1,"*",num2,"is",num1*num2)
else:
    print("Invalid Choice")

