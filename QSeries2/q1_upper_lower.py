# count Upper and lower Characters in String
# isupper() and islower() method used to check upper and lower character in string
def count_upper_lower():
    """Track and count upper and lower character in string"""
    string = input("Enter a string: ")  # accept input string from user
    count_upper = 0  # track upper character count
    count_lower = 0  # track lower character
    for char in string:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    print("No of Uppercase Characters: ", count_upper)
    print("No of Lowercase Characters: ", count_lower)


count_upper_lower()
