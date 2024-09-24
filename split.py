#. Splitting strings with split()


import sys

# Input string and delimiter
string = "Hello, World! Welcome to Python."
delimiter = ' '  # Space is used as the delimiter

# Manually calculate the length of the string
string_len = 0
for _ in string:
    string_len += 1

# Function to split the string based on the delimiter
def split(string, delimiter):
    # Initialize an empty list to store substrings
    substrings = []
    current_substring = ""

    i = 0
    while i < string_len:
        if string[i] == delimiter:  
            substrings.append(current_substring)  
            current_substring = ""  
        else:
            current_substring += string[i]  
        i += 1

    if current_substring:
        substrings.append(current_substring)

    return substrings

result = split(string, delimiter)

sys.stdout.write("Splitted String: " + str(result) + "\n")
