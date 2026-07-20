# Employee API

## About

This project is a simple Employee Management REST API developed using FastAPI.

It provides the following functionalities:

- Get all employees
- Get employee details by ID
- Search employees using department and salary range
- Add a new employee
- Handle errors using HTTPException
- Log API activities using Python logging


## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Postman


## Project Setup

1. Install the required packages.

```bash
pip install -r requirements.txt
```

2. Go to the app folder.

```bash
cd app
```

3. Start the FastAPI server.

```bash
uvicorn main:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```


## API Endpoints

- GET  `/employees`         :  Get all employees 
- GET  `/employees/{emp_id}`:  Get employee by ID 
- GET  `/employees/search`  :  Search employees by department and salary
- POST `/employees`         :  Add a new employee 


## Sample API Requests and Responses

### Get All Employees

**Request**

```
GET /employees
```

**Response**

```json
{
    "status": "success",
    "message": "Employee fetched successfully",
    "data": [
        {
            "id": 1,
            "name": "Anushka",
            "department": "IT",
            "salary": 20000
        }
    ]
}
```

### Add Employee

**Request**

```json
POST /employees

{
    "id": 6,
    "name": "Rahul",
    "department": "IT",
    "salary": 35000
}
```

**Response**

```json
{
    "status": "success",
    "message": "Employee Added Successfully",
    "data": {
        "id": 6,
        "name": "Rahul",
        "department": "IT",
        "salary": 35000
    }
}
```

## Deployment Details

This project runs locally using the Uvicorn server.

Run the project using:

```bash
uvicorn main:app --reload
```

Access the API using:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Error Handling

The API uses `HTTPException` to return appropriate error messages.

Some common status codes used are:

- 400 Bad Request
- 404 Not Found

---

## Logging

Application logs are stored in the `employee.txt` file.

---

## Testing

The API was tested using:

- Swagger UI
- Postman

The Postman collection is included in the project as:

```
Employee-API.postman_collection.json
```