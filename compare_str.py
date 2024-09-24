#Comparing strings



import sys

string1 = "Hello"
string2 = "Hello"
length1 = 0
length2 = 0

for _ in string1:
    length1 += 1

for _ in string2:
    length2 += 1

def compare_strings(s1, s2):
    if length1 != length2:
        return False

    i = 0
    while i < length1:
        if s1[i] != s2[i]:
            return False
        i += 1
    
    return True
if compare_strings(string1, string2):
    sys.stdout.write("The strings are equal.\n")
else:
    sys.stdout.write("The strings are not equal.\n")
