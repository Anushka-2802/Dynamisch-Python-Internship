from fastapi import FastAPI
from Pydantic_model import EmployeeCreate,EmployeeResponse

app=FastAPI()


# Request Model
'''A Request Model is a Pydantic model that defines the structure of the data the client sends to the API.'''

@app.post("/employee",response_model=EmployeeResponse)
def emp_add(employee:EmployeeCreate):
    return employee


# Response model
'''A Response Model is a Pydantic model that define which fields should be returned.'''

@app.get("/employee", response_model=EmployeeResponse)
def get_emp_details():
    return {
        "name": "Anushka",
        "age": 21,
        "username": "anu",
        "password": 280205,   # This will be ignored
        "department": "HR"
    }