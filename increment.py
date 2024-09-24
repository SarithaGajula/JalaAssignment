# Write a method for increment and decrement operators(++, --)

import sys
def increment(value):
    value += 1 
    sys.stdout.buffer.write(bytes("Incremented Value: " + str(value) + "\n", 'utf-8'))

def decrement(value):
    value -= 1  
    sys.stdout.buffer.write(bytes("Decremented Value: " + str(value) + "\n", 'utf-8'))
    
increment(10)  
decrement(10)  