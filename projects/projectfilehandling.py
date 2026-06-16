# Smart Notes Organizer - Part 1
# Beginner-friendly Python file handling project

# =====================================================================
# TASK 1: Create a sample notes file
# =====================================================================
print("--- Task 1: Creating Sample Notes File ---")

# We use 'w' mode to write and create the file.
# Using 'with' automatically closes the file when we are done.
with open("my_notes.txt", "w") as file:
    file.write("1. Python is an interpreted programming language.\n")
    file.write("2. [IMPORTANT] Remember to practice coding daily.\n")
    file.write("3. File handling allows us to read and write data.\n")
    file.write("4. [IMPORTANT] Submit the assignment before Friday.\n")
    file.write("5. Keep your code clean and add comments.\n")

print("File 'my_notes.txt' created successfully!\n")


# =====================================================================
# TASK 2: Preview file content using read(n)
# =====================================================================
print("--- Task 2: Previewing First 15 Characters ---")

with open("my_notes.txt", "r") as file:
    # read(15) reads exactly the first 15 characters of the file
    preview = file.read(15)
    print(f"Preview: '{preview}'\n")


# =====================================================================
# TASK 3: Read all lines using readlines()
# =====================================================================
print("--- Task 3: Reading All Lines into a List ---")

with open("my_notes.txt", "r") as file:
    # readlines() stores every line as an element in a Python list
    all_lines = file.readlines()
    print("List of lines:", all_lines)
    print(f"Total number of lines: {len(all_lines)}\n")


# =====================================================================
# TASK 4 & 5: Loop line-by-line, Filter with conditions, and Copy
# =====================================================================
print("--- Task 4 & 5: Filtering and Copying Important Notes ---")

# We open the source file to read ('r') and the target file to write ('w')
with open("my_notes.txt", "r") as source_file, open("important_notes.txt", "w") as target_file:
    
    print("Scanning notes for '[IMPORTANT]'...")
    
    # Loop through the file line by line (memory efficient)
    for line in source_file:
        
        # Condition: Check if '[IMPORTANT]' is inside the current line
        if "[IMPORTANT]" in line:
            print(f"-> Found and Copied: {line.strip()}")
            
            # Write the selected line into the new file
            target_file.write(line)

print("\nFiltering complete! Check 'important_notes.txt' for your results.")