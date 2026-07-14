from pydantic import BaseModel

class Employee(BaseModel):
    name:str
    id:int
    department:str
    salary:int


