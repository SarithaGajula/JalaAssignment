#Define a static variable and access that through a class



import sys

class MyClass:
    static_variable = 42
    def print_static_variable():
        sys.stdout.write("Accessing static variable: " + str(MyClass.static_variable) + "\n")

MyClass.print_static_variable()
sys.stdout.write("Static variable directly: " + str(MyClass.static_variable) + "\n")
