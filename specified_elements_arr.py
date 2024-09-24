#Write a method to verify if the array contains two specified elements(12,23)


import sys

def contains_elements(arr, element1, element2):
    found_element1 = False
    found_element2 = False
    count = 0
    for _ in arr:
        count += 1
    i = 0
    while i < count:
        if arr[i] == element1:
            found_element1 = True
        if arr[i] == element2:
            found_element2 = True
        i += 1
    return found_element1 and found_element2
array = [10, 12, 20, 23, 30] 
if contains_elements(array, 12, 23):
    sys.stdout.write("The array contains both 12 and 23.\n")
else:
    sys.stdout.write("The array does not contain both 12 and 23.\n")
