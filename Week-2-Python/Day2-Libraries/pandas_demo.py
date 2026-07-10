'''
Pandas is an open-source Python library used for data manipulation, analysis, and cleaning. 
It provides easy-to-use data structures like Series and DataFrame to work with structured data 
such as CSV files, Excel sheets, SQL databases, and JSON.
'''
import pandas as pd 
data={
     "Id":[100,101,102,103,104,105],
     "name":["Anushka","Prachi","Esha","Divya","Arfa","Abhilasha"],
     "marks":[80,80,75,85,83,84]
}
'''A DataFrame is a 2D labeled data structure with rows and columns, similar to an Excel or SQL table'''
df=pd.DataFrame(data)
print(df)

# View data
print("\nFirst five rows\n",df.head())   #first 5 rows
print("\nLast five rows\n",df.tail())   #last 5 rows
print("\nFirst two rows\n",df.head(2))   #first 2 rows
print("\nLast three rows\n",df.tail(3))   #last 3 rows

print(df.info()) #Information about dataframe
print(df.describe()) #satistical summary 

print(df.columns) #Columns in dataframe
print(df.shape) #shape

#selecting columns
print(df[["name","marks"]])

#selecting row
print(df.loc[0])
print(df.iloc[1])

#select student having marks more than 80
print(df[df["marks"]>80])



