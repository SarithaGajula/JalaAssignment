#Write a program to generate IOException.


import os
import sys

def read_from_device(device):
    try:
        # Try to read from a non-existent device
        with os.popen(device) as file:
            content = file.read()
    except IOError as e:
        sys.stdout.write(f"Error: {e}\n")
        sys.exit(1)

# Attempt to read from a non-existent device
read_from_device("/dev/non_existent_device")
