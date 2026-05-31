# Modules, Exceptions, JSON Files

# math_utils contines reusable codes for mathematical operations.

import math
print(math.sqrt(16))  # Using the sqrt function from math module
print(math.pi)

#Common built-in modules

import json
import os
import datetime

todday = datetime.date.today()
print(todday)

print(os.path.exists("day06_files_exceptions.py"))  # Check if the file exists

# Exception handling

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always be executed.")


#try     -> code that may fail
#except  -> handle the error
#finally -> always runs

# Common Python exceptions

# ValueError : invalid values, example: int("abc") gives a ValueError
#TypeError : Wrong data type, example: "abc" + 123 gives a TypeError
#KeyError : dictionary key not found, example: d = {"a": 1}; print(d["b"]) gives a KeyError
# FileNotFoundError : file not found, example: open("non_existent_file.txt") gives a FileNotFoundError
#ZeroDivisionError : division by zero, example: 10 / 0 gives a ZeroDivisionError

application = {
    "company": "WSO2",
    "status": "applied"
}

try:
    print(application["salary"])
except KeyError:
    print("Salary key not found")

print(application.get("salary", "Salary not available")) # better version

# JSON file handling

# Json looks very similar to Python dictionary/list 

applications = [
    {
        "company": "WSO2",
        "role": "Backend Engineer",
        "status": "applied"
    }
]

with open("applications.json", "w") as file:
    json.dump(applications, file, indent=4)

with open("applications.json", "r") as file:
    applications = json.load(file)

print(applications)

# JSON is commonly used for data exchange between systems and APIs. 
# In Python, the json module is used to convert Python objects to JSON and JSON back to Python objects.

# Why use with open()

with open("applications.json", "r") as file:
    data = file.read()

# with open() uses a context manager. It automatically closes the file after the block finishes, even if an error occurs.

