# Write a function to add integer values of an array.


import sys

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

array = [1, 2, 3, 4, 5]  
result = sum_array(array)
sys.stdout.write(f"The sum of the array is: {result}\n")
