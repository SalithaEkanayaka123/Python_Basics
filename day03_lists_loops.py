

# Exercise 1 

technology_list = ["Python", "Java", "React", "Node Js", "Angular"]

for technology in technology_list:
    print(f"technology: {technology}")

# Exercise 2
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

print(f"Total: {total}")

# Exercise 3

salaries = [200000, 266000, 300000, 350000, 400000]

for salary in salaries:
    if salary > 300000:
        print(f"{salary} is greater than 300000")

# Exercise 4

statuses = ["applied", "interview", "rejected", "applied", "selected"]

for status in statuses:
    if status == "applied":
        print("Waiting for response")
    elif status == "interview":
        print("Preparing for interview")
    elif status == "rejected":
        print("Keep trying")
    elif status == "selected":
        print("Congratulations! You got the job!")

# Exercise 5

companies = []

for i in range(5):
    company = input("Enter a company name : ")
    companies.append(company)

print(f"Company List: {companies}")

# Exercise 6

skills = ["Java", "Spring Boot", "SQL", "Docker", "Python"]

if "Python" in skills:
    print("Python skill found")
else:
    print("Python skill not found")

#Exercise 7
applications = []

while True:
    print("\n1. Add application")
    print("2. View applications")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        company = input("Enter company name: ")
        role = input("Enter role: ")
        applications.append(f"{company} - {role}")
        print("Application added successfully")

    elif choice == "2":
        print("\nApplications:")
        for application in applications:
            print(application)

    elif choice == "3":
        print("Exiting application tracker")
        break

    else:
        print("Invalid choice")

