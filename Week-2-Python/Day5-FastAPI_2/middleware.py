'''
Middleware is a function that runs before the request reaches your API after your API send the response

'''

from fastapi import FastAPI
import time

app = FastAPI()

@app.middleware("http")  #Run this function for every HTTP request
async def process_time(request, call_next):

    start_time = time.time()

    response = await call_next(request)  #Send the request to the next step

    end_time = time.time()

    print(f"Execution Time: {end_time - start_time:.4f} seconds")

    return response

@app.get("/")
async def home():
    return {"message": "Welcome"}



#Logging Requests

@app.middleware("http")
async def log_request(request, call_next):

    print("Request Method:", request.method)
    print("URL:", request.url)

    response = await call_next(request)

    return response

@app.get("/employee")
async def employee():
    return {"message": "Employee API"}