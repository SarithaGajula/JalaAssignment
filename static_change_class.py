#Define a static variable and change within the class


class MyClass:
    static_var = 0  

    @classmethod
    def change_static_var(cls, value):
        cls.static_var = value  
MyClass.change_static_var(20)
import sys
sys.stdout.write(str(MyClass.static_var) + '\n') 
