#Write two methods with the same name and same number of parameters of same type


import sys

class Example:
    def method(self, a):
        sys.stdout.write(f"First method: {a + 1}\n")  # First method

    def method(self, a):  # This will overwrite the first one
        sys.stdout.write(f"Second method: {a * 2}\n")  # Second method

# Usage
obj = Example()
obj.method(5)  # This will call the second method (overwritten)