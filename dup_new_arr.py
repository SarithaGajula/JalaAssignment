# Write a program to remove the duplicate elements and return the new array




def remove_duplicates(array):
    unique_elements = []
    
    i = 0
    while True:
        try:
            value = array[i]
        except IndexError:
            break
        
        if value not in unique_elements:
            unique_elements += [value]  # Append if it's not a duplicate
        
        i += 1
    
    return unique_elements

# Example usage
array = [1, 2, 3, 2, 4, 5, 1, 6, 5]
new_array = remove_duplicates(array)

# Display new array using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(new_array[i]) + " ")
        i += 1
    except IndexError:
        break

