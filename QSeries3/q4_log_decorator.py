def decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Before Execution")
        print("Arguments Passed:", args)
        result = func(*args, **kwargs)
        print("Return Value:", result)
        print("After Execution")
        return result
    return wrapper

@decorator
def average(a, b, c, d):
    return (a + b + c + d) / 4

print("Result of Average:", average(10, 20, 23, 24))