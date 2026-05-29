
# User input in Python 

name = input("Enter your name: ")
print(f"Hello, {name}")

# Even we entered a number, this treat as a String
age = input("Enter your age: ")
print(f"You are {age} years old")

print(type(name))
print(type(age))

# convert age to integer 
age = int(age)
print(type(age))

value = int("10")  # String to int
print(type(value)) 

value = float("3.14")  # String to float
print(type(value))

value = str(100)  # int to String
print(type(value))

value = bool("True")  # String to bool
print(type(value))
print(value)

value = bool(1) # int to bool, any non-zero integer is True, 0 is False'
print(type(value))
print(value)

# Comparion Operators 


current_salary = 30000
expected_salary = 35000

print(current_salary == expected_salary) # Equal to
print(current_salary > expected_salary) # Greater than
print(current_salary < expected_salary) # Less than
print(current_salary >= expected_salary) # Greater than or equal to
print(current_salary <= expected_salary) # Less than or equal to
print(current_salary != expected_salary) # Not equal to


# boolean logic 

has_python_skills = True
has_java_skill = True
has_backend_experience = True

print(has_python_skills and has_java_skill) # Logical AND
print(has_python_skills or has_java_skill) # Logical OR
print(not has_python_skills) # Logical NOT

if has_python_skills and has_backend_experience:
    print("You are eligible for the python backend developer role.")
elif has_java_skill and has_backend_experience:
    print("You are eligible for the Java backend developer role.")
else:
    print("You are not eligible for the backend developer role.")

