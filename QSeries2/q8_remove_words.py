# remove words from list using lambda function
def remove_words():
    colours = input("Enter a list of colours: ").split()
    print(colours)
    Remove_words = input("Enter words you want to remove:").split()
    print(Remove_words)
    remove = list(filter(lambda x: x not in Remove_words, colours))
    print(remove)

remove_words()
