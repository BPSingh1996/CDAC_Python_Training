# Functions : A block of reusable code that helps to use them as single line.
# We shall use () after the name of the function to call/invoke/use it.
# Any function has to be used in this flow: Declared and implemented before use. We create functions as a purpose of
# not having repeated code in our Applications.
# Functions can have paramenters or inputs for the function to work. These will be like inputs that you provide for
# the function for the function to do its job.


def simple_func():
    print("Hello Function")

def add_func():
    first_value = float(input("Enter the First Value: "))
    second_value = float(input("Enter the Second Value: "))
    result = first_value + second_value
    print(f"The Addition value is :{result}" )

def sub_func():
    first_value = float(input("Enter the First Value: "))
    second_value = float(input("Enter the Second Value: "))
    result = first_value - second_value
    print(f"The subtracted value is :{result}")

def mul_func():
    first_value = float(input("Enter the First Value: "))
    second_value = float(input("Enter the Second Value: "))
    result = first_value * second_value
    print(f"The multiple value is :{result}")

def div_func():
    first_value = float(input("Enter the First Value: "))
    second_value = float(input("Enter the Second Value: "))
    result = first_value / second_value
    print(f"The divisible value is :{result}")

# Syntax of calling a function

simple_func()


operation = input("Select a Math Operation: (A)dd, (S)ubtract, (M)ultiply or (D)ivide: ")
# if operation.upper() == "A":
#     add_func()
# elif operation.upper() == "S":
#     sub_func()
# elif operation.upper() == "M":
#     mul_func()
# elif operation.upper() == "D":
#     div_func()
# else:
#     print("Invalid Operation")

# Available from 3.10
match operation.upper():
    case "A" :
        add_func()
    case "S" :
        sub_func()
    case "M" :
        mul_func()
    case "D" :
        div_func()
    case  _  :
        print("Invalid Operation")