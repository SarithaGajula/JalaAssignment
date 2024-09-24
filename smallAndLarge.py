# Print the smaller and larger number


import sys

def find_smaller_and_larger(num1, num2):
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1

    result = (
        f"Smaller number: {smaller}\n"
        f"Larger number: {larger}\n"
    )

    sys.stdout.buffer.write(bytes(result, 'utf-8'))

find_smaller_and_larger(10, 20) 
find_smaller_and_larger(25, 15)
find_smaller_and_larger(5, 5)