#Finding the length of the string

import sys

string = "Hello, World!"
length = 0

for char in string:
    length += 1
sys.stdout.write(f"The length of the string is: {length}\n")
