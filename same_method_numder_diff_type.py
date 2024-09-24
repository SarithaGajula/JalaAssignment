#Write two methods with the same name but different number of parameters of different type and call the method

import sys

class Example:
    def display(self, value: int, count: int = None):
        if count is None:
            # Method with one integer parameter
            sys.stdout.write(f"Single integer value: {value}\n")
        else:
            # Method with one string and one integer parameter
            sys.stdout.write(f"String value: {value}, Count: {count}\n")

# Create an instance of the class
obj = Example()

# Call the methods
obj.display(5)                     # Calls the method with one integer parameter
obj.display("Hello", 3)            # Calls the method with string and integer parameters
