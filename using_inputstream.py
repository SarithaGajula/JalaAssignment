#Write a program to write text to .txt file using InputStream


import sys

def write_to_file(file_path):
    sys.stdout.write("Please provide text (end with Ctrl+D or Ctrl+Z):\n")
    
    # Read from standard input until EOF
    text = sys.stdin.read()

    # Write the captured input to a file
    with open(file_path, 'w') as file:
        file.write(text)

# Specify the path to your text file
file_path = 'output.txt'  # Change this to your desired file path
write_to_file(file_path)

sys.stdout.write(f"Text has been written to {file_path}\n")
