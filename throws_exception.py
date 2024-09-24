#Write a method which throws exception, Call that method in main class without try block


class CustomException(Exception):
    pass

def method_that_throws():
    raise CustomException("Custom Exception: Something went wrong.")

# Calling the method without a try block
method_that_throws()

# This will raise the exception and crash the program without handling
