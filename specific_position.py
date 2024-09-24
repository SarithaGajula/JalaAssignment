#Write a function to insert an element at a specific position in the array



def insert_element(array, position, element):
    new_array = []
    i = 0
    added = False

    while True:
        try:
            if i == position:
                new_array += [element]  # Insert the element at the specified position
                added = True

            new_array += [array[i]]  # Append the current element
            i += 1

        except IndexError:
            if not added:
                new_array += [element]  # If the position is at the end, add the element here
            break

    return new_array

# Example usage
array = [10, 20, 30, 40, 50]
position = 2
element = 25
new_array = insert_element(array, position, element)

# Display the new array using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(new_array[i]) + " ")
        i += 1
    except IndexError:
        break
