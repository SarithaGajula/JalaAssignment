# Write a program to print 1 to 10 using the do-while loop statement


import sys


i = 1
while True:
    sys.stdout.write(f"{i}\n")  
    i += 1
    if i > 10:
        break