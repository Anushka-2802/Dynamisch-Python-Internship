def person():
    """
    Accepts age input from the user and validates it.
    Raises:
        ValueError:
            - If the input is not an integer
            - If age is negative
            - If age is greater than 150
    Prints:
        Accepted message if the age is valid.
    """
    try:
        age=int(input("Enter age: "))
        if age<0:
            raise ValueError("Age must be positive")
        elif age>150:
            raise ValueError("Invalid Age")
        else:
            print("accepted..")
    except ValueError as e:
        print(f"Error:{e}")
person()