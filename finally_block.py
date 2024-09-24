#Write a program with finally block


import sys

class MyCustomException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise MyCustomException("Age must be 18 or older.")

try:
    check_age(16)
except MyCustomException as e:
    sys.stdout.write(e.args[0] + "\n")
finally:
    sys.stdout.write("Execution completed.\n")  # This will always run
