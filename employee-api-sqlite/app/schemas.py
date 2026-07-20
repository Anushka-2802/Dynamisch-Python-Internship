"""
This file contains Pydantic models used for request validation
and API responses
"""
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    """Schema for creating a new employee"""

    id: int
    name: str
    department: str
    salary: int


class EmployeeResponse(BaseModel):
    """Schema for returning employee details"""

    id: int
    name: str
    department: str
    salary: int

    class Config:
        from_attributes = True