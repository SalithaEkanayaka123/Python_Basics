# Functions

# Functions are reusable pieces of code that perform a specific task. 

def hello_world():
    print("Hello World!")

hello_world()  # Calling the function

# Returning function 

def add(a, b):
    return a + b

print(f"addition : {add(5,3)}")

# multiple parameters 

def profile(name, role, experience):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Experience: {experience} years")    

profile("John Doe", "Software Engineer", 5)

# Functions with default parameters 

def profile_overview(name, role, experience = 5):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Experience: {experience} years")

profile_overview("John Doe", "Software Engineer")   
profile_overview("John Doe", "Software Engineer", 6) 

# Default parameters allow us to provide a default value if the caller does not pass that argument.

# Return tuple values 
def profile_overview_2(name, role, experience = 5):
    return {
        "name" : name,
        "role" : role,
        "experience" : experience
    }

profile_1 = profile_overview_2("John Doe", "Software Engineer")
print(profile_1)


#Type hints
# Type hints are used to denote what type the function is returning 

def profile_overview_3(name: str, role: str, experience: int = 5) -> dict:
    return {
        "name" : name,
        "role" : role,
        "experience" : experience
    }

profile_2 = profile_overview_3("John Doe", "Software Engineer")
print(profile_2)


# Clean code idea

# Principles that used to write a clean code in an understandable way.
# 1. Meaningful names

def calculate_salary_difference(current_salary, expected_salary):
    return expected_salary - current_salary

# 2. Single responsibility principle
# 3. Avoid side effects
# 4. Keep functions small
# 5. One function should do one main thing
# 6. Avoid repeated code
# 7. Use constants for fixed values
# 8. Validate user input
# 9. Return values instead of printing inside every function when possible

# Important interview warning: mutable default argument

# Do not do below
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

# Mutable default arguments like lists or dictionaries can keep state between function calls. 
# A safer approach is to use None as the default and create the list inside the function.

def add_skills_safe(skill, skills = None):
    if skills is None:
        skills = []
    skills.append(skill)
    return skills






