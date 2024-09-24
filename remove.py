#Write a function to remove a specific element from an array.


def remove_element(array, target):
    new_array = []
    
    i = 0
    while True:
        try:
            value = array[i]
        except IndexError:
            break
        
        if value != target:  # Only add elements that are not the target
            new_array += [value]
        
        i += 1
    
    return new_array

# Example usage
array = [10, 20, 30, 40, 50, 30]
target = 30
new_array = remove_element(array, target)

# Display the new array using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(new_array[i]) + " ")
        i += 1
    except IndexError:
        break
