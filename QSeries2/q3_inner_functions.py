def calculator():
    '''
    Outer function that performs calculator operations.
    It takes two numbers from the user and accesses
    inner functions to perform addition and multiplication.
    '''
    def add(a,b):
        '''
        Inner function to add two numbers.
        Parameters:
        a (int): First number
        b (int): Second number
        Returns:
        int: Sum of two numbers
        '''
        return a+b
    
    def multiply(a,b):
        '''
        Inner function to multiply two numbers
        parametres:
        a (int): First number
        b (int): Second number
        Returns:
        int:multiplication of two numbers
        '''
        return a*b
    #Access Inner functions
    print("Addition of two numbers:",add(1234,1235))
    print("multiplication of two numbers:",multiply(120,20))

calculator()
