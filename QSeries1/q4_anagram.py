
str1 = input("Enter a string1: ")
str2 = input("Enter a string2: ")
# using sorted() method sort the string
# after sorting strings are equal then it is anagram strings
if sorted(str1) == sorted(str2):
    print("Strings are Anagram")
else:
    print("Strings are not Anagram")

# without sort
str1 = str(input("Enter a string1: "))
str2 = str(input("Enter a string2: "))
count = 0  # used to stores count
for i in str1:  # traverse string 1
    if i in str2:  # check character present in str2
        count = count + 1
if count == len(str1):  # compare count value with length of string
    print("Strings are Anagram")
else:
    print("Strings are not Anagram")
