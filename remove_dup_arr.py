#Write a method to remove duplicate elements from an array



def remove_duplicates(array):
    unique_elements = []
    
    i = 0
    while True:
        try:
            value = array[i]
        except IndexError:
            break
        
        # Check if the value is already in unique_elements
        found = False
        j = 0
        while True:
            try:
                if unique_elements[j] == value:
                    found = True
                    break
            except IndexError:
                break
            j += 1
        
        # If not found, append it to unique_elements
        if not found:
            unique_elements += [value]
        
        i += 1
    
    return unique_elements

# Example usage
array = [10, 20, 10, 30, 40, 20, 50]
new_array = remove_duplicates(array)

# Display the new array using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(new_array[i]) + " ")
        i += 1
    except IndexError:
        break
