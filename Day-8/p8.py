#----------------------------------------------Set---------------------------------------
"""
What is a Set?
--> A Set is an unordered, unindexed collection of unique elements.
--> It removes duplicates automatically.
--> It is mutable, meaning you can add or remove elements after creation.
--> Elements inside a set must be immutable (e.g., numbers, strings, tuples).
--> Sets are defined using:
    - Curly braces: { }
    - set() constructor
--> Sets support mathematical operations like:
    - Union
    - Intersection
    - Difference
    - Symmetric Difference
"""

#----------------------------------------------
# Defining a Set
#----------------------------------------------

# Example 1: Define a set using curly braces
my_set = {1, 2, 3}
print("Example 1:", my_set)

# Example 2: Create a set from a list using set() constructor
numbers = set([1, 2, 3, 4])
print("Example 2:", numbers)

# Example 3: Duplicates are removed automatically
sample = {1, 2, 2, 3, 4, 4}
print("Example 3 (no duplicates):", sample)  # Output: {1, 2, 3, 4}

# Example 4: Set with multiple datatypes (all immutable)
mix = {10, "apple", 3.14}
print("Example 4 (mixed types):", mix)

# Example 5: Creating an empty set
empty = set()  # {} creates an empty dictionary, not a set
print("Example 5 (empty set):", type(empty))  # <class 'set'>


#----------------------------------------------
# Creating a Set Dynamically
#----------------------------------------------

# Example 1: Create a set from a string (characters only, duplicates removed)
chars = set("hello")
print("Dynamic Example 1:", chars)

# Example 2: Create a set from a list with duplicates
list_set = set(["apple", "banana", "apple"])
print("Dynamic Example 2 (from list):", list_set)

# Example 3: Create a set from a tuple
tuple_set = set((1, 2, 3, 2))
print("Dynamic Example 3 (from tuple):", tuple_set)

# Example 4: Create a set using range()
range_set = set(range(5))
print("Dynamic Example 4 (range):", range_set)

# Example 5: Create a set from user input
items = input("Enter items separated by space: ").split()
user_set = set(items)
print("Dynamic Example 5 (user input):", user_set)

#----------------------------------------------
# Set Methods
#----------------------------------------------

fruits = {"apple", "banana", "cherry"}

# Example 1: add() – Adds a new element
fruits.add("orange")
print("After add():", fruits)

# Example 2: remove() – Removes element, raises error if element not found
fruits.remove("banana")
print("After remove():", fruits)

# Example 3: discard() – Removes element, no error if element not found
fruits.discard("grape")  # No error even if "grape" doesn't exist
print("After discard():", fruits)

# Example 4: pop() – Removes and returns a random element
removed_item = fruits.pop()
print("Removed by pop():", removed_item)
print("After pop():", fruits)

# Example 5: clear() – Removes all elements from the set
fruits.clear()
print("After clear():", fruits)  # Output: set()

#----------------------------------------------

# Set Operations

"""
Set Operations:
--> Python sets support mathematical operations similar to those in set theory.
--> These operations are useful when working with collections of unique items.
--> Sets automatically remove duplicates.
--> Main operations include:
    1. Union
    2. Intersection
    3. Difference
    4. Symmetric Difference
    5. Membership Test
"""
#----------------------------------------------

""" 
1. Union (| or .union()):
Combines all elements from both sets. Duplicate values are removed.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Find union using the | operator
union_result = set1 | set2

# Using | operator
print("Union using | :", union_result)

# Using union() method
print("Union using union():", set1.union(set2))


""" 
2. Intersection (& or .intersection()):
Returns only the elements that are common in both sets.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find union using the & operator
intersection_result = set1 & set2

# Using & operator
print("Intersection using & :", intersection_result)

# Using intersection() method
print("Intersection using intersection():", set1.intersection(set2))

""" 
3. Difference (- or .difference()):
Returns elements present in the first set only, not in the second.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# Find union using the - operator
difference_result = set1 - set2

# Using - operator
print("Difference (set1 - set2):", difference_result)

# Using difference() method
print("Difference using difference():", set1.difference(set2))

""" 
4. Symmetric Difference (^ or .symmetric_difference()):
Returns elements that are in either set, but not in both.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Find union using the ^ operator
symmetric_difference_result = set1 ^ set2

# Using ^ operator
print("Symmetric Difference using ^ :", symmetric_difference_result)

# Using symmetric_difference() method
print("Symmetric Difference using method:", set1.symmetric_difference(set2))


""" 
 5. Membership Test (in, not in):
Checks if a particular item exists in a set.
"""

my_set = {"apple", "banana", "cherry"}

# Check if an item exists
print("banana" in my_set)   # True
print("grape" not in my_set)  # True


#Finding common students in two courses
course_A = {"Alice", "Bob", "Charlie"}
course_B = {"Charlie", "David", "Eve"}

# Students in both courses
common_students = course_A & course_B
print("Common Students:", common_students)

# Students only in A
only_A = course_A - course_B
print("Only in Course A:", only_A)

# All unique students
all_students = course_A | course_B
print("All Students:", all_students)


"""
Real-World Data Analysis Example Using set-->

Scenario: Email List Cleaning & Analysis for a Marketing Campaign
Suppose you are a data analyst working on cleaning and analyzing customer email data for a company’s marketing team.

Objectives:

1. Remove duplicate emails
2. Find customers who subscribed but never purchased
3. Find loyal customers (common in both lists)
4. Count unique users
5. Merge both lists without duplication

"""

# Raw Data with duplicates
subscribed_emails = [
    "alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com",
    "alice@gmail.com", "david@gmail.com", "bob@yahoo.com"
]

purchased_emails = [
    "charlie@gmail.com", "eve@gmail.com", "frank@yahoo.com",
    "charlie@gmail.com", "bob@yahoo.com"
]


# Step-by-Step Analysis Using Sets:

# Step 1: Convert lists to sets to remove duplicates

subscribed_set = set(subscribed_emails)
purchased_set = set(purchased_emails)

print("Unique Subscribed Users:", subscribed_set)
print("Unique Purchased Users:", purchased_set)

#Step 2: Find users who subscribed but never purchased

# Users who subscribed but didn't buy anything
only_subscribed = subscribed_set - purchased_set
print("Subscribed but Never Purchased:", only_subscribed)

# Step 3: Find loyal users (subscribed AND purchased)

# Common users in both lists
loyal_users = subscribed_set & purchased_set
print("Loyal Customers:", loyal_users)

#Step 4: Merge both sets to find total unique users

# All unique email addresses
total_unique_users = subscribed_set | purchased_set
print("Total Unique Users:", total_unique_users)
print("Total Count:", len(total_unique_users))

# Step 5: Find customers who only purchased without subscribing

# Users who purchased but were never in the subscribed list
only_purchased = purchased_set - subscribed_set
print("Purchased without Subscribing:", only_purchased)

