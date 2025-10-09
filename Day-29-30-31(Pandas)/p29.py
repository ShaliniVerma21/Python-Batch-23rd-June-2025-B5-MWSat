""" 
Introduction to Pandas-->

- Pandas is an open-source Python library for data analysis and manipulation.
- Built on top of NumPy → hence very efficient for numerical operations.
- Provides fast, flexible, and expressive data structures like Series & DataFrame.
- Commonly used in Data Science, Machine Learning, Business Analytics, Finance, and Research.
- Pandas makes handling structured data (tabular, time-series, etc.) very easy.
"""

""" 
How to Use Pandas in Python

Step 1: Install Pandas, If not installed already:
pip install pandas

Step 2: Import Pandas
Always import with a short alias (pd):
"""
import pandas as pd

""" 
Step 3: Create Pandas Objects
You can create Series (1D) or DataFrame (2D).
"""
import pandas as pd
# Series (like a column)
s = pd.Series([10, 20, 30, 40])
print(s)
# DataFrame (like a table)
data = {"Name": ["Amit", "Ravi", "Neha"], "Age": [25, 30, 22]}
df = pd.DataFrame(data)
print(df)

""" 
Step 4: Read Data (from files)
Pandas is widely used to load CSV, Excel, JSON, SQL data.
"""
# Read CSV
df = pd.read_csv("employees.csv")

# Read Excel
df2 = pd.read_excel("data.xlsx")

# Read JSON
df3 = pd.read_json("data.json")
print(df.head())  # First 5 rows

""" 
Step 5: Explore Data
Useful functions to understand the dataset.
"""
import pandas as pd
data = {"Name": ["Amit", "Ravi", "Neha"], "Age": [25, 30, 22]}
df = pd.DataFrame(data)
print(df)
print(df.shape)       # (rows, columns)
print(df.columns)     # column names
print(df.info())      # data types & non-null values
print(df.describe())  # statistics (mean, std, min, max)
print(df.head(3))     # first 3 rows
print(df.tail(2))     # last 2 rows

""" 
Step 6: Select Data
Select rows & columns easily.
"""
import pandas as pd
# Select one column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Age"]])

# Select row by index
print(df.loc[0])   # by label
print(df.iloc[1])  # by index number

# Conditional selection
print(df[df["Age"] > 25])

""" 
Step 7: Modify Data
Add, update, or delete columns/rows.
"""
# Add new column
df["Country"] = "India"

# Update column
df["Age"] = df["Age"] + 1

# Drop a column
df = df.drop("Country", axis=1)

# Drop a row
df = df.drop(0, axis=0)

""" 
Step 8: Analyze Data
Pandas makes calculations easy.
"""
print(df["Age"].mean())   # Average age
print(df["Age"].max())    # Max age
print(df["Age"].min())    # Min age
print(df["Age"].sum())    # Total

""" 
Step 9: Grouping & Aggregation
Useful for analysis like Excel pivot tables.
"""
grouped = df.groupby("Department")["Salary"].mean()
print(grouped)

""" 
Step 10: Save Data
After analysis, export data back to files.
"""
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")

"""
Basic Examples of Using Pandas : 
"""
import pandas as pd
import numpy as np

# 1. Checking pandas version
print(pd.__version__)

# 2. Creating a simple Series
s = pd.Series([10, 20, 30])
print(s)

# 3. Creating a DataFrame from dictionary
df = pd.DataFrame({"Name": ["Amit", "Ravi"], "Age": [25, 30]})
print(df)

# 4. Using numpy array in pandas
arr = np.array([1,2,3,4])
print(pd.Series(arr))

# 5. Checking top rows of dataframe
print(df.head())

# 6. Checking bottom rows
print(df.tail())

# 7. Checking shape (rows, columns)
print(df.shape)

# 8. Checking columns
print(df.columns)

# 9. Checking data types
print(df.dtypes)

# 10. Checking basic statistics
print(df.describe())

