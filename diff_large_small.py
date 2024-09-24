#Write a function to get the difference of largest and smallest value


import sys

def find_difference(arr):
    count = 0
    for _ in arr:
        count += 1
    
    if count == 0:
        return None  

    
    largest = arr[0]
    smallest = arr[0]

    
    i = 1
    while i < count:
        if arr[i] > largest:
            largest = arr[i]
        if arr[i] < smallest:
            smallest = arr[i]
        i += 1
    difference = largest - smallest

    return difference

array = [10, 20, 5, 40, 50] 

difference = find_difference(array)

if difference is not None:
    sys.stdout.write(f"The difference between the largest and smallest value is: {difference}\n")
else:
    sys.stdout.write("The array is empty.\n")
