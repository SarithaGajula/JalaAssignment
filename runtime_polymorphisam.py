"""A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data members."""


import sys

# Superclass A
class A:
    def __init__(self):
        # Instance variable specific to class A
        self.data_member = "Data member in class A"

# Subclass B (inherits from A)
class B(A):
    def __init__(self):
        # Directly call A's constructor
        A.__init__(self)
        # Instance variable specific to class B
        self.data_member = "Data member in class B"

# Subclass C (inherits from B)
class C(B):
    def __init__(self):
        # Directly call B's constructor
        B.__init__(self)
        # Instance variable specific to class C
        self.data_member = "Data member in class C"

# Class with main method
class MainClass:
    def main(self):
        # Create objects of class B and C
        b_object = B()  # Object of class B
        c_object = C()  # Object of class C

        # Superclass reference to B and C class's objects
        a_ref_to_b = b_object  # A reference pointing to B object
        a_ref_to_c = c_object  # A reference pointing to C object

        # Access data members using superclass reference
        sys.stdout.write("Accessing data member using superclass reference to class B object:\n")
        sys.stdout.write(a_ref_to_b.data_member + "\n")  # Access data member of B
        
        sys.stdout.write("\nAccessing data member using superclass reference to class C object:\n")
        sys.stdout.write(a_ref_to_c.data_member + "\n")  # Access data member of C

# Create an instance of MainClass and run the main method
main_instance = MainClass()
main_instance.main()
