# Custom Exceptions

# Why custom exceptions?

# In real backend projects, we should not always use generic errors like:
# raise Exception("Something went wrong")

# Better is to create meaningful business exceptions:

class InvalidStatusError(Exception):
    pass

# Then use:

raise InvalidStatusError("Invalid status")

# This makes your code professional and easier to understand. 

# Basic custom exception

class InvalidStatusError(Exception):
    pass

VALID_STATUSES = ("Applied", "Interviewing", "Offered", "Rejected")

def validate_status(status: str) -> None:
    if status not in VALID_STATUSES:
        raise InvalidStatusError(f"Invalid status: {status}")   

try:
    validate_status("pending")
except InvalidStatusError as error:
    print(error)

# A custom exception is a user-defined exception class created by extending Python’s built-in Exception class. 
# It is useful for representing business-specific errors clearly

# Multiple custom exceptions
# For the job application tracker, we can create:

class ApplicationError(Exception):
    pass


class InvalidStatusError(ApplicationError):
    pass


class ApplicationNotFoundError(ApplicationError):
    pass


class DuplicateApplicationError(ApplicationError):
    pass


# Why use parent exception?

# Because later we can catch all application-related errors using:
# This is similar to having a base exception in Java.


# raise keyword

# raise is used to throw an exception. 

def divide(a: int, b : int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as error:
    print(error)
