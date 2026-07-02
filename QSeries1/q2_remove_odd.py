#using slicing
string=str(input("Enter a string: "))
#removing whitespace
new_string=string.replace(" ","")
result=new_string[0:len(string):2]
print("After removing odd index character: ",result)


#without slicing
def remove_odd_index(string):
    for i in range(len(string)): 
        if i%2==0:  #checking even odd (if index number mod 2 is zero then it is even index)
           print(string[i],end=" ")
string=str(input("Enter a String: "))
remove_odd_index(string)