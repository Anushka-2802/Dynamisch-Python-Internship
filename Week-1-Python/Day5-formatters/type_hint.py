#Type hint in python used to specify the expected datatype of variables,functions and return value
name:str="anushka"
age:int=21
height:float=5.2
print(name,age,height)

#function type hint
def add(x:int,y:int)->int:
    result= x+y
    print("Addition: ",result)
add(10,20)

#type hint in classes
class student:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def display(self)->None:
        print(self.name,self.age)
obj=student("Anushka",21)
obj.display()

# type hint in list
numbers:list[int]=[12,23,33,45,30]
def total(nums:list[int])->int:
    return sum(nums)
print(total(numbers))