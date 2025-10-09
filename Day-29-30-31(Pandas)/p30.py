"""
Indexing# It seems like the text " and Sel" is incomplete and doesn't provide enough context to
# understand its purpose. If you can provide more information or clarify the context in which
# " and Sel" is being used, I would be happy to help you further.
and Selection--> 

Access rows/columns using:
- df['col_name'] or df[['col1','col2']]
- .loc[] → label-based
- .iloc[] → index-based
"""
# ==========================================================
#        INDEXING AND SELECTION IN PANDAS
# ==========================================================
import pandas as pd
import numpy as np

# Create sample DataFrame
data = {
    "Name": ["Amit", "Ravi", "Neha", "Priya", "Raj", "Simran"],
    "Age": [25, 30, 22, 24, 21, 29],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [40000, 50000, 45000, 48000, 42000, 46000],
    "City": ["Delhi", "Mumbai", "Chennai", "Pune", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)

# 1. Select single column
print(df["Name"])

# 2. Select multiple columns
print(df[["Name", "Salary"]])

# 3. Select row by label using loc[]
print(df.loc[2])

# 4. Select row by index number using iloc[]
print(df.iloc[3])

# 5. Slice rows using iloc[]
print(df.iloc[1:4])

# 6. Conditional selection (rows where Age > 25)
print(df[df["Age"] > 25])

# 7. Selecting specific columns where condition meets
print(df.loc[df["Salary"] > 45000, ["Name", "Department"]])

# 8. Using .at for single value access
print(df.at[1, "City"])  # Row 1, Column City

# 9. Using .iat for fast access (like NumPy)
print(df.iat[2, 3])  # Row 2, Column index 3

# 10. Changing specific cell value using loc
df.loc[0, "Salary"] = 41000
print(df)


# ==========================================================
#        DATA CLEANING
# ==========================================================
"""
Data Cleaning
- Handle missing data using:
- df.dropna() → remove nulls
- df.fillna(value) → fill nulls with a value
- df.isnull() → check for nulls
"""

# Create sample data with missing values
data_clean = {
    "Name": ["Amit", "Ravi", "Neha", None, "Raj", "Simran"],
    "Age": [25, np.nan, 22, 24, np.nan, 29],
    "Department": ["HR", "IT", "Finance", None, "HR", "Finance"]
}
df_clean = pd.DataFrame(data_clean)

# 1. Check for missing values
print(df_clean.isnull())

# 2. Drop rows with missing values
print(df_clean.dropna())

# 3. Drop columns with missing values
print(df_clean.dropna(axis=1))

# 4. Fill missing values with a constant
print(df_clean.fillna("Unknown"))

# 5. Fill missing numerical values with mean
df_clean["Age"].fillna(df_clean["Age"].mean(), inplace=True)
print(df_clean)

# 6. Replace specific values
df_clean.replace("HR", "Human Resources", inplace=True)
print(df_clean)

# 7. Rename columns
df_clean.rename(columns={"Name": "Employee_Name"}, inplace=True)
print(df_clean)

# 8. Check duplicated rows
print(df_clean.duplicated())

# 9. Drop duplicates
print(df_clean.drop_duplicates())

# 10. Reset index after cleaning
df_clean.reset_index(drop=True, inplace=True)
print(df_clean)

# ==========================================================
#        DATA OPERATIONS
# ==========================================================
"""
Data Operations
- Statistical operations: sum(), mean(), count(), min(), max().
- String operations: df['col'].str.upper(), str.lower(), str.contains().
"""

df_ops = df.copy()

# 1. Sum of Salary
print(df_ops["Salary"].sum())

# 2. Mean of Age
print(df_ops["Age"].mean())

# 3. Minimum Salary
print(df_ops["Salary"].min())

# 4. Maximum Salary
print(df_ops["Salary"].max())

# 5. Count total rows
print(df_ops["Department"].count())

# 6. Convert string column to uppercase
print(df_ops["City"].str.upper())

# 7. Filter rows containing 'Delhi'
print(df_ops[df_ops["City"].str.contains("Delhi")])

# 8. Add new calculated column (Bonus = 10% of Salary)
df_ops["Bonus"] = df_ops["Salary"] * 0.1
print(df_ops)

# 9. Modify multiple columns using assign()
df_ops = df_ops.assign(Net_Salary=df_ops["Salary"] + df_ops["Bonus"])
print(df_ops)

# 10. Drop column
df_ops.drop("Bonus", axis=1, inplace=True)
print(df_ops)


