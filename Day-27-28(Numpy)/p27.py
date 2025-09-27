"""
Introduction to Jupyter Notebook : 

1. What is Jupyter Notebook?

- Open-source web-based IDE for Python and data analysis.
- Stands for Julia, Python, R.
   Jupyter = JUlia + PYThon + R (supports multiple languages).
- Used in Data Science, AI, ML, Research and data visualization.
- File extension = .ipynb (IPython Notebook).


2. Why use it?

- Interactive: mix of code + output + explanation + visualization in one place.
- Great for experimentation, documentation, and collaboration.

3. Real-world use cases:

- Data analysis at Netflix, Google, Kaggle competitions.
- Academic research papers.
- Prototyping ML models.

4. Installation & Setup, Working of Jupyter Notebook

- Install Anaconda Distribution (recommended).
- Easy package & environment management.
- Alternative: pip install notebook or pip install jupyterlab.
- Run using Anaconda Navigator or command:
jupyter notebook

- Opens in browser → .ipynb files.
Cells:
   - Code Cell → Write & run Python code.
   - Markdown Cell → Add text, headings, equations.

5. Understanding the Interface

- Dashboard: File browser.
- Notebook Structure:
             Cells → Code cells, Markdown cells, Raw cells.
             Kernel → Executes code.
- Toolbar & Menus:
      Run, stop, restart kernel.
- Save notebook (.ipynb extension).

- Working with Cells
- Code Cell:
print('Hello, Python in Jupyter!')

- Markdown Cell:
Headings: # Heading 1, ## Heading 2.
Formatting: bold, italic, inline code.
Lists, tables, links, LaTeX equations ($a^2+b^2=c^2$).

- Keyboard Shortcuts:
Shift + Enter → Run cell.
A / B → Insert cell above/below.
D + D → Delete cell.

“Jupyter is not just a coding tool — 
it’s your lab notebook for ideas, experiments, and discoveries. 
Master it, and you’ll master the art of presenting data professionally.”
"""
def greet(name):
    return f"Hello, {name}!"
greet("Shalini")



"""
===================================================
    Modules vs Packages vs Libraries in Python
===================================================

1. Module:
   - A single Python file (.py) containing functions, classes, or variables.
   - Helps in reusing code across programs.
   - Example: math, random (built-in modules).
   
2. Package:
   - A collection of modules organized in a directory.
   - Contains an __init__.py file (can be empty).
   - Allows hierarchical structuring of Python code.
   - Example: numpy.linalg (linalg is a sub-package inside numpy).

3. Library:
   - A collection of packages and modules that provide wide functionality.
   - Often maintained by the community for specific purposes.
   - Example: NumPy, Pandas, TensorFlow, Scikit-learn.
   
Hierarchy:
    Library > Package > Module
"""

# -------------------------------
# 1. Example of a Module
# -------------------------------

import math   # math is a built-in Python module

print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))


# -------------------------------
# 2. Example of a Package
# -------------------------------
# NumPy is a library, and inside it we have sub-packages like numpy.linalg

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# Using a sub-package (numpy.linalg)
from numpy import linalg

matrix = np.array([[1, 2], [3, 4]])
print("Determinant of matrix:", linalg.det(matrix))


# -------------------------------
# 3. Example of a Library
# -------------------------------
# Pandas is a full library containing multiple modules & sub-packages

import pandas as pd

data = {"Name": ["Shalini", "Rahul", "Kavita"], "Age": [28, 30, 25]}
df = pd.DataFrame(data)
print("\nDataFrame from Pandas Library:\n", df)


