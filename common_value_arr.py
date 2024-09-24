#Write a program to find the common values between two arrays



import sys

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

common_values = []

i = 0
while True:
    try:
        value1 = array1[i]
    except IndexError:
        break

    j = 0
    while True:
        try:
            value2 = array2[j]
        except IndexError:
            break

        if value1 == value2:
            common_values += [value1]  # Append to common_values

        j += 1
    i += 1

# Display common values using sys.stdout.write()
k = 0
while True:
    try:
        sys.stdout.write(str(common_values[k]) + " ")
        k += 1
    except IndexError:
        break

