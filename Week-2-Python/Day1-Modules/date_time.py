from datetime import datetime,date,time

def current_datetime():
    '''Display current date and time'''
    now=datetime.now()
    print(now)

def current_date():
    '''Display Current date'''
    today=date.today()
    print("todays date: ",today)

def current_time():
    '''Display Current time'''
    time=datetime.now().time()
    print("Current time: ",time)

def custom():
    """
    Create and display custom date and time.
    """
    custom_date=date(2005,2,5)
    custom_t=time(10,30,45)
    print("custom_date",custom_date)
    print("custom_time",custom_t)

def format_datetime(): 
    """Format date and time""" 
    now = datetime.now() 
    print("\nFormatted Date and Time") 
    print("Date:", now.strftime("%d-%m-%Y")) 
    print("Time:", now.strftime("%H:%M:%S")) 
    print("Day:", now.strftime("%A")) 
    print("Month:", now.strftime("%B")) 
    print("Year:", now.strftime("%Y"))

current_datetime()
current_date()
current_time()
custom()
format_datetime()

