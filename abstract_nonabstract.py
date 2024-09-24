#Create an abstract class with abstract and non-abstract methods.


import sys

# Define the abstract class
class Animal:
    def non_abstract_method(self):
        return "This is a non-abstract method."

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Define the subclass
class Dog(Animal):
    def sound(self):
        return "Bark"

# Create an object of the subclass
my_dog = Dog()

# Call the non-abstract method
non_abstract_output = my_dog.non_abstract_method()
# Call the abstract method
sound_output = my_dog.sound()

# Using sys.stdout to output the results
sys.stdout.write(non_abstract_output + "\n")
sys.stdout.write(sound_output + "\n")
