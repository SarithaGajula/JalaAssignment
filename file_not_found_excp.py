#Write a program to generate FileNotFoundException



import os
import sys

def check_file_existence(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except FileNotFoundError as e:
        sys.stdout.write(f"Error: {e}\n")
        sys.exit(1)

check_file_existence("non_existent_file.txt")
