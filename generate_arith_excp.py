#Write a program to generate Arithmetic Exception


import sys

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        sys.stdout.write("Arithmetic Error: Cannot divide by zero.\n")
        sys.exit(1)
    else:
        sys.stdout.write(f"Result: {result}\n")

divide_numbers(10, 0)
