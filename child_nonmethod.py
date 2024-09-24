#Create an instance for the child class in child class and call non-abstract methods.



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

    def create_instance_and_call_non_abstract(self):
        # Create an instance of Dog within Dog
        dog_instance = Dog()
        # Call the non-abstract method
        return dog_instance.non_abstract_method()

# Create an object of the subclass
my_dog = Dog()

# Call the method that creates an instance and calls the non-abstract method
output = my_dog.create_instance_and_call_non_abstract()

# Using sys.stdout to output the result
sys.stdout.write(output + "\n")
