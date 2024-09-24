#Write a program to print even number between 10 and 20 using while


import sys
number = 10
while number <= 20:
    if number % 2 == 0:
        sys.stdout.buffer.write(bytes(f"{number}\n", 'utf-8'))
    number += 1