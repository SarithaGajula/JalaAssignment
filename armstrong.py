# Write a program to find Armstrong number or not.

import sys

def is_armstrong(num):
    
    str_num = str(num)
    num_digits = len(str_num)
    
    sum_of_powers = 0
    for digit in str_num:
        sum_of_powers += int(digit) ** num_digits
    
    return sum_of_powers == num

try:
    user_input = int(input("Enter a number: "))
    
    if is_armstrong(user_input):
        sys.stdout.write(f"{user_input} is an Armstrong number.\n")
    else:
        sys.stdout.write(f"{user_input} is not an Armstrong number.\n")
except ValueError:
    sys.stdout.write("Please enter a valid integer.\n")
