#Write a program to read text file


import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                sys.stdout.write(line)
    except FileNotFoundError:
        sys.stdout.write("File not found: " + file_path + "\n")
    except Exception as e:
        sys.stdout.write("An error occurred: " + str(e) + "\n")

# Specify the path to your text file
file_path = 'example.txt'  # Change this to your file path
read_file(file_path)
