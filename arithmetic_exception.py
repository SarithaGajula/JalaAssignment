#Write a program to generate Arithmetic Exception without exception handling.

import sys

def divide_numbers(a, b):
    result = a / b  # This will cause ZeroDivisionError when b is 0
    sys.stdout.write(f"Result: {result}\n")

# This will raise a ZeroDivisionError
divide_numbers(10, 0)
