from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes

app=FastAPI()

app.include_router(routes.router)

origins=[
     "http://localhost:3000",
     "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


