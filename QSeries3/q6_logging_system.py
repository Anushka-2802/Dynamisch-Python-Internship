import logging
logging.basicConfig(filename="login.log",level=logging.INFO)
try:
    name=input("Enter a name: ")
    age=int(input("Enter a age: " ))
    logging.info(f"User Input: {name} : {age}") #INFO
    if age < 0:
        raise ValueError("Age Must be positive")
    if age>100:
        logging.warning("Age entered is usually high") #WARNING
        print("Age enterd is usually high")
    
    print("welcome",name)
    logging.info("User Register successfully...")
    
except ValueError as e:
    logging.error(f"Error: {e}") #ERROR
    print("Invalid Input:",e)
