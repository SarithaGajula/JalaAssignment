#Write a program to print 1 to 20 numbers using the while loop.


import sys

number = 1
while number <= 20:
    sys.stdout.buffer.write(bytes(str(number) + "\n", 'utf-8'))
    number += 1 