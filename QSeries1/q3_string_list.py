# simply use split method to convert string into list of word

string = "The quick brown fox jumps over the lazy dog."
string.split()
print(string)

# without split method
string = "hello i am anushka"
word = ""
new_list = []
for i in string:
    if i != " ":  # check for a space
        word = word + i
    else:
        new_list.append(word)
        word = ""
new_list.append(word)
print(new_list)
