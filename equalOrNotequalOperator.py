#Program to equal operator and not equal operators


import sys

def compare_numbers(num1, num2):
    equal = (num1 == num2)
    not_equal = (num1 != num2)

    result = (
        f"{num1} == {num2}: {equal}\n"
        f"{num1} != {num2}: {not_equal}\n"
    )
    
    sys.stdout.buffer.write(bytes(result, 'utf-8'))
compare_numbers(10, 10)  
compare_numbers(10, 20)  