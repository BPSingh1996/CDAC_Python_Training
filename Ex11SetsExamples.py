# sets: unordered and ummutable collections but can hold only unique values in it. It can allow to add and remove
# items from it.
# sets are created using {} braces.
names = { "Phani","Vinot","Bhanu","Ramnath","Joydip"}
print(names)
for name in names:
    print(name)
#print(names[1]) #As the Sets are unordered, You cannot use indexing to the collection.You cannot alter the items in
# the set, however, You can add/remove items from the set.
#prints the values in unordered manner.

names.add("Murali")
print(names)

#Addding bulk records:
trainers = {"Krishna","Nathan","Somnath"} #Adding another set into the current set.
names.update(trainers)
print(names)
#Removing items from the set:
# remove and discard function: remove throws an error if an item is not found to remove from the set, but discard
# shall not throw any exception.
names.remove("Bhanu")
print(names)
names.discard("Vinot")
print(names)

#How many ways can we remove items in colllection: 4 ways: remove, discard, pop and clear.
names.add("Bhanu")
print(names)
