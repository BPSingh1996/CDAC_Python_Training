# File Reading writing is done using the built in global methods
'''
File Modes for read/write the files:
w : writing overwrites if the file exists.
r : reading, Default mode
a : append mode: Appends the file and the data is added at the end of the file.
x : Exclusive creation, creates a new file and writes to it, if the file exists raises an Exception
t : Text mode, opening the file as text file.
* : wild character for both reading and writing
'''
from fileinput import filename

##################################### Writing a text file #################################
file_name = "SampleFile.txt"
try:
    with open(file_name,'x') as file:
        file.write("Hello world from Python into a file")
        print(f".txt file '{file_name} has been created successfully")
except FileNotFoundError as err:
    print(f"Error Details: {err}")
except Exception as genEx:
    print(f"Unknown error: {genEx}")

############################### Writing Json data ###########################################
# JSON : Javascript object Notation.
import json # json file operations
empRecord = [{
                "empId": 123,
                "empName":"Bhanu Pratap",
                "empAddress":"Delhi",
                "salary": 90000
},{

                "empId": 321,
                "empName":"Ramesh",
                "empAddress":"Meerut",
                "salary": 90000
}]

file_name = "emprecords.json"
try:
    with open(file_name, 'w') as file:
        json.dump(empRecord,file,indent=4)
        print(f"Json data stored successfully ")
except FileNotFoundError as err:
    print(f"Error Details: {err}")
except Exception as genEx:
    print(f"Unknown error: {genEx}")

################################### Converting an List of Employees to JSON file ########################
class Customer:
    def __init__(self,name,address,bill):
        self.csname = name
        self.address = address
        self.bill = bill

    def to_dict(self):
        return {"csname" : self.csname,"address":self.address,"Bill":self.bill}

def writeJsonFile(jsondata,fileName):
    try:
        with open(fileName,'w') as file:
            json.dump(jsondata, file, indent=4)
    except Exception as e:
        print(f"{e}")



customers = [Customer("Bhanu","Delhi",4900),
             Customer("Pratap","Mumbai",7900),
             Customer("Rahul","Pune",9000)]

jsonObjects = [cst.to_dict() for cst in customers]

json_data = json.dumps(jsonObjects)

writeJsonFile(jsonObjects, "Customers.json")
