"""This file contains all Employee API endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal
from logger import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    """Fetch all employees"""

    employees = crud.get_all_employees(db)

    if not employees:
        logger.warning("Employee list is empty")
        raise HTTPException(status_code=404, detail="Employee Not Found")

    logger.info("Fetched all employees")

    return employees


@router.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    """Fetch employee using employee ID"""

    employee = crud.get_employee_by_id(db, emp_id)

    if employee is None:
        logger.warning("Employee not found")
        raise HTTPException(status_code=404, detail="Employee Not Found")

    logger.info(f"Employee {emp_id} fetched")

    return employee


@router.get("/employees/search", response_model=list[schemas.EmployeeResponse])
def search_employee(
    department: str,
    min_salary: int,
    max_salary: int,
    db: Session = Depends(get_db)
):
    """Search employees by department and salary range."""

    employees = crud.search_employees(
        db,
        department,
        min_salary,
        max_salary
    )

    if not employees:
        logger.warning("Search returned no employees")
        raise HTTPException(status_code=404, detail="Employee Not Found")

    logger.info("Employee search successful")

    return employees


@router.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    """Add a new employee"""

    existing = crud.get_employee_by_id(db, employee.id)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    logger.info("Employee added")

    return crud.create_employee(db, employee)


@router.put("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    emp_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    """Update employee derails"""
    updated = crud.update_employee(db, emp_id, employee)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    logger.info("Employee updated")

    return updated


@router.delete("/employees/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    """Delete an employee"""

    deleted = crud.delete_employee(db, emp_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    logger.info("Employee deleted")

    return {
        "message": "Employee deleted successfully"
    }