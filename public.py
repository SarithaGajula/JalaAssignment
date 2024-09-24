"""
Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or different 
package.
"""


import sys

# Class simulating public fields and methods
class PublicClass:
    def __init__(self):
        # Public fields
        self.public_field1 = "Public Field 1"
        self.public_field2 = "Public Field 2"

    # Public method
    def public_method(self):
        return "This is a public method"

    def display(self):
        sys.stdout.write("Accessing public fields in PublicClass:\n")
        sys.stdout.write(self.public_field1 + "\n")
        sys.stdout.write(self.public_field2 + "\n")
        sys.stdout.write(self.public_method() + "\n")


# Class in the same "package" accessing PublicClass
class AccessPublic:
    def access_fields_and_methods(self):
        public_instance = PublicClass()
        sys.stdout.write("Accessing public fields and methods from AccessPublic:\n")
        sys.stdout.write(public_instance.public_field1 + "\n")
        sys.stdout.write(public_instance.public_field2 + "\n")
        sys.stdout.write(public_instance.public_method() + "\n")


# Class in a different "package" accessing PublicClass
class AccessPublicDifferentPackage:
    def access_public_members(self):
        public_instance = PublicClass()
        sys.stdout.write("Accessing public fields and methods from AccessPublicDifferentPackage:\n")
        sys.stdout.write(public_instance.public_field1 + "\n")
        sys.stdout.write(public_instance.public_field2 + "\n")
        sys.stdout.write(public_instance.public_method() + "\n")


# Main execution
def main():
    # Accessing public fields and methods from the same "package"
    access_instance = AccessPublic()
    access_instance.access_fields_and_methods()

    # Accessing public fields and methods from a different "package"
    different_access_instance = AccessPublicDifferentPackage()
    different_access_instance.access_public_members()


# Run the main function
if __name__ == "__main__":
    main()
