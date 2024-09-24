#Create a nested loop dictionary


import sys

n = 3  # Size of the dictionary
nested_dict = {}

# Custom function to simulate range
def custom_range(end):
    i = 0
    while i < end:
        yield i
        i += 1

# Loop for creating nested dictionary
for i in custom_range(n):
    inner_dict = {}
    for j in custom_range(n):
        inner_dict[i] = j
    nested_dict[i] = inner_dict

# Output the dictionary
sys.stdout.write("{")
first = True
for key in nested_dict:
    if not first:
        sys.stdout.write(", ")
    first = False
    sys.stdout.write(f"{key}: {nested_dict[key]}")
sys.stdout.write("}")

