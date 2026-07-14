'''
CORS: Cross-Origin Resource Sharing is a browser security mechanism 
that controls whether a web application from one origin can access resources from another origin

We use CORSMiddleware to allow trusted frontend applications 
such as React or Angular running on different origins to communicate with our FastAPI backend

'''


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
@app.get("/student")
def get_student():
    return{
        "name":"Anushka",
        "department":"AI"
    }