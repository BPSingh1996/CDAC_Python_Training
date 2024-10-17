# Magic methods are methods that are invoked automatically and can be customized as your overiding of those methods:
# __init__ is a magic method of Python. You don't call this method, explicitly, but internally called when you
# instantiateit.


class Employee:
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name

    def __str__(self):
        return f"{self.name} earns {self.salary}"


    def __eq__(self, other):
        return True if self.name == other.name and self.salary == other.salary else False

#As you create the Employee, your magic methods get called.
person1 = Employee("Bhanu",560000)
print(person1.name)
print(person1)

person2 = Employee("Rahul",560000)
print(person1 ==person2)