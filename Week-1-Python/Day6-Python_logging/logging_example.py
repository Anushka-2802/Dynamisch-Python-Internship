#logging used to track events,errors and programs while program is running
import logging
logging.basicConfig(level=logging.DEBUG)
logging.info(" Program started")
logging.warning(" Low memory")
logging.error(" File not found")

#Levels logging 
# 1.DEBUG :Detail info for debuging
# 2.INFO : General program information 
# 3.WARNING : Something happen unexpectedly 
# 4.ERROR : Program error occured 
# 5.CRITICAL: Serious error

#DEBUG
logging.debug("This is debug message")

#WARNING
logging.basicConfig(level=logging.WARNING)
logging.warning("Low memory")

#ERROR
logging.basicConfig(level=logging.ERROR)
n1=10
n2=0
try:
    result= n1/n2
except ZeroDivisionError:
    logging.error("Divide by zero error")

#CRITICAL
logging.basicConfig(level=logging.CRITICAL)
logging.critical("System crashed")

#Simple Example
logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin" and password == "1234":
    logging.info("Login Successful")
    print("Welcome Admin")
else:
    logging.error("Invalid Login")
    print("Wrong Username or Password")