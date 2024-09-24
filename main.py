"""A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance."""



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
        # Create objects for class A, B, and C
        sys.stdout.write("Calling methods from class A:\n")
        a = A()
        a.specific_a1()
        a.specific_a2()
        a.override_method()

        sys.stdout.write("\nCalling methods from class B:\n")
        b = B()
        b.specific_b1()
        b.specific_b2()
        b.override_method()

        sys.stdout.write("\nCalling methods from class C:\n")
        c = C()
        c.specific_c1()
        c.specific_c2()
        c.override_method()

# Running the main method
MainClass.main()
