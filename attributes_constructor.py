#Write a program which illustrates the concept of attributes of a constructor


import sys

class Person:
    def default_constructor(self):
        self.name = "John Doe"  # Default attribute
        self.age = 30           # Default attribute

    def parameterized_constructor(self, name, age):
        self.name = name        # Parameterized attribute
        self.age = age          # Parameterized attribute

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Main:
    def run(self):
        # Using default constructor
        person1 = Person()
        person1.default_constructor()
        sys.stdout.write(person1.display_info() + "\n")

        # Using parameterized constructor
        person2 = Person()
        person2.parameterized_constructor("Alice", 25)
        sys.stdout.write(person2.display_info() + "\n")

main = Main()
main.run()
