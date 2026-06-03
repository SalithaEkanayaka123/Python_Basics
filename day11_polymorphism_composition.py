# What is polymorphism?
# Polymorphism means same method name, different behavior depending on the object.

class EmailNotificationService:
    def send (self, message: str) -> None:
        print(f"Sending email: {message}")


class SmsNotificationService:
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")

def notify_user (service, message: str) -> None:
    service.send(message)

email_service = EmailNotificationService()
sms_service = SmsNotificationService()

notify_user(email_service, "Your interview is tomorrow")
notify_user(sms_service, "Your interview is tomorrow")

# Polymorphism allows different objects to be used through the same interface or method name. 
# In Python, if an object has the required method, it can be used regardless of its exact class.

# Python uses duck typing

# In Jave we need an interface, in python , the object just needs to have the method we want to call. 
# This is called duck typing: "If it looks like a duck and quacks like a duck, it's a duck."   

def notify_user(service, message):
    service.send(message)

# Duck typing means Python focuses on whether an object has the required behavior, not its declared type. 
# If the object has the needed method, Python can use it.

# Inheritance: is-a relationship

# Inheritance means one class is a type of another class.

class NotificationService:
    def send(self, message: str) -> None:
        print(f"Sending notification: {message}")

class EmailNotificationService(NotificationService):
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SmsNotificationService(NotificationService):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

#EmailNotificationService is a NotificationService
#SmsNotificationService is a NotificationService

# This is is-a relationship: EmailNotificationService and SmsNotificationService are types of NotificationService.

# Composition: has-a relationship
# Composition means one class contains an instance of another class.

class ConsoleNotificationService:
    def send(self, message: str) -> None:
        print(f"Notification: {message}")

class ApplicationTracker:

    def __init__(self, notification_service: ConsoleNotificationService):
        self.notification_service = notification_service
    
    def add_application(self, company: str, role:str) -> None:
        print(f"Application added: {company} - {role}")
        self.notification_service.send("New job application added")

notification_service = ConsoleNotificationService()
tracker = ApplicationTracker(notification_service)

tracker.add_application("Google", "Software Engineer")

# Why composition is important

#Because later you can pass:

#EmailNotificationService
#SmsNotificationService
#ConsoleNotificationService
#MockNotificationService for tests

#This is very useful in backend development.

#Java comparison:

#Spring dependency injection
#Constructor injection
#Service interface
#Implementation class

#Python version:

#Pass dependency through constructor
#Use object behavior
#Keep code flexible
