
# UNDERSTANDING DECORATOR FUNCTIONS:
"""
def outer():
    print("I am outer")
    def inner():
        print("I am inner")
    return inner
    
fnc=outer()
fnc()
"""

import time
# DECORATOR FUNCTIONS: WRAP ANOTHER FUNCTION & GIVES IT ADDITIONAL FUNCTIONALITY:
def decorator_function(function):
    def wrapper_function(*args, **kwargs):
        # do something BEFORE the function
        time.sleep(2)
        function(*args, **kwargs)      #modify this fnc
        # do something AFTER the function
    return wrapper_function

@decorator_function
def say_hello():
    print("Hi guys")
    
def say_bye():
    print("Bye guys")
    
say_hello()
say_bye()