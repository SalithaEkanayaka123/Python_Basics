# Day 6 - Modules, Exceptions, and JSON File Handling
# Mini project: Job application tracker with file persistence

import json
import os

VALID_STATUSES = ("applied", "interview", "rejected", "selected")
FILE_NAME = "applications.json"


def display_menu() -> None:
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search by company")
    print("4. Count by status")
    print("5. Save applications")
    print("6. Load applications")
    print("7. Exit")


def is_valid_status(status: str) -> bool:
    return status in VALID_STATUSES


def create_application(company: str, role: str, status: str) -> dict[str, str]:
    return {
        "company": company,
        "role": role,
        "status": status
    }


def add_application(applications: list[dict[str, str]]) -> None:
    company = input("Enter company name: ").strip()
    role = input("Enter role: ").strip()
    status = input("Enter status applied/interview/rejected/selected: ").strip().lower()

    if company == "" or role == "":
        print("Company and role cannot be empty")
        return

    if not is_valid_status(status):
        print("Invalid status")
        return

    application = create_application(company, role, status)
    applications.append(application)

    print("Application added successfully")


def view_applications(applications: list[dict[str, str]]) -> None:
    if len(applications) == 0:
        print("No applications found")
        return

    print("\nApplications:")

    for index, application in enumerate(applications, start=1):
        print(
            f"{index}. {application['company']} - "
            f"{application['role']} - "
            f"{application['status']}"
        )


def search_by_company(applications: list[dict[str, str]]) -> None:
    search_company = input("Enter company name to search: ").strip().lower()

    for application in applications:
        if application["company"].lower() == search_company:
            print("Application found:")
            print(application)
            return

    print("Application not found")


def count_by_status(applications: list[dict[str, str]]) -> None:
    status_count = {}

    for application in applications:
        status = application["status"]

        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    if len(status_count) == 0:
        print("No applications found")
        return

    print("Status count:")

    for status, count in status_count.items():
        print(f"{status}: {count}")


def save_applications(applications: list[dict[str, str]]) -> None:
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(applications, file, indent=4)

        print("Applications saved successfully")

    except OSError as error:
        print(f"Error while saving applications: {error}")


def load_applications() -> list[dict[str, str]]:
    if not os.path.exists(FILE_NAME):
        print("No saved applications file found")
        return []

    try:
        with open(FILE_NAME, "r") as file:
            applications = json.load(file)

        print("Applications loaded successfully")
        return applications

    except json.JSONDecodeError:
        print("Invalid JSON file format")
        return []

    except OSError as error:
        print(f"Error while loading applications: {error}")
        return []


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
            search_by_company(applications)
        elif choice == "4":
            count_by_status(applications)
        elif choice == "5":
            save_applications(applications)
        elif choice == "6":
            applications = load_applications()
        elif choice == "7":
            print("Exiting application tracker")
            break
        else:
            print("Invalid choice")


run_application_tracker()

# Understanding the code: