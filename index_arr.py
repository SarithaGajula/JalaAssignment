#without using python predefined function



def find_index(array, target):
    i = 0
    while True:
        try:
            if array[i] == target:
                return i  # Return the index if found
        except IndexError:
            break
        i += 1
    return -1  # Return -1 if the element is not found

# Example usage
array = [10, 20, 30, 40, 50]
target = 30
index = find_index(array, target)

# Display the index using sys.stdout.write()
import sys
sys.stdout.write("Index of " + str(target) + ": " + str(index))
