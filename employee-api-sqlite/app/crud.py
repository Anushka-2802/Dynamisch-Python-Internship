"""
This file contains all database operations such as
Create, Read, Update and Delete
"""

from sqlalchemy.orm import Session
import models
import schemas


# Get all employees
def get_all_employees(db: Session):
    return db.query(models.Employee).all()


# Get employee by ID
def get_employee_by_id(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


# Search employees
def search_employees(db: Session, department: str, min_salary: int, max_salary: int):
    return (
        db.query(models.Employee)
        .filter(
            models.Employee.department == department,
            models.Employee.salary >= min_salary,
            models.Employee.salary <= max_salary
        )
        .all()
    )


# Add employee
def create_employee(db: Session, employee: schemas.EmployeeCreate):

    db_employee = models.Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


# Update employee
def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeCreate):

    db_employee = get_employee_by_id(db, emp_id)

    if db_employee:

        db_employee.name = employee.name
        db_employee.department = employee.department
        db_employee.salary = employee.salary

        db.commit()
        db.refresh(db_employee)

    return db_employee


# Delete employee
def delete_employee(db: Session, emp_id: int):

    db_employee = get_employee_by_id(db, emp_id)

    if db_employee:
        db.delete(db_employee)
        db.commit()

    return db_employee