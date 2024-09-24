#Write a program to check whether a file is having read access and write access permissions.


import os
import sys

class FilePermissions:
    def __init__(self, filename):
        self.filename = filename

    def check_permissions(self):
        read_access = os.access(self.filename, os.R_OK)
        write_access = os.access(self.filename, os.W_OK)
        return read_access, write_access

# Usage
filename = "example.txt"  # Replace with your file
permissions_checker = FilePermissions(filename)
readable, writable = permissions_checker.check_permissions()

# Output the results using sys.stdout.write
sys.stdout.write(f"Read access: {readable}\n")
sys.stdout.write(f"Write access: {writable}\n")
