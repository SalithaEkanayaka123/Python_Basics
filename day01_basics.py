# day 1 - python basics 

name = "Salitha"
age = 27
salary_expectation = 35000.0
is_java_developer = True

print("Name:", name) # str
print("Age:", age) # int
print("Salary Expectation:", salary_expectation) # float
print("Is Java Developer:", is_java_developer) # bool

# Data Types 
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of salary_expectation:", type(salary_expectation))
print("Type of is_java_developer:", type(is_java_developer))

# Learn Dynamic Typing 

value = "Salitha"
print("Type of value:", type(value))
value = 100
print("Type of value after reassignment:", type(value))

# Python allow this because it is dynamically typed language, 
# we can change the type of variable by reassigning it

# Arithmetic practice 

basic_salary = 30000
expected_salary = 35000

difference = expected_salary - basic_salary
percentage_increase = (difference / basic_salary) * 100

print("Difference in Salary:", difference)
print("Percentage Increase:", percentage_increase, "%")

print(10 + 5) # Addition
print(10 - 5) # Subtraction
print(10 * 5) # Multiplication
print(10 / 5) # Division
print(10 // 3) # Floor Division
print(10 % 3) # Modulus
print(10 ** 2) # Exponentiation

# String indexing and slicing

role = "Senior Software Engineer"
print("First character:", role[0]) # S
print(role[1]) # Second character
print(role[-1]) # Negative indexing, -1 is the last character, -2 is the second last character and so on.

print(role[0:6]) # Slicing, from index 0 to 5 (6 is exclusive)
print(role[7:15]) # Slicing, from index 7 to 14 (15 is exclusive)
print(role[:6]) # Slicing, from the beginning to index 5 (6 is exclusive)
print(role[7:]) # Slicing, from index 7 to the end of the string
print(role[::-1]) # Slicing with step, from the end to the beginning, step -1 means reverse the string

#Python String are indexed from 0. Negative indexes start from the end. Slicing allows part of a string using 
# [start:end:step]


# String methods 

message = " python developer interview "

print(message.upper()) # Convert to uppercase
print(message.lower()) # Convert to Lowercase
print(message.title()) # Convert to Title Case
print(message.strip()) # Remove leading and trailing whitespace
print(message.replace("python", "java")) # Replace substring
print(message.find("developer")) # Find substring, returns the index of the first occurrence, -1 if not found

# String in python are immutable, String methods return a new string of changing the original string. 

# f-string formatting
# Use this style in modern Python

name = "Salitha"
role = "Python Backend Developer"
experience = 4

print(f"My name is {name}. I am learning to become a {role} with {experience}+ years of backend experience.")
