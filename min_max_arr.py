#Write a function to find the minimum and maximum value of an array


import sys

def find_min_max(arr):
    count = 0
    for _ in arr:
        count += 1

    if count == 0:
        return None, None

    min_value = arr[0]
    max_value = arr[0]
    
    i = 1  
    while i < count:
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]
        i += 1
    
    return min_value, max_value
array = [10, 20, 5, 40, 50]  

min_value, max_value = find_min_max(array)

if min_value is not None and max_value is not None:
    sys.stdout.write(f"Minimum value: {min_value}, Maximum value: {max_value}\n")
else:
    sys.stdout.write("Array is empty.\n")
