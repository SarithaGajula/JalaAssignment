#Delete a value from a dictionar



import sys

# Create a sample dictionary
students = {
    "Alice": {"Math": 85, "Science": 90},
    "Robert": {"Math": 78, "Science": 82},
    "Charlie": {"Math": 92, "Science": 89},
}

# Deleting a student
del students["Robert"]  # Remove Robert from the dictionary

# Output the updated dictionary to standard output using sys
sys.stdout.write("Updated dictionary after deletion:\n")
for student, subjects in students.items():
    sys.stdout.write(f"{student}: {subjects}\n")
