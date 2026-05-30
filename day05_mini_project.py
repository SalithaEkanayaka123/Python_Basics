# Day 5 - Functions and Clean Code
# Mini project: Job application tracker refactored with functions

#print("\n--- Job Application Tracker ---")
#    print("1. Add application")
#    print("2. View applications")
#    print("3. Search by company")
#    print("4. Count by status")
#    print("5. View unique companies")
#    print("6. Exit")

VALID_STATUSES = ("applied", "interview", "rejected", "selected")

def create_application (name, role, status :  str = "applied") -> dict[str, str]:
    return {
        "name" : name,
        "role" : role,
        "status" : status
    }

def add_application(applications : list[dict[str, str]]) -> None:
    name = input("Please enter the candidiate name: ").strip()
    role = input("Please enter the role: ").strip()
    status = input("status applied/interview/rejected/selected : ").strip().lower()
    while not validate_status(status):
        print("Invalid status. Please enter a valid status.")
        status = input("status applied/interview/rejected/selected : ").strip().lower()
    while not validate_name(name):
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Please enter the candidiate name: ").strip()
    while not validate_role(role):
        print("Role cannot be empty. Please enter a valid role.")
        role = input("Please enter the role: ").strip()

    application = create_application(name, role, status)
    applications.append(application)
    print("Application added successfully.")

def validate_status(status: str) -> bool:
    return status in VALID_STATUSES

def validate_name(name: str | None) -> bool:
    return name is not None and name.strip() != "" 

def validate_role(role : str | None)-> bool:
    return role is not None and role.strip() != ""

def view_applications(applications : list[dict[str, str]]) -> None:
    if len(applications) == 0:
        print("No applications found.")
    else:
        for index, application in enumerate(applications, start = 1):
            print(
                f"{index}. {application['name']} - "
                f"{application['role']} - "
                f"{application['status']}"
            )

def search_by_name(applications : list[dict[str, str]]) -> None:
    search_name = input("Please enter the candidate name for search: ").strip()

    for application in applications:
        if application["name"].strip().lower() == search_name.lower():
            print("Application found")
            print(application)
            return
    
    print("Application not found")

# get the count of each application status

def get_status_count(applications : list[dict[str, str]]) -> None:
    status_count = {}

    for application in applications:

        status = application["status"]

        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
    
    if len(status_count) == 0:
        print("No applications found.")
    

    print("Status count:")

    for status, count in status_count.items():
        print(f"{status}: {count}")

def view_unique_companies(applications: list[dict[str, str]]) -> None:
    names = []

    for application in applications:
        names.append(application["name"])

    unique_names = set(names)

    if len(unique_names) == 0:
        print("No names found")
        return

    print("Unique names:")

    for name in unique_names:
        print(name)

def display_menu() -> None:
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by names")
    print("4. Count by status")
    print("5. View unique names")
    print("6. Exit")

def run_application_tracker() -> None:
    applications = []

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            search_by_name(applications)
        elif choice == "4":
            get_status_count(applications)
        elif choice == "5":
            view_unique_companies(applications)
        elif choice == "6":
            print("Exiting application tracker")
            break
        else:
            print("Invalid choice")


run_application_tracker()

    
