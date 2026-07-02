def display_marks(marks):
    print("Student Marks")
    print(marks)

def remove_duplicate(marks):
    unique=[]
    for i in marks:
        if i not in unique:
            unique.append(i)
    print("After removing duplicates:")
    print(marks)
    return marks

def highest_marks(marks):
    temp=sorted(marks,reverse=True) 
    print("Highest 3 marks: ")
    print(temp[:3])

def lowest_marks(marks):
    temp=sorted(marks)
    print("lowest marks: ")
    print(temp[:3])

def even_odd(marks):
    even=[]
    odd=[]
    for i in marks:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)    
    print(even)
    print(odd)

marks = [78, 45, 90, 67, 45, 90, 56, 34, 89]

while True:
    print("1. Display Marks")
    print("2. Remove Duplicates")
    print("3. Highest 3 Marks")
    print("4. Lowest 3 Marks")
    print("5. Even/Odd Marks")
    print("6. Exit")
    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        display_marks(marks)

    elif choice == 2:
        marks = remove_duplicate(marks)

    elif choice == 3:
        highest_marks(marks)

    elif choice == 4:
        lowest_marks(marks)
      
    elif choice == 5:
        even_odd(marks)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
