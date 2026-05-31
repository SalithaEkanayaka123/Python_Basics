def filter_by_status(
    applications: list[dict[str, str]],
    status: str
) -> list[dict[str, str]]:
    return [
        application
        for application in applications
        if application["status"] == status
    ]


def get_company_names(applications: list[dict[str, str]]) -> list[str]:
    return [
        application["company"]
        for application in applications
    ]


def sort_applications_by_company(
    applications: list[dict[str, str]]
) -> list[dict[str, str]]:
    return sorted(
        applications,
        key=lambda application: application["company"].lower()
    )


def has_application_for_company(
    applications: list[dict[str, str]],
    company: str
) -> bool:
    return any(
        application["company"].lower() == company.lower()
        for application in applications
    )

applications = [
    {"company": "WSO2", "role": "Backend Engineer", "status": "applied"},
    {"company": "IFS", "role": "Software Engineer", "status": "interview"},
    {"company": "Virtusa", "role": "Senior Software Engineer", "status": "applied"},
    {"company": "Hatchyard", "role": "Java Developer", "status": "rejected"}
]

print(filter_by_status(applications, "applied"))
print(get_company_names(applications))
print(sort_applications_by_company(applications))
print(has_application_for_company(applications, "IFS"))