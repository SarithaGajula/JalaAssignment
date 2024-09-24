#Write a program to generate ClassNotFoundException


import sys

def import_class(class_name):
    try:
        __import__(class_name)
    except ImportError as e:
        sys.stdout.write(f"Error: {e}\n")
        sys.exit(1)

import_class("NonExistentClass")
