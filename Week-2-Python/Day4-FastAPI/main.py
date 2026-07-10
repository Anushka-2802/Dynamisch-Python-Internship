from fastapi import FastAPI
from Pydantic_model import Employee , EmployeeResponse , EmployeeCreate


app = FastAPI()

# Home Page
@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management System"
    }
    
# Path Parameter
'''Path parameter is a variable that is part of URL path '''
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int,name:str):
    return {
        "employee_id": employee_id,
        "name":"Anushka"
    }

# Multiple Path Parameters
@app.get("/departments/{department}/employees/{emp_id}")
def get_emp(department: str, emp_id: int):
    return {
        "department": department,
        "emp_id": emp_id
    }

# Query Parameter
'''Query parameter used to filer,search,sort and customize result'''

@app.get("/employee")
def get_employee_details(emp_id: int, department: str, city: str):
    return {
        "emp_id": emp_id,
        "department": department,
        "city": city
    }

# Add employee by importing created pydantic module
@app.post("/")
def add_emp(employee:Employee):
    return{
        "message":"Employee Added Successfully",
        "Employee":employee
    }