"""
Data Via CSV using numpy

1. Introduction
CSV (Comma Separated Values) is a common format to store tabular data.
NumPy provides efficient ways to read, write, and manipulate CSV files.

Main functions:
- numpy.loadtxt() → Reads simple CSV files.
- numpy.genfromtxt() → Reads CSV with missing values / advanced handling.
- numpy.savetxt() → Saves NumPy arrays into CSV.


2. Steps to Work with CSV using NumPy
- Prepare a CSV file (like students.csv).
- Load data into NumPy arrays (loadtxt, genfromtxt).
- Perform operations (sum, mean, filter, etc.).
- Save processed data back into a CSV.

3. Sample CSV File (students.csv)
ID,Name,Math,Science,English
1,Amit,78,85,82
2,Neha,92,88,95
3,Rahul,67,72,70
4,Anjali,85,79,90
5,Rohan,58,60,65


Note- 
- Use loadtxt() for numeric-only CSV.
- Use genfromtxt() for mixed data (string + numbers).
- Perform operations using NumPy functions (sum, mean, max, min).
- Save back to CSV using savetxt().
"""

"""
Programs: Load, Analyze, and Save CSV Data
"""

import numpy as np
import os

# ------------------------------------------------------------------
# Utility: Get current script directory (so code works anywhere)
# ------------------------------------------------------------------
base_path = os.path.dirname(__file__)  
csv_file = os.path.join(base_path, "students.csv")  # CSV input file
output_file = os.path.join(base_path, "results.csv")  # CSV output file

# ------------------------------------------------------------------
# Program 1: Load CSV (Only Numeric Columns) using loadtxt
# ------------------------------------------------------------------
# - skip header row
# - select columns: Math (2), Science (3), English (4)
# ------------------------------------------------------------------
data = np.loadtxt(csv_file, delimiter=",", skiprows=1, usecols=(2, 3, 4))
print("\n--- Program 1: Load CSV (Numeric Only) ---")
print("Data from CSV:\n", data)
print("Shape of data (rows, columns):", data.shape)  # Extra functionality

# ------------------------------------------------------------------
# Program 2: Load CSV with Mixed Data using genfromtxt
# ------------------------------------------------------------------
# - Reads both strings and numbers
# - Keeps header row as column names
# ------------------------------------------------------------------
data_mixed = np.genfromtxt(csv_file, delimiter=",", dtype=None, encoding="utf-8", names=True)

print("\n--- Program 2: Load CSV with Mixed Data ---")
print("CSV Data with column names:")
print(data_mixed)
print("Student Names:", data_mixed['Name'])
print("Math Marks:", data_mixed['Math'])
print("All column names:", data_mixed.dtype.names)  # Extra functionality

# ------------------------------------------------------------------
# Program 3: Basic Statistics from CSV Data
# ------------------------------------------------------------------
marks = np.loadtxt(csv_file, delimiter=",", skiprows=1, usecols=(2, 3, 4))

print("\n--- Program 3: Statistics ---")
print("Average per subject [Math, Science, English]:", np.mean(marks, axis=0))
print("Highest in Math:", np.max(marks[:, 0]))
print("Highest in Science:", np.max(marks[:, 1]))
print("Highest in English:", np.max(marks[:, 2]))
print("Lowest in Math:", np.min(marks[:, 0]))
print("Lowest in Science:", np.min(marks[:, 1]))
print("Lowest in English:", np.min(marks[:, 2]))
print("Overall Class Average (all subjects):", np.mean(marks))  # Extra functionality

# ------------------------------------------------------------------
# Program 4: Save Processed Data into New CSV
# ------------------------------------------------------------------
# - Calculate total & average marks for each student
# - Save results into 'results.csv'
# ------------------------------------------------------------------
total = np.sum(marks, axis=1)       # Total per student
average = np.mean(marks, axis=1)    # Average per student

# Combine: Math, Science, English, Total, Average
result = np.column_stack((marks, total, average))

# Save into CSV file
np.savetxt(
output_file,
result,
delimiter=",",
header="Math,Science,English,Total,Average",
comments='',
fmt='%0.2f'
)

print("\n--- Program 4: Save Results ---")
print(f"Results saved successfully to {output_file}")
