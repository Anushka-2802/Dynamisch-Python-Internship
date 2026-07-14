'''
Error handling is dectecting a problem and returning a meaningful response 
instead of crashing the application 
HTTPException is a class provided by FastAPI used to return HTTP Error 
'''

from fastapi import FastAPI,HTTPException

app=FastAPI()

employees={
    101:"Anushka",
    102:"Prachi",
    103:"Esha",
    104:"Abhilasha"

}

@app.get("/employees/{employee_id}")
def get_employee(employee_id:int):
    
    if employee_id not in employees:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    
    return{
        "employee_id":employee_id,
        "name":employees[employee_id]
    }
    

# Add employee: age is greater than 18

@app.post("/employees/{employee_age}")
def add_employee(employee_age:int):
    if employee_age < 18:
        raise HTTPException(
            status_code=400,
            detail="Employee age must be atleast 18 years old"
        )
    return{
        "message":"Employee added successfully"
    }

