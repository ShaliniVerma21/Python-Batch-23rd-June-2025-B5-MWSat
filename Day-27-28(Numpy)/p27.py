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
