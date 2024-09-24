#Updating the values in dictionary


import sys

# Create a dictionary with student ID and names
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "Diana",
    105: "Ethan"
}

# Modifying an existing student's name
students[102] = "Robert"  # Change Bob to Robert

# Output the updated dictionary to standard output using sys
for key, value in students.items():
    sys.stdout.write(f"{key}: {value}\n")
