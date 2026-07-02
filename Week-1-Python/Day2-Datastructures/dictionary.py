#Print dictionary 
dic1={'Name':'Anushka','Id':63, 'salary':40000, 'age':21 }
print(dic1)
x=dic1.get('Name') #Accessing items 
print(x)

#methods
dic2={'location':'phaltan'}
print(dic2)
dic1.update(dic2)
print("After concatenation:",dic1)
dic1.pop('age')
print("After removing age value pair: ",dic1)
dic1.popitem()
print("After removing last item: ",dic1)

#take dictionary input from user
n=int(input("Enter a number of element: "))
dic={}
for i in range(n):
    key=input("Enter key : ")
    value=input("Enter Value: ")
    dic[key]=value 
print(dic)


# keys in range between 1 to 10 and values are cube of keys 
dic_cube={}
for i in range(1,11):
    dic_cube[i]=i**3
print(dic_cube)
