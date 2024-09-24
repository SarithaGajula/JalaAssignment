"""
Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package. 
Also, Access the PROTECTED fields and methods from child class located in a different 
package
Access the PROTECTED fields and methods from any class in different package
"""


import sys

# Class with protected fields and methods
class Parent:
    def __init__(self):
        # Protected fields
        self._protected_field1 = "Protected Field 1"
        self._protected_field2 = "Protected Field 2"

    # Protected method
    def _protected_method(self):
        return "This is a protected method"

    def display(self):
        sys.stdout.write("Accessing protected fields in Parent:\n")
        sys.stdout.write(self._protected_field1 + "\n")
        sys.stdout.write(self._protected_field2 + "\n")
        sys.stdout.write(self._protected_method() + "\n")


# Class in the same "package" accessing Parent
class AccessProtected:
    def access_fields_and_methods(self):
        parent_instance = Parent()
        sys.stdout.write("Accessing protected fields and methods from AccessProtected:\n")
        sys.stdout.write(parent_instance._protected_field1 + "\n")
        sys.stdout.write(parent_instance._protected_field2 + "\n")
        sys.stdout.write(parent_instance._protected_method() + "\n")


# Child class in a different "package" accessing Parent
class Child(Parent):
    def access_protected_members(self):
        sys.stdout.write("Accessing protected fields and methods from Child:\n")
        sys.stdout.write(self._protected_field1 + "\n")
        sys.stdout.write(self._protected_field2 + "\n")
        sys.stdout.write(self._protected_method() + "\n")


# Class in a different "package" trying to access protected members
class AccessProtectedDifferentPackage:
    def access_protected(self):
        parent_instance = Parent()
        sys.stdout.write("Trying to access protected fields from AccessProtectedDifferentPackage:\n")
        try:
            sys.stdout.write(parent_instance._protected_field1 + "\n")  # Accessing protected field
        except AttributeError as e:
            sys.stdout.write("Cannot access protected field: " + e.__str__() + "\n")

        try:
            sys.stdout.write(parent_instance._protected_method() + "\n")  # Accessing protected method
        except AttributeError as e:
            sys.stdout.write("Cannot access protected method: " + e.__str__() + "\n")


# Main execution
def main():
    # Accessing protected fields and methods from the same "package"
    access_instance = AccessProtected()
    access_instance.access_fields_and_methods()

    # Accessing protected fields and methods from the Child class
    child_instance = Child()
    child_instance.access_protected_members()

    # Accessing protected fields and methods from a different "package"
    different_access_instance = AccessProtectedDifferentPackage()
    different_access_instance.access_protected()


# Run the main function
if __name__ == "__main__":
    main()

