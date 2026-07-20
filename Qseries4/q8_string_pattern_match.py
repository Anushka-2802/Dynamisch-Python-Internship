import re
"""
Checks whether a string contains only
uppercase letters, lowercase letters,
numbers, and underscores using regular expressions.
"""
text = input("Enter a string: ")

pattern = r'^[A-Za-z0-9_]+$'

if re.match(pattern, text):
    print("Valid String")
else:
    print("Invalid String")