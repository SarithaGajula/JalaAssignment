#Write a program with multiple catch blocks


import sys

def perform_operations(a, b):
    try:
        result = a / b
        sys.stdout.write(f"Result of division: {result}\n")
        value = int("invalid")  # This will cause a ValueError
    except ZeroDivisionError:
        sys.stdout.write("Error: Cannot divide by zero.\n")
    except ValueError:
        sys.stdout.write("Error: Invalid value conversion.\n")
    except Exception as e:
        sys.stdout.write(f"An unexpected error occurred: {e}\n")

# Test with division by zero and invalid value conversion
perform_operations(10, 0)
perform_operations(10, 2)
