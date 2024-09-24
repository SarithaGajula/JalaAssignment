#Define a static variable and access that through a instance.


import sys

class MyClass:
    static_variable = 42
    def print_static_variable(self):
        sys.stdout.write("Accessing static variable through instance: " + str(self.static_variable) + "\n")

my_instance = MyClass()
my_instance.print_static_variable()
sys.stdout.write("Static variable directly through instance: " + str(my_instance.static_variable) + "\n")
