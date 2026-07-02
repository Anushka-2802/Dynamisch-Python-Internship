"""Take string as a input
first character is stored in new variable
from remaining part second occurance of first character is replaced by "$"
concate two string to get changed string
"""


def change_text(text):  # function to replace string character

    first = text[0]  # store first character
    remaining = text[1:]  # remaining characters
    new = remaining.replace(
        text[0], "$"
    )  # replace second occurance of first character with "$"
    newtext = first + new  # concatenation of string
    print(newtext)


text = str(input("Enter a string: "))
change_text(text)


# without replace method
def change_text(text):
    first = text[0]  # store first character
    result = first
    for i in range(1, len(text)):  # loop for remaining character
        if (
            text[i] == first
        ):  # charcter is similar to the first character then concate with $
            result = result + "$"
        else:
            result = result + text[i]
    print(result)


text = "restart"
change_text(text)
