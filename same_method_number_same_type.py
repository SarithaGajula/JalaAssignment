#Write two methods with the same name but different number of parameters of same type and call the methods


import sys

class Example:
    def display(self, value1):
        sys.stdout.write("Value: " + value1 + "\n")

    def display(self, value1, value2):
        sys.stdout.write("Values: " + value1 + " and " + value2 + "\n")

obj = Example()

# Calling the first method
obj.display("Hello")  # This will not work as expected because of method overriding

# Calling the second method
obj.display("Hello", "World")

