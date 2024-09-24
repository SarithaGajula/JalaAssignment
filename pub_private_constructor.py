#Apply private, public, protected and default access modifiers to the constructor

import sys

class Example:
    public_attribute = "I am public"  # Public attribute
    _protected_attribute = "I am protected"  # Protected attribute
    __private_attribute = "I am private"  # Private attribute

    @staticmethod
    def show():
        sys.stdout.write(Example.public_attribute + "\n")
        sys.stdout.write(Example._protected_attribute + "\n")
        sys.stdout.write(Example.__private_attribute + "\n")

# Creating an object of the class
obj = Example()

# Accessing the public and protected attributes and method
obj.show()

# Accessing the protected attribute (not recommended, but possible)
sys.stdout.write(obj._protected_attribute + "\n")

# Attempting to access the private attribute will raise an AttributeError
# Uncommenting the next line will cause an error
# sys.stdout.write(obj.__private_attribute + "\n")
