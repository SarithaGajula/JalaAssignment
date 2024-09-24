"""A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B. 
Call an overridden method with super class reference to B and C class’s objects"""




import sys

# Superclass A
class A:
    def specific_a1(self):
        sys.stdout.write("Method specific to class A1\n")
        
    def specific_a2(self):
        sys.stdout.write("Method specific to class A2\n")
    
    # Overridden method
    def override_method(self):
        sys.stdout.write("Override method in class A\n")

# Subclass B (inherits from A)
class B(A):
    def specific_b1(self):
        sys.stdout.write("Method specific to class B1\n")
    
    def specific_b2(self):
        sys.stdout.write("Method specific to class B2\n")
    
    # Overridden method
    def override_method(self):
        sys.stdout.write("Override method in class B\n")

# Subclass C (inherits from B)
class C(B):
    def specific_c1(self):
        sys.stdout.write("Method specific to class C1\n")
    
    def specific_c2(self):
        sys.stdout.write("Method specific to class C2\n")
    
    # Overridden method
    def override_method(self):
        sys.stdout.write("Override method in class C\n")

# Class with main method
class MainClass:
    @staticmethod
    def main():
        # Create objects of class B and C
        b_object = B()  # Object of class B
        c_object = C()  # Object of class C

        # Superclass reference to B and C class's objects
        a_ref_to_b = b_object  # A reference pointing to B object
        a_ref_to_c = c_object  # A reference pointing to C object

        sys.stdout.write("Calling overridden method using superclass reference to class B object:\n")
        a_ref_to_b.override_method()  # Calls B's override method
        
        sys.stdout.write("\nCalling overridden method using superclass reference to class C object:\n")
        a_ref_to_c.override_method()  # Calls C's override method

# Running the main method
MainClass.main()
