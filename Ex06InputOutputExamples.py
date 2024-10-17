#Exercise 1 : Rectangle area calculator

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
area = length * breadth
print(f"The area of the rectangle is {area:} cm²") #WindowKey + Alt + 0178 to print square symbol



# #Exercise 2: Shopping Cart app:

item = input("What item you want to buy? ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
totalbill = price * quantity
print(f"You have bought {quantity} {item}s")
print(f"The total bill is Rs. ₹{totalbill}") #Ctrl+Alt+4 can be used to print Rupee sumbol.



#Exercise 3: Program to calculate the square of a number

number = float(input("Enter the number: "))
square = number * number
print(f"Square of {number} is {square}")



#Exercise 4 : word filling game.

adjective1 = input("Enter an adjective (Description): ")
noun1 = input("Enter a noun (person, place or a thing): ")
adjective2 = input("Enter and adjective ( Description): ")
verb1 = input("Enter a verb ending with ing: ")
adjective3 = input("Enter and adjective ( Description): ")
print(f"Today I went to {adjective1} zoo!")
print(f"In the zoo, I saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")