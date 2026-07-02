#Decorators are flexible way to modify or extend behavior of functions or methods without changing their actual code
def decorator(func):
    def wrapper(*args,**kwarg):
        print("Before Execution: ")
        result=func(*args,**kwarg)
        print("After Execution: ")
        return result
    return wrapper
@decorator
def add(a,b):
    return a+b
print(add(5,15))

