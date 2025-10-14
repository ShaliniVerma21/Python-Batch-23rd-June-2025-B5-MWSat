# Topic: Work with MySQL, Excel, JSON, and CSV files in Python
# Real-time Examples: Employee Management, Product Data, Orders Data

# ------------------------------------------------
# 1️⃣ MYSQL DATABASE OPERATIONS
# ------------------------------------------------
# Required Library: mysql-connector-python
# pip install mysql-connector-python

import mysql.connector
import pandas as pd
import json
import csv

# ========== Example 1: Employee Management System ==========
# Connect to MySQL and perform CRUD operations
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Shaliniv532",
        password="Shaliniv532@",
        database="company_db"
    )
    cursor = conn.cursor()

    # Create Employee table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(50),
        salary FLOAT
    )
    """)

    # Insert Data
    cursor.execute("INSERT INTO employees(name, department, salary) VALUES(%s,%s,%s)", ("Shalini", "IT", 70000))
    cursor.execute("INSERT INTO employees(name, department, salary) VALUES(%s,%s,%s)", ("Sharad", "HR", 60000))
    conn.commit()

    # Fetch Data
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print("Employee:", row)
except Exception as e:
    print("Error:", e)
finally:
    conn.close()

# ========== Example 2: Product Data Management ==========
# Store and retrieve product catalog from MySQL
try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="your_password", 
        database="store_db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        category VARCHAR(50),
        price FLOAT
    )
    """)

    cursor.execute("INSERT INTO products(name, category, price) VALUES(%s,%s,%s)", ("Laptop", "Electronics", 55000))
    cursor.execute("INSERT INTO products(name, category, price) VALUES(%s,%s,%s)", ("Mouse", "Accessories", 500))
    conn.commit()

    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print("Product:", row)
except Exception as e:
    print("Error:", e)
finally:
    conn.close()

# ========== Example 3: Orders Database ==========
# Save and read customer order details
try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="your_password", 
        database="sales_db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(50),
        product VARCHAR(50),
        quantity INT,
        total_price FLOAT
    )
    """)

    cursor.execute("INSERT INTO orders(customer_name, product, quantity, total_price) VALUES(%s,%s,%s,%s)",
                   ("Rahul", "Laptop", 1, 55000))
    cursor.execute("INSERT INTO orders(customer_name, product, quantity, total_price) VALUES(%s,%s,%s,%s)",
                   ("Trisha", "Mouse", 2, 1000))
    conn.commit()

    cursor.execute("SELECT * FROM orders")
    for row in cursor.fetchall():
        print("Order:", row)
except Exception as e:
    print("Error:", e)
finally:
    conn.close()


# ------------------------------------------------
# 2️⃣ EXCEL FILE OPERATIONS
# ------------------------------------------------
# Required Library: pandas, openpyxl
# pip install pandas openpyxl

# ========== Example 1: Employee Report ==========
employee_data = {'Name': ['Shalini', 'Sharad'], 'Department': ['IT', 'HR'], 'Salary': [70000, 60000]}
df_emp = pd.DataFrame(employee_data)
df_emp.to_excel("employee_report.xlsx", index=False)
print("\nEmployee Excel file created successfully!")

# ========== Example 2: Product Price List ==========
product_data = {'Product': ['Laptop', 'Mouse', 'Keyboard'], 'Category': ['Electronics', 'Accessories', 'Accessories'],
                'Price': [55000, 500, 1500]}
df_prod = pd.DataFrame(product_data)
df_prod.to_excel("product_list.xlsx", index=False)
print("Product Excel file created successfully!")

# ========== Example 3: Orders Report ==========
order_data = {'Customer': ['Rahul', 'Trisha'], 'Product': ['Laptop', 'Mouse'], 'Quantity': [1, 2], 'Total': [55000, 1000]}
df_order = pd.DataFrame(order_data)
df_order.to_excel("order_report.xlsx", index=False)
print("Order Excel file created successfully!")


# ------------------------------------------------
# 3️⃣ JSON FILE OPERATIONS
# ------------------------------------------------
# Required Library: json (built-in)

# ========== Example 1: Employee Data (JSON) ==========
employee_json = {
    "employees": [
        {"name": "Shalini", "role": "Trainer", "salary": 70000},
        {"name": "Sharad", "role": "Manager", "salary": 80000}
    ]
}
with open("employees.json", "w") as f:
    json.dump(employee_json, f, indent=4)
print("\nEmployee JSON file saved!")

# ========== Example 2: Product Catalog (JSON) ==========
product_json = {
    "products": [
        {"product": "Laptop", "price": 55000, "stock": 15},
        {"product": "Mouse", "price": 500, "stock": 100}
    ]
}
with open("products.json", "w") as f:
    json.dump(product_json, f, indent=4)
print("Product JSON file saved!")

# ========== Example 3: Orders Record (JSON) ==========
orders_json = {
    "orders": [
        {"customer": "Rahul", "product": "Laptop", "quantity": 1, "total": 55000},
        {"customer": "Trisha", "product": "Mouse", "quantity": 2, "total": 1000}
    ]
}
with open("orders.json", "w") as f:
    json.dump(orders_json, f, indent=4)
print("Orders JSON file saved!")


# ------------------------------------------------
# 4️⃣ CSV FILE OPERATIONS
# ------------------------------------------------
# Required Library: csv (built-in), pandas (for analysis)

# ========== Example 1: Employee CSV ==========
employee_csv = [["Name", "Department", "Salary"],
                ["Shalini", "IT", 70000],
                ["Sharad", "HR", 60000]]
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employee_csv)
print("\nEmployee CSV created!")

# ========== Example 2: Product CSV ==========
product_csv = [["Product", "Category", "Price"],
               ["Laptop", "Electronics", 55000],
               ["Mouse", "Accessories", 500]]
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(product_csv)
print("Product CSV created!")

# ========== Example 3: Orders CSV ==========
orders_csv = [["Customer", "Product", "Quantity", "Total"],
              ["Rahul", "Laptop", 1, 55000],
              ["Trisha", "Mouse", 2, 1000]]
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(orders_csv)
print("Orders CSV created!")

# ------------------------------------------------
# END OF FILE
# ------------------------------------------------
# Summary:
# ✅ MySQL → Structured relational storage
# ✅ Excel → Business analysis and reporting
# ✅ JSON → Web APIs and configs
# ✅ CSV → Lightweight tabular data exchange
# ------------------------------------------------
