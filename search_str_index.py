#Searching in strings using index()



import sys

string = "Hello, World!"
search_char = "W"  

length = 0
for _ in string:
    length += 1

index = -1  
i = 0
while i < length:
    if string[i] == search_char:
        index = i
        break
    i += 1

if index != -1:
    sys.stdout.write(f"Character '{search_char}' found at index: {index}\n")
else:
    sys.stdout.write(f"Character '{search_char}' not found\n")
