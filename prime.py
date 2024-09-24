#Write a program to find the prime or not.


def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    i = 2
    while i * i <= number:  # Check divisibility up to the square root of the number
        if number % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
        i += 1

    return True  # If no divisors are found, it's prime

# Example usage
number = 29
result = is_prime(number)

# Display the result using sys.stdout.write()
import sys
if result:
    sys.stdout.write(str(number) + " is a prime number")
else:
    sys.stdout.write(str(number) + " is not a prime number")
