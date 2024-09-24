#Write a program to print the odd and even numbers.



import sys

def print_numbers(n, i=0):
    if i > n:
        return
    if i % 2 == 0:
        sys.stdout.write(f"Even: {i}\n")
    else:
        sys.stdout.write(f"Odd: {i}\n")
    print_numbers(n, i + 1)

limit = 10 
print_numbers(limit)