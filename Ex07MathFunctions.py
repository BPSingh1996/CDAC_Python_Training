# math is a std library provided by python for performing math operations within your app

import math # You shall use the APIs available in this library
x = math.pi
y = -5.6
z = 5
print(x)
result = round(x)
print(result)
print(y)
result = abs(y) # abs gives the no of digits from 0;
print(result)
result = max(x, y, z)
print(result)
result = min(x, y, z)
print(result)

result = math.ceil(x)
print(result)
result = math.floor(y)
print(result)
result = math.sqrt(81) # Gets the Square roof of a number
print(result)
result = pow(2, 6) # 2 to the power of 6
print(result)
# Explore other Functions of math for powerful math operations like logs, claculus operations, permutations and
# combinations
result = math.perm(8, 5) #no of ways to choose k(50 things from n(8) items.
print(result)

#Exercise 2 : Circumference of a cirle
radius = float(input("Enter the radius of the circle "))
cicumference = 2 * math.pi * radius
print(f"Circumference of the circle with {radius} is {cicumference} m")

# Area of a circle
radius = float(input("Enter the radius of the circle "))
area = math.pi * pow(radius,2)
print(f"Area of the circle with radius {radius} is {area}")

#Find the hypotenuse of a Triangle:
a = float(input("Enter the base of triangle "))
h = float(input("Enter the height of triangle "))
l = math.sqrt(pow(a,2) + pow(h,2))
print(l)