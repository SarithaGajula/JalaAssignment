#Extract a string using Substring



import sys


string = "Hello, World!"
start_index = 7  
end_index = 12   

substring = ""
i = start_index
while i < end_index:
    substring += string[i]
    i += 1
sys.stdout.write(substring + "\n")
