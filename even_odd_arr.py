#Write a method to find number of even number and odd numbers in an array



import sys

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    count = 0
    for _ in arr:
        count += 1
    i = 0
    while i < count:
        if arr[i] % 2 == 0: 
            even_count += 1
        else: 
            odd_count += 1
        i += 1

    return even_count, odd_count
array = [10, 21, 4, 45, 66, 93, 50] 

even_count, odd_count = count_even_odd(array)

sys.stdout.write(f"Number of even numbers: {even_count}\n")
sys.stdout.write(f"Number of odd numbers: {odd_count}\n")
