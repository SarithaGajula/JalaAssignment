#Create a program to create two class.
#Import the respective packages


import sys
import datetime  # Example of an additional package

class ClassA:
    def display_message(self):
        message = "Hello from ClassA!"
        sys.stdout.write(message + "\n")

class ClassB:
    def display_message(self):
        message = "Hello from ClassB!"
        sys.stdout.write(message + "\n")

# Creating instances of both classes
a = ClassA()
b = ClassB()

# Calling the display_message method for both classes
a.display_message()
b.display_message()

# Using the datetime package as an example
current_time = datetime.datetime.now()
sys.stdout.write(f"Current time: {current_time}\n")
