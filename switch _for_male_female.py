#Print gender (Male/Female) program according to given M/F using switch.


import sys

def get_gender(code):
    if code == 'M':
        return "Male"
    elif code == 'F':
        return "Female"
    else:
        return "Invalid Input"

input_code = 'M' 
result = get_gender(input_code)
sys.stdout.write(f'The gender for code "{input_code}" is {result}.\n')
