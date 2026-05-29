# Dictionary in Python 

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. 

application = {
    "company": "ABC company",
    "role": "Software Engineer",
    "status": "applied"
}

print(application)
print(application["company"])
print(application["role"])
print(application["status"])

# Access dictionary values using the get() method

print(application.get("company"))
print(application.get("role"))
print(application.get("status"))

# print(application["salary"]) This gives an error if the key does not exist. 
# print(application.get("salary")) this returns None if the key does not exist.

# Better
print(application.get("salary", "Not available"))

# Add and uppdate dictionary values

application = {
    "company": "ABC company",
    "role": "Software Engineer",
    "status": "applied"
}

application["location"] = "Sri Lanka"
application["status"] = "interview"
print(application)

# Loop through dictionary

for key, value in application.items():
    print(f"{key}: {value}")

for key in application.keys():
    print(key)

for value in application.values():
    print(value)

# List of dictionaries

applications = [
    {
        "company": "WSO2",
        "role": "Backend Engineer",
        "status": "applied"
    },
    {
        "company": "IFS",
        "role": "Software Engineer",
        "status": "interview"
    },
    {
        "company": "Hatchyard",
        "role": "Java Developer",
        "status": "rejected"
    }
]

for application in applications:
    print(f"Company: {application['company']}, Role: {application['role']}, Status: {application['status']}")


# Count applications by status

applications = [
    {"company": "WSO2", "role": "Backend Engineer", "status": "applied"},
    {"company": "IFS", "role": "Software Engineer", "status": "interview"},
    {"company": "Hatchyard", "role": "Java Developer", "status": "rejected"},
    {"company": "XigeniX", "role": "Full Stack Developer", "status": "applied"}
]

count = {}

for application in applications:
    status = application["status"]

    if status in count:
        count[status] += 1
    else:
        count[status] = 1

print(count)


# Search application by company

search_company = "IFS"


for application in applications:
    if application["company"] == search_company:
        print("Application found")
        print(application)
        break
    else:
        print("Application not found")

# Tuple in Python 

# Tuple is a like a list but it is immutable. Once a tuple is created, you cannot change its values.

application_statuses = ("applied", "interview", "rejected", "selected")

print(application_statuses)
print(application_statuses[0])

# we cannot change the values of a tuple
# application_statuses[0] = "pending" This gives an error

application_statuses[0] = "pending"


# Set in Python 
# A set is a collection of unique values. It is unordered and mutable.

skills = {"Java", "Python", "SQL", "Java", "Python"}

print(skills) # this will remove duplicates 

