#Handle the Arithmetic exception using try-catch block.


import sys

try:
    # Generate an Arithmetic Exception
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    sys.stdout.write("Error: Division by zero is not allowed.") 

# Exit the program
sys.exit()