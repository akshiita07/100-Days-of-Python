# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapperFunction(*args):
        output_val=function(*args)
        print(f"You called {function.__name__}{args}\nIt returned: {output_val}")
        return output_val
    return wrapperFunction

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)