# Day 4 - Dictionary, Tuple, Set
# Mini project: Job application tracker using list of dictionaries

VALID_STATUSES = ("applied", "interview", "rejected", "selected")

applications = []

while True:
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by company")
    print("4. Count by status")
    print("5. View unique companies")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        company = input("Enter company name: ").strip()
        role = input("Enter role: ").strip()
        status = input("Enter application status (applied/interview/rejected/selected): ").strip().lower()

        if company == "" or role == "":
            print("Company and role cannot be empty.")
        elif status not in VALID_STATUSES:
            print("Invalid status. Please enter one of the following: applied, interview, rejected, selected.")
        else:
            application = {
                "company": company,
                "role": role,
                "status": status
            }
            applications.append(application)
            print("Application added successfully.")
    
    elif choice == "2":
        if len(applications) == 0:
            print("No applications found.")
        else:
            for index, application in enumerate(applications, start = 1):
                print(
                    f"{index}. {application['company']} - "
                    f"{application['role']} - "
                    f"{application['status']}"
                )
    
    elif choice == "3":
        search_company = input("Enter company name to search: ").strip()
        found = False

        for application in applications:
            if application["company"].lower() == search_company.lower():
                print("Application found:")
                print(application)
                found = True
                break
        
        if not found:
            print("Application not found.")
    
    elif choice == "4":
        status_count = {}

        for application in applications:
            status = application["status"]

            if status in status_count:
                status_count[status] += 1
            else:
                status_count[status] = 1

        print("Status count:")
        for status, count in status_count.items():
            print(f"{status}: {count}")

    elif choice == "5":
        companies = []

        for application in applications:
            companies.append(application["company"])

        unique_companies = set(companies)

        print("Unique companies:")
        for company in unique_companies:
            print(company)

    elif choice == "6":
        print("Exiting application tracker")
        break

    else:
        print("Invalid choice")


# Question 1 : What is a dictionary in Python? Answered above

# Difference between list and dictionary?

# A list stores values in order and is accessed by index.
#  A dictionary stores key-value pairs and is accessed by key.

# Question 3: Difference between list, tuple, and set?

#Type	Ordered	Mutable	Duplicates
#list	Yes	    Yes	    Yes
#tuple	Yes	    No	    Yes
#set	No	    Yes	    No

# Question 4: Why use tuple?

# Tuple is useful when we want to store values that should not be changed, 
# such as fixed statuses, coordinates, or constant configuration values.

