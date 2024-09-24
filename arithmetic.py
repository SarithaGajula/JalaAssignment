#Write a function for arithmetic operators(+,-,*,/)


import sys

def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b 
    sys.stdout.buffer.write(bytes("Addition: " + str(addition) + "\n", 'utf-8'))
    sys.stdout.buffer.write(bytes("Subtraction: " + str(subtraction) + "\n", 'utf-8'))
    sys.stdout.buffer.write(bytes("Multiplication: " + str(multiplication) + "\n", 'utf-8'))
    sys.stdout.buffer.write(bytes("Division: " + str(division) + "\n", 'utf-8'))

arithmetic_operations(10, 2)