# ==========================================================
#        MERGING, JOINING, CONCATENATION
# ==========================================================
"""
Merging, Joining, Concatenation
- pd.concat([df1, df2]) → stack datasets.
- pd.merge(df1, df2, on='key') → SQL-style join.
"""
import pandas as pd
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
print("Merge on Emp_ID")
merged = pd.merge(df1, df2, on="Emp_ID")
print(merged)

# 2. Inner join
print("Inner join")
print(pd.merge(df1, df2, how="inner", on="Emp_ID"))

# 3. Left join
print("Left join")
print(pd.merge(df1, df2, how="left", on="Emp_ID"))

# 4. Right join
print("Right join")
print(pd.merge(df1, df2, how="right", on="Emp_ID"))

# 5. Outer join
print("Outer join")
print(pd.merge(df1, df2, how="outer", on="Emp_ID"))

# 6. Concatenate vertically
print("Concatenate vertically")
print(pd.concat([df1, df1]))

# 7. Concatenate horizontally
print("Concatenate horizontally")
print(pd.concat([df1, df2], axis=1))

# 8. Append new rows
print("Append new rows")
new_row = {"Emp_ID": 4, "Name": "Raj", "Department": "Sales"}
df1 = pd.concat([df1, pd.DataFrame([new_row])])
print(df1)

# 9. Merge with different key names
print("Merge with different key names")
df3 = pd.DataFrame({"Employee_ID": [1, 2, 3], "City": ["Delhi", "Mumbai", "Chennai"]})
print(pd.merge(df1, df3, left_on="Emp_ID", right_on="Employee_ID"))

# 10. Combine using update
print("Combine using update")
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
# Create sample DataFrame
data = {
    "Name": ["Amit", "Ravi", "Neha", "Priya", "Raj", "Simran"],
    "Age": [25, 30, 22, 24, 21, 29],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [40000, 50000, 45000, 48000, 42000, 46000],
    "City": ["Delhi", "Mumbai", "Chennai", "Pune", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)
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