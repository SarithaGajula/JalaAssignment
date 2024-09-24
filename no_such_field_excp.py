#Write a program to generate NoSuchFieldException.


import sys

class SampleClass:
    existing_field = "This field exists."

def access_field(obj, field_name):
    try:
        value = obj.__dict__[field_name]  # Attempt to access the attribute
    except KeyError:
        sys.stdout.write(f"Error: No such field: '{field_name}'\n")
        sys.exit(1)

# Create an instance of SampleClass without using __init__
sample = SampleClass()

# Attempt to access a non-existent field
access_field(sample, "non_existent_field")
