"""
========================================
      NumPy in Data Analysis
========================================

Introduction
- NumPy stands for "Numerical Python".
- It is the core Python library for numerical and scientific computing.
- Provides powerful N-dimensional arrays and mathematical functions.
- Faster and more memory-efficient than Python lists.
- Widely used in:
  * Data Analysis
  * Machine Learning
  * Artificial Intelligence
  * Image Processing
  * Statistics and Finance
  
  How to use:
- Install NumPy if you don't have it: pip install numpy
"""
#1.Importing NumPy:
import numpy as np

#2.Print NumPy version:
print(np.__version__)

# Helper printing function to keep output readable
def hr():
    print('\n' + '='*80 + '\n')

def section_header(title):
    hr()
    print(f"### {title} ###\n")

section_header("Hello")

#3. Create a basic 1D array:
arr = np.array([1,2,3])
print(arr)

#4.Check type:
print(type(arr))

#5.Check array shape:
print(arr.shape)

#6.Create 2D array:
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)

#7.Check dimensions:
print(matrix.ndim)

#8.Create 3D array:
arr3d = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr3d)

#9.Print data type:
print(arr3d.dtype)

#10.Convert list to array with float:
arr_float = np.array([1,2,3], dtype=float)
print(arr_float)

"""
List vs Array
- Python Lists:
  * Can store multiple data types (int, float, string, etc.)
  * Slower for large computations
  * Require loops for element-wise operations

- NumPy Arrays:
  * Store elements of the same data type
  * More efficient and faster (implemented in C)
  * Support vectorized operations (no loops needed)
  * Use less memory compared to lists

"""

#Example:
# Example 1: Multiply each element by 2
lst = [1, 2, 3, 4]
print("List multiplied by 2:", [x*2 for x in lst])
import numpy as np
arr = np.array([1, 2, 3, 4])
print("NumPy array multiplied by 2:", arr * 2)

# Example 2: Add 5 to each element
lst2 = [10, 20, 30]
print("List add 5:", [x + 5 for x in lst2])
arr2 = np.array([10, 20, 30])
print("NumPy array add 5:", arr2 + 5)

# Example 3: Square each element
lst3 = [2, 3, 4]
print("List squared:", [x**2 for x in lst3])
arr3 = np.array([2, 3, 4])
print("NumPy array squared:", arr3**2)

# Example 4: Sum of all elements
lst4 = [1, 2, 3, 4, 5]
print("Sum using list:", sum(lst4))
arr4 = np.array([1, 2, 3, 4, 5])
print("Sum using NumPy array:", arr4.sum())

# Example 5: Multiply two sequences element-wise
lst5_a = [1, 2, 3]
lst5_b = [4, 5, 6]
print("List element-wise multiplication:", [x*y for x,y in zip(lst5_a, lst5_b)])
arr5_a = np.array([1, 2, 3])
arr5_b = np.array([4, 5, 6])
print("NumPy array element-wise multiplication:", arr5_a * arr5_b)


"""
 Some Common Methods in NumPy
 
- Array Creation: 
  NumPy arrays allow efficient element access and manipulation without using loops.
  Arrays are homogeneous, vectorized, and memory-efficient.  
    np.array([1, 2, 3, 4])
    np.zeros((3,3))     → 3x3 matrix of zeros
    np.ones((2,4))      → 2x4 matrix of ones
    np.arange(1,10,2)   → [1, 3, 5, 7, 9]
    np.linspace(0,1,5)  → [0. ,0.25,0.5,0.75,1.]
"""
import numpy as np

# Example 1: Convert list to array
arr1 = np.array([1, 2, 3, 4])
print("Array from list:", arr1)

# Example 2: Create 3x3 zero matrix
arr2 = np.zeros((3,3))
print("3x3 Zeros:\n", arr2)

# Example 3: Create 2x4 ones matrix
arr3 = np.ones((2,4))
print("2x4 Ones:\n", arr3)

# Example 4: Create sequence using arange
arr4 = np.arange(1, 10, 2)
print("Arange 1 to 9 step 2:", arr4)

# Example 5: Create linearly spaced array
arr5 = np.linspace(0, 1, 5)
print("Linspace 0 to 1, 5 numbers:", arr5)

# Example 6: Create empty array
arr6 = np.empty((2,3))
print("Empty 2x3 array:\n", arr6)

# Example 7: Create identity matrix
arr7 = np.eye(3)
print("3x3 Identity matrix:\n", arr7)

# Example 8: Create full array with specific value
arr8 = np.full((2,3), 7)
print("2x3 Full array with 7:\n", arr8)

# Example 9: Random integers array
arr9 = np.random.randint(1, 10, (2,4))
print("Random 2x4 integers:\n", arr9)

# Example 10: Random float array between 0 and 1
arr10 = np.random.rand(3,3)
print("Random 3x3 float array:\n", arr10)


""" 
- Attributes:
  Array attributes describe structure, size, and data type.
    arr.shape    → Dimensions of array
    arr.ndim     → Number of dimensions
    arr.size     → Total number of elements
    arr.dtype    → Data type of array elements
"""

arr = np.arange(12).reshape(3,4)

# Example 1: Shape of array
print("Shape:", arr.shape)

# Example 2: Number of dimensions
print("Dimensions:", arr.ndim)

# Example 3: Total number of elements
print("Total elements:", arr.size)

