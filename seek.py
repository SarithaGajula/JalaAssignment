#Write a program to read a file a just to a particular index using seek()



import sys

# Using file descriptor 0 for reading stdin (input redirected)
file = sys.stdin

# Read the entire file
content = file.read()

# Start reading from a particular index (e.g., 10) and get 20 characters
index = 10  # Adjust to the index you want
length = 20  # Number of characters to read
result = content[index:index + length]

# Write the result using sys.stdout.write
sys.stdout.write(result)