"""
Main Data Structures-->
- Series: A 1-D labeled array (like a single column in Excel).
- DataFrame: A 2-D labeled data structure (like an Excel sheet).
- Panel: Deprecated, earlier used for 3-D data.
"""
# 1. Series from list
s = pd.Series([100, 200, 300])
print(s)

# 2. Series with custom index
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s2)

# 3. Accessing Series elements
print(s2["b"])

# 4. DataFrame from dictionary
df = pd.DataFrame({"City":["Delhi","Mumbai","Chennai"], "Population":[10,20,30]})
print(df)

# 5. Accessing a column
print(df["City"])

# 6. Accessing multiple columns
print(df[["City", "Population"]])

# 7. Accessing a row using loc
print(df.loc[1])

# 8. Accessing by index using iloc
print(df.iloc[0])

# 9. Adding a new column
df["Country"] = ["India","India","India"]
print(df)

# 10. Deleting a column
df = df.drop("Country", axis=1)
print(df)

"""
Creating Pandas Objects
- Create from lists, dictionaries, NumPy arrays, 
or external files (CSV, Excel, SQL, JSON).
- Flexible structure: easy to build tables dynamically.
"""
# 1. From Python list
s = pd.Series([1,2,3,4])
print(s)

# 2. From dictionary (Series)
s2 = pd.Series({"a":100,"b":200,"c":300})
print(s2)

# 3. From dictionary (DataFrame)
df = pd.DataFrame({"Name":["Ravi","Priya"], "Age":[22,24]})
print(df)

# 4. From numpy array
arr = np.array([[1,2],[3,4]])
df2 = pd.DataFrame(arr, columns=["A","B"])
print(df2)

# 5. From tuple list
data = [("Amit",25), ("Neha",30)]
df3 = pd.DataFrame(data, columns=["Name","Age"])
print(df3)

# 6. From scalar value
s3 = pd.Series(5, index=[0,1,2,3])
print(s3)

# 7. From CSV file (if exists)
# df4 = pd.read_csv("data.csv")

# 8. From JSON string
json_data = '[{"Name":"Raj","Age":21},{"Name":"Simran","Age":22}]'
df4 = pd.read_json(json_data)
print(df4)

# 9. Empty DataFrame
df_empty = pd.DataFrame()
print(df_empty)

# 10. DataFrame with date range index
dates = pd.date_range("2023-01-01", periods=5)
df5 = pd.DataFrame(np.random(5,2), index=dates, columns=["A","B"])
print(df5)


"""
Reading and Writing Data
- pd.read_csv(), pd.read_excel(), pd.read_json() → Read data.
- df.to_csv(), df.to_excel() → Write data.

Pandas supports reading & writing data in multiple formats:
- pd.read_csv() / df.to_csv() → CSV files
- pd.read_excel() / df.to_excel() → Excel files
- pd.read_json() / df.to_json() → JSON data
- pd.read_sql() / df.to_sql() → SQL databases
"""
# 1. Read CSV
# df = pd.read_csv("employees.csv")

# 2. Write CSV
df = pd.DataFrame({"Name":["A","B"], "Age":[20,30]})
df.to_csv("output.csv", index=False)

# 3. Read Excel
# df2 = pd.read_excel("data.xlsx")

# 4. Write Excel
df.to_excel("output.xlsx", index=False)

# 5. Read JSON
json_data = '[{"City":"Delhi","Pop":200},{"City":"Mumbai","Pop":300}]'
df3 = pd.read_json(json_data)
print(df3)

# 6. Write JSON
df3.to_json("output.json")

# 7. Reading only specific columns from CSV (example)
# df4 = pd.read_csv("employees.csv", usecols=["Name","Age"])

# 8. Writing without index
df.to_csv("output_no_index.csv", index=False)

# 9. Reading limited rows
# df5 = pd.read_csv("employees.csv", nrows=5)

# 10. Storing dataframe in clipboard (copy-paste like Excel)
df.to_clipboard(index=False)