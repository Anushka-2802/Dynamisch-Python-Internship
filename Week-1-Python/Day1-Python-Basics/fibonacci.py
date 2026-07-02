def fibonacci(n):
    a=0
    b=1
    for n in range(2,n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
fibonacci(10)