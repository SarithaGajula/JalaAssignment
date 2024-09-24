# Write a program to palindrome or not.


import sys

def is_palindrome(s):
    cleaned = ''
    for char in s:
        if char != ' ':
            cleaned += char.lower()
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

input_string = "madam"
result = is_palindrome(input_string)
if result:
    sys.stdout.write(f'"{input_string}" is a palindrome.\n')
else:
    sys.stdout.write(f'"{input_string}" is not a palindrome.\n')
