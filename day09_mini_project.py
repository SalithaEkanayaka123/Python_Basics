from dataclasses import dataclass
from abc import ABC, abstractmethod


VALID_STATUSES = ("applied", "interview", "rejected", "selected")


@dataclass
class JobApplication:
    company: str
    role: str
    _status: str

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str) -> None:
        if new_status not in VALID_STATUSES:
            raise ValueError("Invalid status")

        self._status = new_status

    def display_summary(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"

    @classmethod
    def create_default(cls, company: str, role: str):
        return cls(company, role, "applied")


class ApplicationValidator:

    @staticmethod
    def is_valid_status(status: str) -> bool:
        return status in VALID_STATUSES

    @staticmethod
    def is_not_empty(value: str) -> bool:
        return value.strip() != ""


class NotificationService(ABC):

    @abstractmethod
    def notify(self, application: JobApplication) -> None:
        pass


class ConsoleNotificationService(NotificationService):

    def notify(self, application: JobApplication) -> None:
        print(f"Notification: Application updated - {application.display_summary()}")


class ApplicationTracker:
    def __init__(self, notification_service: NotificationService):
        self.applications: list[JobApplication] = []
        self.notification_service = notification_service

    def add_application(self, application: JobApplication) -> None:
        self.applications.append(application)
        print("Application added successfully")
        self.notification_service.notify(application)

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

    def update_status(self, company: str, new_status: str) -> None:
        application = self.search_by_company(company)

        if application is None:
            print("Application not found")
            return

        try:
            application.status = new_status
            print("Status updated successfully")
            self.notification_service.notify(application)
        except ValueError as error:
            print(error)


def display_menu() -> None:
    print("\n--- Advanced OOP Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by company")
    print("4. Update status")
    print("5. Exit")


def run_tracker() -> None:
    notification_service = ConsoleNotificationService()
    tracker = ApplicationTracker(notification_service)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            company = input("Enter company name: ").strip()
            role = input("Enter role: ").strip()
            status = input("Enter status or leave empty for default: ").strip().lower()

            if not ApplicationValidator.is_not_empty(company):
                print("Company cannot be empty")
                continue

            if not ApplicationValidator.is_not_empty(role):
                print("Role cannot be empty")
                continue

            if status == "":
                application = JobApplication.create_default(company, role)
            elif ApplicationValidator.is_valid_status(status):
                application = JobApplication(company, role, status)
            else:
                print("Invalid status")
                continue

            tracker.add_application(application)

        elif choice == "2":
            tracker.view_applications()

        elif choice == "3":
            company = input("Enter company name: ").strip()
            application = tracker.search_by_company(company)

            if application is None:
                print("Application not found")
            else:
                print(application.display_summary())

        elif choice == "4":
            company = input("Enter company name: ").strip()
            new_status = input("Enter new status: ").strip().lower()
            tracker.update_status(company, new_status)

        elif choice == "5":
            print("Exiting tracker")
            break

        else:
            print("Invalid choice")


run_tracker()