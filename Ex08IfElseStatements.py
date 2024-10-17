#If : Do some code only if some condition is TRUE or FALSE, else do another thing.

age = int(input("Enter the age for applying your Credit Card: "))

#Check for the validation:
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!!!")
elif age < 0:
    print("You are not even born!!!")
else:
    print("Your must be 18+ to sign up")

####################### Important Points #############################
'''
Python relies on indentation to define the scope.
elif : if the previous conditions are not true, then try this condition.
the if or elif should mathch for a boolean expression.
else isn't mandatory block.
'''


############################Ternery Operations in Python ####################