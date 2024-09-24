#Call the constructors(both default and argument constructors) of super class from a child class.


import sys

class SuperClass:
    def default_constructor(self):
        self.value = "Default Constructor"

    def one_argument_constructor(self, arg1):
        self.value = arg1

class ChildClass(SuperClass):
    def call_constructors(self):
        # Calling default constructor
        self.default_constructor()
        
        # Calling one-argument constructor
        self.one_argument_constructor("One Argument Constructor")

class Main:
    def run(self):
        child = ChildClass()
        child.call_constructors()
        sys.stdout.write(child.value + "\n")

main = Main()
main.run()

