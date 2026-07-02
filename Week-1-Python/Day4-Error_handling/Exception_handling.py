#Exception handling allows program to handle unwanted errors during execution 
#It enables program to detect errors manage them properly and continue execution
#try expect : these blocks are used to handle error and exception  
#code in try block is run when there is no error if try block catch the error then except block is executed

#Divide by zero error
try:
    num1=int(input("Enter a number 1: "))
    num2=int(input("Enter a number 2: "))
    result=num1/num2

except Exception as e:
    print(e) 

else:
    print("Result: ",result)

#Usedefined Exceptions    
class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter marks: "))
    if marks > 100:
        raise InvalidMarksError

except InvalidMarksError :
    print("Marks cannot be greater than 100")

class Age:
    def check_age(self):
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                raise ValueError("Age must be positive")
        except ValueError as e:
            print(e)
        else:
            print("Age of person is", age)
obj = Age()
obj.check_age()

#Simple program for banking system
class BankAccount:
    def withdraw_money(self):
        try:
            balance=10000
            amount=int(input("Enter amount you want to withdraw: "))
            if amount<0:
                raise ValueError("amount must be positive")
            if amount>balance:
                raise ValueError("Insufficient Balance")
        except ValueError as e:
            print(e)

        else: #if error is not occur in try block then else block is execute
            balance=balance-amount
            print("withdraw Successfully!!")
            print("Remaining balance:",balance)

        finally: #finally block always run with or without exception
            print("Thank You !!")
obj=BankAccount()
obj.withdraw_money()
