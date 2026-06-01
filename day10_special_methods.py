
# What are special methods?
# Special methods are methods with double underscores before and after the name. 

#__init__
#__str__
#__repr__
#__eq__
#__len__

# They are also called dunder methods.

# Special methods in Python allow objects to customize built-in behavior such as object creation, 
# string representation, comparison, length calculation, and arithmetic operations.

# __str__

# __str__ defines what should be shown when we print an object.
# Without __str__:

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status


application = JobApplication("WSO2", "Backend Engineer", "applied")

print("That is not readable.")
print(application)

# with __str__

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status

    def __str__(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"


application = JobApplication("WSO2", "Backend Engineer", "applied")

print(application)

# __str__ returns a user-friendly string representation of an object. It is used by print() and str().

# __repr__
# __repr__ is mainly for developers and debugging. It should return a string that, if possible, can be used to recreate the object.

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status

    def __repr__(self) -> str:
        return (
            f"JobApplication(company='{self.company}', "
            f"role='{self.role}', status='{self.status}')"
        )


application = JobApplication("IFS", "Software Engineer", "interview")

print(repr(application))

# __repr__ returns a developer-friendly string representation of an object. It should ideally be useful for debugging.

#__str__  -> user-friendly
#__repr__ -> developer/debugging-friendly

# Use both __str__ and __repr__

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
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


application = JobApplication("Virtusa", "Senior Software Engineer", "applied")

print(application)
print(repr(application))

# __eq__
# __eq__ defines how two objects should be compared using ==

class JobApplication:
    def __init__(self, company: str, role: str):
        self.company = company
        self.role = role


app1 = JobApplication("WSO2", "Backend Engineer")
app2 = JobApplication("WSO2", "Backend Engineer")

print(app1 == app2)

# Because Python compares object references by default.

class JobApplication:
    def __init__(self, company: str, role: str):
        self.company = company
        self.role = role

    def __eq__(self, other) -> bool:
        if not isinstance(other, JobApplication):
            return False

        return self.company == other.company and self.role == other.role


app1 = JobApplication("WSO2", "Backend Engineer")
app2 = JobApplication("WSO2", "Backend Engineer")

print(app1 == app2)

# __eq__ customizes object equality. By default, objects are compared by identity, but with __eq__, we can compare based on object data.

# __len__
# __len__ allows us to use len() on our own class.

class ApplicationTracker:
    def __init__(self):
        self.applications = []

    def add_application(self, application: str) -> None:
        self.applications.append(application)

    def __len__(self) -> int:
        return len(self.applications)


tracker = ApplicationTracker()

tracker.add_application("WSO2 - Backend Engineer")
tracker.add_application("IFS - Software Engineer")

print(len(tracker))

# __len__ allows an object to define its length when passed to the built-in len() function.

# __dict__
# Every normal Python object stores its attributes in __dict__.

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status


application = JobApplication("Hatchyard", "Java Developer", "applied")

print(application.__dict__)

#This is useful for understanding how Python stores object data.

#But in real code, better to create your own method:

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status

    def to_dict(self) -> dict:
        return {
            "company": self.company,
            "role": self.role,
            "status": self.status
        }

application = JobApplication("Hatchyard", "Java Developer", "applied")

print(application.to_dict())
