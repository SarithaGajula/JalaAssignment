#Write a function to test if array contains a specific value


import sys

def contains_value(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

array = [10, 20, 30, 40, 50]  
target = 30  

if contains_value(array, target):
    sys.stdout.write(f"{target} is found in the array.\n")
else:
    sys.stdout.write(f"{target} is not found in the array.\n")
