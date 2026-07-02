#Package is a collection of multiple modules organized inside folder

#numpy: Used for numerical and array operations
import numpy as np

marks = np.array([78, 85, 90, 67, 88])
print("Student Marks:", marks)

average = np.mean(marks)  #average of marks
print("Average Marks:", average)

highest = np.max(marks) # Highest marks
print("Highest Marks:", highest)

lowest = np.min(marks) # Lowest marks
print("Lowest Marks:", lowest)

total = np.sum(marks) # Total marks
print("Total Marks:", total)

#pandas-used for data analysis and table handling

import pandas as pd
# Student data
data = {
    "Name": ["Anushka", "Prachi", "Divya", "Arfa"],
    "Marks": [85, 90, 78, 88],
    "City": ["Ratnagiri", "Pune", "Mumbai", "Satara"]
}
df = pd.DataFrame(data)
print("Student Records:\n")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())

#Matplotlib-used for plotting graphs
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.title("Simple Graph")
plt.show()

