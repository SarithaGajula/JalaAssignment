#Program for relational operators (<,<==, >, >==)


import sys

def compare_numbers(num1, num2):
    less_than = num1 < num2
    less_than_or_equal = num1 <= num2
    greater_than = num1 > num2
    greater_than_or_equal = num1 >= num2
    
    
    result = (
        f"{num1} < {num2}: {less_than}\n"
        f"{num1} <= {num2}: {less_than_or_equal}\n"
        f"{num1} > {num2}: {greater_than}\n"
        f"{num1} >= {num2}: {greater_than_or_equal}\n"
    )
    

    sys.stdout.buffer.write(bytes(result, 'utf-8'))


compare_numbers(10, 20)  
compare_numbers(15, 15)
compare_numbers(25, 20)