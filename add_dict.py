# Create a Dictionary with at least 5 key value pairs of the Student ID and Name
#1.1. Adding the values in dictionary


import sys

# Creating the dictionary
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}

# Adding a new student
students[106] = "Frank"

# Displaying student names
for name in students.values():
    sys.stdout.write(name + "\n")
