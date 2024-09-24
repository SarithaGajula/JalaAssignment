#Create a program to create two class.
#Call each class by creating an object to it 

import sys
class ClassOne:
    def display(self):
        message = "This is Class One."
        for char in message:
            if char != '.':
                end = char + '\n'
                # Manual way to output instead of using print()
                sys.stdout.write(end)

class ClassTwo:
    def display(self):
        message = "This is Class Two."
        for char in message:
            if char != '.':
                end = char + '\n'
                # Manual way to output instead of using print()
                sys.stdout.write(end)

# Create objects for each class
obj1 = ClassOne()
obj2 = ClassTwo()

# Call the display method
obj1.display()
obj2.display()
