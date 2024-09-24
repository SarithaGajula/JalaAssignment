#Write a program to create your own exception


import sys

class MyCustomException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise MyCustomException("Age must be 18 or older.")

try:
    check_age(16)
except MyCustomException as e:
    sys.stderr.write(e.args[0] + "\n")  # Print the error message to stderr
    sys.exit(1)  # Exit the program with a non-zero status
