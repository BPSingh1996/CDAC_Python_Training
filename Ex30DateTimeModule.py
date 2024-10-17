# DateTime module in python contains classes for working with Date and Time. with these APIs, you can perform
# operations on Date and Time like extractiong the System Date and Time, performing mathematical opertations on Date
# and Time.
import datetime as dt
from queue import PriorityQueue

#current datetime
now = dt.datetime.now()
print(f"Current Date and time is: {now}")

#current time:
time = now.strftime("%H: %M: %S")
print(time)

time = f"{now.time().hour} : {now.time().minute} : {now.time().second}"
print(time)

#current Date

date = dt.datetime.today()
date = now.strftime("%d-%m-%Y")
print(f"Today date is {date}")

#How about taking inputs from the user
dob = input("Enter the Date of birth as %d-%m-%Y  ")
date_of_birth = dt.datetime.strptime(dob,"%d-%m-%Y")
print(f"Your date of Birth is: {date_of_birth}")


#Todo: Calculate the age based on the date of birth:

def calculate_age(dateofbirth):
    today = dt.datetime.today()
    age = today.year - dateofbirth.year
    if(today.month, today) < (dateofbirth.month, dateofbirth.day):
        age -=1
    return age

dob = dt.datetime(1996,12,22)
age = calculate_age(dob)
print(age)

#Adding date
my_retirement_year = now.year + 4
print(f"The selected year is {my_retirement_year}")

#Adding days:
my_retirement_date = now + dt.timedelta(days=365)
print(f"The selected date is {my_retirement_date}")

#Subtract the days:
old_date = dt.date(2002,12,22)
diff = dt.datetime.now().date() - old_date
print(f"No of days: {diff.days}")