#b Lambda Function = Short functions that have only one expression. They are small anonymous function that can be
# defined using lambda keyword and can have one expression statement in it.
# It is created when you want to use the function for a small period of time, like callback functions.
from xml.sax import make_parser

# def add(a,b):
#     return a + b


add = lambda a, b : a + b
result = add(13,12)
print(result)

max_value = lambda x,y : x if x>y else y
print(max_value(14,15))

is_even = lambda x : x % 2 == 0
age_validation = lambda x : True if x >= 18 else False


print(is_even(20))
print(is_even(19))
print(age_validation(32))
if age_validation(13):
    print("You can vote")
else:
    print("You are not 18 to vote")

# Practically,Lambda is used for callback functions, some builtin functions of python that came after 3.10 uses these
# lambdas for filtering, reducing, sorting operations.

grades = [90,45,67,56,62,89,24,67]
passing_grades = list(filter(lambda grade : grade > 60, grades))
even_grades = list(filter(lambda grade : grade % 2 == 0, grades))
odd_grades = list(filter(lambda grade : grade % 2 != 0,grades))

#Exercise 1: With the grades, get me the list of all even grades and odd grades.

print(passing_grades)
print(even_grades)
print(odd_grades)

#################################### Map Feature in Python #############################
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(grades)
results = list(map(lambda grade : "pass" if grade > 40 else "Fail", grades))
print(results)
square_numbers = list(map(lambda num : num*num, numbers))
print(square_numbers)

################################Sorting Feature in Python#############################
users = {"Bhanu Pratap": "apple123", "aditya" : "test123", "Kumar":"myPad","ram":"rma@123"}
# Sorting the values based on keys:
sorted_users = sorted(users, key = lambda x : x[1])
print(sorted_users)