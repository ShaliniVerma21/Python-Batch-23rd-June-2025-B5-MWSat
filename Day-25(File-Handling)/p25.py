"""
===========================================
Python File Handling - Complete Guide
===========================================

Introduction:
-------------
File Handling in Python is a mechanism to work with files stored on your computer.
Files are used to store data permanently (unlike variables which store data temporarily in memory).
Python provides built-in functions and methods to perform operations like creating, opening, reading, writing, updating, renaming, and deleting files.

Why File Handling?
------------------
1. Data Persistence – Store information permanently (logs, reports, user data).
2. Large Data Handling – Handle data bigger than memory size.
3. Communication – Share data between programs or systems.
4. Automation – Automate daily tasks such as backups, logs, and reports.

File Types in Python:
---------------------
1. Text Files  (.txt, .csv, .log) – Human-readable data stored as characters.
2. Binary Files (.bin, .jpg, .png, .pdf) – Non-text files stored in binary form.

File Modes (How to Open Files):
-------------------------------
Mode   Description
----   -------------------------------------------------------------
'r'    Read (default mode). Opens file for reading. Error if file not found.
'w'    Write. Creates a new file or overwrites the existing file.
'a'    Append. Opens file for adding data at the end. Creates file if not exists.
'x'    Exclusive creation. Creates a new file. Error if file already exists.
'b'    Binary mode. Used for non-text files like images, videos, PDFs.
't'    Text mode (default). Used for text-based files.
'r+'   Read and write (no truncation). File must exist.
'w+'   Write and read. Overwrites existing file or creates a new one.
'a+'   Append and read. Data is added at the end, file is readable too.

Important File Functions & Methods:
-----------------------------------
open(filename, mode)  : Opens the file in the specified mode.
read([size])          : Reads the entire file or specified number of characters.
readline()            : Reads a single line from the file.
readlines()           : Reads all lines and returns them as a list.
write(string)         : Writes a string into the file.
writelines(list)      : Writes multiple lines at once from a list.
close()               : Closes the file to free system resources.
seek(offset)          : Moves the file cursor to a specific position.
tell()                : Returns the current position of the cursor.
os.rename(src, dest)  : Renames a file.
os.remove(file)       : Deletes a file.
with open() as f      : Context manager for safe file handling (auto closes).

Best Practices:
---------------
1. Always use `with open()` to avoid forgetting `close()`.
2. Use proper error handling (`try-except`) to handle missing files.
3. Use correct mode ('r', 'w', 'a', etc.) based on the task.
4. For large files, read in chunks to save memory.
5. Always close files after use (auto-handled in `with` block).

Real-World Applications:
------------------------
- Log files for applications.
- Reading/writing CSV files in data analysis.
- Storing configuration settings.
- Creating backups and reports.
- Managing user-generated content (notes, uploads).
"""

import os   # Importing OS module to perform file system operations 
            # like checking existence, deleting, and renaming files.

# ================================================================
# Example 1: Creating and Closing a File
# ================================================================
f = open("example1.txt", "w")   # Create a new file (or overwrite if exists)
f.write("Hello, this is Example 1 file.\n")
f.close()                       # Always close after use
print("[Example 1]: File created and closed.")

# ================================================================
# Example 2: Reading a File
# ================================================================
with open("example2.txt", "w") as f:
    f.write("Python File Handling Example 2\n")
    f.write("Learning Read Operation\n")

with open("example2.txt", "r") as f:
    content = f.read()
    print("\n[Example 2 - Reading]:\n", content)

# ================================================================
# Example 3: Writing into a File
# ================================================================
with open("example3.txt", "w") as f:
    f.write("Line 1: Writing Example in Python\n")
    f.write("Line 2: Overwrites the existing content if file exists\n")

print("[Example 3]: Data written to 'example3.txt'.")

# ================================================================
# Example 4: Appending Data into a File
# ================================================================
with open("example4.txt", "a") as f:
    f.write("First Line\n")
    f.write("Appending new line without deleting old content\n")

print("[Example 4]: Data appended to 'example4.txt'.")

# ================================================================
# Example 5: Deleting a File
# ================================================================
with open("todelete.txt", "w") as f:
    f.write("This file will be deleted.")

if os.path.exists("todelete.txt"):
    os.remove("todelete.txt")
    print("[Example 5]: 'todelete.txt' deleted successfully.")

# ================================================================
# Example 6: Renaming a File
# ================================================================
with open("oldname.txt", "w") as f:
    f.write("This file will be renamed.")

if os.path.exists("oldname.txt"):
    os.rename("oldname.txt", "newname.txt")
    print("[Example 6]: 'oldname.txt' renamed to 'newname.txt'.")

# ================================================================
# Example 7: Updating File Content (Read + Write)
# ================================================================
with open("update.txt", "w") as f:
    f.write("Old Content\n")

with open("update.txt", "r+") as f:
    data = f.read()
    f.seek(0)  # Move cursor to beginning
    f.write("Updated Content\n" + data)

print("[Example 7]: 'update.txt' updated with new content.")

# ================================================================
# Example 8: Checking if File Exists
# ================================================================
filename = "checkfile.txt"
with open(filename, "w") as f:
    f.write("This file exists.\n")

if os.path.exists(filename):
    print(f"[Example 8]: '{filename}' exists in the directory.")

# ================================================================
# Example 9: Reading Specific Lines
# ================================================================
with open("lines.txt", "w") as f:
    f.write("Line1: Hello\nLine2: Python\nLine3: File Handling\n")

