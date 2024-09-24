#Write a program to read a file stream supports random access

import io

# Simulating file content with BytesIO (you can replace this with an actual file stream)
file_stream = io.BytesIO(b"Hello, this is a random access file stream example.")

# Move to a particular index (random access)
file_stream.seek(18)  # Randomly jumping to index 18

# Read a portion of the file after seeking
content = file_stream.read(20)  # Read 20 bytes from the current position

# Output the read content using sys.stdout.write
import sys
sys.stdout.write(content.decode())  # Decoding bytes to string

# You can use file_stream.seek(0) to move back to the start and read again if needed
