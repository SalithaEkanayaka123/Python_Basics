# Day 12 - Custom Exceptions and Business Error Handling

from dataclasses import dataclass


VALID_STATUSES = ("applied", "interview", "rejected", "selected")


class ApplicationError(Exception):
    """Base exception for application tracker errors."""
    pass


class InvalidStatusError(ApplicationError):
    """Raised when an invalid application status is used."""
    pass


class ApplicationNotFoundError(ApplicationError):
    """Raised when an application cannot be found."""
    pass


class DuplicateApplicationError(ApplicationError):
    """Raised when the same company and role already exist."""
    pass


@dataclass
class JobApplication:
    company: str
    role: str
    status: str

    def __post_init__(self) -> None:
        self.company = self.company.strip()
        self.role = self.role.strip()
        self.status = self.status.strip().lower()

        if self.company == "":
            raise ValueError("Company cannot be empty")

        if self.role == "":
            raise ValueError("Role cannot be empty")

        if self.status not in VALID_STATUSES:
            raise InvalidStatusError(f"Invalid status: {self.status}")

    def __str__(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, JobApplication):
            return False

        return (
            self.company.lower() == other.company.lower()
            and self.role.lower() == other.role.lower()
        )


class ApplicationTracker:
    def __init__(self):
        self.applications: list[JobApplication] = []

    def add_application(self, application: JobApplication) -> None:
        if application in self.applications:
            raise DuplicateApplicationError(
                f"Application already exists: {application.company} - {application.role}"
            )

        self.applications.append(application)

    def view_applications(self) -> None:
        if len(self.applications) == 0:
            print("No applications found")
            return

        for index, application in enumerate(self.applications, start=1):
            print(f"{index}. {application}")

    def find_by_company(self, company: str) -> JobApplication:
        for application in self.applications:
            if application.company.lower() == company.lower():
                return application

        raise ApplicationNotFoundError(f"No application found for company: {company}")

    def update_status(self, company: str, new_status: str) -> None:
        new_status = new_status.strip().lower()

        if new_status not in VALID_STATUSES:
            raise InvalidStatusError(f"Invalid status: {new_status}")

        application = self.find_by_company(company)
        application.status = new_status


def display_menu() -> None:
    print("\n--- Job Application Tracker With Custom Exceptions ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by company")
    print("4. Update status")
    print("5. Exit")


def run_tracker() -> None:
    tracker = ApplicationTracker()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                company = input("Enter company name: ")
                role = input("Enter role: ")
                status = input("Enter status applied/interview/rejected/selected: ")

                application = JobApplication(company, role, status)
                tracker.add_application(application)

                print("Application added successfully")

            elif choice == "2":
                tracker.view_applications()

            elif choice == "3":
                company = input("Enter company name: ").strip()
                application = tracker.find_by_company(company)

                print("Application found:")
                print(application)

            elif choice == "4":
                company = input("Enter company name: ").strip()
                new_status = input("Enter new status: ").strip()

                tracker.update_status(company, new_status)

                print("Status updated successfully")

            elif choice == "5":
                print("Exiting tracker")
                break

            else:
                print("Invalid choice")

        except ApplicationError as error:
            print(f"Application error: {error}")

        except ValueError as error:
            print(f"Validation error: {error}")


run_tracker()

# Understand