with open("lines.txt", "r") as f:
    lines = f.readlines()
    print("[Example 9]: Second line is ->", lines[1].strip())

# ================================================================
# Example 10: Working with Cursor (seek & tell)
# ================================================================
with open("cursor.txt", "w") as f:
    f.write("ABCDEFGHIJ")

with open("cursor.txt", "r") as f:
    print("[Example 10]: Cursor at start ->", f.tell())
    f.seek(5)   # Move cursor to 5th index
    print("Reading from 5th character onwards ->", f.read())


# ================================================================
# 10 REAL EXAMPLES FOR EACH OPERATION
# ================================================================

# ---------------- READ Examples ----------------
print("\n========= READ OPERATION EXAMPLES =========")

# Prepare a file
with open("read_master.txt", "w") as f:
    f.write("Line1: Hello World\nLine2: Python Rocks\nLine3: File Handling is powerful\nLine4: Keep learning\nLine5: Done\n")

# 1. Read whole file
with open("read_master.txt", "r") as f:
    print("Read1:", f.read())

# 2. Read line by line
with open("read_master.txt", "r") as f:
    print("Read2 (line by line):")
    for line in f:
        print(line.strip())

# 3. Using readline()
with open("read_master.txt", "r") as f:
    print("Read3 (readline):", f.readline())

# 4. Using readlines()
with open("read_master.txt", "r") as f:
    print("Read4 (readlines):", f.readlines())

# 5. Using seek() and tell()
with open("read_master.txt", "r") as f:
    print("Cursor at:", f.tell())
    f.seek(10)
    print("After seek(10):", f.read())

# 6. Read only first 20 characters
with open("read_master.txt", "r") as f:
    print("Read5 (first 20 chars):", f.read(20))

# 7. Read specific lines into a list
with open("read_master.txt", "r") as f:
    lines = f.readlines()
    print("Read6 (specific line):", lines[2])

# 8. Using loop with enumerate
with open("read_master.txt", "r") as f:
    print("Read7 (enumerate lines):")
    for i, line in enumerate(f, start=1):
        print(i, line.strip())

# 9. Check if file is readable
with open("read_master.txt", "r") as f:
    print("Read8 (is readable?):", f.readable())

# 10. Read and close explicitly
f = open("read_master.txt", "r")
print("Read9 (explicit close):", f.readline())
f.close()


# ---------------- WRITE Examples ----------------
print("\n========= WRITE OPERATION EXAMPLES =========")

# 1. Shopping list
with open("write1.txt", "w") as f:
    f.write("Milk\nEggs\nBread\n")

# 2. Student names
with open("write2.txt", "w") as f:
    f.write("Shalini\nRahul\nMahi\n")

# 3. Numbers
with open("write3.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"Number: {i}\n")

# 4. Sentences
with open("write4.txt", "w") as f:
    f.write("Python makes file handling simple.\n")

# 5. JSON-like text
with open("write5.txt", "w") as f:
    f.write("{\"name\": \"Shalini\", \"age\": 28}\n")

# 6. Write multiplication table
with open("write6.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"5 x {i} = {5*i}\n")

# 7. Write poem
with open("write7.txt", "w") as f:
    f.write("Roses are red,\nViolets are blue.\n")

# 8. Write CSV-like data
with open("write8.txt", "w") as f:
    f.write("Name, Age, City\nShalini, 28, Mumbai\nRahul, 30, Delhi\n")

# 9. Write log file
with open("write9.txt", "w") as f:
    f.write("INFO: Program started\n")

# 10. Overwrite existing file
with open("write10.txt", "w") as f:
    f.write("This file is overwritten.\n")

print("Check 'write1.txt' to 'write10.txt'")


# ---------------- APPEND Examples ----------------
print("\n========= APPEND OPERATION EXAMPLES =========")

# 1. Tasks
with open("append1.txt", "a") as f:
    f.write("Task 1 Completed\n")

# 2. Logs
with open("append2.txt", "a") as f:
    f.write("Log: System started\n")

# 3. Marks
with open("append3.txt", "a") as f:
    f.write("Math: 90\nScience: 85\n")

# 4. Feedback
with open("append4.txt", "a") as f:
    f.write("Feedback: Excellent teaching!\n")

# 5. Contact
with open("append5.txt", "a") as f:
    f.write("Name: Jay, Phone: 1234567890\n")

# 6. Append time-stamp
with open("append6.txt", "a") as f:
    f.write("Timestamp: Appended entry\n")

# 7. Append JSON data
with open("append7.txt", "a") as f:
    f.write("{\"user\": \"Shalini\", \"role\": \"admin\"}\n")

# 8. Append shopping item
with open("append8.txt", "a") as f:
    f.write("Bananas\n")

# 9. Append poem
with open("append9.txt", "a") as f:
    f.write("New line added to poem.\n")

# 10. Append result
with open("append10.txt", "a") as f:
    f.write("Result: Passed\n")

print("Data appended to 'append1.txt' to 'append10.txt'")


# ---------------- DELETE Examples ----------------
print("\n========= DELETE OPERATION EXAMPLES =========")

# Create files to delete
for i in range(1, 11):
    with open(f"delete{i}.txt", "w") as f:
        f.write(f"File delete{i}.txt")

# Delete files
for i in range(1, 11):
    if os.path.exists(f"delete{i}.txt"):
        os.remove(f"delete{i}.txt")
        print(f"delete{i}.txt deleted.")

print("\nAll file handling examples executed successfully!")
