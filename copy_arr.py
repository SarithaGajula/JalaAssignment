#Write a function to copy an array to another array.


def copy_array(source):
    destination = []
    i = 0

    while True:
        try:
            value = source[i]
        except IndexError:
            break

        destination += [value]  # Append to destination
        i += 1

    return destination

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = copy_array(array1)

# Display copied array using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(array2[i]) + " ")
        i += 1
    except IndexError:
        break

