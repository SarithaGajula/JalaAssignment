#Create an instance for the child class in child class and call abstract methods


import sys

# Define the base class
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define the subclass
class Dog(Animal):
    def sound(self):
        return "Bark"

    def create_instance_and_call_sound(self):
        # Create an instance of Dog within Dog
        dog_instance = Dog()
        # Call the sound method
        return dog_instance.sound()

# Create an object of the subclass
my_dog = Dog()

# Call the method that creates an instance and calls the sound method
output = my_dog.create_instance_and_call_sound()

# Using sys.stdout to output the result
sys.stdout.write(output + "\n")
