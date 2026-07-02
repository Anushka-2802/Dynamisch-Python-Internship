from datetime import date
class Person:
    def __init__(self):
        self.name=" "
        self.country=" "
        self.date_of_birth=None
    def details(self):
        self.name=input("Enter your name: ")
        self.country=input("Enter country name: ")
        year=int(input("Enter your birth year: "))
        month=int(input("Enter your birth month: "))
        day=int(input("Enter your birth day: "))
        self.date_of_birth= date(year,month,day)
        print("Name: ",self.name)
        print("country: ",self.country)
        print("date of birth: ",self.date_of_birth)

    def age_calculation(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if (today.month,today.day)<(self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        print(f"Age of {self.name} is:",age)
obj=Person()
obj.details()
obj.age_calculation()
        
