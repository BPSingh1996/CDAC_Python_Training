# Inheritance: A feature of OOP that allows to extend a class to add new methods and modify existing features for a
# given class, as the class is immutable.
#The class that does not have any base class is called as PARENT/SUPER/BASE class.
class BaseClass:
    def base_func(self):
        print("Base class function")

# The class that extends is called as CHILD/SUB/DERIVED class.
class DerivedClass(BaseClass): #Syntax of inheritance in Python
    def derived_func(self):
        print("Drived class function")

#Unlike C++, We dont have private or public inheritance, all the members of the base class can automatically get
# derived in the derived class.
obj = DerivedClass()
obj.base_func()
obj.derived_func()

#############################################################################################
class Account:
    def __init__(self,holder, initialAmount):
        self.account_holder = holder
        self.balance = initialAmount
# If a base class has a parameterized init, the derived class init must pass the values before any action is done
# with itself. You refer the immediate base class using super keyword.
class SBAccount(Account):
    def __init__(self,name, amount):
        super().__init__(name,amount)
        print("SB Account Created")

    def calc_interest(self):
        interest = self.balance * (6.5/100) * 0.25
        self.balance += interest
        return interest
  #      return self.balance

acc = SBAccount("Bhanu",50000)
print(f"Intrest is {acc.calc_interest()}")
print(acc.balance)
print(acc.account_holder)
