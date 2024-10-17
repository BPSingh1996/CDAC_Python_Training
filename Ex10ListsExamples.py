# Python does not have the concept of arrays.
# Lists are the way of storing large amount of data and represent them as a single unit. You refer each element
# inside it by index operator []
# Lists = ordered, changable and you can have duplicate.
fruits = ["Apple","Mango","Orange"]
print(fruits)
print(fruits[0]) #Indexing is a way to refer each item in the List. it starts from 0.
print(fruits[1])
print(fruits[2])
#print(fruits[3])

for fruit in fruits:
    print(fruit)
print(len(fruits))
print(f"The no of fruits in our basket in {len(fruits)}")
print("Pinepple"in fruits) #False
print("apple" in fruits)   #False
print("Apple" in fruits)   #True

#print(dir(fruits))

#help(fruits)

fruits.append("Pineapple") # Adds the element to the bottom of the list.
print("Pineapple" in fruits)  # Now True

print(len(fruits))
print(fruits)
fruits.insert(1, "Guava")
print(fruits)
fruits.insert(0, "Kiwi")
print(fruits)
fruits.remove("Apple")
print(fruits)
fruits.sort() #Sorts the elements temporarily
print(fruits)
print(fruits[-1]) #Use -ve index to get the last item
print(fruits[2:4]) #returns 3rd and 4th item . Starts from index 2(included) and ends at index 4(excluded)
print(fruits[:3]) #from the start index to the 3rd index (excluding)
print(fruits[2:]) #from the 2nd index till the last

print(fruits)
######################################### Modifying the contents of the List ###############################
fruits[1:3] = ["Watermelon","Dragon Fruit"]
print(fruits)
fruits[1:3] = ["Watermelon","Dragon Fruit","Banana"]
print(fruits)

# If you insert more items than what Your intend to replace, the new items will be inserted from the location where
# you have specified.