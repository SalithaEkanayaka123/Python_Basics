# Small program : Python backend interview eligibility check


# enter name, years of experience, java experience, python basics is there or not, fast api knowledge is there or not 
# then return the results 

name = input("What is the your name? ")
experience = int(input("How many experience do you have? "))
has_java_skills = input("Do you have Java skills? (yes/no) ").lower() == "yes"
has_python_skills = input("Do you have Python skills? (yes/no) ").lower() == "yes"
has_fastapi_knowledge = input("Do you have FastAPI knowledge? (yes/no) ").lower() == "yes"

print("\nInterview Eligibility Check Results")
print(f"name : {name}")
print(f"Experience : {experience} years")
print(f"Java Skills : {'Yes' if has_java_skills else 'No'}")
print(f"Python Skills : {'Yes' if has_python_skills else 'No'}")
print(f"FastAPI Knowledge : {'Yes' if has_fastapi_knowledge else 'No'}")    

if experience >= 3 and has_python_skills and has_fastapi_knowledge:
    print("Conngratulations! You are eligible to apply Senior Python Developer role.")
elif experience >= 2 and has_python_skills:
    print("Congratulations! You are eligible to apply for the Junior Python Developer role.")
elif experience >= 3 and has_java_skills:
    print("Congratulations! You are eligible to apply for the Java Developer role.")
else:
    print("Sorry, you are not eligible for the backend developer roles at this time.")
