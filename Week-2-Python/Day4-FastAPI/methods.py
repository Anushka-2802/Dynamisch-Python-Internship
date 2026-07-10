from fastapi import FastAPI

app=FastAPI()

#GET :Retrive data
@app.get("/employee/{emp_id}")
def get_employee(emp_id:int):
    return{
        "message":"Employee Detail fetched Successfully",
        "name":"Anushka",
        "emp_id":emp_id
    }

#Post: Create new data
@app.post("/employee")
def add_employee(name:str,emp_id:int,department:str):
    return{
        "message":"Employee Added Sucessfully",
        
        "employee":{ 
        "name":name,
        "emp_id":emp_id,
        "department":department
        }
    }

#PUT: update existing data
@app.put("/employee/{emp_id}")
def update_employee(name:str,emp_id:int,department:str):
    return{
          "message":"Employee Update Successfully",
          "employee":{
              "name":name,
              "emp_id":emp_id,
              "department":department
 
          }
    }

#DELETE: delete data
@app.delete("/employee/{emp_id}")
def deleted_emp(emp_id:int):
    return{
        "message":"Employee Deleted Succesfully",
        "deleted_emp_id":emp_id
    }
