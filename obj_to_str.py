#Converting integer objects to Strings



import sys

# Input integer
number = 12345

# Function to convert an integer to a string
def int_to_string(num):
    if num == 0:
        return "0"  # Handle the case for zero

    is_negative = num < 0
    if is_negative:
        num = -num  # Work with the absolute value for conversion

    string_representation = ""

    # Extract digits and build the string representation
    while num > 0:
        digit = num % 10  # Get the last digit
        string_representation = chr(48 + digit) + string_representation  # '0' has an ASCII value of 48
        num //= 10  # Remove the last digit

    if is_negative:
        string_representation = '-' + string_representation

    return string_representation

result = int_to_string(number)
sys.stdout.write(f"Integer: {number}, String: '{result}'\n")
