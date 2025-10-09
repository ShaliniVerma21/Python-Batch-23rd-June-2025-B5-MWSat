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



# ==========================================================
#        MERGING, JOINING, CONCATENATION
# ==========================================================
"""
Merging, Joining, Concatenation
- pd.concat([df1, df2]) → stack datasets.
- pd.merge(df1, df2, on='key') → SQL-style join.
"""

# Create sample DataFrames
df1 = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Name": ["Amit", "Ravi", "Neha"],
    "Department": ["HR", "IT", "Finance"]
})

df2 = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Salary": [40000, 50000, 45000]
})

# 1. Merge on Emp_ID
merged = pd.merge(df1, df2, on="Emp_ID")
print(merged)

# 2. Inner join
print(pd.merge(df1, df2, how="inner", on="Emp_ID"))

# 3. Left join
print(pd.merge(df1, df2, how="left", on="Emp_ID"))

# 4. Right join
print(pd.merge(df1, df2, how="right", on="Emp_ID"))

# 5. Outer join
print(pd.merge(df1, df2, how="outer", on="Emp_ID"))

# 6. Concatenate vertically
print(pd.concat([df1, df1]))

# 7. Concatenate horizontally
print(pd.concat([df1, df2], axis=1))

# 8. Append new rows
new_row = {"Emp_ID": 4, "Name": "Raj", "Department": "Sales"}
df1 = pd.concat([df1, pd.DataFrame([new_row])])
print(df1)

# 9. Merge with different key names
df3 = pd.DataFrame({"Employee_ID": [1, 2, 3], "City": ["Delhi", "Mumbai", "Chennai"]})
print(pd.merge(df1, df3, left_on="Emp_ID", right_on="Employee_ID"))

# 10. Combine using update
df1.update(df2)
print(df1)

# ==========================================================
#        GROUPING AND AGGREGATION
# ==========================================================
"""
Grouping and Aggregation
- df.groupby('col') → group data.
- Aggregations: sum(), mean(), count(), agg().
"""

df_group = df.copy()

# 1. Group by Department and find mean salary
print(df_group.groupby("Department")["Salary"].mean())

# 2. Count number of employees per department
print(df_group.groupby("Department")["Name"].count())

# 3. Find max salary per department
print(df_group.groupby("Department")["Salary"].max())

# 4. Multiple aggregations
print(df_group.groupby("Department").agg({"Salary": ["mean", "max", "min"]}))

# 5. Group by multiple columns
print(df_group.groupby(["Department", "City"])["Salary"].sum())

# 6. Using .size() to count records
print(df_group.groupby("Department").size())

# 7. Using .get_group()
print(df_group.groupby("Department").get_group("IT"))

# 8. Using transform to broadcast results
df_group["Avg_Salary"] = df_group.groupby("Department")["Salary"].transform("mean")
print(df_group)

# 9. Sort grouped result
grouped_sorted = df_group.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(grouped_sorted)

# 10. Reset index after groupby
print(grouped_sorted.reset_index())

# ==========================================================
#        SORTING AND FILTERING
# ==========================================================
"""
Sorting & Filtering
- df.sort_values(by='col')
- df[df['col'] > 50] → filter rows.
"""
df_sort = df.copy()

# 1. Sort by Salary ascending
print(df_sort.sort_values(by="Salary"))

# 2. Sort by Salary descending
print(df_sort.sort_values(by="Salary", ascending=False))

# 3. Sort by multiple columns
print(df_sort.sort_values(by=["Department", "Salary"], ascending=[True, False]))

# 4. Filter rows where Salary > 45000
print(df_sort[df_sort["Salary"] > 45000])

# 5. Filter by multiple conditions
print(df_sort[(df_sort["Salary"] > 42000) & (df_sort["Department"] == "IT")])

# 6. Filter rows using query()
print(df_sort.query("Age > 25 and Department == 'IT'"))

# 7. isin() filter
print(df_sort[df_sort["Department"].isin(["IT", "HR"])])

# 8. Between() function
print(df_sort[df_sort["Age"].between(22, 28)])

# 9. Drop rows based on condition
df_sort = df_sort[df_sort["Salary"] >= 42000]
print(df_sort)

# 10. Reset index after filtering
df_sort.reset_index(drop=True, inplace=True)
print(df_sort)