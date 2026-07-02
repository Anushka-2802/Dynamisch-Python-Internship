def vowels():
    """make a list of names that start with vowels AEIOU"""

    names = ["Anushka", "prachi", "divya", "Arfa"]
    result = list(filter(lambda x: x[0].lower() in "aeiou", names))
    print(result)

vowels()
