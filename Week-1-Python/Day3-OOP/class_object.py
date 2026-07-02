#class is a blueprint or template for creating objects 
#object is a instance of class to access properties of class
class Details:
    name="Anushka"
    age=21
    occupation="Software Engineer"
    emp_id=63
    networth=20000
    def info(self):
        print(f"{self.name} is a intern in dynamisch company")
        print(f"Anushka is {self.age} years old")
        print(f"Anushka is a {self.occupation}")
    
a=Details() # object of class Details
a.info() #access method (info()) of Details class 
