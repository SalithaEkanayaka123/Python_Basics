# Day 11 - Polymorphism and Composition
# Mini project: Job application tracker with notification services

from abc import ABC, abstractmethod
from dataclasses import dataclass


VALID_STATUSES = ("applied", "interview", "rejected", "selected")


@dataclass
class JobApplication:
    company: str
    role: str
    status: str

    def __post_init__(self):
        if self.status not in VALID_STATUSES:
            raise ValueError("Invalid status")

    def __str__(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"


class NotificationService(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotificationService(NotificationService):

    def send(self, message: str) -> None:
        print(f"Email notification: {message}")


class SmsNotificationService(NotificationService):

    def send(self, message: str) -> None:
        print(f"SMS notification: {message}")


class ConsoleNotificationService(NotificationService):

    def send(self, message: str) -> None:
        print(f"Console notification: {message}")


class ApplicationTracker:
    def __init__(self, notification_service: NotificationService):
        self.applications: list[JobApplication] = []
        self.notification_service = notification_service

    def add_application(self, application: JobApplication) -> None:
        self.applications.append(application)
        self.notification_service.send(f"Application added: {application}")

    def view_applications(self) -> None:
        if len(self.applications) == 0:
            print("No applications found")
            return

        for index, application in enumerate(self.applications, start=1):
            print(f"{index}. {application}")

    def update_status(self, company: str, new_status: str) -> None:
        if new_status not in VALID_STATUSES:
            print("Invalid status")
            return

        for application in self.applications:
            if application.company.lower() == company.lower():
                application.status = new_status
                self.notification_service.send(f"Status updated: {application}")
                return

        print("Application not found")


def run_demo() -> None:
    notification_service = ConsoleNotificationService()
    tracker = ApplicationTracker(notification_service)

    app1 = JobApplication("WSO2", "Backend Engineer", "applied")
    app2 = JobApplication("IFS", "Software Engineer", "interview")

    tracker.add_application(app1)
    tracker.add_application(app2)

    print("\nApplications:")
    tracker.view_applications()

    print("\nUpdating status:")
    tracker.update_status("WSO2", "interview")

    print("\nApplications after update:")
    tracker.view_applications()


run_demo()

# Understand