'''
A Custom Exception represents a specific error.
An Exception Handler catches that exception and returns a custom response.
'''


from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

app=FastAPI()

employees = {
    101: "Anushka",
    102: "Riya"
}


class EmployeeNotFound(Exception):
    def __init__(self, emp_id:int):
        self.emp_id=emp_id

@app.exception_handler(EmployeeNotFound)
async def employee_not_found_handler(
    request:Request,
    exc:EmployeeNotFound
):
    return JSONResponse(
        status_code=404,
        content={
           "success":False,
           "message":f"Employee {exc.emp_id} not found"
        }
    )

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):

    if emp_id not in employees:
        raise EmployeeNotFound(emp_id)

    return {
        "employee_id": emp_id,
        "name": employees[emp_id]
    }


