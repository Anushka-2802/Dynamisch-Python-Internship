# Program to read a file line by line and store it into an array
lines_array = []
# Open the file in read mode
with open("myfile.txt", "r") as file:
    for line in file:
        lines_array.append(line.strip())

# Display the array
print("Lines stored in array:")
print(lines_array)