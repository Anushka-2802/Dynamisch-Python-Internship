'''
groupby is used to group rows based on one or more columns 
and perform aggregate operations like sum(), mean(), count(), max(), and min().
'''
import pandas as pd

data = {
    "Department":["IT","HR","IT","HR","Sales"],
    "Employee":["Anu","Prachi","Divya","Esha","Abhilasha"],
    "Salary":[50000,40000,60000,45000,55000]
}

df = pd.DataFrame(data)
print(df)

#Average Salary department wise
result=df.groupby("Department")["Salary"].mean()
print(result)

# Total Salary
print("Total Salary",df.groupby("Department")["Salary"].sum())

# Max Salary
print("Max Salary",df.groupby("Department")["Salary"].max())

# Min Salary
print("Min Salary",df.groupby("Department")["Salary"].min())

# Multiple Aggregation
print(df.groupby("Department")["Salary"].agg(["sum","mean","max","min"]))


'''merge is used to combine two DataFrames based on a common column'''

student = pd.DataFrame({
    "ID":[1,2,3,4],
    "Name":["Anu","Bob","Carlo","Rahul"]
})

marks = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[80,90,85]
})

result=pd.merge(student,marks,on="ID")
print(result)

#Left Merge returns all records from the left DataFrame and matching records from the right
left_merge=pd.merge(student,marks,on="ID",how="left")
print("\nLeft Merge\n",left_merge)

#Right Merge returns all records from the right DataFrame and matching records from the left
right_merge=pd.merge(student,marks,on="ID",how="right")
print("\nRight Merge\n",right_merge)

#Inner Merge returns only the matching records from both DataFrames
inner_merge=pd.merge(student,marks,on="ID",how="inner")
print("\nInner Merge\n",inner_merge)

#Outer Merge returns all records from both DataFrames; non-matching values are filled with NaN
outer_merge=pd.merge(student,marks,on="ID",how="outer")
print("\nOuter Merge\n",outer_merge)

'''
join combines DataFrames based on their index
It is mainly used when both DataFrames share the same index
'''
Student = pd.DataFrame({
    "Name": ["Anushka", "Rahul", "Priya", "Amit"]
}, index=[1,2,3,4])

Marks = pd.DataFrame({
    "Marks": [85,90,88,75]
}, index=[2,3,4,5])
 
join_result=Student.join(Marks)
print(join_result)

#Left join keeps all rows from the left DataFrame Student
left_join=Student.join(Marks,how="left")
print("\nLeft join\n",left_join)

#Right join keeps all rows from the right DataFrame (marks).
right_join=Student.join(Marks,how="right")
print("\nRight join\n",right_join)

#Inner join keeps only matching indexes from both DataFrames.
inner_join=Student.join(Marks,how="inner")
print("\nInner join\n",inner_join)

#Outer joinkeeps all indexes from both DataFrames.
outer_join=Student.join(Marks,how="outer")
print("\nOuter join\n",outer_join)
