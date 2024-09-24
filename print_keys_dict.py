#Print the keys present in a particular dictionary


import sys

# Create a sample dictionary
students = {
    "Alice": {"Math": 85, "Science": 90},
    "Robert": {"Math": 78, "Science": 82},
    "Charlie": {"Math": 92, "Science": 89},
}

# Accessing and printing the keys
sys.stdout.write("Keys in the dictionary:\n")
for student in students.keys():
    sys.stdout.write(f"{student}\n")
