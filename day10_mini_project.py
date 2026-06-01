# Day 10 - Python Special Methods
# Mini project: Job application tracker with special methods

VALID_STATUSES = ("applied", "interview", "rejected", "selected")


class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        if status not in VALID_STATUSES:
            raise ValueError("Invalid status")

        self.company = company
        self.role = role
        self.status = status

    def __str__(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"

    def __repr__(self) -> str:
        return (
            f"JobApplication(company='{self.company}', "
            f"role='{self.role}', status='{self.status}')"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, JobApplication):
            return False

        return (
            self.company.lower() == other.company.lower()
            and self.role.lower() == other.role.lower()
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "company": self.company,
            "role": self.role,
            "status": self.status
        }


class ApplicationTracker:
    def __init__(self):
        self.applications: list[JobApplication] = []

    def add_application(self, application: JobApplication) -> None:
        if application in self.applications:
            print("Application already exists")
            return

        self.applications.append(application)
        print("Application added successfully")

    def view_applications(self) -> None:
        if len(self.applications) == 0:
            print("No applications found")
            return

        for index, application in enumerate(self.applications, start=1):
            print(f"{index}. {application}")

    def search_by_company(self, company: str) -> JobApplication | None:
        for application in self.applications:
            if application.company.lower() == company.lower():
                return application

        return None

    def __len__(self) -> int:
        return len(self.applications)

    def __str__(self) -> str:
        return f"ApplicationTracker(total_applications={len(self)})"

    def to_dict_list(self) -> list[dict[str, str]]:
        return [application.to_dict() for application in self.applications]


def run_demo() -> None:
    tracker = ApplicationTracker()

    app1 = JobApplication("WSO2", "Backend Engineer", "applied")
    app2 = JobApplication("IFS", "Software Engineer", "interview")
    app3 = JobApplication("WSO2", "Backend Engineer", "applied")

    tracker.add_application(app1)
    tracker.add_application(app2)
    tracker.add_application(app3)

    print("\nApplications:")
    tracker.view_applications()

    print("\nTracker Summary:")
    print(tracker)

    print("\nTotal applications:")
    print(len(tracker))

    print("\nDeveloper representation:")
    print(repr(app1))

    print("\nDictionary format:")
    print(tracker.to_dict_list())


run_demo()

# Understand this