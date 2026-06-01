# @staticmethod
# A static method belongs to the class, but it does not use object data

class SalaryCalculator:

    @staticmethod
    def calculate_increment_percentage(current_salary: float, expected_salary: float) -> float:
        difference = expected_salary - current_salary
        return (difference / current_salary)  * 100

percentage = SalaryCalculator.calculate_increment_percentage(50000, 60000)
print(f"Expected Increment Percentage: {percentage:.2f}%")

# Here we do not create an object:
# calculator = SalaryCalculator()

# We directly call:
# SalaryCalculator.calculate_increment_percentage(50000, 60000)

#@classmethod

# A class method recieves the class itself as the first parameter, ussually named as "cls". 

class JobApplication:
    default_status = "applied"

    def  __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role 
        self.status = status
    
    @classmethod
    def create_default_application(cls, company:str, role:str):
        return cls(company, role, cls.default_status)
    
application = JobApplication.create_default_application("Google", "Software Engineer")

print(application.company)  
print(application.role)     
print(application.status)   

# A class method receives the class as the first argument using cls. 
# It can access class-level data and is often used as an alternative constructor.

# Difference between instance method, static method, and class method

#Method type	    First parameter	    Access instance data?	Access class data?
#Instance method	    self	                Yes	                    Yes
#Static method	        none	                No	                    No
#Class method	        cls	                    No	                    Yes

class Developer:
    company = "ABC Tech"

    def __init__(self, name: str):
        self.name = name
    
    def instance_method(self):
        return self.name
    
    @staticmethod
    def stattic_method():
        return "Utility method"
    
    @classmethod
    def class_method(cls):
        return cls.company
    
devloper = Developer("Alice")
print(devloper.instance_method())
print(Developer.stattic_method())  
print(Developer.class_method())  

# property
# In Java those denote as getters setters

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
       valid_statuses = ("applied", "interview", "rejected", "selected")
       if new_status not in valid_statuses:
           raise ValueError("Invalid status")
       self._status = new_status

application = JobApplication("Google", "Software Engineer", "applied")
print(application.status)  

application.status = "interview"
print(application.status)

# application.status = "wrong"  # This will raise ValueError

#@property allows us to control access to attributes like getters and setters, while still using simple attribute syntax.

# dataclass

# A dataclass reduce boilerplate code for classes that are primarily used to store data.
#  It automatically generates methods like __init__, __repr__, and __eq__ based on the class attributes.

# Normal class

class JobApplication:
    def __init__(self, company: str, role: str, status: str):
        self.company = company
        self.role = role
        self.status = status

from dataclasses import dataclass


@dataclass
class JobApplication:
    company: str
    role: str
    status: str


application = JobApplication("WSO2", "Backend Engineer", "applied")
print(application) 

# like @Data annotation in java lombok

# A dataclass is used to create classes that mainly store data. 
# It automatically generates methods like __init__, __repr__, and comparison-related methods depending on configuration.

# Dataclass with method

@dataclass
class JobApplication:
    company: str
    role: str
    status: str

    def display_summary(self) -> str:
        return f"{self.company} - {self.role} - {self.status}"


application = JobApplication("Virtusa", "Senior Software Engineer", "interview")
print(application.display_summary())

# Abstract class

#An abstract class defines methods that child classes must implement.

from abc import ABC, abstractmethod

class NotificationService(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotificationService(NotificationService):

    def send(self, message: str) -> None:
        print(f"Sending email: {message}")


class SmsNotificationService(NotificationService):

    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")


service = EmailNotificationService()
service.send("Your interview is tomorrow")

#An abstract class is used to define a common contract for child classes. In Python, we use the abc module and @abstractmethod.

#Java comparison:

#interface NotificationService {
 #   void send(String message);
#}

#Python:

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
