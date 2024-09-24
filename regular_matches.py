#Matching a String Against a Regular Expression With matches()



import sys

string = "Hello, World!"
pattern = "Hello, Worl."  

string_len = 0
pattern_len = 0

for _ in string:
    string_len += 1

for _ in pattern:
    pattern_len += 1

def matches(string, pattern):
    if string_len != pattern_len:
        return False
    
    i = 0
    while i < string_len:
        if pattern[i] != '.' and string[i] != pattern[i]:
            return False
        i += 1
    
    return True

if matches(string, pattern):
    sys.stdout.write("String matches the pattern.\n")
else:
    sys.stdout.write("String does not match the pattern.\n")
