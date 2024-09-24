#Replacing characters in strings with replace()


import sys

string = "Hello, World!"
old_char = 'o'  
new_char = 'x'  

string_len = 0
for _ in string:
    string_len += 1

def replace(string, old_char, new_char):
    replaced_string = ""

    i = 0
    while i < string_len:
        if string[i] == old_char:
            replaced_string += new_char  
        else:
            replaced_string += string[i] 
        i += 1

    return replaced_string

result = replace(string, old_char, new_char)

sys.stdout.write(f"Original String: {string}\n")
sys.stdout.write(f"Replaced String: {result}\n")
