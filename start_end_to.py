#startsWith(), endsWith() and compareTo()

#startwith()
import sys
string = "Hello, World!"
prefix = "Hello"

string_len = 0
prefix_len = 0

for _ in string:
    string_len += 1

for _ in prefix:
    prefix_len += 1

def startsWith(string, prefix):
    if prefix_len > string_len:
        return False
    
    i = 0
    while i < prefix_len:
        if string[i] != prefix[i]:
            return False
        i += 1
    return True

if startsWith(string, prefix):
    sys.stdout.write("String starts with the prefix.\n")
else:
    sys.stdout.write("String does not start with the prefix.\n")

#endwith()

string = "Hello, World!"
suffix = "World!"

suffix_len = 0

for _ in suffix:
    suffix_len += 1
def endsWith(string, suffix):
    if suffix_len > string_len:
        return False

    i = 0
    while i < suffix_len:
        if string[string_len - suffix_len + i] != suffix[i]:
            return False
        i += 1
    return True
if endsWith(string, suffix):
    sys.stdout.write("String ends with the suffix.\n")
else:
    sys.stdout.write("String does not end with the suffix.\n")

#compareTo()

# Input strings
string1 = "Hello"
string2 = "Hello"
string1_len = 0
string2_len = 0

for _ in string1:
    string1_len += 1

for _ in string2:
    string2_len += 1

def compareTo(s1, s2):
    min_len = string1_len if string1_len < string2_len else string2_len
    i = 0

    while i < min_len:
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i]) 
        i += 1

    return string1_len - string2_len
comparison_result = compareTo(string1, string2)

if comparison_result == 0:
    sys.stdout.write("The strings are equal.\n")
elif comparison_result > 0:
    sys.stdout.write("String1 is greater than String2.\n")
else:
    sys.stdout.write("String1 is smaller than String2.\n")

