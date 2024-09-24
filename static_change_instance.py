#Define a static variable and change within the instance



import sys

class MyClass:
    static_var = 0  

    def change_static_var(self, value):
        MyClass.static_var = value  
instance = MyClass()
instance.change_static_var(10)
sys.stdout.write(str(MyClass.static_var) + '\n')  