# Example 4: Data type of elements
arr_float = np.array([1.5, 2.5, 3.5])
print("Data type:", arr_float.dtype)

# Example 5: Bytes per element
print("Bytes per element:", arr_float.itemsize)

# Example 6: Total bytes used
print("Total bytes:", arr_float.nbytes)

# Example 7: Type of array object
print("Type of array object:", type(arr))

# Example 8: Check if array is writeable
print("Is array writeable:", arr.flags.writeable)

# Example 9: Check array memory layout
print("Is array C-contiguous:", arr.flags.c_contiguous)

# Example 10: Copy vs view
arr_view = arr.view()
arr_copy = arr.copy()
print("Original array:\n", arr)
print("View (shares data):\n", arr_view)
print("Copy (independent):\n", arr_copy)


""" 
- Mathematical Functions:
    np.sum(arr)     → Sum of all elements
    np.mean(arr)    → Mean value
    np.sqrt(arr)    → Square root
    np.max(arr)     → Maximum value
    np.min(arr)     → Minimum value
"""
arr = np.array([1, 4, 9, 16, 25])

# Example 1: Sum
print("Sum:", np.sum(arr))

# Example 2: Mean
print("Mean:", np.mean(arr))

# Example 3: Square root
print("Square root:", np.sqrt(arr))

# Example 4: Maximum
print("Maximum:", np.max(arr))

# Example 5: Minimum
print("Minimum:", np.min(arr))

# Example 6: Standard deviation
print("Standard deviation:", np.std(arr))

# Example 7: Cumulative sum
print("Cumulative sum:", np.cumsum(arr))

# Example 8: Cumulative product
print("Cumulative product:", np.cumprod(arr))

# Example 9: Element-wise exponential
print("Exponential:", np.exp(arr))

# Example 10: Natural logarithm
print("Natural log:", np.log(arr))

""" 
- Reshaping:
    arr.reshape(3,3) → Reshape into 3x3 matrix
"""
# Original array
arr = np.arange(12)
print("Original array:", arr)

# Example 1: Reshape to 3x4
arr1 = arr.reshape(3,4)
print("Reshape 3x4:\n", arr1)

# Example 2: Reshape to 2x6
arr2 = arr.reshape(2,6)
print("Reshape 2x6:\n", arr2)

# Example 3: Reshape with -1 (auto)
arr3 = arr.reshape(4,-1)
print("Reshape 4x-1:\n", arr3)

# Example 4: Flatten
arr_flat = arr1.flatten()
print("Flattened array:", arr_flat)

# Example 5: Transpose
arr_T = arr1.T
print("Transposed array:\n", arr_T)

# Example 6: Resize array (in-place)
arr_resize = arr.copy()
arr_resize.resize((6,2))
print("Resized array 6x2:\n", arr_resize)

# Example 7: Ravel (flatten without copy)
print("Ravel array:", arr1.ravel())

# Example 8: Swap axes
arr_swap = arr1.swapaxes(0,1)
print("Swap axes 0 and 1:\n", arr_swap)

# Example 9: Expand dimensions
arr_exp = np.expand_dims(arr1, axis=0)
print("Expand dims axis 0:", arr_exp.shape)

# Example 10: Squeeze (remove single-dim axes)
arr_sq = np.squeeze(arr_exp)
print("Squeezed array shape:", arr_sq.shape)


""" 
- Indexing & Slicing:
    arr[0]      → First element
    arr[-1]     → Last element
    arr[1:4]    → Elements from index 1 to 3
    matrix[:,1] → All rows, second column
"""
# 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
matrix = np.arange(1,10).reshape(3,3)
print(matrix)

# Example 1: First element
print("First element:", arr[0])

# Example 2: Last element
print("Last element:", arr[-1])

# Example 3: Slice elements 1 to 3
print("Slice 1:4:", arr[1:4])

# Example 4: Slice with step
print("Slice 0:5:2:", arr[0:5:2])

# Example 5: Reverse array
print("Reversed array:", arr[::-1])

# Example 6: 2D array element
print("Element at (1,2):", matrix[1,2])

# Example 7: All rows, second column
print("Second column:", matrix[:,1])

# Example 8: First row, all columns
print("First row:", matrix[0,:])

# Example 9: Boolean indexing (elements > 5)
print("Elements > 5:", matrix[matrix > 5])

# Example 10: Fancy indexing (select rows 0 and 2)
print("Select row 0 and 2:\n", matrix[[0,2],:])

""" 
Why NumPy is Essential?

1. Efficient Numerical Computations:
NumPy arrays are faster and more memory-efficient than Python lists because they are implemented 
in C and support vectorized operations.

2. Powerful Array Operations:
- NumPy allows operations on entire arrays without explicit loops (vectorization).
- Supports mathematical, statistical, and linear algebra operations directly on arrays.

3. Built-in Methods for Fast Computation:
NumPy provides a wide variety of methods and functions for:
    - Array creation (arange, zeros, ones, linspace)
    - Mathematical computations (sum, mean, sqrt, max, min)
    - Reshaping and indexing (reshape, flatten, slicing, fancy indexing)
    - Random number generation (rand, randint)
    - Linear algebra (dot, transpose, inv)

4. Data Analysis and Machine Learning:
NumPy arrays are the foundation of libraries like Pandas, SciPy, scikit-learn, 
TensorFlow, and PyTorch, making it indispensable for data analysis, AI, ML, and scientific computing.
"""
