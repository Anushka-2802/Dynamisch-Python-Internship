from fastapi import APIRouter,HTTPException
from schemas import Employee
from database import employee_data
from loggers import logger

router=APIRouter()

#Fetch all employee

@router.get("/employees")
def get_all_employee():

    """Fetch all employee records"""

    if not employee_data:

        logger.warning("Employee list is empty.") 
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    logger.info(f"Fetched {len(employee_data)} employees.")

    return{
        "status": "success",
        "message": "Employee fetched successfully",
        "data":employee_data
    }


# Search employee

@router.get("/employees/search")
def search_employee(department: str, min_salary: int, max_salary: int):
    
    """Search employees using department and salary range"""

    result = []

    for emp in employee_data:
        if (
            emp["department"] == department
            and emp["salary"] >= min_salary
            and emp["salary"] <= max_salary
        ):
            result.append(emp)


    if not result:
        logger.warning("Employee Not Found")
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    
    logger.info("Employee found successfully")

    return {
        "status": "success",
        "message": "Employee found",
        "data": result
    }

#Fetch employee by id 

@router.get("/employees/{emp_id}")
def get_employee_by_id(emp_id:int):

    """Fetch employee by ID"""

    if emp_id < 0:
        logger.error("Invalid employee ID received")
        raise HTTPException(
            status_code=400,
            detail="Emp_id must be positive"      
        )
    
    for emp in employee_data:
        if emp["id"]==emp_id:

            logger.info(f"Employee with ID {emp_id} fetched successfully.")

            return{
             "status":"success",
             "message":"Employee fetched successfully",
             "data":emp
            }

    else:
        logger.warning("Employee Not Found")
        raise HTTPException(
                status_code=404,
                detail="Employee Not Found"
            )


#Add Employee

@router.post("/employees")
def add_employee(employee:Employee):

    """Add a new employee"""

    for emp in employee_data:
        if emp["id"]==employee.id:

            logger.error(f"Employee ID {employee.id} already exists.")

            raise HTTPException(
                status_code=400,
                detail="Employee Id already exists"
            )
        
    emp_dict=employee.model_dump()
    employee_data.append(emp_dict)

    logger.info(f"Employee {employee.name} added successfully.")

    return{
        "status": "success",
        "message":"Employee Added Successfully",
        "data": emp_dict
    }


#Update employee data

@router.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: Employee):

    for emp in employee_data:

        if emp["id"] == emp_id:

            emp["name"] = employee.name
            emp["department"] = employee.department
            emp["salary"] = employee.salary

            logger.info(f"Employee {emp_id} updated successfully.")

            return {
                "status": "success",
                "message": "Employee Updated Successfully",
                "data": emp
            }

    logger.warning(f"Employee {emp_id} not found.")

    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )


#Delete employee details

@router.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):

    for emp in employee_data:

        if emp["id"] == emp_id:

            employee_data.remove(emp)

            logger.info(f"Employee {emp_id} deleted successfully.")

            return {
                "status": "success",
                "message": "Employee Deleted Successfully"
            }

    logger.warning(f"Employee {emp_id} not found.")

    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )