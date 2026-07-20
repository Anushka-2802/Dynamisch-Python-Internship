import os

"""
Creates a file, writes text into it,
and renames the file.
"""

with open("oldfile.txt", "w") as file:
    file.write("Hello, this is a sample file.")

os.rename("oldfile.txt", "newfile.txt")

print("File renamed successfully.")