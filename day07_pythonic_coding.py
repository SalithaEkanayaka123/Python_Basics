# Normal loop vs list comprehension

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# Pythonic way:

squares = [ number * number for number in numbers ]
print(squares)

# List comprehension is a concise way to create a new list by applying an expression to each item in an existing iterable.

# List comprehension with condition

salaries = [200000, 266000, 300000, 350000, 400000]

high_salaries = [ salary for salary in salaries if salary > 300000 ]
print(high_salaries)

# Use list comprehension in job applications

applications = [
    {"company": "WSO2", "role": "Backend Engineer", "status": "applied"},
    {"company": "IFS", "role": "Software Engineer", "status": "interview"},
    {"company": "Virtusa", "role": "Senior Software Engineer", "status": "applied"},
    {"company": "Hatchyard", "role": "Java Developer", "status": "rejected"}
]

applied_applications = [ application for application in applications if application["status"] == "applied" ]
print(applied_applications)

# Dictionary comprehension

skills = ["Java", "Python", "SQL"]

skill_levels = { skill: "beginner" for  skill in skills}
print(skill_levels)

# Lambda function
# A lambda is a small anonymous function.

double = lambda number : number * 2
print(double(5))

# A lambda is an anonymous function used for short, simple operations. It is commonly used with functions like sorted, map, and filter.


# Sorting lists
salaries = [300000, 200000, 400000, 266000]

salaries.sort()
print(salaries)

# Decending order

salaries.sort(reverse=True)
print(salaries)

# sorted function returns a new sorted list without modifying the original list.

sorted_salaries = sorted(salaries)
print(sorted_salaries)
print(salaries) # original list is unchanged

# Sorting list of dictionaries

applications = [
    {"company": "WSO2", "role": "Backend Engineer", "salary": 350000},
    {"company": "IFS", "role": "Software Engineer", "salary": 300000},
    {"company": "Virtusa", "role": "Senior Software Engineer", "salary": 400000}
]

sorted_applications = sorted(
    applications,
    key = lambda application : application["salary"],
    reverse= True
)

for application in sorted_applications:
    print(f"company : {application['company']} - role : {application['role']} - salary : {application['salary']}")


# We can sort a list of dictionaries using sorted() with a key function. A lambda is often used to tell Python which field should be used for sorting.

# filter()

applications = [
    {"company": "WSO2", "status": "applied"},
    {"company": "IFS", "status": "interview"},
    {"company": "Virtusa", "status": "applied"}
]

applied_applications = list(
    filter(lambda application : application["status"] == "applied", applications)
)

print(applied_applications)

# map()

companies = ["wso2", "ifs", "virtusa"]

uppercase_companies = list(map(lambda company: company.upper(), companies))

print(uppercase_companies)

# any() and all()

skills = ["Java", "Spring Boot", "Python"]

has_python = any(skill == "Python" for skill in skills)

print(has_python)

scores = [80, 75, 90, 60]

all_passed = all(score >= 50 for score in scores)

print(all_passed)

# any() returns True if at least one item matches the condition. all() returns True only if every item matches the condition.
