#Write a program to throw exception with your own message


import sys

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception message.")
except CustomError as e:
    message = e.args[0]  # Accessing the first argument of the exception
    sys.stderr.write("Error: " + message + "\n")

