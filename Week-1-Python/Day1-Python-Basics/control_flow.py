# Conditional Statement if elif else
# Even odd 
num=int(input("Enter number: "))
if num%2==0:
    print("Number is Even")
else:
    print("Number is odd")

# Multiple if elif
marks=75
if marks>90:
    print("A Grade")

elif marks>70:
    print("B Grade")

else:
    print("C Grade")

#Loops
#for loop (Table of number)
num1=int(input("\nEnter The Number:"))

for i in range(1, 11):
    print(num1, "x", i, "=", num1 * i)

# While loop (Sum of number)
num=1
total=0
while num <= 5:
    total=total+num
    num+=1
print("\nSum of Numbers :",total)




