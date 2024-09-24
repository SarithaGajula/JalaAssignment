#Create a program to create two class.
#1.1. Create a constructor and a method for each class


import sys

# Define the first class
class ClassA:
    def set_name(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name} from ClassA!"

# Define the second class
class ClassB:
    def set_age(self, age):
        self.age = age

    def display_age(self):
        return f"You are {self.age} years old in ClassB."

# Create an instance of ClassA
object_a = ClassA()
object_a.set_name("Alice")  # Set the name using a method

# Create an instance of ClassB
object_b = ClassB()
object_b.set_age(30)  # Set the age using a method

# Call the method from ClassA
greeting_output = object_a.greet()

# Call the method from ClassB
age_output = object_b.display_age()

# Using sys.stdout to output the results
sys.stdout.write(greeting_output + "\n")
sys.stdout.write(age_output + "\n")
