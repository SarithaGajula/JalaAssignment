"""
Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.
"""


import sys

# Class with private fields and methods
class Parent:
    def __init__(self):
        # Private fields
        self.__private_field1 = "Private Field 1"
        self.__private_field2 = "Private Field 2"

    # Private method
    def __private_method(self):
        return "This is a private method"

    def main(self):
        # Print private fields
        sys.stdout.write("Accessing private fields in the main method:\n")
        sys.stdout.write(self.__private_field1 + "\n")
        sys.stdout.write(self.__private_field2 + "\n")
        
        # Call the private method
        sys.stdout.write("Calling the private method:\n")
        sys.stdout.write(self.__private_method() + "\n")

# Subclass trying to access private fields and methods
class Child(Parent):
    def access_private_members(self):
        try:
            sys.stdout.write("Trying to access private fields from subclass:\n")
            sys.stdout.write(self.__private_field1 + "\n")  # This will raise an AttributeError
        except AttributeError as e:
            sys.stdout.write("Cannot access private field: " + e.__str__() + "\n")

        try:
            sys.stdout.write("Trying to call private method from subclass:\n")
            sys.stdout.write(self.__private_method() + "\n")  # This will also raise an AttributeError
        except AttributeError as e:
            sys.stdout.write("Cannot access private method: " + e.__str__() + "\n")

# Create instances and run the main method
parent_instance = Parent()
parent_instance.main()

# Create an instance of the Child class and try to access private members
child_instance = Child()
child_instance.access_private_members()
