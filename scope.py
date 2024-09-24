#Define the local and Global variables with the same name and print both variables and understand the scope of the variables


import sys


var = 100  # This is a global variable

def my_function():

    var = 200  # This is a local variable
    
    sys.stdout.buffer.write(bytes("Local variable: " + str(var) + "\n", 'utf-8'))

sys.stdout.buffer.write(bytes("Global variable: " + str(var) + "\n", 'utf-8'))
my_function()
sys.stdout.buffer.write(bytes("Global variable after function call: " + str(var) + "\n", 'utf-8'))