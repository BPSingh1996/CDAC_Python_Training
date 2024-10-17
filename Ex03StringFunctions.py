# String is a class in Python that come with functions that help in transforming the values based on the user
# requirement.
name = "bhanu pratap"
#No of characters in the string : len
print(len(name))
print(name.capitalize())
# capitalize every word in a string
print(name.title())
print(name.upper())

# find out if the string has only number:
print(name.isdigit())
#find out if the string has only alphabets:
print(name.isalpha())
#find out a character in string:
print(name.find('b'))
#find and replace
print(name.replace('a', 'aa'))

#print(dir(name))
#help(type(name))


#Every variable internally is an oblject in python. It has a method called id which could be used to identify the
# object. It is purely for understanding purpose.
num=123
print((id(num)))