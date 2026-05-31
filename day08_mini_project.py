# Day 8 - Python OOP Basics
# Mini project: Job application tracker using classes

VALID_STATUSES = ("applied", "interview", "rejected", "selected")


class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status

    def update_status(self, new_status: str) -> None:
        if new_status not in VALID_STATUSES:
            print("Invalid status")
            return

        self.status = new_status
        print("Status updated successfully")

    def display_summary(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"

    def to_dict(self) -> dict[str, str]:
        return {
            "company": self.company,
            "role": self.role,
            "status": self.status
        }


class ApplicationTracker:
    def __init__(self):
        self.applications = []

    def add_application(self, application: JobApplication) -> None:
        self.applications.append(application)
        print("Application added successfully")

    def view_applications(self) -> None:
        if len(self.applications) == 0:
            print("No applications found")
            return

        for index, application in enumerate(self.applications, start=1):
            print(f"{index}. {application.display_summary()}")

    def search_by_company(self, company: str) -> JobApplication | None:
        for application in self.applications:
            if application.company.lower() == company.lower():
                return application

        return None

    def count_by_status(self) -> dict[str, int]:
        status_count = {}

        for application in self.applications:
            status = application.status

            if status in status_count:
                status_count[status] += 1
            else:
                status_count[status] = 1

        return status_count


def display_menu() -> None:
    print("\n--- OOP Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by company")
    print("4. Count by status")
    print("5. Update status")
    print("6. Exit")


def run_tracker() -> None:
    tracker = ApplicationTracker()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            company = input("Enter company name: ").strip()
            role = input("Enter role: ").strip()
            status = input("Enter status applied/interview/rejected/selected: ").strip().lower()

            if company == "" or role == "":
                print("Company and role cannot be empty")
                continue

            if status not in VALID_STATUSES:
                print("Invalid status")
                continue

            application = JobApplication(company, role, status)
            tracker.add_application(application)

        elif choice == "2":
            tracker.view_applications()

        elif choice == "3":
            company = input("Enter company name to search: ").strip()
            application = tracker.search_by_company(company)

            if application is None:
                print("Application not found")
            else:
                print("Application found:")
                print(application.display_summary())

        elif choice == "4":
            status_count = tracker.count_by_status()

            if len(status_count) == 0:
                print("No applications found")
            else:
                for status, count in status_count.items():
                    print(f"{status}: {count}")

        elif choice == "5":
            company = input("Enter company name: ").strip()
            application = tracker.search_by_company(company)

            if application is None:
                print("Application not found")
            else:
                new_status = input("Enter new status: ").strip().lower()
                application.update_status(new_status)

        elif choice == "6":
            print("Exiting application tracker")
            break

        else:
            print("Invalid choice")


run_tracker()

# understanding the code:
# This code implements a simple job application tracker using Object-Oriented Programming (OOP) concepts in Python.
# It defines two main classes: JobApplication and ApplicationTracker.
# JobApplication represents a single job application with attributes like company, role, and status.
# ApplicationTracker manages a collection of JobApplication instances and provides methods to add, view, search, and update applications.
# The run_tracker function provides a command-line interface for interacting with the tracker.
