students = []
while True:
    print("======Student Management System=======")
    print("1. Add Student")
    print("2. Display Marks")
    print("3. Display Details")
    print("4. Search student ")
    print("5. Remove Student")
    print("6. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        name = str(input("Enter Name: "))
        rollno = int(input("Enter Roll No: "))
        marks = int(input("Enter Marks: "))
        print("Student Addded successfully!!")
        student = {"name": name, "rollno": rollno, "marks": marks}
        students.append(student)
        file = open("storage.txt", "a")
        file.write(
            "\nName: " + name + "\nRoll_no: " + str(rollno) + "\nMarks: " + str(marks)
        )
        file.close()

    elif choice == 2:
        roll_no = int(input("Enter Roll No: "))
        found = False
        for student in students:
            if student["rollno"] == roll_no:
                print("Marks of student: ", student["marks"])
                found = True
        if found == False:
            print("Student not found")

    elif choice == 3:
        n = input("Enter Name: ")
        found = False
        for student in students:
            if student["name"] == n:
                print("Name :", student["name"])
                print("Roll No :", student["rollno"])
                print("Marks :", student["marks"])
                found = True
        if found == False:
            print("Student not found")

    elif choice == 4:
        roll = int(input("Enter Roll Number: "))
        found = False
        for student in students:
            if student["rollno"] == roll:
                print("Student is present in record")
                found = True
        if found == False:
            print("Student is not present")

    elif choice == 5:
        roll = int(input("Enter Roll Number: "))
        found = False
        for student in students:
            if student["rollno"] == roll:
                students.remove(student)
                print("Student remove successfully!!")
                found = True
        if found == False:
            print("Student not found")

    elif choice == 6:
        print(".....End.....")
        break
    else:
        print("Invalid Input")
