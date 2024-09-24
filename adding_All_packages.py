#Create a program to create two class.
#Create a __init__.py for adding all packages


import sys

# Simulating __init__.py by defining classes directly
class ClassA:
    def greet(self):
        return "Hello from Class A!"

class ClassB:
    def greet(self):
        return "Hello from Class B!"

# Simulating package behavior
def main():
    a = ClassA()
    b = ClassB()

    sys.stdout.write(a.greet() + "\n")
    sys.stdout.write(b.greet() + "\n")

if __name__ == "__main__":
    main()
