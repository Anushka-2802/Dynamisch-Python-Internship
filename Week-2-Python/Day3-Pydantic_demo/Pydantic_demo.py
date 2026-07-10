'''Pydantic is a Python library used for data validation, parsing, and serialization using Python type hints'''
from pydantic import BaseModel,ValidationError,Field,EmailStr,field_validator,model_validator

class Student(BaseModel):

    id:int
    name:str
    age:int

student=Student(
    id=101,
    name="Anushka",
    age=21
)
print(student)
print("\nDictionary\n",student.model_dump())  # Convert model to dictionary


# Automatic type conversion

class details(BaseModel):
    name:str
    age:int 
    city:str="pune" #default value

person=details(name="Anushka",   
               age="21")     #age passed as a string
print(person)
print("\nJson\n",person.model_dump_json())  # Convert model to JSON


# Validation Error handling 
class validation(BaseModel):
    name:str
    age:int
    marks:int
try:
    val_error=validation(name="Anushka",
                    age="Twenty",marks="60")
    print(val_error)
    
except ValidationError as e:
    print("Validation Error")
    print(e)

# Field Validation
'''
Field Parameter: gt,ge,lt,le,max_length,min_length,default,description
'''
class voter(BaseModel):
    name:str=Field(min_length=3,max_length=6)
    age:int=Field(gt=18)
try:   
  vote=voter(name="Anushka",
           age=21)
  print(vote)
except ValidationError as e:
    print("Validation Error")
    print(e)

# Email Validation
class User(BaseModel):
    name:str
    email:EmailStr
try:
    user=User(name="Anushka",
          email="ABC")   # Email is not in proper format
    print(user)

except ValidationError as e:
    print("Validation Error")
    print(e)

#nested Model
class Address(BaseModel):
    city:str
    state:str

class Information(BaseModel):
    name:str
    age:int
    phone:int
    address:Address

info=Information(name="Anushka",
                 age=21,
                 phone=8080579302,
                 address={
                 "city":"Phaltan",
                 "state":"Maharastra"})
print(info)

# field_validator
class user(BaseModel):
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('User must be 18 or older')
        return v
try:
    user(name="Anushka", age=16)
except ValidationError as e:
    print(e.json())
