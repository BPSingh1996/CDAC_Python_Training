#Variables = A Containers for a value. It behaves like the valure that it contains.
# Srtings are the way to store characters in Python. All inputs and outpurs shall be strings. U may have to convert
# to other data types if U want to do some calculations.

name = 'Bhanu' # variable in python.\
print(name) # don't use the "" while using the variables.

name = 'Bhanu Pratap' #variables allow to change the value any time in the course of the program.
#If a variable has 2 or more words U should seperate them using _.
first_name = "Bhanu"
last_name = "Singh"
mid_name = 'Pratap'
full_name = first_name + " " + last_name
print(full_name)
print(f"{first_name} {mid_name}")

# if you want to know the kind of varialbe your are using we can use type function.
print(type(full_name)) # the data type is string
####################### int data type ################################################
age = 27
age+=3
print(age)
#we use other data types only if we are computing any mathematical functionality.
print("The data type of age is " + str(type(age)))
print("UR age is " + str(age)) #old stype
print(f"UR age is {age}") # new stype using f(ormat) string.

############################# float data type ############################################
height = 23.45 # decimal values wer use floats.
print(height)
print(type(height)) #class 'float'
print("Your height is " + str(height) + " inches")
print(f"Your height is {height} inches")
print(f"YOUR HEIGHT IS {height}") # no need to typecast


############################ boolean data type ###########################################
is_male = True # True , T is uppercase
print(is_male)
print(type(is_male))
print(int(is_male)) # use int() to typecast to int so that U can evaluate it to 0 or 1.


####################### Important Points #####################################################
'''
Naming conventions :
lowercase, underscore_between_words. should not start with numbers.
There is no specific type for numbers and floats. A variable could hold either 
Python allows extremly large values for numerical without loosing any precision 
Strings with "" or '' are same. Its only a matter of convenience.
Bool values should be True or False and is case sensitive. 
All conventions and coding stds are defined by PEP (Python Enhancement Proposal).
Currently it is PEP 8
If a varable is declared but not assignmed. it is None. In the context of the boolean it is False.
'''
name, age, attractive = 'Bhanu' , 27, True
print(f"{name} is of {age} years and his personality is {attractive}")

bhanu = rajan = ram = 27
#alll the variables will have the same value
print(f"{bhanu}, {rajan}, {ram}")