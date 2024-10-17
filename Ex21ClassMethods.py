# Methods that belong to a class but not to any instance is called as classmethods. Workds like Static methods of
# other programming languages. But unlike static methods, class methods can access instance data and instance members.

class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self,name,gpa):
        self.student_name = name
        self.student_gpa = gpa
        Student.count +=1
        Student.total_gpa +=gpa

    def get_student_info(self):
        return f"{self.student_name} {self.student_gpa}"
 #   @staticmethod
    @classmethod
    def get_count(cls):
        return f"The total no of Students are {cls.count} and the data is: {cls.__name__}" # it gets the class name

    @classmethod
    def get_all_gpa(cls):
        return f"The total GPA of the Students in the college is {cls.total_gpa:.2f}"

    @classmethod
    def get_avg_gpas(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The Avg gpa is {cls.total_gpa/cls.count:.2f}"

s1 = Student("Bhanu",6.5)
print(s1.get_student_info())
s2 = Student("Ramesh", 7.2)
print(s2.get_student_info())
s3 = Student("Rahul", 5.2)
print(s3.get_student_info())
s4 = Student("Ravi", 4.2)
print(s4.get_student_info())

print(Student.get_count())
print(Student.get_all_gpa())
print(Student.get_avg_gpas())

print(f"The average Gpa is {Student.total_gpa/Student.count:.2f}")