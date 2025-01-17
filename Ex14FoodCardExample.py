# Example of Food Cart
food_items = {
    "Idly" : 25,
    "Masala Dosa" : 65,
    "Coffee" : 15,
    "Tea" : 15,
    "Rice Item" : 35
} #Dictionary of Food Items and their price tag.

bill_amount = 0
items = {}   #Dictionary of purchased items
is_processing = True
while is_processing:
    print("######################MENU############################")
    for food_item, price in food_items.items():
        print(f"{food_item}: ₹{price:.2f}")
    item = input("Enter the food Item from the list above: or (q) to Quit: ").title()
    if item.lower() == "q":
        break
    elif item not in food_items.keys():
        print("This item is not available with Us!!!!")
        break
    quantity = int(input("Enter the quantitity of the food U want: "))
    items[item] = food_items[item] * quantity  #storing the values in dictionary as key and value
print(f"#################Itemized Bill####################")
for key in items.keys():
    bill_amount += items[key]
    print(f"Item Name: {key}, Unit Price: ₹{food_items[key]}, Quantity: {items[key]/food_items[key]} Total: ₹"
          f"{items[key]:.2f}")
print(f"The Total Bill: {bill_amount}")