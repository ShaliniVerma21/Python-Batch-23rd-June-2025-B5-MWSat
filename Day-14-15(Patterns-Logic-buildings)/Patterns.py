"""
In Python, patterns are often created using nested loops:

1. Outer loop controls rows.
2. Inner loop controls columns/elements in a row.
3. print() is used with end='' to control spacing and avoid newline.
4. print() → Moves to the next line after each row.

There are multiple types such as:

1. Number Patterns
2. Alphabetical Patterns
3. Special Symbol Patterns
4. Star Patterns
"""

# 1. Number Patterns

# Example 1: Right-Angled Triangle (1 to i)
rows = 5
for i in range(1, rows + 1):      # Outer loop for each row
    for j in range(1, i + 1):     # Inner loop from 1 to current row number
        print(j, end=" ")         # Print numbers from 1 to i
    print()                       # Newline after each row

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Example 2: Inverted Right-Angled Triangle
rows = 5
for i in range(rows, 0, -1):      # Outer loop decreasing from rows to 1
    for j in range(1, i + 1):     # Inner loop from 1 to i
        print(j, end=" ")          # Print numbers from 1 to i
    print()                       # Newline after each row

# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Example 3: Left-Aligned Right-Angled Triangle
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Print spaces for left alignment
    for j in range(1, i + 1):
        print(j, end=" ")             # Print numbers from 1 to i
    print()                           # Newline after each row

# Output:
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# Example 4: Square Number Pattern
rows = 5
for i in range(1, rows + 1):         # Rows from 1 to 5
    for j in range(1, rows + 1):     # Columns also from 1 to 5
        print(j, end=" ")             # Print numbers from 1 to 5
    print()                           # Newline after each row

# Output:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# Example 5: Rectangle Pattern (4x6)
for i in range(4):                   # 4 rows
    for j in range(1, 7):            # 6 columns
        print(j, end=" ")             # Print numbers from 1 to 6
    print()                           # Newline after each row

# Output:
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6

# Example 6: Pyramid Number Pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Padding for centering
    for j in range(1, i + 1):
        print(j, end=" ")             # Print numbers from 1 to i
    print()                           # Newline after each row

# Output:
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# Example 7: Diamond Number Pattern
rows = 4
# Top Half
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Leading spaces for centering
    for j in range(1, i + 1):
        print(j, end=" ")             # Print numbers from 1 to i
    print()                           # Newline after each row
# Bottom Half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")  # Leading spaces for centering
    for j in range(1, i + 1):
        print(j, end=" ")             # Print numbers from 1 to i
    print()                           # Newline after each row

# Output:
#    1
#   1 2
#  1 2 3
# 1 2 3 4
#  1 2 3
#   1 2
#    1

# Example 8: Hollow Square Numbers
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == rows or j == 1 or j == rows:
            print(j, end=" ")           # Print border numbers
        else:
            print(" ", end=" ")         # Print hollow space
    print()                           # Newline after each row

# Output:
# 1 2 3 4 5
# 1       5
# 1       5
# 1       5
# 1 2 3 4 5

# Example 9: Pascal Triangle
rows = 5
for i in range(rows):
    num = 1
    print(" " * (rows - i), end="")  # Padding for centering
    for k in range(i + 1):
        print(num, end=" ")            # Print current number
        num = num * (i - k) // (k + 1)  # Binomial coefficient formula
    print()                           # Newline after each row

# Output:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Example 10: Floyd’s Triangle
rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")            # Print current number
        num += 1                       # Increment number
    print()                           # Newline after each row

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# 2. Alphabetical Patterns

# Example 1: Right-Angled Triangle (A to ith letter)
rows = 5
for i in range(1, rows + 1):        # Outer loop for each row
    for j in range(i):              # Inner loop for characters in a row
        print(chr(65 + j), end=" ") # Convert number to character (A = 65)
    print()                         # Newline after each row
    
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E

# Example 2: Inverted Right-Angled Triangle
rows = 5
for i in range(rows, 0, -1):        # Outer loop for decreasing rows
    for j in range(i):              # Inner loop for characters in a row
        print(chr(65 + j), end=" ") # Convert number to character (A = 65)
    print()                         # Newline after each row

# Output:
# A B C D E
# A B C D
# A B C
# A B
# A

# Example 3: Left-Aligned Right-Angled Triangle
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")   # Spaces for left alignment
    for j in range(i):
        print(chr(65 + j), end=" ")    # Convert number to character (A = 65)
    print()                           # Newline after each row

