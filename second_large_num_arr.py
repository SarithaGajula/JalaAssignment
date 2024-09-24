#3. Write a method to find the second largest number in an array


import sys

def find_second_largest(arr):

    count = 0
    for _ in arr:
        count += 1
    
    if count < 2:
        return None 
    largest = arr[0]
    second_largest = None
    i = 1
    while i < count:
        if arr[i] > largest:
            largest = arr[i]
        i += 1
    i = 0
    while i < count:
        if arr[i] != largest: 
            if second_largest is None or arr[i] > second_largest:
                second_largest = arr[i]
        i += 1

    return second_largest
array = [10, 20, 30, 40, 50] 

second_largest = find_second_largest(array)

if second_largest is not None:
    sys.stdout.write(f"The second largest number is: {second_largest}\n")
else:
    sys.stdout.write("The array doesn't have a second largest number.\n")
