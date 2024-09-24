#Write a function to reverse an array of integer values



import sys

def reverse_array(arr):
    count = 0
    for _ in arr:
        count += 1
    
    reversed_array = []
    i = count - 1
    while i >= 0:
        reversed_array.append(arr[i])
        i -= 1
    
    return reversed_array
array = [10, 20, 30, 40, 50]  

reversed_array = reverse_array(array)
sys.stdout.write("Reversed array: " + str(reversed_array) + "\n")
