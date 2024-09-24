# Write a program to print “Bright IT Career” ten times using for loop


import sys

message = "Bright IT Career\n"
for i in range(10):
    sys.stdout.buffer.write(bytes(message, 'utf-8'))