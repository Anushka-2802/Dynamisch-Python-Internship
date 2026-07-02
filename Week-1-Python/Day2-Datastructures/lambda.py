#lambda function is a small anonymous function
# It can take any number of arguments but have only single expression 
x=lambda a:a+10
print(x(5))

x=lambda a,b,c: a+b*c
print(x(120,100,2))

#lambda function use as asynchronous function inside other function
def add(n):
    return lambda a:a+n
add_fun=add(3)
print(add_fun(10))

#double all the numbers in list
numbers=[1,2,3,4,5,6]
double=list(map(lambda x:x*2,numbers)) #map() applies function to every element of iterable
print(double)

#print odd number from list
numbers=[1,2,3,4,5,6]
odd_numbers=list(filter(lambda x: x % 2 != 0 ,numbers))
print(odd_numbers)