# Output:
#     A
#    A B
#   A B C
#  A B C D
# A B C D E

# Example 4: Square Alphabet Pattern
rows = 5
for i in range(rows):
    for j in range(rows):
        print(chr(65 + j), end=" ")   # Print A to E in every row
    print()                           # Newline after each row

# Output:
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# Example 5: Rectangle Pattern (4x6)
for i in range(4):                   # 4 rows
    for j in range(6):              # 6 columns
        print(chr(65 + j), end=" ")  # Print A to F in every row
    print()                           # Newline after each row

# Output:
# A B C D E F
# A B C D E F
# A B C D E F
# A B C D E F

# Example 6: Alphabet Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")     # Centering
    for j in range(i):
        print(chr(65 + j), end=" ")      # Convert number to character (A = 65)
    print()                           # Newline after each row

# Output:
#     A
#    A B
#   A B C
#  A B C D
# A B C D E

# Example 7: Diamond Alphabet Pattern
rows = 4
# Top Half
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Leading spaces for centering
    for j in range(i):
        print(chr(65 + j), end=" ")   # Convert number to character (A = 65)
    print()                           # Newline after each row
# Bottom Half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")  # Leading spaces for centering
    for j in range(i):
        print(chr(65 + j), end=" ")   # Convert number to character (A = 65)
    print()                           # Newline after each row

# Output:
#    A
#   A B
#  A B C
# A B C D
#  A B C
#   A B
#    A

# Example 8: Hollow Square Alphabet Pattern
rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print(chr(65 + j), end=" ")  # Print borders only
        else:
            print(" ", end=" ")          # Print hollow space
    print()                           # Newline after each row

# Output:
# A B C D E
# A       E
# A       E
# A       E
# A B C D E

# Example 9: Repeated Character Triangle (Same Letter per Row)
rows = 5
for i in range(rows):
    ch = chr(65 + i)                  # Current character (A, B, C, ...)
    for j in range(i + 1):
        print(ch, end=" ")            # Print the same character
    print()                           # Newline after each row

# Output:
# A
# B B
# C C C
# D D D D
# E E E E E

# Example 10: Alphabet Floyd's Triangle
rows = 5
ch = 65  # ASCII of A
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end=" ")        # Print current character
        ch += 1                       # Increment character
    print()                           # Newline after each row
    
# Output:
# A
# B C
# D E F
# G H I J
# K L M N O

# 3. Special Symbol Patterns

# Example 1: Right-Angled Star Triangle
rows = 5
for i in range(1, rows + 1):      # Outer loop for rows
    for j in range(i):            # Inner loop for columns
        print("$", end=" ")       # Print symbol with space
    print()                       # Move to next line

# Output:
# $ 
# $ $ 
# $ $ $ 
# $ $ $ $ 
# $ $ $ $ $ 

# Example 2: Inverted @ Triangle
rows = 5
for i in range(rows, 0, -1):      # Outer loop for decreasing rows
    for j in range(i):            # Inner loop for columns
        print("@", end=" ")        # Print symbol with space
    print()                       # Move to next line

# Output:
# @ @ @ @ @ 
# @ @ @ @ 
# @ @ @ 
# @ @ 
# @ 

# Example 3: Right-Aligned # Triangle
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "# " * i)  # Print spaces and symbols

# Output:
#     # 
#    # # 
#   # # # 
#  # # # # 
# # # # # # 

# Example 4: Hollow & Square
rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("&", end=" ")       # Print border symbols
        else:
            print(" ", end=" ")       # Print hollow space
    print()                           # Newline after each row

# Output:
# & & & & & 
# &       & 
# &       & 
# &       & 
# & & & & & 

# Example 5: Left-Aligned Increasing % Triangle
rows = 5
for i in range(1, rows + 1):
    print("% " * i)                 # Print % symbols increasing per row

# Output:
# % 
# % % 
# % % % 
# % % % % 
# % % % % % 

# Example 6: Left-Aligned Decreasing ! Triangle
rows = 5
for i in range(rows, 0, -1):
    print("! " * i)                 # Print ! symbols decreasing per row

# Output:
# ! ! ! ! ! 
# ! ! ! ! 
# ! ! ! 
# ! ! 
# ! 

# Example 7: Pyramid of ^ Symbols
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "^ " * i)  # Print spaces and symbols

