# Decorators are a powerful tool to allow you to modify or extend the behavior of a function without permanently
# modifying the function itself.
# A Decorator is a function that takes another function as argument(CALLBACK FUNCTIONS) and then call this function
# inside this function before returning it back.\
#
from operator import rshift


#peroformance Monitoring
#Authentication and authorization

def my_func_formatter(func):
    def wrapper(*args):
        print("###################")
        result=func(*args)
        print(f"the result is {result}")
        print("*******************")
    return wrapper

@my_func_formatter
def say_hello(*args):
    print("Hello")


say_hello("bbh")

def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Calling Function: {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"Function {func.__name__} returned: {result}")
    return wrapper

@my_func_formatter
@logger
def add_func(a,b):
    return a+b

add_func(4,6)