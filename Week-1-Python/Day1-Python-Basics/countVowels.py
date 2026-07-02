def count_vowels(text):
    vowels="AEIOUaeiou"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count
text=str(input("Enter Your Name: "))
print("Total numbers of vowels:",count_vowels(text))