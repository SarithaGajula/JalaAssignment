"""Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class"""


import sys

class MyClass:
    def default_constructor(self):
        self.value = "Default Constructor"

    def one_argument_constructor(self, arg1):
        self.value = arg1

    def two_argument_constructor(self, arg1, arg2):
        self.value = arg1 + " and " + arg2

class Main:
    def run(self):
        obj1 = MyClass()
        obj1.default_constructor()

        obj2 = MyClass()
        obj2.one_argument_constructor("One Argument Constructor")

        obj3 = MyClass()
        obj3.two_argument_constructor("First Argument", "Second Argument")

        sys.stdout.write(obj1.value + "\n")
        sys.stdout.write(obj2.value + "\n")
        sys.stdout.write(obj3.value + "\n")

main = Main()
main.run()
