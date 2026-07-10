'''
Data Cleaning is the process of:
Removing missing values, Filling missing values, Removing duplicate records
Correcting incorrect data types, Renaming columns, Removing unwanted spaces
'''

import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 104, 105, 106],
    "Name": [" Anushka ", "Rahul", "Priya", None, None, "Amit ", "Sneha"],
    "Age": [21, "22", None, 23, 23, 20, 20],
    "Department": ["IT", "HR", "it", "Sales", "Sales", None, "HR"],
    "Salary": [50000, 45000, None, 60000, 60000, 55000, None],
    "City": ["Pune ", " Mumbai", "Pune", "Delhi", "Delhi", "Nagpur", None]
}

df = pd.DataFrame(data)

print(df)

#check and count null values
print(df.isnull())
print("Count of null value\n",df.isnull().sum())

#remove missing values
df1=df.dropna()
print("\n",df1)

#fill missing value using Average
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("\n",df)

#fill name with unknown
df["Name"]=df["Name"].fillna("Unknown")

#Fill department
df["Department"]=df["Department"].fillna("Not Assigned")

#convert age into numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

#fill age with mean
df["Age"]=df["Age"].fillna(df["Age"].mean())

#Remove duplicate
df=df.drop_duplicates()
print("\n",df)

#convert department to uppercase
df["Department"]=df["Department"].str.upper()


#rename 
df.rename(columns={"Salary":"Monthly salary"}, inplace=True)

#final dataframe
print("\n",df)