# Output:
#     ^ 
#    ^ ^ 
#   ^ ^ ^ 
#  ^ ^ ^ ^ 
# ^ ^ ^ ^ ^ 

# Example 8: Diamond Pattern with +
rows = 5
# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "+ " * i)  # Print spaces and symbols
# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "+ " * i)  # Print spaces and symbols

# Output:
#     + 
#    + + 
#   + + + 
#  + + + + 
# + + + + + 
#  + + + + 
#   + + + 
#    + + 
#     + 

# Example 9: Cross Pattern with ~
rows = 5
for i in range(rows):
    for j in range(rows):
        if i == j or i + j == rows - 1:
            print("~", end=" ")         # Print cross symbols
        else:
            print(" ", end=" ")         # Print hollow space
    print()                           # Newline after each row

# Output:
# ~       ~ 
#   ~   ~   
#     ~     
#   ~   ~   
# ~       ~ 

# Example 10: Hollow Diamond with #
rows = 5
# Upper part
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")           # Print leading spaces
    for k in range(1, 2*i):
        if k == 1 or k == 2*i - 1:
            print("#", end="")        # Print border symbols
        else:
            print(" ", end=" ")       # Print hollow space
    print()                           # Newline after each row
# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")           # Print leading spaces
    for k in range(1, 2*i):
        if k == 1 or k == 2*i - 1:
            print("#", end="")        # Print border symbols
        else:
            print(" ", end=" ")       # Print hollow space
    print()                           # Newline after each row

# Output:
#     #    
#    # #   
#   #   #  
#  #     # 
# #       #
#  #     # 
#   #   #  
#    # #   
#     #    

# 4. Star Patterns

# 1. Right-Angled Triangle (Left-Aligned)
rows = 5
for i in range(1, rows + 1):     # Loop through rows from 1 to 5
    for j in range(i):           # Inner loop to print '*' i times
        print("*", end=" ")       # Print '*' with a space, stay on the same line
    print()                      # Move to the next line after each row

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# 2. Right-Angled Triangle (Right-Aligned)
rows = 5
for i in range(1, rows + 1):     # Loop through rows from 1 to 5
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# 3. Inverted Right-Angled Triangle (Left-Aligned)
rows = 5
for i in range(rows, 0, -1):     # Loop from 5 down to 1
    for j in range(i):            # Inner loop to print '*' i times
        print("*", end=" ")        # Print '*' with a space, stay on the same line
    print()                       # Move to the next line after each row

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# 4. Inverted Right-Angled Triangle (Right-Aligned)
rows = 5
for i in range(rows, 0, -1):     # Loop from 5 down to 1
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# 5. Pyramid Pattern
rows = 5
for i in range(1, rows + 1):     # Loop through rows from 1 to 5
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# 6. Inverted Pyramid
rows = 5
for i in range(rows, 0, -1):     # Loop from 5 down to 1
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# 7. Diamond Pattern
rows = 5
# Top Half
for i in range(1, rows + 1):     # Loop through rows for the top half
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols
# Bottom Half
for i in range(rows - 1, 0, -1):  # Loop through rows for the bottom half
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# 8. Hollow Rectangle
rows = 5
cols = 7
for i in range(1, rows + 1):     # Loop through rows
    for j in range(1, cols + 1): # Loop through columns
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end=" ")    # Print '*' for borders
        else:
            print(" ", end=" ")    # Print space for hollow part
    print()                       # Move to the next line after each row

# Output:
# * * * * * * *
# *           *
# *           *
# *           *
# * * * * * * *

# 9. Hollow Pyramid
rows = 5
for i in range(1, rows + 1):     # Loop through rows
    for j in range(rows - i):    # Print leading spaces
        print(" ", end="")
    for k in range(2 * i - 1):   # Loop to print '*' and spaces
        if k == 0 or k == 2 * i - 2 or i == rows:
            print("*", end="")     # Print '*' for borders
        else:
            print(" ", end=" ")     # Print space for hollow part
    print()                       # Move to the next line after each row

# Output:
#     *
#    * *
#   *   *
#  *     *
# *********

# 10. Hourglass Pattern
rows = 5
# Upper part
for i in range(rows, 0, -1):     # Loop from 5 down to 1 for upper part
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols
# Lower part
for i in range(2, rows + 1):     # Loop from 2 to 5 for lower part
    print(" " * (rows - i) + "* " * i)  # Print leading spaces and '*' symbols

# Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# 100 popular & Intresting Patterns using different logics