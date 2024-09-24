#Write a program to read a file stream


import sys

def read_file_stream():
    sys.stdout.write("Reading from file stream (end with Ctrl+D or Ctrl+Z):\n")
    
    # Read from standard input until EOF
    text = sys.stdin.read()
    
    # Output the read content
    sys.stdout.write("Content read from the stream:\n")
    sys.stdout.write(text)

# Call the function to read from the file stream
read_file_stream()
