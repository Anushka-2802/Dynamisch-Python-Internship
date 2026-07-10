from pydantic import BaseModel,Field

'''
Pydantic is used for data validation and parsing
A Pydantic model inherits from BaseModel
FastAPI automatically converts JSON into a Pydantic object
Invalid data results in an automatic 422 Unprocessable Entity response
Pydantic models are mainly used for request bodies in POST, PUT
'''

class Employee(BaseModel):
    name:str
    emp_id:int
    age:int
    department:str
    city:str

class EmployeeResponse(BaseModel):
    name:str
    age:int
    department:str

class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str
    password: int