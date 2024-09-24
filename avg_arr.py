#Write a function to calculate the average value of an array of integer


import sys

def average_array(arr):
    total = 0
    count = 0
    
    for num in arr:
        total += num
        count += 1
    
    if count == 0:
        return 0  
    
    average = total / count
    return average
array = [1, 2, 3, 4, 5] 
result = average_array(array)
sys.stdout.write(f"The average of the array is: {result}\n")
