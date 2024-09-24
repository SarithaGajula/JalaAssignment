#Define variables for different Data Types int, Boolean, char, float, double and print on the Console.



import sys

int_var = 10         
float_var = 10.5      
bool_var = True       
str_var = 'A'   


# Convert integer to bytes and write
sys.stdout.buffer.write(bytes(str(int_var), 'utf-8'))
sys.stdout.buffer.write(b'\n')  # Newline

#In python douuble data type is not there.
# Convert float to bytes and write
sys.stdout.buffer.write(bytes(str(float_var), 'utf-8'))
sys.stdout.buffer.write(b'\n')  # Newline

# Convert boolean to bytes and write
sys.stdout.buffer.write(bytes(str(bool_var), 'utf-8'))
sys.stdout.buffer.write(b'\n')  # Newline

# Convert char (string of length 1) to bytes and write
sys.stdout.buffer.write(bytes(str_var, 'utf-8'))
sys.stdout.buffer.write(b'\n')  # Newline