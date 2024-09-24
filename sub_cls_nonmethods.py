#Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods


import sys

# Define the abstract class
class Animal:
    def speak(self):
        return "Animal speaks"

# Define the subclass
class Dog(Animal):
    def bark(self):
        return "Bark"

    def create_instance_and_access_methods(self):
        # Create an instance of the abstract class
        animal_instance = Animal()
        
        # Access the non-abstract method
        speak_output = animal_instance.speak()
        # Access the subclass method
        bark_output = self.bark()
        
        return speak_output, bark_output

# Create an object of the subclass
my_dog = Dog()

# Call the method that creates an instance and accesses methods
speak_output, bark_output = my_dog.create_instance_and_access_methods()

# Using sys.stdout to output the results
sys.stdout.write(speak_output + " and " + bark_output + "\n")
