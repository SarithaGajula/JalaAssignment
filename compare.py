# Write a program to find the two numbers equal or not.


import sys

def are_numbers_equal(num1, num2):
    if num1 == num2:
        result = "Numbers are equal"
    else:
        result = "Numbers are not equal"
    
    sys.stdout.buffer.write(bytes(result + "\n", 'utf-8'))
    
are_numbers_equal(5, 5)  
are_numbers_equal(10, 15)