# parameters are the way to inserting inputs to the functions. Any variable created in the function is limited to the
# function itself. So any values that YOu want to send to the Function should be sent in the form of arguments or
# parameters. Similarly, any values that YOu want to send outside the function is sent as output or return values. A
# function in Python can


# def add_func(v1,v2):
#     return v1+v2
#
# def sub_func(v1,v2):
#     return v1-v2
#
# def mul_func(v1,v2):
#     return v1*v2
#
# def div_func(v1,v2):
#     return v1/v2
#
# def calculate(v1,v2):
#     sum_value = add_func(v1,v2)
#     sub_value = sub_func(v1,v2)
#     mul_value = mul_func(v1,v2)
#     div_value = div_func(v1,v2)
#     return sum_value, sub_value, mul_value, div_value
#
# value = calculate(13,12) # Internally, the multiple return values will be a Tuple.
# print(f"The Added value is {value[0]}, Subtracted value is {value[1]}, Multiplied value is {value[2]}, Divided value "
#       f"is {value[3]:.2f}")

###############################################################################################

# 4 Kinds of parameters : Positional, Default, Keyword, Arbitrary
def display_invoice(name, amount, due_date):
    print(f"Hi Mr. {name}")
    print(f"An amount of ₹{amount} is pending from your End")
    print(f"The Last date for Payment is on {due_date}")
    print("Please ignore if already paid!!!!")
# In this scenario, the position of the paramenters shall not change when we pass the parameters into the function.
display_invoice("Bhanu", 4500, '21/12/2021')

################################################################################################
#Default Parameters:
def get_net_price(list_price, discount = 0, tax = 0.05 ):
    total_price = list_price * (1 - discount) * (1 * tax)
    return total_price
#Default parameters should not be followed by non-default parameters.
print(get_net_price(500))
#################################################################################################
# Keyword parameters: You can preced a parameter with its identifier and place them in any order
def greeting(message, title, name):
    print(f"{message}!!!!{title}{name}")
#When using keyword parameters, YOu could change the order of the parameters.
greeting(title ="Dr.", message="Good Afternoon", name="Bhanu Pratap")
#############################################################
#Variable no of arguments. You can pass multiple values to the function.
def add_numbers(*args):
    print(type(args))
    total = 0.0
    for arg in args:
        total += arg
    return total
# * is a wild char that imnplies multiple values.
print(add_numbers(1,2,3,4,5,6))

def get_address(**kwargs):
    print(f"{kwargs.get('flat_no')}, {kwargs.get('apartment_name')}, {kwargs.get('city')}, {kwargs.get('pin')}")
    print(type(kwargs))
# ** is a wild char that implies multiple keyword arguments. Internally they are dictionary
get_address(flat_no = 326, area = "RR Nagar", apartment_name = "Vastv Hillview-2", city="Bangalore", pin=560098)