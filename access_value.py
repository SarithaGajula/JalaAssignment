#. Accessing the value in dictionary


import sys

# Create a dictionary with student ID and names
students = {
    101: "Alice",
    102: "Robert",
    103: "Charlie",
    104: "Diana",
    105: "Ethan",
    106: "Fiona"
}

# Accessing a value using the key
student_id = 103
student_name = students[student_id]  # Get the name for ID 103 (Charlie)

# Output the accessed value to standard output using sys
sys.stdout.write(f"Student ID {student_id}: {student_name}\n")
