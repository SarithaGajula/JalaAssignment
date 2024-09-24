#Program to check whether a number is EVEN or ODD using switch.


import sys

def check_even_odd(num):
    # Simulating switch-case using if-else
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


input_number = 10  
result = check_even_odd(input_number)
sys.stdout.write(f'The number {input_number} is {result}.\n')