#Write a program to print largest number among three numbers.



import sys

def find_largest(num1, num2, num3):

    largest = num1
    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    result = f"Largest number: {largest}\n"
    sys.stdout.buffer.write(bytes(result, 'utf-8'))

find_largest(10, 20, 15) 
find_largest(5, 3, 7)
find_largest(30, 30, 25)