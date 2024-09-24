#Write a function to find the duplicate values of an array.


def find_duplicates(array):
    duplicates = []
    seen = []

    i = 0
    while True:
        try:
            value = array[i]
        except IndexError:
            break

        if value not in seen:
            seen += [value]  # Add to seen list
        else:
            if value not in duplicates:
                duplicates += [value]  # Add to duplicates list

        i += 1

    return duplicates

# Example usage
array = [1, 2, 3, 2, 4, 5, 1, 6, 5]
duplicates = find_duplicates(array)

# Display duplicate values using sys.stdout.write()
import sys
i = 0
while True:
    try:
        sys.stdout.write(str(duplicates[i]) + " ")
        i += 1
    except IndexError:
        break

