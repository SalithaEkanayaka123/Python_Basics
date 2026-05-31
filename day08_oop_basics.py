# Python OOP Basics

class JobApplication:
    pass

application = JobApplication()
print(application)

# class is a blueprint for creating objects, and an object is an instance of a class.

# Contructor 
# __init__ -> constructor-like initialization is done using __init__

class JobApplication:

    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

application = JobApplication("Google", "Software Engineer", "Applied")

print(application.company)  # Output: Google
print(application.role)     # Output: Software Engineer
print(application.status)   # Output: Applied

# __init__ is a special method in Python used to initialize object state when an object is created.

# what is self 

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status
    
    def display_summary(self):
        return f"{self.role} - {self.role} - {self.status}"
    
application = JobApplication("Google", "Software Engineer", "Applied")
print(application.display_summary())  

# self refers to the current object instance. It is used to access instance variables and methods inside the class.
# similar to this in java

# instance method 

class JobApplication:
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status
    
    def update_status(self, new_status):
        self.status = new_status
    
    def display_summary(self):
        return f"{self.role} - {self.role} - {self.status}"
    
application = JobApplication("Google", "Software Engineer", "Applied")
print(application.display_summary())  

application.update_status("Interview Scheduled")
print(application.display_summary())  

# Encapsulation in Python

# Python does not enforce private variables exactly like Java.

# in Java : private String company; --> self._company = company 
# This is intended for internal use. (_company)

class JobApplication:
    def __init__(self, company, role, status):
        self._company = company
        self._role = role
        self._status = status

# Python uses naming conventions for encapsulation. 
# A single underscore means protected/internal use by convention. 
# Double underscore triggers name mangling, but Python does not provide strict private access like Java.

# Inheritance

# Inheritance allows one class to reuse another class.

class Application:
    def __init__(self, company, role):
        self.company = company
        self.role = role

    def summary(self):
        return f"{self.company} - {self.role}"
    
class InterviewApplication(Application):
    def __init__(self, company, role, interview_date):
        super().__init__(company, role)
        self.interview_date = interview_date
 
application = InterviewApplication("WSO2", "Backend Engineer", 1)

print(application.summary())

# super() is used to call methods from the parent class, commonly the parent constructor.

# Method overriding

# Parent class 

class Application:
    def summary(self):
        return "General application"

# child class 

class InterviewApplication(Application):
    def summary(self):
        return "Interview application"
        