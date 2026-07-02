class Student:
    def __init__(self, student_id, student_name, student_class):
        """
        initialize parameters
    
        """
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def show_details(self):
        """print details"""
        print("Student id:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student class:", self.student_class)


obj = Student(21, "Anushka Gujar", "XII")
obj.show_details()
